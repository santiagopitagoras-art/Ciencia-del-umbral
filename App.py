<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Atlas Psicodélico Mundial</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=EB+Garamond:ital,wght@0,400;1,400&family=Inconsolata:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --ink:#07090a;--ink2:#0d1214;--ink3:#141b1c;
  --gold:#c09840;--gold2:#d4ad54;--gold3:#eecb70;
  --gp:rgba(192,152,64,.11);--gb:rgba(192,152,64,.22);
  --vd:#3a8a78;--vd2:#4da896;--vd3:#70c0b0;
  --cr:#8a2828;--cr2:#b03838;
  --st:#6070b8;--st2:#8898d8;
  --t1:#bccaba;--t2:#889a88;--t3:#506050;
  --bd:rgba(192,152,64,.14);--bd2:rgba(192,152,64,.28);
}
html,body{height:100%;overflow:hidden;background:var(--ink);font-family:"Cormorant Garamond",Georgia,serif;color:var(--t1)}
::-webkit-scrollbar{width:3px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:var(--bd2);border-radius:2px}
.app{display:flex;flex-direction:column;height:100vh;overflow:hidden}
 
/* HEADER */
.hdr{flex-shrink:0;display:flex;align-items:center;justify-content:space-between;padding:.8rem 2rem;border-bottom:1px solid var(--bd);background:var(--ink2);position:relative;z-index:100}
.hdr::after{content:"";position:absolute;bottom:0;left:8%;right:8%;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
h1{font-size:1.6rem;font-weight:300;letter-spacing:.02em;color:#ece0c0}
h1 em{font-style:italic;color:var(--gold2)}
.hsub{font-family:"Inconsolata",monospace;font-size:.53rem;letter-spacing:.2em;text-transform:uppercase;color:var(--t3);margin-top:.2rem}
.hstats{display:flex;gap:1.3rem}
.hst .n{font-family:"Inconsolata",monospace;font-size:.95rem;font-weight:300;color:var(--gold2);display:block;line-height:1}
.hst .l{font-family:"Inconsolata",monospace;font-size:.44rem;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);display:block;margin-top:2px}
 
/* FILTERBAR */
.fbar{flex-shrink:0;display:flex;align-items:center;padding:0 2rem;border-bottom:1px solid var(--bd);background:rgba(7,9,10,.94);z-index:100}
.fb{font-family:"Inconsolata",monospace;font-size:.52rem;letter-spacing:.16em;text-transform:uppercase;padding:.48rem .8rem;cursor:pointer;color:var(--t3);background:none;border:none;border-bottom:1.5px solid transparent;transition:all .2s}
.fb:hover{color:var(--t1)}.fb.active{color:var(--gold2);border-bottom-color:var(--gold2)}
.fsep{width:1px;height:10px;background:var(--bd);margin:0 .3rem}
.leg{display:flex;gap:.85rem;margin-left:auto;padding-left:1.5rem}
.li{display:flex;align-items:center;gap:5px;font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.08em;text-transform:uppercase;color:var(--t3)}
.ld{width:7px;height:7px;border-radius:50%}
 
/* BODY */
.body{flex:1;display:grid;grid-template-columns:1fr 398px;overflow:hidden;min-height:0}
 
/* MAP */
.mpane{position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 55%,#091612 0%,#040908 100%)}
.mpane::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 58%,rgba(4,9,8,.7) 100%);pointer-events:none;z-index:2}
#msvg{width:100%;height:100%;display:block}
.mhint{position:absolute;bottom:.9rem;left:1.5rem;font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(80,96,80,.45);pointer-events:none}
 
