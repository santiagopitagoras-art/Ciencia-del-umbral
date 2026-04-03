
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ciencia del Umbral · Santiago Schiavoni · Psicólogo de Datos</title>
<meta name="description" content="Dashboard de evidencia científica sobre estados alterados de conciencia, neurociencia psicodélica y terapias emergentes. Por Santiago Schiavoni, psicólogo de datos — Córdoba, Argentina.">
<meta property="og:title" content="Ciencia del Umbral · Santiago Schiavoni">
<meta property="og:description" content="Cartografía de la evidencia clínica sobre estados alterados de conciencia. Datos de Johns Hopkins, Nature Medicine, NEJM y más. Por Santiago Schiavoni, psicólogo de datos.">
<meta property="og:type" content="website">
<meta name="author" content="Santiago Schiavoni">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,700;1,400;1,500&family=IBM+Plex+Mono:wght@300;400;500&family=IBM+Plex+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/3.0.2/topojson.min.js"></script>
<style>
:root {
  --bg: #f8f7f3;
  --bg2: #f0efe9;
  --ink: #181814;
  --ink2: #38382e;
  --ink3: #78786a;
  --rule: #d4d3c8;
  --navy: #1a3a5c;
  --gold: #7a5a1a;
  --teal: #1a5248;
  --rust: #6a2218;
  --sage: #2a4a1a;
  --plum: #3a1a5a;
  --navy-l:#e8edf4;
  --gold-l:#f4eed8;
  --teal-l:#e2eeec;
  --COL: 1px solid var(--rule);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--bg);
  color:var(--ink);
  font-family:'IBM Plex Sans',sans-serif;
  font-weight:300;
  font-size:15px;
  line-height:1.6;
  overflow-x:hidden;
}
.mono{font-family:'IBM Plex Mono',monospace;}
.serif{font-family:'EB Garamond',serif;}
.col{border:var(--COL);}
hr.rule{border:none;border-top:var(--COL);}
nav{
  position:fixed;top:0;left:0;right:0;z-index:900;
  height:50px;display:flex;justify-content:space-between;align-items:center;
  padding:0 2.5rem;
  background:rgba(248,247,243,0.96);backdrop-filter:blur(10px);
  border-bottom:var(--COL);
}
.nav-id{
  font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
  letter-spacing:0.15em;text-transform:uppercase;color:var(--navy);
  display:flex;align-items:center;gap:0.6rem;
}
.live-dot{
  width:6px;height:6px;border-radius:50%;background:var(--navy);
  animation:blink 2.5s ease-in-out infinite;
}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.2}}
.nav-links{display:flex;gap:2rem;list-style:none;}
.nav-links a{
  font-family:'IBM Plex Mono',monospace;font-size:0.55rem;
  letter-spacing:0.12em;text-transform:uppercase;
  color:var(--ink3);text-decoration:none;transition:color .2s;
}
.nav-links a:hover{color:var(--navy);}
.hero{
  min-height:100vh;padding-top:50px;
  display:grid;grid-template-columns:55% 45%;
  border-bottom:var(--COL);
}
.hero-l{
  padding:5rem 3rem 5rem 2.5rem;
  border-right:var(--COL);
  display:flex;flex-direction:column;justify-content:center;
  gap:0;
}
.eyebrow{
  font-family:'IBM Plex Mono',monospace;font-size:0.58rem;
  letter-spacing:0.22em;text-transform:uppercase;color:var(--ink3);
  display:flex;align-items:center;gap:0.75rem;margin-bottom:2rem;
}
.eyebrow::before{content:'';width:20px;height:1px;background:var(--ink3);}
h1{
  font-family:'EB Garamond',serif;font-weight:500;
  font-size:clamp(3.8rem,5.5vw,6.8rem);line-height:.95;
  letter-spacing:-.01em;color:var(--ink);margin-bottom:1.5rem;
}
h1 em{font-style:italic;color:var(--navy);}
.hero-deck{
  font-size:.88rem;line-height:1.85;color:var(--ink2);
  max-width:48ch;margin-bottom:3rem;
}
.hero-kpis{
  display:grid;grid-template-columns:repeat(3,1fr);
  border-top:var(--COL);padding-top:2rem;
}
.kpi{padding-right:1.5rem;border-right:var(--COL);}
.kpi:last-child{border-right:none;padding-right:0;padding-left:1.5rem;}
.kpi:nth-child(2){padding-left:1.5rem;}
.kpi-v{
  font-family:'EB Garamond',serif;font-size:3rem;font-weight:500;
  color:var(--navy);line-height:1;margin-bottom:.3rem;
}
.kpi-l{
  font-family:'IBM Plex Mono',monospace;font-size:.52rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);line-height:1.5;
}
.hero-r{
  background:var(--navy);
  position:relative;overflow:hidden;
  display:flex;align-items:center;justify-content:center;
}
#hero-cv{display:block;width:100%;height:100%;}
.hero-caption{
  position:absolute;bottom:1.5rem;right:1.5rem;
  font-family:'IBM Plex Mono',monospace;font-size:.52rem;
  letter-spacing:.15em;text-transform:uppercase;
  color:rgba(255,255,255,.2);writing-mode:vertical-rl;
}
.sec{border-bottom:var(--COL);}
.sec-in{max-width:1240px;margin:0 auto;padding:5.5rem 2.5rem;}
.sec-hdr{
  display:grid;grid-template-columns:64px 1fr;gap:1.5rem;
  align-items:start;margin-bottom:4rem;
  padding-bottom:2rem;border-bottom:var(--COL);
}
.sec-n{
  font-family:'IBM Plex Mono',monospace;font-size:.58rem;
  letter-spacing:.15em;text-transform:uppercase;color:var(--ink3);
  padding-top:.4rem;
}
.sec-tag{
  font-family:'IBM Plex Mono',monospace;font-size:.55rem;
  letter-spacing:.18em;text-transform:uppercase;color:var(--ink3);
  margin-bottom:.6rem;
}
h2{
  font-family:'EB Garamond',serif;font-weight:500;
  font-size:clamp(2.2rem,3.8vw,4.2rem);line-height:1.0;
  color:var(--ink);
}
h2 em{font-style:italic;color:var(--navy);}
.map-bg{background:var(--bg2);}
.map-legend{
  display:flex;flex-wrap:wrap;gap:1.25rem;margin-bottom:1.5rem;
}
.leg{
  display:flex;align-items:center;gap:.45rem;
  font-family:'IBM Plex Mono',monospace;font-size:.55rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);
}
.leg-sq{width:10px;height:10px;border-radius:1px;flex-shrink:0;}
#world-map-svg{width:100%;display:block;background:#dde5ee;border:var(--COL);}
.country-path{stroke:#f8f7f3;stroke-width:.35;cursor:pointer;transition:opacity .2s;}
.country-path:hover{opacity:.7;}
.map-tip{
  position:fixed;background:var(--ink);color:#fff;
  padding:.7rem 1rem;border-left:3px solid var(--gold);
  font-family:'IBM Plex Mono',monospace;font-size:.6rem;line-height:1.6;
  pointer-events:none;opacity:0;transition:opacity .15s;
  z-index:800;max-width:230px;
}
.map-tip.show{opacity:1;}
.tip-name{font-family:'EB Garamond',serif;font-size:.9rem;font-weight:500;margin-bottom:.2rem;}
.tip-st{font-size:.52rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.3rem;}
.tip-note{color:rgba(255,255,255,.55);font-size:.58rem;}
.map-stats{
  display:grid;grid-template-columns:repeat(4,1fr);
  border:var(--COL);border-top:none;
}
.ms{padding:1.25rem 1.5rem;border-right:var(--COL);}
.ms:last-child{border-right:none;}
.ms-n{
  font-family:'EB Garamond',serif;font-size:2rem;font-weight:500;
  line-height:1;margin-bottom:.25rem;
}
.ms-l{
  font-family:'IBM Plex Mono',monospace;font-size:.52rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);line-height:1.4;
}
.rebus-layout{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;}
.rebus-diagram{border:var(--COL);background:var(--bg2);padding:2rem;}
.rebus-pts{list-style:none;margin-top:0;}
.rp{
  display:grid;grid-template-columns:32px 1fr;gap:1rem;
  padding:1.25rem 0;border-bottom:var(--COL);
}
.rp:first-child{padding-top:0;}
.rp:last-child{border-bottom:none;padding-bottom:0;}
.rp-n{
  font-family:'IBM Plex Mono',monospace;font-size:.6rem;
  color:var(--ink3);padding-top:.25rem;
}
.rp h4{
  font-family:'EB Garamond',serif;font-size:1.05rem;font-weight:500;
  margin-bottom:.3rem;color:var(--ink);
}
.rp p{font-size:.78rem;line-height:1.75;color:var(--ink2);}
.rebus-cite{
  margin-top:2rem;padding:.9rem 1.1rem;
  background:var(--navy-l);border-left:3px solid var(--navy);
  font-family:'IBM Plex Mono',monospace;font-size:.58rem;
  color:var(--ink3);line-height:1.6;
}
.eff-dark{background:var(--ink);}
.eff-dark .sec-n{color:rgba(255,255,255,.18);}
.eff-dark .sec-tag{color:rgba(255,255,255,.35);}
.eff-dark h2{color:#fff;}
.eff-dark h2 em{color:#c8a850;}
.eff-dark .sec-hdr{border-bottom-color:rgba(255,255,255,.08);}
.eff-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4rem;}
.eff-group-lbl{
  font-family:'IBM Plex Mono',monospace;font-size:.55rem;
  letter-spacing:.15em;text-transform:uppercase;
  color:rgba(255,255,255,.3);margin-bottom:1.25rem;
  padding-bottom:.75rem;border-bottom:1px solid rgba(255,255,255,.07);
}
.bar-row2{margin-bottom:1.5rem;}
.bar-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:.35rem;}
.bar-label{font-size:.72rem;color:rgba(255,255,255,.75);line-height:1.3;max-width:28ch;}
.bar-label small{display:block;font-size:.55rem;color:rgba(255,255,255,.3);margin-top:.1rem;font-family:'IBM Plex Mono',monospace;}
.bar-num{
  font-family:'EB Garamond',serif;font-size:1.6rem;font-weight:500;
  line-height:1;flex-shrink:0;margin-left:1rem;
}
.bar-track{height:8px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden;}
.bar-fill{height:100%;border-radius:1px;width:0%;transition:width 1.8s cubic-bezier(.16,1,.3,1);}
.f-navy{background:#5a8abf;}
.f-gold{background:#c8a040;}
.f-teal{background:#2a9870;}
.f-dim{background:rgba(255,255,255,.22);}
.bar-src{
  font-family:'IBM Plex Mono',monospace;font-size:.5rem;
  color:rgba(255,255,255,.2);margin-top:.3rem;letter-spacing:.04em;
}
.scatter-section{background:var(--bg2);}
.scatter-layout{display:grid;grid-template-columns:1fr 400px;gap:4rem;align-items:start;}
#scatter-svg{width:100%;border:var(--COL);background:var(--bg);display:block;}
.scatter-legend-list{list-style:none;}
.sl-item{
  display:flex;align-items:center;gap:.6rem;
  padding:.6rem 0;border-bottom:var(--COL);
  font-size:.72rem;color:var(--ink2);line-height:1.4;
}
.sl-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
.sl-item span{font-family:'IBM Plex Mono',monospace;font-size:.55rem;color:var(--ink3);display:block;}
.radar-layout{display:grid;grid-template-columns:520px 1fr;gap:5rem;align-items:start;}
#radar-svg{display:block;border:var(--COL);background:var(--bg2);}
.radar-legend{list-style:none;}
.rl-item{
  display:flex;align-items:center;gap:.75rem;
  padding:.75rem 0;border-bottom:var(--COL);
  font-size:.75rem;color:var(--ink2);
}
.rl-item:last-child{border-bottom:none;}
.rl-sq{width:12px;height:4px;border-radius:1px;flex-shrink:0;}
.rl-note{font-size:.65rem;color:var(--ink3);margin-top:.2rem;font-family:'IBM Plex Mono',monospace;}
.tl-wrap{overflow-x:auto;padding-bottom:2rem;scrollbar-width:thin;scrollbar-color:var(--rule) transparent;}
.tl-wrap::-webkit-scrollbar{height:3px;}
.tl-wrap::-webkit-scrollbar-thumb{background:var(--rule);}
.tl-row{display:flex;position:relative;min-width:max-content;padding-top:54px;}
.tl-row::before{
  content:'';position:absolute;top:54px;left:0;right:0;
  height:1px;background:var(--rule);
}
.tl-ev{width:230px;flex-shrink:0;padding-right:1.5rem;position:relative;}
.tl-ev.lo{padding-top:80px;}
.tl-dot{
  position:absolute;left:0;top:47px;
  width:14px;height:14px;border-radius:50%;
  background:var(--bg);border:2px solid var(--rule);z-index:2;
}
.tl-dot.hi{border-color:var(--navy);background:var(--navy);}
.tl-stem{position:absolute;left:6px;width:1px;background:var(--rule);}
.tl-ev:not(.lo) .tl-stem{top:61px;height:28px;}
.tl-ev.lo .tl-stem{top:61px;height:28px;}
.tl-yr{
  font-family:'EB Garamond',serif;font-size:1.8rem;font-weight:500;
  color:var(--navy);line-height:1;margin-bottom:.35rem;
}
.tl-title{font-size:.78rem;font-weight:500;color:var(--ink);margin-bottom:.25rem;line-height:1.3;}
.tl-jrn{
  font-family:'IBM Plex Mono',monospace;font-size:.52rem;
  letter-spacing:.06em;color:var(--ink3);margin-bottom:.35rem;
}
.tl-desc{font-size:.68rem;line-height:1.65;color:var(--ink2);}
.badge{
  display:inline-block;margin-top:.45rem;
  padding:.12rem .45rem;border:1px solid var(--rule);
  font-family:'IBM Plex Mono',monospace;font-size:.48rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);border-radius:1px;
}
.badge.tl{border-color:var(--teal);color:var(--teal);}
.badge.nv{border-color:var(--navy);color:var(--navy);}
.card-grid{display:grid;grid-template-columns:repeat(4,1fr);border:var(--COL);}
.ccard{padding:1.5rem;border-right:var(--COL);}
.ccard:last-child{border-right:none;}
.ccard-flag{font-size:.55rem;letter-spacing:.12em;text-transform:uppercase;color:var(--navy);margin-bottom:.4rem;font-family:'IBM Plex Mono',monospace;}
.ccard-title{font-family:'EB Garamond',serif;font-size:.95rem;font-weight:500;margin-bottom:.45rem;line-height:1.2;}
.ccard-body{font-size:.68rem;line-height:1.7;color:var(--ink2);}
footer{background:var(--ink);color:rgba(255,255,255,.4);padding:4.5rem 2.5rem;}
.ft-in{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:280px 1fr;gap:5rem;}
.ft-brand{font-family:'EB Garamond',serif;font-size:1.8rem;font-weight:500;color:#fff;line-height:1.1;margin-bottom:.8rem;}
.ft-desc{font-size:.68rem;line-height:1.8;margin-bottom:1.25rem;}
.ft-sig{font-family:'EB Garamond',serif;font-style:italic;font-size:.85rem;color:rgba(255,255,255,.45);}
.refs-lbl{font-family:'IBM Plex Mono',monospace;font-size:.55rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.25);margin-bottom:.8rem;}
.refs-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;}
.ref{padding:.45rem 0;border-bottom:1px solid rgba(255,255,255,.05);font-size:.58rem;line-height:1.5;display:flex;gap:.45rem;}
.ref-n{color:rgba(196,168,80,.8);flex-shrink:0;}
.rv{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease;}
.rv.in{opacity:1;transform:none;}
.nav-ham{display:none;flex-direction:column;gap:4px;cursor:pointer;padding:4px;}
.nav-ham span{display:block;width:18px;height:1.5px;background:var(--navy);}
.disclaimer{
  margin-top:4rem;padding:1rem 1.5rem;
  border:var(--COL);border-left:3px solid var(--gold);
  font-family:'IBM Plex Mono',monospace;font-size:.6rem;
  color:var(--ink3);line-height:1.6;background:var(--bg2);
}
@media(max-width:960px){
  .hero,.rebus-layout,.scatter-layout,.radar-layout,.eff-grid,.ft-in{grid-template-columns:1fr;}
  .hero-r{min-height:45vh;}
  .card-grid{grid-template-columns:1fr 1fr;}
  .map-stats{grid-template-columns:1fr 1fr;}
  .refs-grid{grid-template-columns:1fr;}
  .nav-links{display:none;}
  .nav-ham{display:flex;}
  .nav-links.open{
    display:flex;flex-direction:column;
    position:absolute;top:50px;left:0;right:0;
    background:rgba(248,247,243,0.98);
    border-bottom:var(--COL);padding:1rem 2.5rem;gap:.75rem;
    z-index:899;
  }
}
</style>
</head>
<body>

<nav>
  <div class="nav-id"><div class="live-dot"></div>Santiago Schiavoni · Psicólogo de Datos</div>
  <ul class="nav-links" id="navLinks">
    <li><a href="#mapa">Mapa</a></li>
    <li><a href="#rebus">REBUS</a></li>
    <li><a href="#eficacia">Eficacia</a></li>
    <li><a href="#scatter">Dosis-Respuesta</a></li>
    <li><a href="#radar">Perfiles</a></li>
    <li><a href="#historia">Historia</a></li>
  </ul>
  <div class="nav-ham" id="navHam" onclick="document.getElementById('navLinks').classList.toggle('open')">
    <span></span><span></span><span></span>
  </div>
</nav>

<section class="hero">
  <div class="hero-l">
    <p class="eyebrow">Neurociencia · Psicodélicos · Análisis de Datos</p>
    <h1>Ciencia<br>del<br><em>Umbral</em></h1>
    <div style="margin-bottom:2rem;padding:1.25rem 1.5rem;border-left:3px solid var(--navy);background:var(--navy-l);">
      <p style="font-family:'IBM Plex Mono',monospace;font-size:.52rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);margin-bottom:.6rem;">Tesis central · Abstract ejecutivo</p>
      <p style="font-family:'EB Garamond',serif;font-size:.95rem;line-height:1.85;color:var(--ink2);font-style:italic;">
        La neurociencia psicodélica no propone una nueva molécula: propone una nueva epistemología terapéutica. El dato no es la droga — es el protocolo de acompañamiento. Lo que los ensayos Fase 3 documentan es que, bajo condiciones precisas de set y setting, el cerebro accede a una ventana de plasticidad en la que los <em>priors</em> patológicos pueden ser reescritos. La molécula abre la ventana. El terapeuta ayuda a reescribir lo que está adentro.
      </p>
      <p style="font-family:'IBM Plex Mono',monospace;font-size:.52rem;color:var(--ink3);margin-top:.7rem;letter-spacing:.05em;">
        Santiago Schiavoni · Psicólogo / People Analytics · UNC Córdoba · 2025
      </p>
    </div>
    <p class="hero-deck">Una cartografía de la evidencia clínica sobre estados alterados de conciencia — desde los ensayos de Harvard en 1962 hasta los primeros estudios Fase 3 completados en 2023.</p>
    <div class="hero-kpis">
      <div class="kpi">
        <div class="kpi-v">71%</div>
        <div class="kpi-l">Respuesta clínica<br>psilocibina · TDM<br>JAMA Psychiatry 2021</div>
      </div>
      <div class="kpi">
        <div class="kpi-v">67%</div>
        <div class="kpi-l">Sin diagnóstico PTSD<br>MDMA Fase 3<br>Nature Medicine 2021</div>
      </div>
      <div class="kpi">
        <div class="kpi-v">60+</div>
        <div class="kpi-l">Años de evidencia<br>clínica acumulada<br>1962 – 2024</div>
      </div>
    </div>
  </div>
  <div class="hero-r">
    <canvas id="hero-cv"></canvas>
    <div class="hero-caption">Estados Alterados · Evidencia Científica</div>
  </div>
</section>

<section class="sec map-bg" id="mapa">
  <div class="sec-in">
    <div class="sec-hdr rv">
      <div class="sec-n mono">01</div>
      <div>
        <div class="sec-tag">Dimensión Global</div>
        <h2>El mundo y los <em>umbrales legales</em></h2>
      </div>
    </div>
    <div class="map-legend rv">
      <div class="leg"><div class="leg-sq" style="background:#2d6a4f"></div>Aprobado federalmente</div>
      <div class="leg"><div class="leg-sq" style="background:#1a3a5c"></div>Ensayos clínicos activos</div>
      <div class="leg"><div class="leg-sq" style="background:#1a5248"></div>Despenalizado</div>
      <div class="leg"><div class="leg-sq" style="background:#4a2a6a"></div>Uso ritual protegido</div>
      <div class="leg"><div class="leg-sq" style="background:#c8cdd5"></div>Sin datos específicos</div>
    </div>
    <div class="rv"><svg id="world-map-svg" viewBox="0 0 960 500"></svg></div>
    <div class="map-stats rv">
      <div class="ms"><div class="ms-n" style="color:#2d6a4f">4</div><div class="ms-l">Países con terapia<br>aprobada / regulada</div></div>
      <div class="ms"><div class="ms-n" style="color:#1a3a5c">30+</div><div class="ms-l">Países con ensayos<br>clínicos activos</div></div>
      <div class="ms"><div class="ms-n" style="color:#1a5248">12</div><div class="ms-l">Jurisdicciones<br>despenalizadas</div></div>
      <div class="ms"><div class="ms-n" style="color:#4a2a6a">75+</div><div class="ms-l">Pueblos con uso ritual<br>documentado</div></div>
    </div>
    <div class="card-grid rv" style="margin-top:3rem;">
      <div class="ccard"><div class="ccard-flag">🇦🇺 Australia · TGA 2023</div><div class="ccard-title">Primera aprobación federal</div><div class="ccard-body">MDMA-PTSD y psilocibina para depresión resistente autorizados por la TGA desde julio 2023.</div></div>
      <div class="ccard"><div class="ccard-flag">🇺🇸 Oregon & Colorado · 2023</div><div class="ccard-title">Servicios de psilocibina regulados</div><div class="ccard-body">Medida 109 de Oregon crea el primer marco de servicios psilocíbicos. FDA otorgó Breakthrough Therapy designation.</div></div>
      <div class="ccard"><div class="ccard-flag">🇧🇷 Brasil · CONAD 1987</div><div class="ccard-title">Ayahuasca legal para uso religioso</div><div class="ccard-body">Primera nación en legalizar la ayahuasca. Estudios de Draulio de Araujo demuestran efectos antidepresivos.</div></div>
      <div class="ccard"><div class="ccard-flag">🇳🇱 Países Bajos · Tolerancia</div><div class="ccard-title">Trufas psilocíbicas legales</div><div class="ccard-body">Esclerocios permanecen legales. Decenas de centros de retiro terapéutico operan con supervisión profesional.</div></div>
    </div>
    <div class="disclaimer rv">⚠ Los datos presentados provienen de estudios peer-reviewed citados. Este dashboard es una síntesis académica con fines de divulgación científica. No constituye recomendación clínica ni de uso de sustancias.</div>
  </div>
</section>

<section class="sec" id="rebus">
  <div class="sec-in">
    <div class="sec-hdr rv">
      <div class="sec-n mono">02</div>
      <div><div class="sec-tag">Mecanismo Neurológico</div><h2>El modelo <em>REBUS</em></h2></div>
    </div>
    <div class="rebus-layout rv">
      <div>
        <div class="rebus-diagram">
          <svg viewBox="0 0 520 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;">
            <defs>
              <marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 Z" fill="#78786a"/></marker>
              <marker id="arr-teal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 Z" fill="#1a5248"/></marker>
              <marker id="arr-navy" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 Z" fill="#1a3a5c"/></marker>
            </defs>
            <ellipse cx="260" cy="110" rx="175" ry="65" fill="#e8edf4" stroke="#c0c8d8" stroke-width="1" stroke-dasharray="4,3"/>
            <text x="260" y="47" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#78786a" letter-spacing="1">CÓRTEX PREFRONTAL — RED DE MODO PREDETERMINADO</text>
            <ellipse cx="260" cy="400" rx="190" ry="70" fill="#e2eeec" stroke="#a0c8b8" stroke-width="1" stroke-dasharray="4,3"/>
            <text x="260" y="472" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#78786a" letter-spacing="1">REGIONES SUBCORTICALES — SEÑAL BOTTOM-UP</text>
            <line x1="200" y1="110" x2="260" y2="110" stroke="#1a3a5c" stroke-width="2.5" opacity=".7"/>
            <line x1="260" y1="110" x2="320" y2="110" stroke="#1a3a5c" stroke-width="2.5" opacity=".7"/>
            <line x1="200" y1="130" x2="150" y2="340" stroke="#c0c0b8" stroke-width="1" stroke-dasharray="3,4" marker-end="url(#arr)" opacity=".5"/>
            <line x1="260" y1="130" x2="260" y2="330" stroke="#c0c0b8" stroke-width="1" stroke-dasharray="3,4" marker-end="url(#arr)" opacity=".5"/>
            <line x1="320" y1="130" x2="370" y2="340" stroke="#c0c0b8" stroke-width="1" stroke-dasharray="3,4" marker-end="url(#arr)" opacity=".5"/>
            <line x1="90" y1="250" x2="150" y2="130" stroke="#7a5a1a" stroke-width="1.5" opacity=".5" marker-end="url(#arr)"/>
            <line x1="430" y1="250" x2="370" y2="130" stroke="#7a5a1a" stroke-width="1.5" opacity=".5" marker-end="url(#arr)"/>
            <line x1="150" y1="355" x2="195" y2="135" stroke="#1a5248" stroke-width="2.5" opacity=".85" marker-end="url(#arr-teal)"/>
            <line x1="260" y1="345" x2="260" y2="140" stroke="#1a5248" stroke-width="3" opacity=".9" marker-end="url(#arr-teal)"/>
            <line x1="370" y1="355" x2="325" y2="135" stroke="#1a5248" stroke-width="2.5" opacity=".85" marker-end="url(#arr-teal)"/>
            <line x1="150" y1="390" x2="260" y2="395" stroke="#1a5248" stroke-width="1.5" opacity=".6"/>
            <line x1="260" y1="395" x2="370" y2="390" stroke="#1a5248" stroke-width="1.5" opacity=".6"/>
            <circle cx="260" cy="110" r="28" fill="#1a3a5c" opacity=".55"/>
            <text x="260" y="107" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff" font-weight="500">mPFC</text>
            <text x="260" y="120" text-anchor="middle" font-family="IBM Plex Mono" font-size="7" fill="rgba(255,255,255,.6)">DMN hub</text>
            <circle cx="190" cy="110" r="20" fill="#1a3a5c" opacity=".5"/>
            <text x="190" y="114" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff">PCC</text>
            <circle cx="330" cy="110" r="20" fill="#1a3a5c" opacity=".5"/>
            <text x="330" y="114" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff">ANG</text>
            <circle cx="88" cy="250" r="18" fill="#7a5a1a" opacity=".75"/>
            <text x="88" y="247" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="#fff">dACC</text>
            <circle cx="432" cy="250" r="18" fill="#7a5a1a" opacity=".75"/>
            <text x="432" y="247" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="#fff">AI</text>
            <circle cx="150" cy="390" r="24" fill="#1a5248" opacity=".9"/>
            <text x="150" y="387" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff" font-weight="500">AMY</text>
            <text x="150" y="400" text-anchor="middle" font-family="IBM Plex Mono" font-size="7" fill="rgba(255,255,255,.6)">emoción</text>
            <circle cx="260" cy="400" r="26" fill="#1a5248" opacity=".9"/>
            <text x="260" y="397" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff" font-weight="500">THAL</text>
            <text x="260" y="410" text-anchor="middle" font-family="IBM Plex Mono" font-size="7" fill="rgba(255,255,255,.6)">relay sensorial</text>
            <circle cx="370" cy="390" r="24" fill="#1a5248" opacity=".9"/>
            <text x="370" y="387" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#fff" font-weight="500">HYP</text>
            <text x="370" y="400" text-anchor="middle" font-family="IBM Plex Mono" font-size="7" fill="rgba(255,255,255,.6)">regulación</text>
            <circle cx="260" cy="110" r="34" fill="none" stroke="#6a2218" stroke-width="1.5" stroke-dasharray="5,4" opacity=".6"/>
            <text x="304" y="82" font-family="IBM Plex Mono" font-size="8" fill="#6a2218" opacity=".8">5-HT2A ↑</text>
            <rect x="10" y="10" width="180" height="80" fill="white" opacity=".85" rx="1"/>
            <line x1="20" y1="26" x2="45" y2="26" stroke="#1a3a5c" stroke-width="2.5"/>
            <text x="52" y="30" font-family="IBM Plex Mono" font-size="9" fill="#38382e">Red DMN (suprimida)</text>
            <line x1="20" y1="42" x2="45" y2="42" stroke="#1a5248" stroke-width="2.5" marker-end="url(#arr-teal)"/>
            <text x="52" y="46" font-family="IBM Plex Mono" font-size="9" fill="#38382e">Señal bottom-up ↑</text>
            <line x1="20" y1="58" x2="45" y2="58" stroke="#c0c0b8" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="52" y="62" font-family="IBM Plex Mono" font-size="9" fill="#38382e">Vía suprimida</text>
            <circle cx="29" cy="76" r="6" fill="#7a5a1a" opacity=".75"/>
            <text x="52" y="79" font-family="IBM Plex Mono" font-size="9" fill="#38382e">Red de saliencia</text>
          </svg>
        </div>
        <p style="font-size:.65rem;color:var(--ink3);margin-top:.75rem;font-family:'IBM Plex Mono',monospace;line-height:1.6;">Basado en: Carhart-Harris & Friston (2019). REBUS and the Anarchic Brain. <em>Pharmacological Reviews</em>, 71(3), 316–344.</p>
      </div>
      <div>
        <p style="font-size:.8rem;line-height:1.85;color:var(--ink2);margin-bottom:2rem;">El modelo REBUS propone que los psicodélicos actúan reduciendo la precisión predictiva de la Red de Modo Predeterminado — el sustrato neurológico de las narrativas rígidas sobre el yo, la rumiación y los patrones patológicos.</p>
        <ul class="rebus-pts">
          <li class="rp"><div class="rp-n">01</div><div><h4>Agonismo 5-HT2A</h4><p>Los psicodélicos se unen a receptores serotoninérgicos 5-HT2A. El resultado es mayor glutamato y aumento de la entropía cerebral: mayor aleatoriedad, menor predictibilidad del disparo neuronal.</p></div></li>
          <li class="rp"><div class="rp-n">02</div><div><h4>Supresión del DMN</h4><p>La Red de Modo Predeterminado pierde dominancia jerárquica. La actividad autocrítica que sostiene la depresión y el PTSD se interrumpe.</p></div></li>
          <li class="rp"><div class="rp-n">03</div><div><h4>Emergencia bottom-up</h4><p>Redes subcorticales y límbicas envían señales que alcanzan el córtex. El cerebro accede a información suprimida — correlacionado clínicamente con el insight terapéutico.</p></div></li>
          <li class="rp"><div class="rp-n">04</div><div><h4>Ventana de plasticidad</h4><p>Post-experiencia: BDNF elevado y sinaptogénesis aumentada crean una ventana de reorganización. Los priors patológicamente rígidos pueden ser reescritos.</p></div></li>
        </ul>
        <div class="rebus-cite">Carhart-Harris, R. & Friston, K. (2019). REBUS and the Anarchic Brain. <em>Pharmacological Reviews</em>, 71(3), 316–344.</div>
      </div>
    </div>
  </div>
</section>

<section class="sec eff-dark" id="eficacia">
  <div class="sec-in">
    <div class="sec-hdr">
      <div class="sec-n mono">03</div>
      <div><div class="sec-tag">Evidencia Clínica</div><h2>Los <em>números</em></h2></div>
    </div>
    <div class="eff-grid" id="eff-wrap">
      <div class="rv">
        <div class="eff-group-lbl">Depresión Mayor · Respuesta clínica</div>
        <div style="margin-bottom:1rem;padding:.65rem .9rem;background:rgba(255,255,255,.04);border-left:2px solid rgba(200,160,64,.4);font-family:'IBM Plex Mono',monospace;font-size:.55rem;color:rgba(255,255,255,.35);line-height:1.6;">⚠ Los datos reflejan protocolos de terapia asistida (PAP/MDMA-AT). La respuesta clínica es del protocolo completo — molécula + acompañamiento terapéutico.</div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Psilocibina + PAP<small>JAMA Psychiatry 2021 · RCT · N=24</small></div><div class="bar-num" style="color:#5a8abf">71%</div></div><div class="bar-track"><div class="bar-fill f-navy" data-w="71"></div></div><div class="bar-src">Respuesta al mes · 54% remisión · Time-to-remission: ~2 sesiones vs. 6–8 sem. SSRI</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Psilocibina vs. Escitalopram<small>NEJM 2021 · Imperial College · N=59</small></div><div class="bar-num" style="color:#2a9870">≈57%</div></div><div class="bar-track"><div class="bar-fill f-teal" data-w="57"></div></div><div class="bar-src">No inferior al SSRI líder; superior en bienestar</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">SSRIs — meta-análisis<small>Cipriani et al. Lancet 2018 · N=116,000</small></div><div class="bar-num" style="color:rgba(255,255,255,.3)">28%</div></div><div class="bar-track"><div class="bar-fill f-dim" data-w="28"></div></div><div class="bar-src">Primera línea estándar · inicio efecto 4–8 semanas</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Placebo</div><div class="bar-num" style="color:rgba(255,255,255,.2)">20%</div></div><div class="bar-track"><div class="bar-fill f-dim" style="opacity:.45" data-w="20"></div></div></div>
      </div>
      <div class="rv">
        <div class="eff-group-lbl">PTSD · Sin diagnóstico post-tratamiento</div>
        <div style="margin-bottom:1rem;padding:.65rem .9rem;background:rgba(255,255,255,.04);border-left:2px solid rgba(200,80,60,.35);font-family:'IBM Plex Mono',monospace;font-size:.55rem;color:rgba(255,255,255,.32);line-height:1.6;">Nota regulatoria: El comité asesor de FDA (jun. 2024) solicitó datos adicionales sobre cegamiento y seguridad. El proceso sigue activo — los datos de eficacia son sólidos; la discusión es metodológica.</div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">MDMA-AT · MAPP2<small>Nature Medicine 2023 · N=104 · Fase 3 · muestra diversa</small></div><div class="bar-num" style="color:#c8a040">71%</div></div><div class="bar-track"><div class="bar-fill f-gold" data-w="71"></div></div><div class="bar-src">Primer Fase 3 replicado · mayoría participantes de color</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">MDMA-AT · MAPP1<small>Nature Medicine 2021 · N=90 · Fase 3</small></div><div class="bar-num" style="color:#c8a040">67%</div></div><div class="bar-track"><div class="bar-fill f-gold" data-w="67"></div></div><div class="bar-src">Primer ensayo Fase 3 de terapia psicodélica en historia</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">TCC prolongada<small>Bradley et al. — meta-análisis</small></div><div class="bar-num" style="color:rgba(255,255,255,.3)">53%</div></div><div class="bar-track"><div class="bar-fill f-dim" data-w="53"></div></div><div class="bar-src">Mejor tratamiento psicoterapéutico estándar</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Placebo + terapia</div><div class="bar-num" style="color:rgba(255,255,255,.2)">32%</div></div><div class="bar-track"><div class="bar-fill f-dim" style="opacity:.45" data-w="32"></div></div></div>
      </div>
      <div class="rv">
        <div class="eff-group-lbl">Adicciones · Abstinencia verificada</div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Tabaco · psilocibina + PAP<small>J. Psychopharmacol. 2014 · NIH follow-up 2023</small></div><div class="bar-num" style="color:#5a8abf">80%</div></div><div class="bar-track"><div class="bar-fill f-navy" data-w="80"></div></div><div class="bar-src">Abstinencia biológicamente verificada a 6 meses</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Alcohol · psilocibina + PAP<small>JAMA Psychiatry 2022 · RCT · N=93</small></div><div class="bar-num" style="color:#2a9870">75%</div></div><div class="bar-track"><div class="bar-fill f-teal" data-w="75"></div></div><div class="bar-src">Reducción días de bebida pesada</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Opioides · ibogaína<small>En revisión regulatoria · FDA · cardiotoxicidad QT</small></div><div class="bar-num" style="color:rgba(200,160,64,.6)">68%*</div></div><div class="bar-track"><div class="bar-fill" style="background:rgba(200,160,64,.35)" data-w="68"></div></div><div class="bar-src">*Eficacia prometedora · riesgo cardíaco bajo evaluación activa</div></div>
        <div class="bar-row2"><div class="bar-top"><div class="bar-label">Tratamientos estándar</div><div class="bar-num" style="color:rgba(255,255,255,.2)">30%</div></div><div class="bar-track"><div class="bar-fill f-dim" style="opacity:.45" data-w="30"></div></div></div>
      </div>
    </div>
  </div>
</section>

<section class="sec scatter-section" id="scatter">
  <div class="sec-in">
    <div class="sec-hdr rv">
      <div class="sec-n mono">04</div>
      <div><div class="sec-tag">Relación Dosis-Respuesta</div><h2>Dosis, respuesta y <em>persistencia</em></h2></div>
    </div>
    <p class="rv" style="font-size:.82rem;line-height:1.8;color:var(--ink2);max-width:68ch;margin-bottom:3rem;margin-top:-2.5rem;">Cada punto representa un estudio clínico. El eje X muestra la dosis relativa; el eje Y la respuesta clínica. El tamaño del círculo codifica la persistencia del efecto en el seguimiento más largo reportado.</p>
    <div class="scatter-layout rv">
      <svg id="scatter-svg" viewBox="0 0 600 420"></svg>
      <div>
        <p style="font-family:'IBM Plex Mono',monospace;font-size:.55rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);margin-bottom:1rem;">Referencias de estudios</p>
        <ul class="scatter-legend-list" id="scatter-legend"></ul>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="radar">
  <div class="sec-in">
    <div class="sec-hdr rv">
      <div class="sec-n mono">05</div>
      <div><div class="sec-tag">Perfiles Comparados</div><h2>Perfil terapéutico de cada <em>sustancia</em></h2></div>
    </div>
    <p class="rv" style="font-size:.82rem;line-height:1.8;color:var(--ink2);max-width:68ch;margin-bottom:3rem;margin-top:-2.5rem;">Comparación multidimensional en seis ejes clínicamente relevantes. Basado en síntesis de evidencia disponible hasta 2024. Pasá el mouse por cada eje para ver la definición.</p>
    <div class="radar-layout rv">
      <svg id="radar-svg" viewBox="0 0 520 520" style="width:520px;max-width:100%;"></svg>
      <div>
        <ul class="radar-legend">
          <li class="rl-item"><div class="rl-sq" style="background:#1a3a5c;height:3px;"></div><div><div>Psilocibina</div><div class="rl-note">Hopkins / Imperial · Depresión, cáncer, adicciones</div></div></li>
          <li class="rl-item"><div class="rl-sq" style="background:#1a5248;height:3px;"></div><div><div>MDMA</div><div class="rl-note">MAPS Fase 3 · PTSD, ansiedad social, trauma</div></div></li>
          <li class="rl-item"><div class="rl-sq" style="background:#7a5a1a;height:3px;"></div><div><div>Ketamina</div><div class="rl-note">FDA aprobada (Spravato) · Depresión resistente</div></div></li>
        </ul>
        <div style="margin-top:2rem;padding:1.25rem;background:var(--bg2);border:var(--COL);">
          <p style="font-family:'IBM Plex Mono',monospace;font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-bottom:.75rem;">Ejes del radar</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.4rem;">
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;border-bottom:var(--COL);">Eficacia clínica general</div>
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;border-bottom:var(--COL);">Persistencia del efecto</div>
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;border-bottom:var(--COL);">Seguridad / tolerabilidad</div>
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;border-bottom:var(--COL);">Amplitud indicaciones</div>
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;">Evidencia disponible</div>
            <div style="font-size:.68rem;color:var(--ink2);padding:.4rem 0;">Acceso regulatorio</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="historia">
  <div class="sec-in" style="padding-bottom:2rem;">
    <div class="sec-hdr rv">
      <div class="sec-n mono">06</div>
      <div><div class="sec-tag">Historia de la Evidencia</div><h2>60 años de <em>ciencia</em></h2></div>
    </div>
    <p class="rv mono" style="font-size:.6rem;color:var(--ink3);margin-bottom:1.5rem;margin-top:-3rem;">← Deslizá para explorar →</p>
  </div>
  <div class="tl-wrap" style="padding-left:2.5rem;padding-right:2.5rem;">
    <div class="tl-row">
      <div class="tl-ev rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">1943</div><div class="tl-title">Hofmann sintetiza el LSD</div><div class="tl-jrn">Sandoz Laboratories · Basilea</div><div class="tl-desc">Descubrimiento accidental del LSD. Inicia 25 años de investigación psiquiátrica con 40,000+ pacientes tratados.</div></div>
      <div class="tl-ev lo rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">1962</div><div class="tl-title">Experimento del Viernes Santo</div><div class="tl-jrn">Harvard · Pahnke / seguimiento Doblin 1991</div><div class="tl-desc">Primer doble ciego con psilocibina. Seguimiento a 25 años confirma efectos duraderos.</div><span class="badge tl">Doble ciego</span></div>
      <div class="tl-ev rv"><div class="tl-dot"></div><div class="tl-stem"></div><div class="tl-yr">1970</div><div class="tl-title">Schedule I — Prohibición</div><div class="tl-jrn">Nixon · Controlled Substances Act</div><div class="tl-desc">30 años de silencio investigativo. Archivos desclasificados confirman motivación política, no científica.</div></div>
      <div class="tl-ev lo rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2006</div><div class="tl-title">Griffiths et al. — La renacencia</div><div class="tl-jrn">Psychopharmacology · Johns Hopkins</div><div class="tl-desc">El paper que reinicia el campo moderno. Psilocibina produce experiencias de significado espiritual duradero.</div><span class="badge nv">Peer-reviewed</span></div>
      <div class="tl-ev rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2016</div><div class="tl-title">Psilocibina en oncología</div><div class="tl-jrn">J. Psychopharmacol. · Hopkins · N=51</div><div class="tl-desc">80% reducción de ansiedad y depresión en pacientes con cáncer terminal. Efecto sostenido a 6 meses.</div><span class="badge tl">RCT</span></div>
      <div class="tl-ev lo rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2019</div><div class="tl-title">Modelo REBUS</div><div class="tl-jrn">Pharmacol. Reviews · Carhart-Harris & Friston</div><div class="tl-desc">Marco teórico unificador basado en inferencia bayesiana. Los psicodélicos relajan priors patológicos vía supresión del DMN.</div><span class="badge nv">Teoría fundacional</span></div>
      <div class="tl-ev rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2021</div><div class="tl-title">Davis et al. · TDM</div><div class="tl-jrn">JAMA Psychiatry · N=24 · RCT</div><div class="tl-desc">71% respuesta clínica, 54% remisión completa.</div><span class="badge tl">RCT</span></div>
      <div class="tl-ev lo rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2021</div><div class="tl-title">Psilocibina vs. Escitalopram</div><div class="tl-jrn">NEJM · Imperial College London · N=59</div><div class="tl-desc">Primera comparación directa contra SSRI líder. No inferior; superior en bienestar.</div><span class="badge nv">NEJM</span></div>
      <div class="tl-ev rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2021</div><div class="tl-title">MAPS MAPP1 · Fase 3</div><div class="tl-jrn">Nature Medicine · 15 sitios · 3 países</div><div class="tl-desc">67% sin diagnóstico PTSD vs. 32% placebo. Primer ensayo Fase 3 completado.</div><span class="badge tl">Fase 3</span></div>
      <div class="tl-ev lo rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2023</div><div class="tl-title">MAPS MAPP2 · Replicación</div><div class="tl-jrn">Nature Medicine · N=104</div><div class="tl-desc">71.2% confirmado. Primera muestra con mayoría de participantes de color.</div><span class="badge tl">Replicado</span></div>
      <div class="tl-ev rv"><div class="tl-dot hi"></div><div class="tl-stem"></div><div class="tl-yr">2023</div><div class="tl-title">Australia aprueba federalmente</div><div class="tl-jrn">TGA · Julio 2023</div><div class="tl-desc">Primera nación en autorizar MDMA y psilocibina para uso clínico a nivel federal.</div><span class="badge nv">Hito regulatorio</span></div>
    </div>
  </div>
</section>

<footer>
  <div class="ft-in">
    <div>
      <div class="ft-brand">Ciencia<br>del Umbral</div>
      <p class="ft-desc">Dashboard de evidencia científica sobre estados alterados de conciencia. Construido como pieza de portfolio en la intersección de neurociencia, psicoanálisis y psicología de datos.</p>
      <p class="ft-sig">Santiago Schiavoni<br>Psicólogo · Analista de Datos<br>Córdoba, Argentina · 2025</p>
    </div>
    <div>
      <div class="refs-lbl">Referencias primarias</div>
      <div class="refs-grid">
        <div class="ref"><span class="ref-n">[1]</span>Davis et al. (2021). Psilocybin-assisted therapy for MDD. JAMA Psychiatry, 78(5), 481–489.</div>
        <div class="ref"><span class="ref-n">[2]</span>Mitchell et al. (2021). MDMA-AT for severe PTSD. Nature Medicine, 27, 1025–1033.</div>
        <div class="ref"><span class="ref-n">[3]</span>Carhart-Harris et al. (2021). Psilocybin vs escitalopram. NEJM, 384, 1402–1411.</div>
        <div class="ref"><span class="ref-n">[4]</span>Carhart-Harris & Friston (2019). REBUS model. Pharmacol. Reviews, 71(3), 316–344.</div>
        <div class="ref"><span class="ref-n">[5]</span>Goodwin et al. (2022). Single-dose psilocybin for TRD. NEJM, 387, 1637–1648.</div>
        <div class="ref"><span class="ref-n">[6]</span>Bogenschutz et al. (2022). Psilocybin for AUD. JAMA Psychiatry, 79(10), 953–962.</div>
        <div class="ref"><span class="ref-n">[7]</span>Griffiths et al. (2016). Psilocybin in cancer. J.Psychopharmacol., 30(12), 1181–1197.</div>
        <div class="ref"><span class="ref-n">[8]</span>Johnson et al. (2014). Psilocybin for tobacco. J.Psychopharmacol., 28(11), 983–992.</div>
      </div>
    </div>
  </div>
</footer>

<div class="map-tip" id="mapTip"><div class="tip-name" id="tipName"></div><div class="tip-st" id="tipSt"></div><div class="tip-note" id="tipNote"></div></div>

<script>
(function(){
  const c=document.getElementById('hero-cv');
  const p=c.parentElement;
  function rsz(){c.width=p.offsetWidth;c.height=p.offsetHeight;}
  rsz();window.addEventListener('resize',rsz);
  const ctx=c.getContext('2d');
  const pts=Array.from({length:55},()=>({x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.35,vy:(Math.random()-.5)*.35}));
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    pts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>c.width)p.vx*=-1;if(p.y<0||p.y>c.height)p.vy*=-1;});
    for(let i=0;i<pts.length;i++)for(let j=i+1;j<pts.length;j++){const dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y,d=Math.hypot(dx,dy);if(d<110){ctx.beginPath();ctx.moveTo(pts[i].x,pts[i].y);ctx.lineTo(pts[j].x,pts[j].y);ctx.strokeStyle=`rgba(255,255,255,${(1-d/110)*.1})`;ctx.lineWidth=.7;ctx.stroke();}}
    pts.forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,1.4,0,Math.PI*2);ctx.fillStyle='rgba(255,255,255,.2)';ctx.fill();});
    requestAnimationFrame(draw);
  }
  draw();
})();

