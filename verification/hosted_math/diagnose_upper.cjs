#!/usr/bin/env node
'use strict';
// Supplementary, read-only evidence after canonical capture failure. This does
// not wait for mathematical readiness and never produces a verification pass.
const fs = require('node:fs');
const path = require('node:path');
const PAGE = 'science/upper_bound.md';
const TOTAL_MS = 60000;
const VIEWPORTS = [{width:1440,height:1000}, {width:760,height:1000}];

function configuration(env) {
  const repository=env.GITHUB_REPOSITORY, revision=env.CAPTURE_REVISION;
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository || '') ||
      repository.split('/').some(part=>part==='.' || part==='..'))
    throw new Error('GITHUB_REPOSITORY must be an exact owner/name');
  if (!/^[a-f0-9]{40}$/.test(revision || ''))
    throw new Error('CAPTURE_REVISION must be a full lowercase commit SHA');
  if (!env.RUNNER_TEMP || !path.isAbsolute(env.RUNNER_TEMP))
    throw new Error('RUNNER_TEMP must be an absolute directory');
  return {repository,revision,url:`https://github.com/${repository}/blob/${revision}/${PAGE}`,
    output:path.join(env.RUNNER_TEMP,'hosted-diagnostic')};
}

// Executed in the existing hosted document: no DOM, styling or renderer writes.
function inspectHostedDocument() {
  const article=document.querySelector('article.markdown-body');
  if (!article) return {article_present:false,title:document.title};
  const errors=[...article.querySelectorAll('merror,[data-mjx-error],.katex-error,math-renderer .flash-error')]
    .map(node=>node.textContent.trim() || 'empty renderer error');
  const renderers=[...article.querySelectorAll('math-renderer')];
  const standalone=[...article.querySelectorAll('math')]
    .filter(node=>!node.parentElement?.closest('math,annotation,annotation-xml'));
  const selected=renderers.length ? renderers : standalone;
  const hosts=selected.map((host,index)=>{
    const math=host.localName==='math' ? [host] : [...host.querySelectorAll('math')]
      .filter(node=>!node.parentElement?.closest('math,annotation,annotation-xml'));
    const readable=math.map(node=>{
      const copy=node.cloneNode(true);
      for (const annotation of copy.querySelectorAll('annotation,annotation-xml')) annotation.remove();
      return {text:copy.textContent.trim(),has_tokens:!!copy.querySelector('mi,mo,mn,mtext,ms'),
        mathml:node.outerHTML};
    });
    const rect=host.getBoundingClientRect();
    return {index:index+1,tag:host.localName,attributes:Object.fromEntries(
      [...host.attributes].map(attribute=>[attribute.name,attribute.value])),
    math_count:math.length,usable:readable.length===1 && !!readable[0].text && readable[0].has_tokens,
    text:host.textContent,html:host.outerHTML,math:readable,
    geometry:{x:rect.x,y:rect.y,width:rect.width,height:rect.height}};
  });
  return {article_present:true,title:document.title,renderer_errors:errors,
    math_renderer_count:renderers.length,top_level_math_count:standalone.length,
    selected_host_count:hosts.length,usable_host_count:hosts.filter(host=>host.usable).length,
    hosts,article_text:article.innerText};
}