/* SVG map styles */
.grat{stroke:rgba(58,138,120,.07);stroke-width:.4;fill:none}
.equator{stroke:rgba(192,152,64,.16);stroke-width:.7;stroke-dasharray:5,4;fill:none}
.land{fill:#19271e;stroke:rgba(70,150,120,.2);stroke-width:.5;transition:fill .15s}
.land:hover{fill:#21332a;cursor:pointer}
.mlabel{font-family:"Inconsolata",monospace;fill:rgba(192,152,64,.22);font-size:6px}
 
/* Markers */
.mk{cursor:pointer}
.mkr{fill:none;stroke-width:.7;animation:mkpulse 3.4s ease-in-out infinite}
.mkr2{fill:none;stroke-width:.45;animation:mkpulse 3.4s ease-in-out infinite .9s;opacity:.35}
.mkc{transition:r .18s}
.mk:hover .mkc{r:7}.mk.act .mkc{r:7.5}
.mk.act .mkr{stroke-width:1.4;animation:mkact 1.9s ease-in-out infinite}
@keyframes mkpulse{0%,100%{r:10;opacity:.2}50%{r:16;opacity:.55}}
@keyframes mkact{0%,100%{r:13;opacity:.6}50%{r:20;opacity:.95}}
 
/* Tooltip */
.mtt{position:absolute;background:rgba(7,9,10,.96);border:1px solid var(--bd2);padding:.42rem .75rem;border-radius:2px;font-family:"Cormorant Garamond",serif;font-style:italic;font-size:.83rem;color:#e8ddc0;white-space:nowrap;display:none;pointer-events:none;z-index:20;box-shadow:0 4px 20px rgba(0,0,0,.55)}
 
/* SIDEBAR */
.sb{border-left:1px solid var(--bd);background:var(--ink2);overflow-y:auto;overflow-x:hidden;display:flex;flex-direction:column}
.sb::before{content:"";display:block;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);flex-shrink:0;position:sticky;top:0;z-index:10}
 
/* Welcome */
.wlc{padding:1.7rem 1.7rem 1.4rem;flex:1}
.worn{text-align:center;font-size:1.1rem;color:var(--gold);opacity:.35;letter-spacing:.28em;margin-bottom:1rem}
.wlc h2{font-size:1.1rem;font-weight:300;font-style:italic;color:#d8ccb0;line-height:1.3;text-align:center;margin-bottom:.4rem}
.wrule{width:50px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:.5rem auto .8rem}
.wlc p{font-family:"EB Garamond",serif;font-size:.81rem;line-height:1.75;color:var(--t2);margin-bottom:.6rem;text-align:center}
.wlc p strong{color:var(--gold2);font-weight:500}.wlc p em{color:var(--vd3);font-style:italic}
.ititle{font-family:"Inconsolata",monospace;font-size:.49rem;letter-spacing:.2em;text-transform:uppercase;color:var(--t3);margin:1rem 0 .4rem;padding-bottom:.32rem;border-bottom:1px solid var(--bd)}
.iitem{display:flex;align-items:center;gap:8px;padding:.34rem .28rem;cursor:pointer;transition:all .15s;border-bottom:1px solid rgba(192,152,64,.04)}
.iitem:hover{background:var(--gp);padding-left:.55rem}
.idot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.iname{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:.86rem;color:#b0a882;transition:color .15s}
.iitem:hover .iname{color:var(--gold2)}
.ireg{font-family:"Inconsolata",monospace;font-size:.45rem;letter-spacing:.05em;padding:2px 5px;border-radius:1px;background:rgba(255,255,255,.03);border:1px solid var(--bd);color:var(--t3);margin-left:auto;white-space:nowrap}
 
/* Detail */
.det{display:none;flex-direction:column;padding-bottom:2rem}
.det.vis{display:flex;animation:dfade .28s ease}
@keyframes dfade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.dback{display:flex;align-items:center;gap:7px;font-family:"Inconsolata",monospace;font-size:.49rem;letter-spacing:.15em;text-transform:uppercase;color:var(--t3);cursor:pointer;padding:.75rem 1.7rem 0;transition:color .18s}
.dback:hover{color:var(--gold2)}
.dhero{padding:.9rem 1.7rem 1rem;border-bottom:1px solid var(--bd);position:relative}
.dhero::after{content:"";position:absolute;bottom:0;left:1.7rem;right:1.7rem;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.dbadge{font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.17em;text-transform:uppercase;margin-bottom:4px;display:flex;align-items:center;gap:6px}
.ddot{width:5px;height:5px;border-radius:50%}
.dname{font-family:"Cormorant Garamond",serif;font-size:1.8rem;font-weight:300;color:#ece0c0;line-height:1;letter-spacing:-.02em}
.dsci{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:.77rem;color:var(--t3);margin-top:3px}
.dtags{display:flex;flex-wrap:wrap;gap:4px;margin-top:.6rem}
.dt{font-family:"Inconsolata",monospace;font-size:.44rem;letter-spacing:.1em;text-transform:uppercase;padding:2px 6px;border-radius:1px;border:1px solid}
.dtr{color:var(--t2);border-color:rgba(136,154,136,.2);background:rgba(136,154,136,.04)}
.dts{color:var(--gold2);border-color:rgba(212,173,84,.2);background:rgba(212,173,84,.04)}
.dstats{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--bd)}
.dst{padding:.55rem .3rem;text-align:center;border-right:1px solid var(--bd)}
.dst:last-child{border-right:none}
.dstn{font-family:"Inconsolata",monospace;font-size:.88rem;font-weight:300;color:var(--gold2);display:block;line-height:1}
.dstl{font-family:"Inconsolata",monospace;font-size:.41rem;letter-spacing:.12em;text-transform:uppercase;color:var(--t3);display:block;margin-top:2px}
/* Section */
.dsec{border-bottom:1px solid var(--bd)}
.dsh{padding:.55rem 1.7rem;display:flex;align-items:center;gap:9px;cursor:pointer;user-select:none;transition:background .15s}
.dsh:hover{background:var(--gp)}
.dsi{width:15px;height:15px;display:flex;align-items:center;justify-content:center;font-size:.68rem;opacity:.55;flex-shrink:0}
.dst2{font-family:"Inconsolata",monospace;font-size:.49rem;letter-spacing:.17em;text-transform:uppercase;flex:1}
.dsa{font-size:.58rem;color:var(--t3);transition:transform .2s;flex-shrink:0}
.dsh.open .dsa{transform:rotate(90deg)}
.dsb{padding:0 1.7rem .85rem;display:none;font-family:"EB Garamond",serif;font-size:.81rem;line-height:1.78;color:#98a898}
.dsb.open{display:block}
/* Chem block */
.chem{font-family:"Inconsolata",monospace;font-size:.57rem;background:rgba(58,138,120,.07);border:1px solid rgba(58,138,120,.17);border-radius:2px;padding:.5rem .72rem;margin:.32rem 0;line-height:1.85;color:var(--vd3)}
.chem .cn{color:#e8ddc0;font-size:.59rem;display:block;margin-bottom:2px}
/* Pharma */
.phb{margin:0 1.7rem .75rem;padding:.62rem .78rem;background:rgba(96,112,184,.06);border:1px solid rgba(96,112,184,.16);border-radius:2px}
.phtitle{font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);margin-bottom:4px;display:block}
.phrow{display:flex;justify-content:space-between;border-bottom:1px solid rgba(96,112,184,.08);padding:1px 0}
.phrow:last-child{border-bottom:none}
.phk{font-family:"Inconsolata",monospace;font-size:.51rem;color:var(--t3)}
.phv{font-family:"Inconsolata",monospace;font-size:.52rem;color:#a8b0d8}
.chips{display:flex;flex-wrap:wrap;gap:5px;padding:.18rem 1.7rem .75rem}
.chc{font-family:"Inconsolata",monospace;font-size:.53rem;padding:3px 8px;border-radius:20px;background:rgba(58,138,120,.1);border:1px solid rgba(58,138,120,.25);color:var(--vd3)}
.cht{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:.79rem;padding:3px 9px;border-radius:1px;background:rgba(192,152,64,.07);border:1px solid rgba(192,152,64,.17);color:var(--gold2)}
.chu{font-family:"EB Garamond",serif;font-size:.79rem;padding:3px 9px;border-radius:1px;background:rgba(112,192,176,.06);border:1px solid rgba(112,192,176,.15);color:var(--vd3)}
.evw{padding:.18rem 1.7rem .85rem}
.evrow{display:flex;justify-content:space-between;margin-bottom:5px}
.evl{font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.1em;color:var(--t3)}
.evv{font-family:"Inconsolata",monospace;font-size:.47rem}
.evtr{height:3px;background:rgba(255,255,255,.05);border-radius:2px;overflow:hidden}
.evfi{height:100%;border-radius:2px;transition:width 1.1s cubic-bezier(.4,0,.2,1)}
.evtk{display:flex;justify-content:space-between;margin-top:3px}
.evtk span{font-family:"Inconsolata",monospace;font-size:.39rem;color:rgba(255,255,255,.12)}
.evno{font-family:"Inconsolata",monospace;font-size:.55rem;color:var(--t3);margin-top:.5rem;line-height:1.6;border-left:2px solid var(--bd2);padding-left:.55rem}
.challenge{margin:0 1.7rem .75rem;padding:.68rem .82rem;border-left:2px solid var(--cr2);background:rgba(138,40,40,.06);border-radius:0 2px 2px 0;font-family:"EB Garamond",serif;font-size:.79rem;line-height:1.7;color:rgba(220,156,136,.88)}
.qb{margin:0 1.7rem .75rem;padding:.68rem .92rem;border-left:2px solid var(--gold);background:var(--gp);font-family:"Cormorant Garamond",serif;font-style:italic;font-size:.87rem;line-height:1.67;color:#c8b888}
.qs{font-style:normal;font-family:"Inconsolata",monospace;font-size:.47rem;letter-spacing:.1em;text-transform:uppercase;color:var(--t3);display:block;margin-top:4px}
.refs{padding:0 1.7rem .38rem;display:flex;flex-direction:column}
.ref{padding:.46rem 0;border-bottom:1px solid rgba(192,152,64,.05);font-family:"EB Garamond",serif;font-size:.74rem;line-height:1.5;color:var(--t3);transition:color .15s}
.ref:hover{color:#b0a880}.ref:last-child{border-bottom:none}
.rau{color:#aca882;font-weight:500}.rti{font-style:italic;color:#8888a0}.rjo{color:var(--vd2);font-size:.67rem}
.rno{display:block;font-size:.65rem;color:var(--t3);font-style:italic;margin-top:1px;padding-left:.5rem;border-left:1px solid var(--bd)}
.rb{float:right;margin-left:5px;font-family:"Inconsolata",monospace;font-size:.39rem;letter-spacing:.1em;text-transform:uppercase;padding:2px 4px;border-radius:1px}
.rbs{background:rgba(58,138,120,.13);color:var(--vd3);border:1px solid rgba(58,138,120,.22)}
.rbe{background:rgba(192,152,64,.1);color:var(--gold2);border:1px solid rgba(192,152,64,.19)}
.rbl{background:rgba(96,112,184,.1);color:var(--st2);border:1px solid rgba(96,112,184,.19)}
 
/* trial badge */
.trb{display:inline-block;font-family:"Inconsolata",monospace;font-size:.46rem;letter-spacing:.1em;text-transform:uppercase;padding:2px 6px;border-radius:1px;margin:.2rem .2rem .2rem 0}
.trb-fda{background:rgba(64,160,96,.12);color:#60c080;border:1px solid rgba(64,160,96,.22)}
.trb-ph3{background:rgba(58,138,120,.12);color:var(--vd3);border:1px solid rgba(58,138,120,.22)}
.trb-ph2{background:rgba(192,152,64,.1);color:var(--gold2);border:1px solid rgba(192,152,64,.2)}
.trb-ph1{background:rgba(96,112,184,.1);color:var(--st2);border:1px solid rgba(96,112,184,.2)}
.trb-bt{background:rgba(176,56,56,.1);color:#d08080;border:1px solid rgba(176,56,56,.2)}
.trial-wrap{padding:.1rem 1.7rem .75rem;display:flex;flex-wrap:wrap;gap:2px}
</style>
</head>
<body>
<div class="app">
<div class="hdr">
  <div>
    <h1><em>Atlas</em> Psicodélico <span style="font-size:.9rem;font-weight:300;color:var(--t3)">mundial</span></h1>
    <div class="hsub">Plantas · Hongos · Química · Tradiciones · Ensayos Clínicos · Evidencia</div>
  </div>
  <div class="hstats">
    <div class="hst"><span class="n">14</span><span class="l">Especies</span></div>
    <div class="hst"><span class="n">~5700</span><span class="l">Años de uso</span></div>
    <div class="hst"><span class="n">50+</span><span class="l">Ensayos clínicos</span></div>
    <div class="hst"><span class="n">80+</span><span class="l">Referencias</span></div>
  </div>
</div>
 
<div class="fbar">
  <button class="fb active" onclick="filt('all',this)">Todo</button>
  <div class="fsep"></div>
  <button class="fb" onclick="filt('america',this)">Américas</button>
  <button class="fb" onclick="filt('africa',this)">África</button>
  <button class="fb" onclick="filt('asia',this)">Asia · Eurasia</button>
  <button class="fb" onclick="filt('oceania',this)">Oceanía</button>
  <button class="fb" onclick="filt('global',this)">Global</button>
  <div class="leg">
    <div class="li"><div class="ld" style="background:#4da896"></div>Planta</div>
    <div class="li"><div class="ld" style="background:#c09840"></div>Hongo</div>
    <div class="li"><div class="ld" style="background:#c07050"></div>Cactus</div>
    <div class="li"><div class="ld" style="background:#7080c8"></div>Semisint.</div>
    <div class="li"><div class="ld" style="background:#b040a0"></div>Delirante</div>
  </div>
</div>
 
<div class="body">
<div class="mpane">
<svg id="msvg" viewBox="0 0 960 500" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;display:block">
<defs>
  <radialGradient id="bg" cx="50%" cy="48%" r="65%">
    <stop offset="0%" stop-color="#0a1a14"/><stop offset="100%" stop-color="#040908"/>
  </radialGradient>
  <filter id="mglow" x="-70%" y="-70%" width="240%" height="240%">
    <feGaussianBlur stdDeviation="2.8" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect width="960" height="500" fill="url(#bg)"/>
<!-- Graticule -->
<g stroke="rgba(58,138,120,.07)" stroke-width=".4" fill="none">
  <line x1="0" y1="91.7" x2="960" y2="91.7"/>
  <line x1="0" y1="183.3" x2="960" y2="183.3"/>
  <line x1="0" y1="366.7" x2="960" y2="366.7"/>
  <line x1="0" y1="458.3" x2="960" y2="458.3"/>
  <line x1="120" y1="0" x2="120" y2="500"/>
  <line x1="240" y1="0" x2="240" y2="500"/>
  <line x1="480" y1="0" x2="480" y2="500" stroke="rgba(192,152,64,.1)"/>
  <line x1="720" y1="0" x2="720" y2="500"/>
  <line x1="840" y1="0" x2="840" y2="500"/>
</g>
<line stroke="rgba(192,152,64,.16)" stroke-width=".7" stroke-dasharray="5,4" fill="none" x1="0" y1="275" x2="960" y2="275"/>
<text x="8" y="272" fill="rgba(192,152,64,.22)" font-family="Inconsolata,monospace" font-size="6" letter-spacing="1">Ecuador</text>
<text x="8" y="90" fill="rgba(80,96,80,.35)" font-family="Inconsolata,monospace" font-size="6">60°N</text>
<text x="8" y="182" fill="rgba(80,96,80,.35)" font-family="Inconsolata,monospace" font-size="6">30°N</text>
<text x="8" y="368" fill="rgba(80,96,80,.32)" font-family="Inconsolata,monospace" font-size="6">30°S</text>
<text x="482" y="10" fill="rgba(192,152,64,.18)" font-family="Inconsolata,monospace" font-size="6">0°</text>
<!-- World map rendered by D3 + TopoJSON -->
<g id="landg"></g>
<!-- Plant markers -->
<g id="mkg"></g>
</svg>
<div class="mtt" id="mtt"></div>
<div class="mhint">Click en un marcador · <span id="rfilt">Todo el mundo</span></div>
</div>
 
<div class="sb" id="sb">
<div class="wlc" id="wp">
  <div class="worn">✦ ✦ ✦</div>
  <h2>Etnobotánica y neurociencia:<br><em>una cartografía de lo sagrado</em></h2>
  <div class="wrule"></div>
  <p>Este atlas une la <strong>sabiduría ritual indígena</strong> milenaria con la <em>investigación clínica contemporánea</em> del renacimiento psicodélico (2000–presente).</p>
  <p>Cada punto es un nudo entre el chamán y el laboratorio, entre la selva amazónica y Hopkins, entre 5700 a.C. y un ensayo de Fase III en 2025.</p>
  <div class="ititle">14 Especies — click para explorar</div>
  <div id="plist"></div>
</div>
<div class="det" id="dp"></div>
</div>
</div>
</div>
 
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/3.0.2/topojson.min.js"></script>
<script>
/* ── REAL WORLD MAP ── */
(async()=>{
  const landg=document.getElementById("landg");
  try{
    const world=await d3.json("https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json");
    const proj=d3.geoEquirectangular().scale(960/(2*Math.PI)).translate([480,275]);
    const path=d3.geoPath().projection(proj);
    const features=topojson.feature(world,world.objects.countries).features;
    features.forEach(f=>{
      const p=document.createElementNS("http://www.w3.org/2000/svg","path");
      p.setAttribute("d",path(f));
      p.setAttribute("fill","#19271e");
      p.setAttribute("stroke","rgba(70,150,120,.22)");
      p.setAttribute("stroke-width","0.5");
      landg.appendChild(p);
    });
  }catch(e){
    console.warn("Map CDN unavailable");
  }
})();
 
 
/* ════════════ PLANT DATA ════════════ */
// lon→x=(lon+180)*(960/360), lat→y=(90-lat)*(500/180)
function mxy(lon,lat){return[(lon+180)*(960/360),(90-lat)*(500/180)]}
 
const DB={
ayahuasca:{name:"Ayahuasca",sci:"Banisteriopsis caapi + Psychotria viridis",col:"#4da896",type:"Planta",rk:"america",region:"Amazonía",since:"~1000 a.C.",lon:-60,lat:-3,
trials:[{l:"MAPS Fase II — TEPT",cls:"trb-ph2"},{l:"UNIFESP RCT — Depresión resist.",cls:"trb-ph2"},{l:"Kings College — Neuroimagen",cls:"trb-ph2"},{l:"ICEERS — Seguridad",cls:"trb-ph1"}],
compounds:[{n:"N,N-DMT",f:"C₁₂H₁₆N₂",mw:"188.27",cl:"Triptamina",ac:"Agonista 5-HT2A/2C; sigma-1"},{n:"Harmina",f:"C₁₃H₁₂N₂O",mw:"212.25",cl:"β-carbolina",ac:"IMAO-A reversible; inhibe degradación del DMT oral"},{n:"Harmalina",f:"C₁₃H₁₄N₂O",mw:"214.26",cl:"β-carbolina",ac:"IMAO-A/B; bloqueo Ca²⁺"},{n:"Tetrahidroharman",f:"C₁₂H₁₄N₂",mw:"186.25",cl:"β-carbolina",ac:"IMAO débil; modulador DAT"}],
traditions:["Shipibo-Conibo (Perú)","Shuar (Ecuador)","Santo Daime (Brasil, 1930)","União do Vegetal — UDV","Curanderismo amazónico mestizo"],
mechanism:"Las β-carbolinas del Banisteriopsis caapi inhiben la MAO-A periférica, permitiendo biodisponibilidad oral del DMT de Psychotria viridis. En el SNC: agonismo 5-HT2A cortical, disrupción masiva de la DMN, aumento de conectividad entre redes normalmente segregadas. Activación límbica y prefrontal medial. La harmina también inhibe GSK-3β (neuroplasticidad y BDNF).",
uses:["TEPT (mayor evidencia emergente)","Depresión mayor resistente","Trastorno por uso de sustancias","Duelo complicado","Ansiedad existencial / cuidados paliativos"],
ev:72,trials_txt:"14 ensayos publicados (2010–2025). MAPS, ICEERS, UNIFESP, Kings College London. RCT con ayahuasca oral en depresión resistente: efecto antidepresivo 1–7 días (Palhano-Fontes 2019).",
challenge:"Variabilidad extrema de preparados. Imposibilidad de doble ciego real. Interacciones farmacológicas graves con IMAOs y serotoninérgicos. Turismo psicodélico no regulado: problema de salud pública y cultural.",
etno:"El término quechua significa 'soga del muerto' (aya=espíritu; wasca=bejuco). Richard Spruce la describe para Occidente en 1851. Uso en más de 75 etnias amazónicas. En el sistema Shipibo-Conibo, el onanya 've' la enfermedad como perturbación en el patrón de ícaros luminosos que rodea al cuerpo. Los ícaros son canciones sagradas que guían la experiencia.",
pharma:{"Inicio de acción":"20–60 min","Pico":"60–120 min","Duración total":"4–6 horas","DMT típico":"0.3–0.7 mg/kg","Vía":"Oral (decocción)","Riesgo con ISRS":"Alto — síndrome serotoninérgico"},
quote:{t:"La planta te dice qué cantar. El ícaro no viene de mí — viene del mundo donde la planta me lleva.",s:"— Curandera Shipibo (en Luna, 1986)"},
refs:[{a:"Palhano-Fontes, F. et al.",t:"Rapid antidepressant effects of ayahuasca in treatment-resistant depression",y:2019,j:"Psychological Medicine",tp:"s",n:"RCT — efecto antidepresivo 1–7 días post-sesión"},{a:"Shanon, B.",t:"The Antipodes of the Mind",y:2002,j:"Oxford Univ. Press",tp:"s",n:"Análisis cognitivo de 2500 experiencias"},{a:"Luna, L.E.",t:"Vegetalismo: Shamanism Among the Mestizo Population of the Peruvian Amazon",y:1986,j:"Almqvist & Wiksell",tp:"e",n:"Etnografía fundamental del curanderismo amazónico"},{a:"Reichel-Dolmatoff, G.",t:"The Shaman and the Jaguar",y:1975,j:"Temple Univ. Press",tp:"e",n:"Iconografía y cosmología tukano"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Análisis químico exhaustivo de DMT oral y β-carbolinas"}]},
 
psilocybe:{name:"Hongos Psilocybe",sci:"Psilocybe cubensis / mexicana / semilanceata",col:"#c09840",type:"Hongo",rk:"america",region:"Mesoamérica / Global",since:"~3500 a.C.",lon:-96,lat:17,
trials:[{l:"FDA Breakthrough Therapy 2018",cls:"trb-fda"},{l:"Hopkins — Depresión (Fase II)",cls:"trb-ph2"},{l:"Imperial College — TRD (RCT)",cls:"trb-ph2"},{l:"COMPASS — Fase III Europa",cls:"trb-ph3"},{l:"NYU — Alcohol (Fase II)",cls:"trb-ph2"},{l:"Hopkins — Tabaco 80% abstinencia",cls:"trb-ph2"}],
compounds:[{n:"Psilocibina",f:"C₁₂H₁₇N₂O₄P",mw:"284.25",cl:"Triptamina (profármaco)",ac:"→ psilocina por fosfatasas"},{n:"Psilocina",f:"C₁₂H₁₆N₂O",mw:"204.27",cl:"Triptamina (activa)",ac:"Agonista 5-HT2A/2C/2B; Ki≈6 nM"},{n:"Baeocistina",f:"C₁₁H₁₅N₂O₄P",mw:"270.22",cl:"Triptamina",ac:"Análogo N-mono-metil; actividad débil"},{n:"Norbaeocistina",f:"C₁₀H₁₃N₂O₄P",mw:"256.19",cl:"Triptamina",ac:"Precursor; trazas"}],
traditions:["Mazateca — María Sabina (veladas)","Mixteca (teonanácatl)","Zapoteca","Curanderismo oaxaqueño"],
mechanism:"Psilocibina (profármaco) → psilocina por desfosforilación. Agonista 5-HT2A cortical (Ki≈6 nM). Disrupción masiva de DMN + aumento de entropía neural (Carhart-Harris 2014). Modelo REBUS (2019): reduce peso de creencias predictivas previas bajo Free Energy Principle — mayor plasticidad y apertura al cambio.",
uses:["Depresión mayor resistente (FDA Breakthrough 2018)","Ansiedad en cáncer terminal","TOC refractario","Dependencia al tabaco (80% abstinencia a 6 meses)","Dependencia al alcohol","Cefalea en racimos","Anorexia nerviosa (exploratorio)"],
ev:90,trials_txt:"40+ ensayos clínicos activos (2025). Johns Hopkins, Imperial College London, NYU, UCSF, Yale. COMPASS Pathways en Fase III para depresión resistente. FDA Breakthrough Therapy Designation (2018).",
challenge:"Estandarización del set & setting como variable terapéutica no farmacológica. Debate: ¿es la experiencia mística el mecanismo o un epifenómeno? Apropiación del uso mazateca.",
etno:"Wasson y Heim documentan el uso mazateca en Life Magazine (1957). María Sabina, curandera mazateca de Huautla, condujo veladas curativas con teonanácatl. Más tarde lamentó: 'los forasteros han corrompido el poder'. Representaciones en cerámica Teotihuacán (~100 d.C.). Castaneda teje hongos y peyote en su obra sobre don Juan Matus — influencia cultural masiva aunque su status académico sigue debatido.",
pharma:{"Dosis umbral":"1–3 mg psilocibina","Dosis moderada":"10–20 mg","Dosis alta (estudio)":"25–30 mg","Inicio":"20–40 min","Pico":"60–90 min","Duración":"4–6 h","Biodisponibilidad oral":"~50%","t½ psilocina":"160 ± 40 min"},
quote:{t:"Debajo del hongo se encuentra el secreto del cielo. Es el camino para conocer lo que no sabemos.",s:"— María Sabina (en Estrada, 1981)"},
refs:[{a:"Carhart-Harris, R. & Friston, K.",t:"REBUS and the Anarchic Brain",y:2019,j:"Pharmacological Reviews",tp:"s",n:"Marco teórico unificado del campo psicodélico"},{a:"Davis, A.K. et al.",t:"Effects of psilocybin-assisted therapy on major depressive disorder",y:2021,j:"JAMA Psychiatry",tp:"s",n:"RCT — mayor relevancia clínica actual"},{a:"Carhart-Harris, R.",t:"The entropic brain",y:2014,j:"Front Hum Neurosci",tp:"s",n:"Hipótesis del cerebro entrópico"},{a:"Wasson, R.G.",t:"Seeking the Magic Mushroom",y:1957,j:"Life Magazine",tp:"e",n:"Primer documento masivo sobre uso ritual mazateca"},{a:"Castaneda, C.",t:"The Teachings of Don Juan",y:1968,j:"Univ. California Press",tp:"l",n:"Obra influyente que popularizó hongos/peyote en Occidente"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Perfil químico completo de Psilocybe; análisis de triptaminas"},{a:"Stamets, P.",t:"Psilocybin Mushrooms of the World",y:1996,j:"Ten Speed Press",tp:"e",n:"Guía botánica de referencia y distribución global"}]},
 
peyote:{name:"Peyote",sci:"Lophophora williamsii (Lem.) J.M.Coult.",col:"#c07050",type:"Cactus",rk:"america",region:"México / Suroeste EEUU",since:"~5700 a.C.",lon:-101,lat:24,
trials:[{l:"Mescalina Fase I (UCSF 2022)",cls:"trb-ph1"},{l:"Zendo Project — Mescalina",cls:"trb-ph1"}],
compounds:[{n:"Mescalina",f:"C₁₁H₁₇NO₃",mw:"211.26",cl:"Feniletilamina",ac:"Agonista 5-HT2A/2C; débil D1/D2"},{n:"Norpeyotina",f:"C₁₀H₁₅NO₃",mw:"197.23",cl:"Feniletilamina",ac:"Análogo; actividad moderada"},{n:"+30 alcaloides",f:"—",mw:"—",cl:"Varios",ac:"Contribuyen al efecto entourage"}],
traditions:["Huichol / Wixáritari (peregrinación a Wirikuta)","Tarahumara / Rarámuri","Native American Church","Cora / Náyari"],
mechanism:"Mescalina: agonista 5-HT2A/2C con afinidad adicional D1/D2 dopaminérgico. Produce experiencias visuales ricas, sinestesias y alteraciones profundas de la autoimagen. Duración 10–12 h por metabolismo más lento (N-acetilación hepática).",
uses:["Bienestar psicológico (uso consuetudinario indígena)","Alcoholismo — estudios preliminares en contexto indígena","Mescalina sintética: depresión (fase I/II emergente)"],
ev:38,trials_txt:"Estudios muy limitados por protección cultural y Clase I. Mescalina sintética: UCSF (2022–), Zendo Project. Conflicto ético sobre investigación vs. soberanía cultural.",
challenge:"Lophophora williamsii en peligro (IUCN). Explotación para turismo amenaza poblaciones silvestres. La mescalina sintética como alternativa ética — debate en curso.",
etno:"Coprolitos con alcaloides de peyote en Shumla Cave (Texas) datan ~5700–3700 a.C. (El-Seedi 2005). Los Wixáritari realizan peregrinación de ~900 km a pie desde Jalisco hasta Wirikuta en recreación cosmológica del origen del mundo. Castaneda describe el peyote como 'Mescalito', una entidad/maestro independiente, en sus obras sobre don Juan.",
pharma:{"Dosis activa mescalina":"200–400 mg","Contenido en cactus fresco":"~0.3–0.5%","Inicio":"1–2 h","Pico":"4–6 h","Duración":"10–12 h","Tolerancia cruzada":"Completa con psilocibina y LSD"},
quote:{t:"El peyote nos enseña a ver de nuevo. Cuando lo tomás por primera vez, ves todo lo que existe.",s:"— Ramón Medina Silva, mara'akame Wixáritari (en Myerhoff, 1974)"},
refs:[{a:"El-Seedi, H. et al.",t:"Prehistoric peyote use: alkaloid analysis and radiocarbon dating",y:2005,j:"J Ethnopharmacology",tp:"s",n:"Confirma 5700 a.C. — uso más antiguo documentado"},{a:"Schultes, R.E. & Hofmann, A.",t:"Plants of the Gods",y:1979,j:"Healing Arts Press",tp:"e",n:"Referencia etnobotánica canónica global"},{a:"Myerhoff, B.",t:"Peyote Hunt: The Sacred Journey of the Huichol Indians",y:1974,j:"Cornell Univ. Press",tp:"e",n:"Etnografía insuperable de la peregrinación wixáritari"},{a:"Castaneda, C.",t:"The Teachings of Don Juan",y:1968,j:"Univ. California Press",tp:"l",n:"Peyote como 'Mescalito' — maestro y aliado en el aprendizaje chamánico"},{a:"Shulgin, A. & Shulgin, A.",t:"PiHKAL: A Chemical Love Story",y:1991,j:"Transform Press",tp:"l",n:"Síntesis y perfil subjetivo de mescalina y 200+ feniletilaminas"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Farmacología detallada; síntesis histórica de 3,4,5-trimetoxifenetilamina"}]},
 
sanpedro:{name:"San Pedro / Wachuma",sci:"Echinopsis pachanoi",col:"#c07050",type:"Cactus",rk:"america",region:"Andes — Perú, Ecuador, Bolivia",since:"~2000 a.C.",lon:-76,lat:-10,
trials:[{l:"Mescalina Fase I (derivado)",cls:"trb-ph1"}],
compounds:[{n:"Mescalina",f:"C₁₁H₁₇NO₃",mw:"211.26",cl:"Feniletilamina",ac:"Idéntico al peyote — 5-HT2A/2C"},{n:"3,4-DMPEA",f:"C₁₀H₁₅NO₂",mw:"181.23",cl:"Feniletilamina",ac:"Actividad sinérgica"}],
traditions:["Curanderismo andino norteño (Trujillo, Lambayeque)","Mesa norte peruana","Comunidades Q'ero","Chamanismo ecuatoriano"],
mechanism:"Idéntico al peyote. Mescalina es el principal alcaloide activo. Concentración muy variable (0.01–2% peso seco) según condiciones de crecimiento. Duración 8–12 h.",
uses:["Sin ensayos clínicos formales independientes","Investigación derivada de estudios con mescalina sintética"],
ev:28,trials_txt:"Datos derivados de estudios de mescalina sintética. Proliferación de retiros no regulados como problema emergente de salud pública.",
challenge:"Confusión sistemática entre turismo psicodélico y uso sagrado. Presión comercial sobre curanderos tradicionales. Paradoja legal: cultivable en Argentina y muchos países.",
etno:"Representaciones en cerámica Chavín (~2000 a.C.) y textiles Tiwanaku. El curandero andino norteño trabaja con la 'mesa': altar de objetos sagrados que representan el cosmos andino. El ritual sucede de noche hasta el amanecer. Douglas Sharon (1978) documentó al curandero Eduardo Calderón 'El Tuno'.",
pharma:{"Mescalina por kg fresco":"0.1–2 g/kg (muy variable)","Preparación":"30–50 cm de cactus cocido","Inicio":"1–2 h","Duración":"8–12 h"},
quote:{t:"El wachuma no se toma — se pide. Hay que pedirle permiso a la planta y al cerro donde creció.",s:"— Eduardo Calderón Palomino 'El Tuno' (en Sharon, 1978)"},
refs:[{a:"Sharon, D.",t:"Wizard of the Four Winds: A Shaman's Story",y:1978,j:"Free Press",tp:"e",n:"Etnografía fundamental del curanderismo andino con San Pedro"},{a:"Glass-Coffin, B.",t:"The Gift of Life",y:1998,j:"Univ. New Mexico Press",tp:"e"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Análisis fitoquímico de mescalina en cactáceas columnares"}]},
 
vilca:{name:"Vilca / Yopo",sci:"Anadenanthera colubrina / peregrina",col:"#4da896",type:"Planta",rk:"america",region:"Gran Chaco · Amazonía · Andes",since:"~4000 a.C.",lon:-62,lat:-22,
trials:[{l:"5-MeO-DMT Fase I/II (Beckley)",cls:"trb-ph1"},{l:"Bufotenina — Investigación preclínica",cls:"trb-ph1"}],
compounds:[{n:"Bufotenina (5-OH-DMT)",f:"C₁₂H₁₆N₂O",mw:"204.27",cl:"Triptamina",ac:"Agonista 5-HT2A/2B/4; sigma-1; activo inhalado"},{n:"5-MeO-DMT",f:"C₁₃H₁₈N₂O",mw:"218.30",cl:"Triptamina",ac:"10–30x más potente que DMT; agonista 5-HT1A/2A"},{n:"N,N-DMT",f:"C₁₂H₁₆N₂",mw:"188.27",cl:"Triptamina",ac:"Agonista 5-HT2A/2C; trazas"}],
traditions:["Culturas andinas precolombinas (Tiwanaku, Wari)","Yanomami (Venezuela/Brasil)","Gran Chaco (Toba, Qom, Wichí)","Pueblos del NOA argentino"],
mechanism:"La bufotenina fue considerada inactiva oralmente hasta estudios recientes que demostraron su potente actividad alucinógena inhalada. El 5-MeO-DMT, aunque en trazas, contribuye significativamente por su extrema potencia. La sinergia de múltiples triptaminas con distintos perfiles de receptor produce el efecto total.",
uses:["Sin ensayos clínicos de vilca integral","5-MeO-DMT: ensayos emergentes en depresión y TEPT","Bufotenina en fase I inicial"],
ev:10,trials_txt:"Sin ensayos de vilca integral. 5-MeO-DMT: Beckley Foundation, MAPS (investigación activa). Bufotenina: investigación preclínica.",
challenge:"Bufotenina en Schedule I (clasificación históricamente basada en datos inexactos). Conocimiento ceremonial en riesgo de extinción en comunidades del NOA argentino y boliviano.",
etno:"Pipas de hueso con residuos alcaloidales en tumbas del NOA (San Pedro de Atacama, Puna de Jujuy) datadas ~4000–500 a.C. Torres & Repke (2006) documentaron 600+ artefactos arqueológicos relacionados. Los Yanomami usan el yopo (epena) para comunicarse con los hekura (espíritus) en rituales de curación.",
pharma:{"Vía":"Inhalación nasal (snuff)","Preparación":"Semillas tostadas + cal (ceniza de Cecropia)","Inicio":"2–5 min","Duración":"15–30 min"},
quote:{t:"El yopo me lleva a ver los antepasados que viven dentro de las montañas. Ellos saben dónde está la enfermedad.",s:"— Chamán Yanomami (en Schultes & Hofmann, 1979)"},
refs:[{a:"Torres, C.M. & Repke, D.B.",t:"Anadenanthera: Visionary Plant of Ancient South America",y:2006,j:"Haworth Press",tp:"e",n:"Monografía arqueobotánica fundamental — 600+ artefactos"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Análisis de bufotenina, 5-MeO-DMT y controversia sobre psicoactividad"},{a:"Shulgin, A. & Shulgin, A.",t:"TIHKAL",y:1997,j:"Transform Press",tp:"l",n:"Perfiles completos de bufotenina y 5-MeO-DMT; síntesis y efectos"}]},
 
salvia:{name:"Salvia divinorum",sci:"Salvia divinorum Epling & Játiva",col:"#7080c8",type:"Planta",rk:"america",region:"Sierra Mazateca, Oaxaca",since:"Precolombino (doc. 1962)",lon:-96.8,lat:18.2,
trials:[{l:"Hopkins — Depresión Fase I (2023)",cls:"trb-ph1"},{l:"Perfil κ-opioide — Investigación básica",cls:"trb-ph1"}],
compounds:[{n:"Salvinorina A",f:"C₂₃H₂₈O₈",mw:"432.46",cl:"Diterpeno neoclerodan",ac:"Agonista κ-opioide (Ki≈1.7 nM). Único psicoactivo natural no-nitrogenado"}],
traditions:["Mazateca — ska Pastora (hoja de la Pastora)","Veladas de curación y adivinación"],
mechanism:"ÚNICO psicodélico potente de origen natural que opera EXCLUSIVAMENTE vía receptores κ-opioides — sin actividad en 5-HT2A (la vía de todos los demás psicodélicos clásicos). Es un terpenoide sin nitrógeno, atraviesa la BHE por difusión pasiva. Produce efectos disociativos radicalmente distintos a LSD o psilocibina.",
uses:["Investigación básica en sistemas κ-opioide","Potencial analgésico (modelos animales)","Depresión — Fase I emergente (Hopkins 2023)","Adicciones (perfil κ anti-recompensa)"],
ev:22,trials_txt:"Fase I emergente en Johns Hopkins (2023). Interés creciente por perfil farmacológico único en adicciones y dolor crónico.",
challenge:"Efectos disociativos severos dificultan diseño terapéutico. La cultura mazateca considera su uso exclusivamente sagrado y objeta la comercialización.",
etno:"Epling & Játiva la describen para la ciencia en 1962. Los mazatecos la llaman 'ska María Pastora' — sincretismo entre su función como mediadora divina y el catolicismo colonial. Salvinorina A aislada por Ortega en 1982. Todos los especímenes son probablemente clones de un único individuo ancestral. Cultivable legalmente en Argentina.",
pharma:{"Dosis activa fumada":"200–500 µg salvinorina A","Inicio fumado":"15–30 seg","Pico":"1–5 min","Duración fumado":"10–20 min","Duración masticado":"30–90 min"},
quote:{t:"Ella no te habla con palabras. Te muestra imágenes que son también sensaciones. Después de verla, entendés cosas que no podés explicar.",s:"— Curandero mazateco (en Siebert, 1994)"},
refs:[{a:"Roth, B.L. et al.",t:"Salvinorin A: a potent naturally occurring κ-opioid selective agonist",y:2002,j:"PNAS",tp:"s",n:"Demostración definitiva del mecanismo κ-opioide selectivo"},{a:"Valdés, L.J.",t:"Salvia divinorum and the Unique Diterpene Hallucinogen",y:1994,j:"J Psychoactive Drugs",tp:"s"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Contexto comparativo; estructura única sin nitrógeno"}]},
 
datura:{name:"Datura / Toloache",sci:"Datura stramonium / inoxia",col:"#b040a0",type:"Planta",rk:"america",region:"México · SW EEUU · India",since:"~1000 a.C.",lon:-106,lat:26,
trials:[{l:"Escopolamina IV — Antidepresivo NIMH",cls:"trb-ph2"},{l:"Escopolamina — Antiemético (aprobado)",cls:"trb-fda"}],
compounds:[{n:"Escopolamina",f:"C₁₇H₂₁NO₄",mw:"303.35",cl:"Tropano",ac:"Antagonista muscarínico M1–M5"},{n:"Atropina",f:"C₁₇H₂₃NO₃",mw:"289.37",cl:"Tropano",ac:"Antagonista muscarínico no selectivo; midriasis"},{n:"Hiosciamina",f:"C₁₇H₂₃NO₃",mw:"289.37",cl:"Tropano",ac:"L-isómero activo de atropina"}],
traditions:["Chamanes Chumash (California — momoy)","Iniciación Tolache (México)","Medicina Ayurveda (D. metel)","Ungüentos de brujas medievales (Europa)","Chamanismo Zuñi y Navajo"],
mechanism:"A diferencia de todos los demás psicodélicos de este atlas, la datura NO actúa vía serotonina sino vía bloqueo colinérgico. Antagonismo de receptores muscarínicos M1–M5 produce: delirio confusional severo, alucinaciones no distinguibles de la realidad, amnesia, midriasis, taquicardia. Margen dosis alucinógena / dosis letal: MÍNIMO.",
uses:["Escopolamina IV: antidepresivo de acción rápida (NIMH)","Parches escopolamina: antiemético aprobado","⚠️ USO PSICODÉLICO: NO RECOMENDADO — riesgo de muerte"],
ev:25,trials_txt:"Escopolamina como antidepresivo de acción rápida: estudios del NIMH (Murrough 2013). Sin ensayos de datura integral — toxicidad extrema lo impide.",
challenge:"⚠️ ADVERTENCIA GRAVE: La datura ha causado numerosas muertes. El delirio anticolinérgico es psicosis sin insight, no un 'viaje'. El turismo psicodélico que la promueve es irresponsable. Antídoto (fisostigmina IV) solo en emergencias hospitalarias.",
etno:"Los chamanes Chumash preparaban momoy con dosis extremadamente cuidadosas — sin supervisión chamánica, el uso era reconocido como suicidio. Los 'ungüentos de bruja' medievales (datura + belladona + mandrágora + beleño en grasa) producían sensación de vuelo por absorción transdérmica. Castaneda describe la datura como 'la planta del diablo' en A Separate Reality — peligrosa y femenina, opuesta al peyote masculino.",
pharma:{"⚠️ ADVERTENCIA":"Margen terapéutico extremadamente estrecho","Atropina letal":"~2–4 mg en adultos","Inicio":"30–60 min","Duración":"12–48 horas","Antídoto":"Fisostigmina IV (solo hospital)"},
quote:{t:"No hay ninguna planta más peligrosa que el jimsonweed. Un poco más de lo necesario y ya no estás aquí para contarlo.",s:"— Richard Evans Schultes (Plants of the Gods, 1979)"},
refs:[{a:"Schultes, R.E. & Hofmann, A.",t:"Plants of the Gods",y:1979,j:"Healing Arts Press",tp:"e",n:"Descripción del uso chamánico y advertencias de toxicidad"},{a:"Castaneda, C.",t:"A Separate Reality",y:1971,j:"Simon & Schuster",tp:"l",n:"Datura como 'planta del diablo' en el aprendizaje de don Juan"}]},
 
iboga:{name:"Iboga / Ibogaína",sci:"Tabernanthe iboga Baill.",col:"#4da896",type:"Planta",rk:"africa",region:"Gabón · Congo · Camerún",since:"~1000 d.C. (documentado)",lon:12,lat:-1,
trials:[{l:"Stanford — Opioides Fase II",cls:"trb-ph2"},{l:"MAPS — Opioides",cls:"trb-ph2"},{l:"UCSF — Investigación activa",cls:"trb-ph2"},{l:"UNESCO Patrimonio Inmaterial 2022",cls:"trb-bt"}],
compounds:[{n:"Ibogaína",f:"C₂₀H₂₆N₂O",mw:"310.43",cl:"Ibogano",ac:"Antagonista NMDA; agonista σ₁/σ₂; inhibe DAT/SERT/NAT; agonista κ/μ opioide"},{n:"Noribogaína (metabolito activo)",f:"C₁₉H₂₄N₂O",mw:"296.41",cl:"Ibogano",ac:"SERT inhibidor; μ-opioide agonista; t½ de días"},{n:"Ibogamina",f:"C₁₉H₂₄N₂",mw:"280.41",cl:"Ibogano",ac:"Débilmente activa; modula el perfil"}],
traditions:["Bwiti Fang — rito de paso ngozé","Bwiti Mitsogo y Punu","Misoko healing","Uso chamánico Baka (pigmeos)"],
mechanism:"Perfil farmacológico más complejo de todos los psicodélicos conocidos. Actúa simultáneamente como: antagonista NMDA + agonista σ₁/σ₂ + inhibidor DAT/SERT/NAT + agonista κ/μ opioide. El metabolito noribogaína (t½ 28–49 h) es responsable del efecto anti-adictivo prolongado. Mecanismo en adicciones: 'reset' de neuroadaptación dopaminérgica acumulada.",
uses:["Dependencia a opiáceos — mayor evidencia clínica","Dependencia a cocaína y alcohol","TEPT","Depresión resistente"],
ev:65,trials_txt:"Stanford Psychedelic Science Group (Fase II). UCSF. MAPS. Clínicas autorizadas en México, Costa Rica, Nueva Zelanda, Países Bajos. 50–80% reducción de síntomas de abstinencia en una sesión.",
challenge:"Riesgo cardíaco real: prolongación QT. Muertes reportadas sin monitoreo cardíaco. Requiere ECG y screening previo.",
etno:"El rito bwiti (ngozé) puede durar 3–7 noches. El iniciado consume dosis muy altas para 'morir y renacer' — visitar a los antepasados y recibir instrucción directa. El nganga (guía) acompaña, no controla. UNESCO reconoció al Bwiti Gabonés como Patrimonio Cultural Inmaterial en 2022. James Fernandez (1982) escribió la monografía etnográfica más completa en 1000 páginas.",
pharma:{"Dosis terapéutica":"12–20 mg/kg","Dosis ritual Bwiti":"~15–30 mg/kg","Inicio":"45–90 min","Duración":"18–36 h","t½ noribogaína":"28–49 h","⚠️ Riesgo QT":"Alto — ECG obligatorio"},
quote:{t:"La iboga no es una droga. Es un rito de paso. Te lleva ante tus antepasados y ellos te dicen cómo vivir.",s:"— Nguema Mintsa, nganga bwiti (en Fernandez, 1982)"},
refs:[{a:"Fernandez, J.W.",t:"Bwiti: An Ethnography of the Religious Imagination in Africa",y:1982,j:"Princeton Univ. Press",tp:"e",n:"Monografía etnográfica de 1000 páginas — referencia insustituible"},{a:"Noller, G. et al.",t:"Ibogaine treatment outcomes for opioid dependence: 12-month follow-up",y:2012,j:"Am J Drug Alcohol Abuse",tp:"s"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Perfil fitoquímico completo de Tabernanthe iboga y alcaloides ibogano"}]},
 
cannabis:{name:"Cannabis Ritual",sci:"Cannabis sativa / indica",col:"#4da896",type:"Planta",rk:"asia",region:"Asia Central / Himalaya",since:"~3000 a.C.",lon:75,lat:30,
trials:[{l:"FDA — Epidiolex (CBD) aprobado",cls:"trb-fda"},{l:"Sativex (THC+CBD) EM aprobado",cls:"trb-fda"},{l:"Dronabinol — Náuseas (FDA)",cls:"trb-fda"},{l:"TEPT — Múltiples ensayos activos",cls:"trb-ph2"}],
compounds:[{n:"Δ9-THC",f:"C₂₁H₃₀O₂",mw:"314.46",cl:"Terpenoide",ac:"Agonista CB1/CB2; modulador GABA/glutamato"},{n:"CBD",f:"C₂₁H₃₀O₂",mw:"314.46",cl:"Terpenoide",ac:"Antagonista CB1 débil; agonista 5-HT1A/TRPV1"},{n:"β-Cariofileno",f:"C₁₅H₂₄",mw:"204.35",cl:"Sesquiterpeno",ac:"Agonista CB2; antiinflamatorio"}],
traditions:["Tantrismo shivaíta (bhang — Atharva Veda ~1500 a.C.)","Sadhus hinduistas","Uso escita (Heródoto ~450 a.C.)","Sufismo (hashishin)","Rastafari (ganja sagrado)"],
mechanism:"El sistema endocannabinoide es modulación retrógrada neuronal. El THC exógeno imita y amplifica la anandamida endógena. Efecto entourage: sinergia entre THC, CBD, CBN y terpenos produce efectos distintos a cualquier compuesto aislado.",
uses:["Dolor crónico neuropático","TEPT (coadyuvante)","Náuseas oncológicas","Epilepsia (Epidiolex FDA 2018)","Esclerosis múltiple (Sativex)"],
ev:80,trials_txt:"Epidiolex (CBD puro) aprobado FDA 2018. Sativex (THC+CBD) aprobado en EM. Cannabis medicinal legal en 40+ países. Múltiples RCTs en dolor, TEPT y náuseas.",
challenge:"Heterogeneidad entre preparados y quimiotipos. Riesgo de psicosis con predisposición genética (COMT val158met). Cannabis de alta potencia en adolescentes: factor de riesgo documentado.",
etno:"Atharva Veda (~1500 a.C.): el bhang es una de las cinco plantas sagradas. Heródoto documenta vapor ritual escita en tiendas ~450 a.C. — arqueólogos encontraron pipas con residuos en tumbas escitas de Crimea (~2500 a.C.). El término 'hashishin' — origen de 'asesino' — es probablemente una calumnia medieval.",
pharma:{"Biodisponibilidad inhalada":"25–35%","Biodisponibilidad oral":"6–20%","THC fumado pico":"10–30 min","t½ THC":"20–36 h"},
quote:{t:"El bhang limpia el pecado, lo libera, lo eleva. El bhang es la alegría del dios Shiva.",s:"— Texto devocional hinduista (en Ott, Pharmacotheon, 1993)"},
refs:[{a:"Russo, E.B.",t:"Taming THC: potential cannabis synergy and the entourage effect",y:2011,j:"British J Pharmacol",tp:"s",n:"Hipótesis del entourage"},{a:"Merlin, M.D.",t:"Archaeological evidence for tradition of psychoactive plant use in the Old World",y:2003,j:"Economic Botany",tp:"e"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Historia etnobotánica completa del cannabis en rituales de todas las culturas"}]},
 
amanita:{name:"Amanita muscaria — Soma",sci:"Amanita muscaria (L.) Lam.",col:"#c09840",type:"Hongo",rk:"asia",region:"Siberia · Escandinavia · Himalayas",since:"~4000 a.C. (hipótesis)",lon:100,lat:62,
trials:[{l:"Muscimol — Preclínico activo",cls:"trb-ph1"},{l:"Amanita Therapeutics (startup 2023)",cls:"trb-ph1"}],
compounds:[{n:"Muscimol",f:"C₄H₆N₂O₂",mw:"114.10",cl:"Isoxazol aminado",ac:"Agonista GABA-A potente — mecanismo único"},{n:"Ácido iboténico (precursor)",f:"C₅H₆N₂O₄",mw:"158.11",cl:"Aminoácido excitatorio",ac:"Neurotóxico en seta fresca — se convierte en muscimol por secado"}],
traditions:["Chamanismo siberiano Evenki/Koryak/Chukchi","Transmisión vía orina ritual","Hipótesis Soma védico (Wasson 1968)"],
mechanism:"Radicalmente distinto de todos los demás psicodélicos. El muscimol actúa como agonista potente de GABA-A (la principal vía inhibitoria cerebral) — NO sobre serotonina. Produce disociación, macropsia/micropsia, sueños despiertos vívidos. CLAVE: el secado (48–72h a <55°C) convierte el ácido iboténico neurotóxico en muscimol activo.",
uses:["Sin ensayos clínicos formales (2025)","Muscimol: interés emergente en ansiedad e insomnio (perfil GABAérgico único)"],
ev:12,trials_txt:"Sin ensayos clínicos. Muscimol en fases preclínicas. Amanita Therapeutics (startup) en investigación (2023+).",
challenge:"Confusión entre ácido iboténico (seta fresca, neurotóxico) y muscimol (seta seca, activo) genera intoxicaciones graves. Hipótesis Soma de Wasson: no consensuada.",
etno:"Wasson (1968) propone que el Soma del Rigveda es Amanita muscaria. El uso chamánico siberiano es el más documentado: el chamán consume, orina, y los participantes beben la orina para aprovechar el muscimol ya metabolizado. Los renos del Ártico buscan activamente Amanita. Posible nexo con el mito de Santa Claus: el chamán lapón de traje rojo y blanco (colores de Amanita) visitando familias en invierno.",
pharma:{"Muscimol activo (seca)":"5–10 mg","Secado para conversión":"48–72h a <55°C","Inicio":"30–90 min","Duración":"4–8 h"},
quote:{t:"El chamán bebe el jugo del hongo y ve el mundo espiritual. Luego le damos su orina a los que no pueden tomar el hongo — funciona igual.",s:"— Relato de chamán Koryak (en Wasson, 1968)"},
refs:[{a:"Wasson, R.G.",t:"Soma: Divine Mushroom of Immortality",y:1968,j:"Harcourt Brace",tp:"e",n:"Hipótesis fundacional Soma=Amanita. Influyente y controvertida."},{a:"Michelot, D. & Melendez-Howell, L.M.",t:"Amanita muscaria: chemistry, biology, toxicology, and ethnomycology",y:2003,j:"Mycological Research",tp:"s"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Análisis crítico de la hipótesis Soma; farmacología del muscimol"}]},
 
harmala:{name:"Harmal / Esfand",sci:"Peganum harmala L.",col:"#c09840",type:"Planta",rk:"asia",region:"Persia · Asia Central · Mediterráneo",since:"~3000 a.C.",lon:53,lat:35,
trials:[{l:"Harmina — Antidepresivo preclínico",cls:"trb-ph1"},{l:"Parkinson — Estudios preliminares",cls:"trb-ph1"}],
compounds:[{n:"Harmina",f:"C₁₃H₁₂N₂O",mw:"212.25",cl:"β-carbolina",ac:"IMAO-A reversible potente; inhibe GSK-3β (neuroplasticidad)"},{n:"Harmalina",f:"C₁₃H₁₄N₂O",mw:"214.26",cl:"β-carbolina",ac:"IMAO-A/B; bloqueo Ca²⁺; sedante a dosis altas"},{n:"Tetrahidroharman",f:"C₁₂H₁₄N₂",mw:"186.25",cl:"β-carbolina",ac:"IMAO débil; modulador DAT"}],
traditions:["Zoroastrismo (haoma — posiblemente)","Islam sufí (humo de esfand para purificación)","Medicina persa y árabe clásica (Ibn Sina)","Norte de África (bakhour)","Componente de 'anahuasca'"],
mechanism:"Las β-carbolinas de Peganum harmala son los más potentes inhibidores de MAO-A de origen vegetal conocidos. Su rol principal: potenciador de otras sustancias — hace biodisponible el DMT oral. La harmina también inhibe GSK-3β (neuroplasticidad, BDNF) — relevante en depresión.",
uses:["Componente de 'anahuasca' (DMT + harmala)","Antidepresivo potencial (harmina vía GSK-3β/BDNF)","Antiparasitario (malaria, Leishmania — in vitro)"],
ev:28,trials_txt:"Fortunato (2010): harmina produce efectos antidepresivos en modelos animales vía BDNF. Sin ensayos clínicos propios. Investigación activa en combinaciones.",
challenge:"Interacciones peligrosas con tiramina (crisis hipertensivas) y serotoninérgicos. Semillas contienen dosis potencialmente tóxicas.",
etno:"Mencionada en textos persas desde ~3000 a.C. como planta de fuego y purificación. En Irán y Afganistán, quemar semillas de esfand es práctica cotidiana para purificar casas. Ott (1993) sistematizó el principio 'anahuasca' — múltiples culturas descubrieron independientemente la combinación triptamina + IMAO: Peganum en Persia/Arabia + Acacia, Banisteriopsis en Amazonía.",
pharma:{"Dosis IMAO activa":"3–5 g semillas (≈100–150 mg harmina)","Inicio IMAO":"30–45 min","Duración IMAO":"4–6 h","⚠️ Riesgo tiramina":"Alto — evitar quesos, embutidos, vino"},
quote:{t:"El esfand es el guardián del umbral. Antes de entrar a cualquier mundo invisible, hay que pasarlo por el humo del esfand para ir limpio.",s:"— Tradición popular iraní (en Ott, Pharmacotheon, 1993)"},
refs:[{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"β-carbolinas como IMAOs naturales; término 'anahuasca' acuñado aquí"},{a:"Fortunato, J.J. et al.",t:"Acute harmine administration induces antidepressive-like effects and increases BDNF",y:2010,j:"Prog Neuropsychopharmacol Biol Psychiatry",tp:"s"},{a:"Shulgin, A. & Shulgin, A.",t:"TIHKAL",y:1997,j:"Transform Press",tp:"l",n:"Perfiles de harmina, harmalina; síntesis y efectos subjetivos"}]},
 
ergot:{name:"Cornezuelo / LSD-25",sci:"Claviceps purpurea → LSD-25 (Hofmann, 1943)",col:"#7080c8",type:"Semisintético",rk:"global",region:"Europa (Eleusis) · Global",since:"Eleusis: ~1500 a.C. · LSD: 1943",lon:23,lat:38,
trials:[{l:"FDA — Sin aprobación (Clase I)",cls:"trb-bt"},{l:"Gasser (Suiza) — Ansiedad RCT",cls:"trb-ph2"},{l:"MAPS — Alcoholismo meta-análisis",cls:"trb-ph2"},{l:"Beckley Foundation — Neuroimagen",cls:"trb-ph2"},{l:"Microdosificación — Fase I/II activa",cls:"trb-ph1"}],
compounds:[{n:"LSD-25",f:"C₂₀H₂₅N₃O",mw:"323.43",cl:"Ergolina semisintética",ac:"Agonista parcial 5-HT2A/2C/2B, 5-HT1A, D2/D4. Activo a 50–75 µg"},{n:"Ergina (LSA)",f:"C₁₆H₁₇N₃O",mw:"267.33",cl:"Ergolina natural",ac:"Agonista 5-HT2A débil; en Turbina corymbosa (ololiuhqui)"},{n:"Ácido d-lisérgico",f:"C₁₆H₁₆N₂O₂",mw:"268.31",cl:"Ergolina (precursor)",ac:"Sustancia de partida para síntesis de LSD"}],
traditions:["Misterios de Eleusis (hipótesis kykeon ergotizado — Wasson, Hofmann, Ruck 1978)","Ololiuhqui azteca (LSA — documentado Sahagún ~1558)","Terapia LSD psiquiátrica (1950s–70s: Sandoz, Spring Grove)","Contracultura 1960s (Leary, Kesey)"],
mechanism:"LSD es el agonista 5-HT2A más potente conocido (activo a 50–75 µg). Modelo REBUS (Carhart-Harris & Friston 2019): reduce peso de creencias predictivas previas bajo Inferencia Activa — el cerebro bajo LSD tiene menor confianza en sus predicciones habituales, mayor plasticidad. Duración 8–12 h.",
uses:["Alcoholismo (meta-análisis Krebs 2012: 59% abstinencia vs 38% control)","Ansiedad en cáncer terminal","Cefalea en racimos","Microdosificación (Fase I/II activa — sin indicación confirmada)"],
ev:62,trials_txt:"Renacimiento: Gasser (Suiza 2014), MAPS, Beckley Foundation, Imperial College, Univ. Zurich. Meta-análisis de 6 RCTs de los 1950s–70s para alcoholismo (Krebs 2012).",
challenge:"Duración de 8–12h complica protocolos clínicos. Regulación Clase I en mayoría de países. El legado cultural 1960s contamina la lectura científica neutral.",
etno:"Albert Hofmann sintetizó el LSD-25 el 16/11/1938. El 19/04/1943 (Bicycle Day) experimentó el primer viaje registrado. Wasson, Hofmann y Carl Ruck proponen en 'The Road to Eleusis' (1978) que el kykeon de Eleusis contenía ergina de cebada parasitada por Claviceps. Leary, Metzner y Ram Dass publicaron 'The Psychedelic Experience' (1964) basado en el Bardo Thodol.",
pharma:{"Dosis mínima activa":"25–50 µg","Dosis estándar (terapéutico)":"100–200 µg","Inicio":"30–60 min","Pico":"3–5 h","Duración":"8–12 h","Tolerancia":"3 días; cruzada completa con psilocibina y mescalina"},
quote:{t:"El LSD me dio la certeza de que el mundo no es lo que creemos que es. Me mostró que existe una dimensión que la ciencia todavía no puede medir.",s:"— Albert Hofmann, LSD: My Problem Child (1979)"},
refs:[{a:"Hofmann, A.",t:"LSD: My Problem Child",y:1979,j:"McGraw-Hill",tp:"e",n:"Autobiografía del descubridor. Historia completa del LSD."},{a:"Wasson, R.G., Hofmann, A. & Ruck, C.A.P.",t:"The Road to Eleusis",y:1978,j:"Harcourt Brace",tp:"e",n:"Hipótesis del kykeon ergotizado — ensayo más influyente de etnomicología clásica"},{a:"Carhart-Harris, R. & Friston, K.",t:"REBUS and the Anarchic Brain",y:2019,j:"Pharmacological Reviews",tp:"s",n:"Marco teórico unificado del campo psicodélico"},{a:"Krebs, T.S. & Johansen, P.Ø.",t:"LSD for alcoholism: meta-analysis of RCTs",y:2012,j:"J Psychopharmacology",tp:"s"},{a:"Leary, T., Metzner, R. & Alpert, R.",t:"The Psychedelic Experience",y:1964,j:"University Books",tp:"l",n:"Manual de LSD basado en el Bardo Thodol. Definió el marco cultural de los 60s."},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Historia química completa del LSD; análisis de la hipótesis eleusiana"}]},
 
kava:{name:"Kava",sci:"Piper methysticum G. Forst.",col:"#4da896",type:"Planta",rk:"oceania",region:"Vanuatu · Fiyi · Tonga · Samoa",since:"~3000 a.C.",lon:168,lat:-17,
trials:[{l:"Cochrane Review positivo (2015)",cls:"trb-ph3"},{l:"Sarris RCT — Ansiedad (2013)",cls:"trb-ph2"},{l:"Australia — Suplemento aprobado",cls:"trb-fda"}],
compounds:[{n:"Kavaina",f:"C₁₅H₁₄O₃",mw:"242.27",cl:"Kavalactona",ac:"Modulador GABA-A; bloqueador canales Na⁺; ansiolítico"},{n:"Dihidrokavaina",f:"C₁₅H₁₆O₃",mw:"244.29",cl:"Kavalactona",ac:"Relajante muscular; anticonvulsivante"},{n:"Metisticina",f:"C₁₅H₁₄O₄",mw:"258.27",cl:"Kavalactona",ac:"Inhibidor CYP450; modulador GABA"}],
traditions:["Ceremonia del nakamal (Vanuatu)","Diplomacia y resolución de conflictos melanesia","Rituales de paso polinesia","Comunicación con ancestros"],
mechanism:"Las kavalactonas NO actúan vía serotonina. Efecto ansiolítico por: modulación positiva GABA-A (sitios distintos a las benzodiacepinas), bloqueo canales Na⁺ y Ca²⁺, antagonismo AMPA. Produce ansiolisis y relajación muscular SIN amnesia ni dependencia marcada. No produce tolerancia cruzada con benzodiacepinas.",
uses:["Ansiedad generalizada (RCT positivos)","Insomnio","Abstinencia alcohólica (exploratorio)","Menopausia — síntomas de ansiedad"],
ev:70,trials_txt:"Múltiples RCTs. Cochrane Review positivo (2015). Aprobado como suplemento en Australia. Único de este atlas no clasificado como sustancia controlada con evidencia clínica sólida.",
challenge:"Hepatotoxicidad con preparados de bajo grado (partes aéreas, no raíz noble). Comisión Europea lo prohibió 2002–2008, luego revocó. Interacciones con alcohol y benzodiacepinas.",
etno:"Cultivada y seleccionada por 3000+ años en Oceanía. Más de 80 cultivares. La ceremonia del nakamal es simultáneamente política, religiosa y medicinal. James Cook la documentó en su segundo viaje (1773). La OMS emitió en 2007 un informe favorable sobre preparados nobles.",
pharma:{"Dosis ansiolítica":"150–300 mg kavalactonas/día","Inicio":"30–60 min","Duración":"2–4 h","Vía":"Oral (bebida acuosa de raíz molida)"},
quote:{t:"El kava no te hace perder la mente — te abre el corazón. Con kava, los enemigos pueden hablar.",s:"— Jefe tribal de Vanuatu (en Lebot, Merlin & Lindstrom, 1992)"},
refs:[{a:"Lebot, V., Merlin, M. & Lindstrom, L.",t:"Kava: The Pacific Drug",y:1992,j:"Yale Univ. Press",tp:"e",n:"Referencia etnobotánica definitiva"},{a:"Sarris, J. et al.",t:"Kava in the treatment of generalized anxiety disorder: RCT",y:2013,j:"J Clinical Psychopharmacology",tp:"s"},{a:"Ott, J.",t:"Pharmacotheon",y:1993,j:"Natural Products Co.",tp:"l",n:"Análisis químico de kavalactonas y etnobotánica completa"}]}
};
 
/* ════════════ BUILD INDEX ════════════ */
const plist = document.getElementById("plist");
Object.entries(DB).forEach(([id,p])=>{
  const d=document.createElement("div");
  d.className="iitem"; d.dataset.id=id; d.dataset.rk=p.rk;
  d.onclick=()=>sel(id);
  d.innerHTML=`<div class="idot" style="background:${p.col}"></div><span class="iname">${p.name}</span><span class="ireg">${p.region.split("·")[0].split("/")[0].trim().substring(0,12)}</span>`;
  plist.appendChild(d);
});
 
/* ════════════ DRAW MARKERS ════════════ */
const mkg = document.getElementById("mkg");
const mkMap = {};
Object.entries(DB).forEach(([id,p])=>{
  const [cx,cy] = mxy(p.lon,p.lat);
  const g = document.createElementNS("http://www.w3.org/2000/svg","g");
  g.setAttribute("class","mk"); g.setAttribute("id","mk-"+id);
  g.setAttribute("data-rk",p.rk);
  g.setAttribute("transform",`translate(${cx},${cy})`);
  g.onclick = ()=>sel(id);
  g.innerHTML = `
    <circle class="mkr2" r="16" stroke="${p.col}" style="animation-delay:${Math.random()*4}s"/>
    <circle class="mkr" r="11" stroke="${p.col}" style="animation-delay:${Math.random()*2}s"/>
    <circle class="mkc" r="4.5" fill="${p.col}" filter="url(#mglow)"/>
    <circle r="1.8" fill="${['#80d0c0','#e8c060','#e09070','#a0b0e8','#d870c0'][['#4da896','#c09840','#c07050','#7080c8','#b040a0'].indexOf(p.col)]}"/>`;
  mkg.appendChild(g);
  mkMap[id] = g;
});
 
/* ════════════ TOOLTIP ════════════ */
const tt = document.getElementById("mtt");
const mpane = document.querySelector(".mpane");
Object.entries(mkMap).forEach(([id,g])=>{
  const p=DB[id];
  g.addEventListener("mouseenter",()=>{tt.textContent=p.name;tt.style.display="block"});
  g.addEventListener("mousemove",e=>{
    const r=mpane.getBoundingClientRect();
    tt.style.left=(e.clientX-r.left-tt.offsetWidth/2)+"px";
    tt.style.top=(e.clientY-r.top-42)+"px";
  });
  g.addEventListener("mouseleave",()=>tt.style.display="none");
});
 
/* ════════════ SELECT PLANT ════════════ */
function sel(id){
  const p=DB[id]; if(!p)return;
  tt.style.display="none";
  document.querySelectorAll(".mk").forEach(g=>g.classList.remove("act"));
  mkMap[id].classList.add("act");
  
  document.getElementById("wp").style.display="none";
  const dp=document.getElementById("dp");
  dp.className="det vis";
 
  const ec=p.ev>=70?"#4da896":p.ev>=40?"#c09840":"#c07050";
  const chemH=(p.compounds||[]).map(c=>`<div class="chem"><span class="cn">${c.n} &nbsp;·&nbsp; <span style="color:var(--t3);font-size:.52rem">${c.f} · PM: ${c.mw}</span></span><span>Clase: ${c.cl}</span><br><span>Actividad: ${c.ac}</span></div>`).join("");
  const pharH=p.pharma?`<div class="phb"><span class="phtitle">Farmacocinética y dosificación</span>${Object.entries(p.pharma).map(([k,v])=>`<div class="phrow"><span class="phk">${k}</span><span class="phv">${v}</span></div>`).join("")}</div>`:"";
  const tradH=(p.traditions||[]).map(t=>`<span class="cht">${t}</span>`).join("");
  const usesH=(p.uses||[]).map(u=>`<span class="chu">${u}</span>`).join("");
  const trialBadges=(p.trials||[]).map(t=>`<span class="trb ${t.cls}">${t.l}</span>`).join("");
  const quoteH=p.quote?`<div class="qb">"${p.quote.t}"<span class="qs">${p.quote.s}</span></div>`:"";
  const refsH=(p.refs||[]).map(r=>`<div class="ref"><span class="rb ${r.tp==="s"?"rbs":r.tp==="l"?"rbl":"rbe"}">${r.tp==="s"?"Cient.":r.tp==="l"?"Lit.":"Etno."}</span><span class="rau">${r.a}</span> (${r.y}). <span class="rti">${r.t}</span>${r.j?`. <span class="rjo">${r.j}</span>`:""}${r.n?`<span class="rno">${r.n}</span>`:""}</div>`).join("");
 
  dp.innerHTML=`
<div class="dback" onclick="back()">← volver al atlas</div>
<div class="dhero">
  <div class="dbadge" style="color:${p.col}"><div class="ddot" style="background:${p.col}"></div>${p.type}</div>
  <div class="dname">${p.name}</div>
  <div class="dsci">${p.sci}</div>
  <div class="dtags"><span class="dt dtr">${p.region}</span><span class="dt dts">Desde ${p.since}</span></div>
</div>
<div class="dstats">
  <div class="dst"><span class="dstn">${(p.refs||[]).length}</span><span class="dstl">Refs.</span></div>
  <div class="dst"><span class="dstn">${(p.uses||[]).length}</span><span class="dstl">Indicac.</span></div>
  <div class="dst"><span class="dstn">${(p.traditions||[]).length}</span><span class="dstl">Tradc.</span></div>
  <div class="dst"><span class="dstn">${(p.compounds||[]).length}</span><span class="dstl">Compuest.</span></div>
</div>
${S("⬡","vd","Compuestos activos",chemH,true,true)}
${S("◈","vd","Mecanismo neurológico",`<div class="dsb open">${p.mechanism}</div>`,true,false)}
${pharH?S("⚗","st","Farmacocinética",pharH,true,true):""}
${trialBadges?S("🧪","vd","Ensayos clínicos",`<div class="trial-wrap">${trialBadges}</div><div class="evw"><div class="evrow"><span class="evl">Nivel de evidencia</span><span class="evv" style="color:${ec}">${p.ev}/100</span></div><div class="evtr"><div class="evfi" id="efi-${id}" style="width:0;background:${ec}"></div></div><div class="evtk"><span>0</span><span>25</span><span>50</span><span>75</span><span>100</span></div><div class="evno">${p.trials_txt}</div></div>`,true,true):""}
${quoteH?`<div class="dsec">${quoteH}</div>`:""}
${S("✦","go","Contexto etnobotánico",`<div class="dsb open">${p.etno}</div>`,true,false)}
${S("❧","go","Tradiciones",`<div class="chips">${tradH}</div>`,false,true)}
${S("＋","vd","Aplicaciones clínicas",`<div class="chips">${usesH}</div>`,false,true)}
${S("△","cr","Desafío principal",`<div class="challenge">${p.challenge}</div>`,true,true)}
${S("≡","sm","Bibliografía",`<div class="refs">${refsH}</div>`,true,true)}`;
 
  setTimeout(()=>{const f=document.getElementById("efi-"+id);if(f)f.style.width=p.ev+"%"},80);
 
  dp.querySelectorAll(".dsh").forEach(h=>{
    h.onclick=()=>{
      const b=h.nextElementSibling; if(!b)return;
      b.classList.toggle("open",!b.classList.contains("open"));
      h.classList.toggle("open",!h.classList.contains("open"));
    };
  });
  document.getElementById("sb").scrollTop=0;
}
 
const CC={vd:"var(--vd3)",go:"var(--gold2)",st:"var(--st2)",cr:"var(--cr2)",sm:"var(--t2)"};
function S(ic,ck,title,content,open,chips){
  const c=CC[ck]||"var(--t1)";
  return `<div class="dsec"><div class="dsh ${open?"open":""}"><div class="dsi">${ic}</div><div class="dst2" style="color:${c}">${title}</div><div class="dsa">›</div></div>${content}</div>`;
}
 
function back(){
  document.getElementById("wp").style.display="block";
  document.getElementById("dp").className="det";
  document.querySelectorAll(".mk").forEach(g=>g.classList.remove("act"));
}
 
function filt(region,el){
  document.querySelectorAll(".fb").forEach(b=>b.classList.remove("active"));
  el.classList.add("active");
  const labels={all:"Todo el mundo",america:"Américas",africa:"África",asia:"Asia · Eurasia",oceania:"Oceanía",global:"Global"};
  document.getElementById("rfilt").textContent=labels[region]||region;
  document.querySelectorAll(".mk").forEach(g=>{
    const show=region==="all"||g.dataset.rk===region;
    g.style.opacity=show?"1":"0.08";
    g.style.pointerEvents=show?"auto":"none";
    g.style.transition="opacity .4s ease";
  });
  document.querySelectorAll(".iitem").forEach(i=>{
    i.style.display=(region==="all"||i.dataset.rk===region)?"flex":"none";
  });
}
</script>
</body>
</html>