const cdata={'Australia':{s:'approved',l:'Aprobado federalmente',n:'MDMA y psilocibina autorizados por TGA desde julio 2023',c:'#2d6a4f'},'United States':{s:'clinical',l:'Ensayos Fase 3 · Oregon/Colorado regulados',n:'FDA Breakthrough Therapy. Oregon Measure 109 operativo desde 2023',c:'#1a3a5c'},'Canada':{s:'clinical',l:'Acceso especial + ensayos activos',n:'Exenciones Sec.56 para terminales',c:'#1a3a5c'},'United Kingdom':{s:'clinical',l:'Ensayos clínicos activos',n:'Imperial College, King\'s College, Compass Pathways Fase 3',c:'#1a3a5c'},'Switzerland':{s:'clinical',l:'Uso compasivo + ensayos',n:'Universidad de Zurich lidera investigación',c:'#1a3a5c'},'Germany':{s:'clinical',l:'Ensayos activos',n:'MIND Foundation activa',c:'#1a3a5c'},'Netherlands':{s:'decrim',l:'Tolerancia — trufas legales',n:'Esclerocios psilocíbicos legales. Centros de retiro operativos',c:'#1a5248'},'Portugal':{s:'decrim',l:'Despenalización total 2001',n:'Todas las drogas despenalizadas para uso personal',c:'#1a5248'},'Brazil':{s:'trad',l:'Ayahuasca legal — uso religioso',n:'CONAD legalizó en 1987. Estudios UFRN confirman efecto antidepresivo',c:'#4a2a6a'},'Mexico':{s:'trad',l:'Uso indígena protegido',n:'Hongos y peyote amparados por ley',c:'#4a2a6a'},'Peru':{s:'trad',l:'Ayahuasca — Patrimonio Cultural',n:'Reconocida por Ministerio de Cultura 2008',c:'#4a2a6a'},'Colombia':{s:'trad',l:'Uso ritual / despenalizado',n:'Yagé protegido. Corte Constitucional despenalizó uso personal',c:'#4a2a6a'},'New Zealand':{s:'clinical',l:'Ensayos clínicos activos',n:'Framework regulatorio en desarrollo',c:'#1a3a5c'},'Israel':{s:'clinical',l:'MDMA ensayos aprobados',n:'Pionero en ensayos MDMA para PTSD en veteranos',c:'#1a3a5c'},'Czech Republic':{s:'decrim',l:'Despenalizado',n:'Cantidades para uso personal despenalizadas',c:'#1a5248'},'Spain':{s:'clinical',l:'Ensayos activos',n:'Múltiples ensayos de MDMA y psilocibina en curso',c:'#1a3a5c'},'Denmark':{s:'clinical',l:'Ensayos activos',n:'Copenhagen Center for Research in Psychedelic Science',c:'#1a3a5c'},'Jamaica':{s:'trad',l:'Psilocibina legal',n:'Setas de psilocibina nunca ilegalizadas',c:'#4a2a6a'}};