async function run(env=process.env) {
  const started=Date.now(), deadline=started+TOTAL_MS;
  const config=configuration(env);
  fs.mkdirSync(config.output,{recursive:true});
  const report={schema_version:1,kind:'supplementary_hosted_diagnostic',
    verification_result:null,canonical_readiness_bypassed:true,
    repository:config.repository,revision:config.revision,path:PAGE,url:config.url,
    started_at:new Date(started).toISOString(),budget_ms:TOTAL_MS,observations:[],errors:[]};
  const filename=path.join(config.output,'diagnostic.json');
  const save=()=>{
    report.elapsed_ms=Date.now()-started;
    fs.writeFileSync(filename,JSON.stringify(report,null,2)+'\n');
  };
  // Also bounds launch/content/screenshot calls whose own APIs may not expose a
  // timeout. Persist partial evidence before terminating a stalled diagnostic.
  const watchdog=setTimeout(()=>{
    report.errors.push('Supplementary diagnostic exceeded its 60-second total budget');
    save();process.exit(1);
  },Math.max(1,deadline-Date.now()-25));
  let browser;
  async function bounded(label,limit,operation) {
    const budget=Math.min(limit,deadline-Date.now()-250);
    if (budget<=0) throw new Error(label+': total diagnostic budget exhausted');
    let timer;
    try {
      return await Promise.race([operation(budget),new Promise((resolve,reject)=>{
        timer=setTimeout(()=>reject(new Error(label+': exceeded '+budget+' ms')),budget);
      })]);
    } finally {clearTimeout(timer);}
  }
  try {
    const {chromium}=require('playwright');
    browser=await bounded('Browser launch',10000,timeout=>chromium.launch({headless:true,timeout}));
    // A fresh context has no account, cookies, stored credentials or auth state.
    const context=await bounded('Anonymous context',3000,()=>browser.newContext({
      viewport:VIEWPORTS[0],serviceWorkers:'block'}));
    const page=await bounded('Diagnostic page',3000,()=>context.newPage());
    // Never follow a main-document redirect or navigate beyond this pinned URL.
    await bounded('Navigation guard',3000,()=>page.route('**/*',route=>{
      const request=route.request();
      if (!['GET','HEAD'].includes(request.method())) return route.abort('blockedbyclient');
      if (request.isNavigationRequest() && request.frame()===page.mainFrame() && request.url()!==config.url)
        return route.abort('blockedbyclient');
      return route.continue();
    }));
    const response=await bounded('Pinned GitHub navigation',25000,timeout=>
      page.goto(config.url,{waitUntil:'domcontentloaded',timeout}));
    report.http_status=response?.status() ?? null;
    report.observed_url=page.url();
    save();
    if (report.http_status!==200 || report.observed_url!==config.url)
      throw new Error('The exact pinned GitHub source did not return HTTP200');
    // Fixed settling interval, deliberately independent of renderer readiness.
    await bounded('Five-second settling wait',5500,()=>new Promise(resolve=>{
      const timer=setTimeout(resolve,5000);timer.unref();
    }));
    for (const viewport of VIEWPORTS) {
      const item={viewport,observed_at:new Date().toISOString(),errors:[]};
      report.observations.push(item);save();
      try {
        await bounded('Viewport',2000,()=>page.setViewportSize(viewport));
        item.data=await bounded('Read-only document evaluation',4000,()=>page.evaluate(inspectHostedDocument));
        save();
      } catch (error) {item.errors.push(String(error));save();}
      try {
        const html='upper-'+viewport.width+'.html';
        const content=await bounded('Hosted HTML',3000,()=>page.content());
        fs.writeFileSync(path.join(config.output,html),content);item.html=html;save();
      } catch (error) {item.errors.push(String(error));save();}
      try {
        const screenshot='upper-'+viewport.width+'.png';
        await bounded('Hosted screenshot',5000,timeout=>page.screenshot({
          path:path.join(config.output,screenshot),fullPage:true,timeout}));
        item.screenshot=screenshot;save();
      } catch (error) {item.errors.push(String(error));save();}
    }
  } catch (error) {report.errors.push(String(error));save();}
  finally {
    if (browser) {
      try {await bounded('Browser close',1000,()=>browser.close());}
      catch (error) {report.errors.push(String(error));}
    }
    save();
  }
  console.log('Supplementary hosted diagnostic only; no verification result: '+filename);
  return report.errors.length || report.observations.some(item=>item.errors.length) ? 1 : 0;
}

if (require.main===module) run().then(code=>{process.exit(code);}).catch(error=>{
  console.error('Supplementary diagnostic configuration error: '+String(error));process.exit(1);
});
module.exports={configuration,inspectHostedDocument,run};