const tip=document.getElementById('mapTip');
const svg=d3.select('#world-map-svg');
const proj=d3.geoNaturalEarth1().scale(153).translate([480,250]);
const path=d3.geoPath().projection(proj);
svg.append('path').datum(d3.geoGraticule()()).attr('d',path).attr('fill','none').attr('stroke','rgba(255,255,255,.35)').attr('stroke-width','.4');
fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json').then(r=>r.json()).then(world=>{
  const countries=topojson.feature(world,world.objects.countries);
  svg.selectAll('.cp').data(countries.features).join('path').attr('class','country-path').attr('d',path).attr('fill',d=>{const cd=cdata[d.properties&&d.properties.name];return cd?cd.c:'#c8cdd5';})
  .on('mousemove',(ev,d)=>{const nm=d.properties&&d.properties.name,cd=cdata[nm];if(!cd)return;document.getElementById('tipName').textContent=nm;document.getElementById('tipSt').textContent=cd.l;document.getElementById('tipSt').style.color=cd.c;document.getElementById('tipNote').textContent=cd.n;tip.style.left=(ev.clientX+14)+'px';tip.style.top=(ev.clientY-10)+'px';tip.classList.add('show');})
  .on('mouseleave',()=>tip.classList.remove('show'));
  svg.append('path').datum({type:'Sphere'}).attr('d',path).attr('fill','none').attr('stroke','#b8c2cc').attr('stroke-width','1');
}).catch(()=>{svg.append('text').attr('x',480).attr('y',250).attr('text-anchor','middle').attr('font-family','IBM Plex Mono,monospace').attr('font-size','12').attr('fill','#999').text('Conectá a internet para ver el mapa interactivo.');});

const scatterData=[
  {id:'A',label:'Psilocibina · TDM',substance:'psilocibina',dose:8,response:71,persist:12,journal:'JAMA Psych. 2021'},
  {id:'B',label:'Psilocibina · cáncer terminal',substance:'psilocibina',dose:8,response:80,persist:6,journal:'J.Psychopharmacol. 2016'},
  {id:'C',label:'Psilocibina · depresión resistente',substance:'psilocibina',dose:8,response:58,persist:3,journal:'NEJM 2021'},
  {id:'D',label:'Psilocibina · tabaco',substance:'psilocibina',dose:7,response:80,persist:6,journal:'J.Psychopharmacol. 2014'},
  {id:'E',label:'Psilocibina · alcohol',substance:'psilocibina',dose:8,response:75,persist:8,journal:'JAMA Psych. 2022'},
  {id:'F',label:'MDMA · PTSD (MAPP1)',substance:'mdma',dose:7,response:67,persist:12,journal:'Nature Med. 2021'},
  {id:'G',label:'MDMA · PTSD (MAPP2)',substance:'mdma',dose:7,response:71,persist:12,journal:'Nature Med. 2023'},
  {id:'H',label:'Ketamina · depresión',substance:'ketamina',dose:5,response:56,persist:1,journal:'Am.J.Psych. 2019'},
  {id:'I',label:'Ketamina · depresión resistente',substance:'ketamina',dose:6,response:61,persist:2,journal:'Biol.Psychiatry 2020'},
  {id:'J',label:'Ayahuasca · depresión',substance:'ayahuasca',dose:4,response:64,persist:3,journal:'Psychol.Med. 2019'},
];
const sColors={psilocibina:'#1a3a5c',mdma:'#1a5248',ketamina:'#7a5a1a',ayahuasca:'#4a2a6a'};
const sW=600,sH=420,sMg={t:30,r:20,b:55,l:65};
const sSvg=d3.select('#scatter-svg');
const sW2=sW-sMg.l-sMg.r,sH2=sH-sMg.t-sMg.b;
const sg=sSvg.append('g').attr('transform',`translate(${sMg.l},${sMg.t})`);
const xS=d3.scaleLinear().domain([0,10]).range([0,sW2]);
const yS=d3.scaleLinear().domain([40,100]).range([sH2,0]);
const rS=d3.scaleSqrt().domain([0,18]).range([7,26]);
sg.append('g').selectAll('line').data(yS.ticks(5)).join('line').attr('x1',0).attr('x2',sW2).attr('y1',d=>yS(d)).attr('y2',d=>yS(d)).attr('stroke','#d4d3c8').attr('stroke-width',.8);
sg.append('g').selectAll('line').data([2,4,6,8]).join('line').attr('x1',d=>xS(d)).attr('x2',d=>xS(d)).attr('y1',0).attr('y2',sH2).attr('stroke','#d4d3c8').attr('stroke-width',.8);
const bands=[{x:0,w:3,l:'Dosis baja'},{x:3,w:4,l:'Dosis media'},{x:7,w:3,l:'Dosis alta'}];
bands.forEach(b=>{sg.append('rect').attr('x',xS(b.x)).attr('y',0).attr('width',xS(b.x+b.w)-xS(b.x)).attr('height',sH2).attr('fill','rgba(26,58,92,0.03)');sg.append('text').attr('x',xS(b.x+b.w/2)).attr('y',-6).attr('text-anchor','middle').attr('font-family','IBM Plex Mono').attr('font-size',8).attr('fill','#b8b8a8').attr('letter-spacing','.5').text(b.l.toUpperCase());});
sg.append('g').attr('transform',`translate(0,${sH2})`).call(d3.axisBottom(xS).tickValues([1,2,3,4,5,6,7,8,9,10]).tickSize(0).tickPadding(10)).call(g=>{g.select('.domain').remove();g.selectAll('text').attr('font-family','IBM Plex Mono').attr('font-size',9).attr('fill','#78786a');});
sg.append('g').call(d3.axisLeft(yS).ticks(5).tickSize(0).tickPadding(10)).call(g=>{g.select('.domain').remove();g.selectAll('text').attr('font-family','IBM Plex Mono').attr('font-size',9).attr('fill','#78786a');});
sg.append('text').attr('x',sW2/2).attr('y',sH2+44).attr('text-anchor','middle').attr('font-family','IBM Plex Mono').attr('font-size',9).attr('fill','#78786a').attr('letter-spacing','1').text('INTENSIDAD DE DOSIS');
sg.append('text').attr('transform','rotate(-90)').attr('x',-sH2/2).attr('y',-52).attr('text-anchor','middle').attr('font-family','IBM Plex Mono').attr('font-size',9).attr('fill','#78786a').attr('letter-spacing','1').text('RESPUESTA CLÍNICA (%)');
sg.selectAll('circle').data(scatterData).join('circle').attr('cx',d=>xS(d.dose)).attr('cy',d=>yS(d.response)).attr('r',d=>rS(d.persist)).attr('fill',d=>sColors[d.substance]).attr('opacity',.65).attr('stroke',d=>sColors[d.substance]).attr('stroke-width',1.5);
sg.selectAll('.sl').data(scatterData).join('text').attr('class','sl').attr('x',d=>xS(d.dose)+rS(d.persist)+3).attr('y',d=>yS(d.response)+4).attr('font-family','IBM Plex Mono').attr('font-size',8).attr('fill','#38382e').text(d=>d.id);
const szLg=sg.append('g').attr('transform',`translate(${sW2-140},10)`);
[{v:1,l:'1 mes'},{v:6,l:'6 meses'},{v:12,l:'12 meses'}].forEach((d,i)=>{szLg.append('circle').attr('cx',i*48).attr('cy',20).attr('r',rS(d.v)).attr('fill','none').attr('stroke','#78786a').attr('stroke-width',1);szLg.append('text').attr('x',i*48).attr('y',38).attr('text-anchor','middle').attr('font-family','IBM Plex Mono').attr('font-size',7).attr('fill','#78786a').text(d.l);});
const legList=document.getElementById('scatter-legend');
scatterData.forEach(d=>{legList.innerHTML+=`<li class="sl-item"><div class="sl-dot" style="background:${sColors[d.substance]}"></div><div><strong>${d.id}</strong> — ${d.label}<span>${d.journal} · Respuesta ${d.response}%</span></div></li>`;});

const rData=[{axis:'Eficacia\nclínica',psi:88,mdma:85,ket:70},{axis:'Persistencia\nefecto',psi:92,mdma:80,ket:45},{axis:'Seguridad\ntolerab.',psi:90,mdma:82,ket:68},{axis:'Amplitud\nindicac.',psi:85,mdma:55,ket:60},{axis:'Evidencia\ndisp.',psi:80,mdma:88,ket:92},{axis:'Acceso\nregulatorio',psi:45,mdma:50,ket:95}];
const rSvg=d3.select('#radar-svg');
const rW=520,rH=520,rCx=260,rCy=265,rRad=180;
const N=rData.length;
const angleSlice=(Math.PI*2)/N;
const rScale=d3.scaleLinear().domain([0,100]).range([0,rRad]);
const levels=5;
for(let l=1;l<=levels;l++){rSvg.append('circle').attr('cx',rCx).attr('cy',rCy).attr('r',rRad*(l/levels)).attr('fill','none').attr('stroke','#d4d3c8').attr('stroke-width',.8);}
rData.forEach((_,i)=>{const ang=angleSlice*i-Math.PI/2;rSvg.append('line').attr('x1',rCx).attr('y1',rCy).attr('x2',rCx+rRad*Math.cos(ang)).attr('y2',rCy+rRad*Math.sin(ang)).attr('stroke','#d4d3c8').attr('stroke-width',.8);});
rData.forEach((d,i)=>{const ang=angleSlice*i-Math.PI/2;const lx=rCx+(rRad+28)*Math.cos(ang);const ly=rCy+(rRad+28)*Math.sin(ang);const lines=d.axis.split('\n');lines.forEach((ln,li)=>{rSvg.append('text').attr('x',lx).attr('y',ly+(li-lines.length/2+.5)*13).attr('text-anchor','middle').attr('dominant-baseline','middle').attr('font-family','IBM Plex Mono').attr('font-size',9).attr('fill','#38382e').attr('letter-spacing','.5').text(ln);});});
function radarPoints(key){return rData.map((d,i)=>{const ang=angleSlice*i-Math.PI/2;const r=rScale(d[key]);return[rCx+r*Math.cos(ang),rCy+r*Math.sin(ang)];});}
const rCols={psi:'#1a3a5c',mdma:'#1a5248',ket:'#7a5a1a'};
['ket','mdma','psi'].forEach(k=>{const pts=radarPoints(k);rSvg.append('polygon').attr('points',pts.map(p=>p.join(',')).join(' ')).attr('fill',rCols[k]).attr('fill-opacity',.12).attr('stroke',rCols[k]).attr('stroke-width',2);rSvg.selectAll(null).data(pts).join('circle').attr('cx',p=>p[0]).attr('cy',p=>p[1]).attr('r',4).attr('fill',rCols[k]).attr('opacity',.85);});
for(let l=1;l<=levels;l++){rSvg.append('text').attr('x',rCx+4).attr('y',rCy-rRad*(l/levels)-3).attr('font-family','IBM Plex Mono').attr('font-size',7.5).attr('fill','#78786a').text(l*20+'%');}

const radarTooltips={'Eficacia\nclínica':'Tasa de respuesta clínica ponderada en indicación principal','Persistencia\nefecto':'Duración del beneficio en el seguimiento más largo reportado. Psilocibina lidera con efectos a 12+ meses','Seguridad\ntolerab.':'Perfil de efectos adversos y riesgo de abuso. Psilocibina y MDMA tienen perfil benigno','Amplitud\nindicac.':'Número de patologías distintas con evidencia de eficacia documentada','Evidencia\ndisp.':'Volumen y calidad de ensayos peer-reviewed disponibles','Acceso\nregulatorio':'Disponibilidad clínica legal actual. Ketamina es la única aprobada por FDA (Spravato 2019)'};
const rTip=d3.select('body').append('div').style('position','fixed').style('pointer-events','none').style('background','#181814').style('color','#fff').style('padding','.7rem 1rem').style('border-left','3px solid #1a3a5c').style('font-family','IBM Plex Mono,monospace').style('font-size','.6rem').style('line-height','1.6').style('max-width','240px').style('opacity','0').style('transition','opacity .15s').style('z-index','900').style('border-radius','1px');
rData.forEach((d,i)=>{const ang=angleSlice*i-Math.PI/2;const lx=rCx+(rRad+28)*Math.cos(ang);const ly=rCy+(rRad+28)*Math.sin(ang);rSvg.append('circle').attr('cx',lx).attr('cy',ly).attr('r',22).attr('fill','transparent').style('cursor','help').on('mousemove',(ev)=>{rTip.html(`<strong style="font-family:'EB Garamond',serif;font-size:.9rem;display:block;margin-bottom:.3rem;">${d.axis.replace('\n',' ')}</strong>${radarTooltips[d.axis]}`).style('left',(ev.clientX+14)+'px').style('top',(ev.clientY-10)+'px').style('opacity','1');}).on('mouseleave',()=>rTip.style('opacity','0'));});

const io=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');e.target.querySelectorAll('[data-w]').forEach((b,i)=>{setTimeout(()=>{b.style.width=b.dataset.w+'%';},120+i*160);});}});},{threshold:.08});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const effIO=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.querySelectorAll('[data-w]').forEach((b,i)=>{setTimeout(()=>{b.style.width=b.dataset.w+'%';},80+i*150);});}});},{threshold:.05});
document.getElementById('eff-wrap').querySelectorAll('.bar-row2').forEach(el=>effIO.observe(el));
</script>
</body>
</html>
