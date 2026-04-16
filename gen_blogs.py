#!/usr/bin/env python3
# Generates 10 blog post HTML files for Dakbedrijf 'T Noorden

SHARED_CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --navy-deep:#060e1e; --navy-mid:#0d1f3c; --navy-light:#1a3660;
      --blue-vivid:#1e4fa3; --blue-accent:#2e6fd4;
      --silver:#c8d8ec; --silver-light:#e8f0fa; --white:#f5f9ff;
      --steel:#7a9ab8; --ice:#a8cce4; --gold-accent:#d4a843;
      --text-body:#b8cfe0; --text-muted:#6a8aa8;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Bitter', Georgia, serif; background: var(--navy-deep); color: var(--text-body); overflow-x: hidden; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--navy-deep); }
    ::-webkit-scrollbar-thumb { background: var(--blue-accent); border-radius: 3px; }
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: flex; align-items: center; justify-content: space-between; padding: 0 5%; height: 88px; background: rgba(6,14,30,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(46,111,212,0.25); }
    .nav-logo { display: flex; align-items: center; gap: 14px; text-decoration: none; }
    .nav-logo img { height: 110px; width: auto; filter: drop-shadow(0 0 8px rgba(46,111,212,0.5)); }
    .nav-logo-text { font-family: 'Fjalla One', sans-serif; font-size: 1rem; letter-spacing: 0.08em; color: var(--silver-light); line-height: 1.2; text-transform: uppercase; }
    .nav-logo-text span { display: block; font-size: 0.65rem; letter-spacing: 0.2em; color: var(--steel); }
    .nav-back { font-family: 'Barlow Condensed', sans-serif; font-size: 0.82rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--steel); text-decoration: none; display: flex; align-items: center; gap: 8px; transition: color 0.2s; }
    .nav-back:hover { color: var(--white); }
    .nav-cta { font-family: 'Barlow Condensed', sans-serif; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; padding: 10px 24px; background: var(--blue-accent); color: var(--white); border: none; border-radius: 2px; text-decoration: none; transition: background 0.25s; }
    .nav-cta:hover { background: #3a7de0; }

    /* ARTICLE HERO */
    .art-hero {
      padding: 130px 8% 64px; position: relative; overflow: hidden;
      background: linear-gradient(160deg, #060e1e 0%, #0d1f3c 55%, #0a1628 100%);
      border-bottom: 1px solid rgba(46,111,212,0.2);
    }
    .art-hero::before { content: ''; position: absolute; inset: 0; background-image: linear-gradient(rgba(46,111,212,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(46,111,212,0.06) 1px, transparent 1px); background-size: 60px 60px; }
    .art-hero-inner { max-width: 820px; margin: 0 auto; position: relative; }
    .art-breadcrumb { font-family: 'Barlow Condensed', sans-serif; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
    .art-breadcrumb a { color: var(--text-muted); text-decoration: none; transition: color 0.2s; }
    .art-breadcrumb a:hover { color: var(--white); }
    .art-breadcrumb span { color: rgba(46,111,212,0.5); }
    .art-cat { font-family: 'Barlow Condensed', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--white); background: var(--blue-accent); padding: 4px 12px; border-radius: 2px; display: inline-block; margin-bottom: 18px; }
    .art-title { font-family: 'Fjalla One', sans-serif; font-size: clamp(2rem, 4.5vw, 3.2rem); color: var(--white); line-height: 1.1; margin-bottom: 20px; }
    .art-meta { font-family: 'Barlow Condensed', sans-serif; font-size: 0.78rem; letter-spacing: 0.1em; color: var(--steel); display: flex; align-items: center; gap: 18px; flex-wrap: wrap; }
    .art-meta-dot { color: rgba(46,111,212,0.4); }

    /* ARTICLE BODY */
    .art-body { padding: 64px 8% 80px; }
    .art-body-inner { max-width: 820px; margin: 0 auto; }
    .art-img { width: 100%; border-radius: 4px; margin-bottom: 48px; border: 1px solid rgba(46,111,212,0.2); display: block; }
    .art-img-placeholder { width: 100%; height: 340px; border-radius: 4px; margin-bottom: 48px; border: 1px solid rgba(46,111,212,0.2); display: flex; align-items: center; justify-content: center; }
    .art-lead { font-size: 1.12rem; line-height: 1.85; color: var(--silver); margin-bottom: 40px; font-weight: 600; border-left: 3px solid var(--blue-accent); padding-left: 20px; }
    .art-body-inner h2 { font-family: 'Fjalla One', sans-serif; font-size: 1.6rem; color: var(--white); margin-top: 48px; margin-bottom: 16px; }
    .art-body-inner h3 { font-family: 'Fjalla One', sans-serif; font-size: 1.2rem; color: var(--silver-light); margin-top: 32px; margin-bottom: 12px; }
    .art-body-inner p { font-size: 0.95rem; line-height: 1.85; color: var(--text-body); margin-bottom: 20px; }
    .art-body-inner ul, .art-body-inner ol { padding-left: 0; list-style: none; margin-bottom: 24px; }
    .art-body-inner ul li, .art-body-inner ol li { font-size: 0.95rem; line-height: 1.75; color: var(--text-body); padding: 8px 0 8px 28px; position: relative; border-bottom: 1px solid rgba(46,111,212,0.07); }
    .art-body-inner ul li::before { content: ''; position: absolute; left: 0; top: 17px; width: 8px; height: 8px; border-radius: 50%; background: var(--blue-accent); }
    .art-body-inner ol { counter-reset: li; }
    .art-body-inner ol li { counter-increment: li; }
    .art-body-inner ol li::before { content: counter(li); position: absolute; left: 0; top: 8px; font-family: 'Fjalla One', sans-serif; font-size: 0.85rem; color: var(--blue-accent); }
    .tip-box { background: rgba(46,111,212,0.08); border: 1px solid rgba(46,111,212,0.25); border-left: 3px solid var(--blue-accent); border-radius: 3px; padding: 20px 24px; margin: 32px 0; }
    .tip-box-label { font-family: 'Barlow Condensed', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--blue-accent); margin-bottom: 8px; }
    .tip-box p { margin: 0; font-size: 0.9rem; color: var(--silver); }
    .warn-box { background: rgba(212,168,67,0.07); border: 1px solid rgba(212,168,67,0.3); border-left: 3px solid var(--gold-accent); border-radius: 3px; padding: 20px 24px; margin: 32px 0; }
    .warn-box-label { font-family: 'Barlow Condensed', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold-accent); margin-bottom: 8px; }
    .warn-box p { margin: 0; font-size: 0.9rem; color: #d4c48a; }
    .sum-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 16px; margin: 32px 0; }
    .sum-item { background: rgba(10,22,46,0.8); border: 1px solid rgba(46,111,212,0.18); border-radius: 3px; padding: 20px; }
    .sum-item h4 { font-family: 'Fjalla One', sans-serif; font-size: 1rem; color: var(--white); margin-bottom: 8px; }
    .sum-item p { font-size: 0.84rem; color: var(--text-muted); margin: 0; line-height: 1.6; }
    .art-divider { height: 1px; background: linear-gradient(90deg, var(--blue-accent), transparent); margin: 48px 0; opacity: 0.25; }

    /* CTA BLOCK */
    .art-cta { background: var(--navy-mid); border: 1px solid rgba(46,111,212,0.25); border-radius: 4px; padding: 40px; margin: 48px 0 0; text-align: center; }
    .art-cta h3 { font-family: 'Fjalla One', sans-serif; font-size: 1.6rem; color: var(--white); margin-bottom: 10px; }
    .art-cta p { font-size: 0.92rem; color: var(--text-muted); margin-bottom: 24px; }
    .btn-primary { font-family: 'Barlow Condensed', sans-serif; font-size: 0.9rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; padding: 16px 36px; background: var(--blue-accent); color: var(--white); border: none; border-radius: 2px; text-decoration: none; cursor: pointer; transition: all 0.25s; display: inline-block; }
    .btn-primary:hover { background: #3a7de0; transform: translateY(-2px); box-shadow: 0 8px 30px rgba(46,111,212,0.4); }
    .btn-ghost { font-family: 'Barlow Condensed', sans-serif; font-size: 0.9rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; padding: 15px 32px; background: transparent; color: var(--silver); border: 1px solid rgba(200,216,236,0.3); border-radius: 2px; text-decoration: none; display: inline-block; transition: all 0.25s; }
    .btn-ghost:hover { border-color: var(--silver); color: var(--white); }

    /* RELATED */
    .art-related { padding: 64px 8% 80px; background: var(--navy-mid); border-top: 1px solid rgba(46,111,212,0.15); }
    .art-related-inner { max-width: 1100px; margin: 0 auto; }
    .art-related-title { font-family: 'Fjalla One', sans-serif; font-size: 1.5rem; color: var(--white); margin-bottom: 28px; }
    .rel-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
    .rel-card { background: rgba(10,22,46,0.8); border: 1px solid rgba(46,111,212,0.18); border-radius: 3px; padding: 22px; text-decoration: none; display: block; transition: border-color 0.2s, transform 0.2s; }
    .rel-card:hover { border-color: rgba(46,111,212,0.4); transform: translateY(-2px); }
    .rel-cat { font-family: 'Barlow Condensed', sans-serif; font-size: 0.65rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--blue-accent); margin-bottom: 8px; }
    .rel-title { font-family: 'Fjalla One', sans-serif; font-size: 1rem; color: var(--white); line-height: 1.3; margin-bottom: 8px; }
    .rel-meta { font-family: 'Barlow Condensed', sans-serif; font-size: 0.7rem; color: var(--text-muted); }

    /* FOOTER */
    footer { background: var(--navy-mid); border-top: 1px solid rgba(46,111,212,0.2); padding: 60px 8% 32px; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 48px; margin-bottom: 48px; }
    .footer-heading { font-family: 'Barlow Condensed', sans-serif; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; color: var(--steel); margin-bottom: 20px; }
    .footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .footer-links a { font-size: 0.88rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s; }
    .footer-links a:hover { color: var(--white); }
    .footer-brand-text { font-size: 0.88rem; line-height: 1.7; color: var(--text-muted); margin-top: 16px; max-width: 280px; }
    .footer-contact-item { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 14px; }
    .footer-contact-item span { font-size: 0.88rem; line-height: 1.6; color: var(--text-muted); }
    .footer-contact-item strong { color: var(--silver); }
    .footer-bottom { border-top: 1px solid rgba(46,111,212,0.15); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }
    .footer-copy { font-family: 'Barlow Condensed', sans-serif; font-size: 0.75rem; letter-spacing: 0.08em; color: var(--text-muted); }
    .footer-legal { display: flex; gap: 20px; }
    .footer-legal a { font-family: 'Barlow Condensed', sans-serif; font-size: 0.75rem; letter-spacing: 0.08em; color: var(--text-muted); text-decoration: none; transition: color 0.2s; }
    .footer-legal a:hover { color: var(--white); }
    @media (max-width: 1024px) { .footer-grid { grid-template-columns: 1fr 1fr; } .rel-grid { grid-template-columns: 1fr 1fr; } .sum-grid { grid-template-columns: 1fr; } }
    @media (max-width: 768px) { nav { height: 72px; padding: 0 4%; } .nav-logo img { height: 72px; } .nav-back { display: none; } .nav-cta { font-size: 0.78rem; padding: 9px 16px; } .art-hero { padding: 110px 5% 48px; } .art-body { padding: 48px 5% 64px; } .art-related { padding: 48px 5% 60px; } }
    @media (max-width: 600px) { .footer-grid { grid-template-columns: 1fr; } .footer-bottom { flex-direction: column; text-align: center; } .rel-grid { grid-template-columns: 1fr; } }

    /* WHATSAPP */
    .float-whatsapp { position: fixed; bottom: 100px; right: 32px; z-index: 90; width: 52px; height: 52px; border-radius: 50%; background: #25D366; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 18px rgba(37,211,102,0.5); text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }
    .float-whatsapp:hover { transform: scale(1.1); box-shadow: 0 6px 28px rgba(37,211,102,0.7); }
    .float-phone { position: fixed; bottom: 40px; right: 32px; z-index: 90; width: 52px; height: 52px; border-radius: 50%; background: var(--blue-accent); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 18px rgba(46,111,212,0.5); text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }
    .float-phone:hover { transform: scale(1.1); box-shadow: 0 6px 28px rgba(46,111,212,0.7); }

    /* POPUP */
    .popup-overlay{position:fixed;inset:0;z-index:200;background:rgba(4,10,24,0.88);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;padding:20px;opacity:0;pointer-events:none;visibility:hidden;transition:opacity 0.3s,visibility 0.3s}
    .popup-overlay.open{opacity:1;pointer-events:auto;visibility:visible}
    .popup-box{background:linear-gradient(160deg,#0a1628 0%,#0d1f3c 100%);border:1px solid rgba(46,111,212,0.3);border-radius:8px;width:100%;max-width:560px;max-height:92vh;overflow-y:auto;position:relative;box-shadow:0 24px 80px rgba(0,0,0,0.6);transform:translateY(20px) scale(0.98);transition:transform 0.3s}
    .popup-overlay.open .popup-box{transform:translateY(0) scale(1)}
    .popup-stripe{height:3px;background:linear-gradient(90deg,var(--blue-accent),var(--ice),var(--blue-accent));border-radius:8px 8px 0 0}
    .popup-top{position:sticky;top:0;z-index:2;display:flex;align-items:center;justify-content:space-between;padding:22px 26px 18px;background:linear-gradient(160deg,#0a1628 0%,#0d1f3c 100%);border-bottom:1px solid rgba(46,111,212,0.2)}
    .popup-top-left{display:flex;flex-direction:column;gap:4px}
    .popup-title{font-family:'Fjalla One',sans-serif;font-size:1.45rem;color:var(--white);letter-spacing:0.04em;text-transform:uppercase}
    .popup-sub{font-size:0.78rem;color:var(--steel);display:flex;align-items:center;gap:6px}
    .popup-sub::before{content:'';display:inline-block;width:6px;height:6px;border-radius:50%;background:#4ade80}
    .popup-close{width:36px;height:36px;border-radius:50%;background:rgba(46,111,212,0.1);border:1px solid rgba(46,111,212,0.25);color:var(--silver);font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:background 0.2s,color 0.2s}
    .popup-close:hover{background:rgba(46,111,212,0.3);color:var(--white)}
    .popup-body{padding:22px 26px 26px}
    .hf-group{margin-bottom:14px}
    .hf-label{display:block;font-family:'Barlow Condensed',sans-serif;font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:var(--steel);margin-bottom:6px}
    .hf-input,.hf-textarea{width:100%;background:rgba(6,14,30,0.6);border:1px solid rgba(46,111,212,0.22);border-radius:2px;color:var(--silver-light);font-family:'Bitter',serif;font-size:0.88rem;padding:10px 14px;outline:none;transition:border-color 0.2s,box-shadow 0.2s;-webkit-appearance:none}
    .hf-input::placeholder,.hf-textarea::placeholder{color:var(--text-muted)}
    .hf-input:focus,.hf-textarea:focus{border-color:rgba(46,111,212,0.7);box-shadow:0 0 0 3px rgba(46,111,212,0.1)}
    .hf-textarea{resize:none;line-height:1.5}
    @media(max-width:600px){.popup-box{max-height:95vh;border-radius:12px}.popup-top,.popup-body{padding-left:18px;padding-right:18px}}
"""

SHARED_NAV = """
<nav>
  <a class="nav-logo" href="index.html">
    <img src="logo.png" alt="Dakbedrijf 'T Noorden" />
    <div class="nav-logo-text">Dakbedrijf<span>'T Noorden</span></div>
  </a>
  <a class="nav-back" href="blog.html">← Terug naar blog</a>
  <a class="nav-cta" href="#" onclick="event.preventDefault();openPopup()">Gratis Offerte</a>
</nav>
"""

SHARED_FOOTER = """
<footer>
  <div class="footer-grid">
    <div>
      <a class="nav-logo" href="index.html" style="display:inline-flex;margin-bottom:4px;">
        <img src="logo.png" alt="Dakbedrijf 'T Noorden" style="height:100px;filter:drop-shadow(0 0 8px rgba(46,111,212,0.4));" />
        <div class="nav-logo-text" style="margin-left:12px;">Dakbedrijf<span>'T Noorden</span></div>
      </a>
      <p class="footer-brand-text">Uw betrouwbare dakspecialist in Noord-Nederland. Wij staan garant voor vakmanschap, kwaliteit en eerlijke prijzen.</p>
    </div>
    <div>
      <div class="footer-heading">Diensten</div>
      <ul class="footer-links">
        <li><a href="dakrenovatie.html">Dakrenovatie</a></li>
        <li><a href="bitumen-daken.html">Bitumen Daken</a></li>
        <li><a href="daklekkage.html">Daklekkage</a></li>
        <li><a href="dakinspectie.html">Dakinspectie</a></li>
        <li><a href="dak-isolatie.html">Dak Isolatie</a></li>
        <li><a href="spoed.html">Spoed</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-heading">Bedrijf</div>
      <ul class="footer-links">
        <li><a href="index.html#over-ons">Over Ons</a></li>
        <li><a href="index.html#werkgebied">Werkgebied</a></li>
        <li><a href="index.html#portfolio">Portfolio</a></li>
        <li><a href="index.html#reviews">Reviews</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="index.html#contact">Contact</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-heading">Contact</div>
      <div class="footer-contact-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="var(--blue-accent)" stroke-width="1.5" stroke-linecap="round" style="width:16px;height:16px;flex-shrink:0;margin-top:2px"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 3.07 9.81 19.79 19.79 0 0 1 1 1.18 2 2 0 0 1 3 0h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.09 7.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16z"/></svg>
        <span><strong>06 12 37 08 53</strong><br/>Ma&ndash;Vr 07:30&ndash;17:30</span>
      </div>
      <div class="footer-contact-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="var(--blue-accent)" stroke-width="1.5" stroke-linecap="round" style="width:16px;height:16px;flex-shrink:0;margin-top:2px"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <span><strong>info@dakbedrijftnoorden.nl</strong></span>
      </div>
      <div style="margin-top:20px;">
        <a class="btn-primary" href="#" onclick="event.preventDefault();openPopup()" style="font-size:0.8rem;padding:12px 24px;">Gratis Offerte</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">&copy; 2024 Dakbedrijf &apos;T Noorden &middot; KvK 12345678 &middot; BTW NL123456789B01</div>
    <div class="footer-legal">
      <a href="privacybeleid.html">Privacybeleid</a>
      <a href="algemene-voorwaarden.html">Algemene Voorwaarden</a>
      <a href="privacybeleid.html#cookie">Cookiebeleid</a>
    </div>
  </div>
</footer>
"""

SHARED_POPUP = """
<div class="popup-overlay" id="offertePopup" onclick="if(event.target===this)closePopup()">
  <div class="popup-box">
    <div class="popup-stripe"></div>
    <div class="popup-top">
      <div class="popup-top-left">
        <div class="popup-title">Gratis Offerte</div>
        <div class="popup-sub">Vrijblijvend &middot; Reactie binnen 24 uur</div>
      </div>
      <button class="popup-close" onclick="closePopup()" aria-label="Sluiten">&#10005;</button>
    </div>
    <div class="popup-body">
      <form data-form="popup">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
          <div class="hf-group"><label class="hf-label">Voornaam *</label><input type="text" class="hf-input" name="voornaam" placeholder="Jan" required /></div>
          <div class="hf-group"><label class="hf-label">Achternaam *</label><input type="text" class="hf-input" name="achternaam" placeholder="Janssen" required /></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
          <div class="hf-group"><label class="hf-label">Telefoon *</label><input type="tel" class="hf-input" name="telefoon" placeholder="06 12 37 08 53" required /></div>
          <div class="hf-group"><label class="hf-label">E-mailadres *</label><input type="email" class="hf-input" name="email" placeholder="uw@email.nl" required /></div>
        </div>
        <div class="hf-group" style="margin-bottom:14px;"><label class="hf-label">Postcode &amp; Stad *</label><input type="text" class="hf-input" name="postcode_stad" placeholder="9700 AB Groningen" required /></div>
        <div class="hf-group" style="margin-bottom:18px;"><label class="hf-label">Uw Bericht</label><textarea class="hf-textarea" name="bericht" rows="3" placeholder="Beschrijf uw situatie of vraag&hellip;"></textarea></div>
        <button type="submit" class="btn-primary" style="width:100%;font-size:1rem;padding:15px;justify-content:center;">Verstuur Aanvraag &rarr;</button>
        <p style="font-size:0.76rem;color:var(--text-muted);margin-top:10px;text-align:center;">&#128274; Geen verplichtingen &middot; Gratis advies &middot; 100% vrijblijvend</p>
      </form>
    </div>
  </div>
</div>
"""

SHARED_WIDGETS = """
<a class="float-whatsapp" href="https://wa.me/31612370853" target="_blank" rel="noopener" aria-label="WhatsApp ons">
  <svg viewBox="0 0 24 24" fill="white" width="26" height="26"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>
<a class="float-phone" href="tel:+31612370853" aria-label="Bel ons">
  <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" style="width:24px;height:24px"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 3.07 9.81 19.79 19.79 0 0 1 1 1.18 2 2 0 0 1 3 0h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.09 7.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16z"/></svg>
</a>
"""

SHARED_JS = """
<script>
  function openPopup() { document.getElementById('offertePopup').classList.add('open'); document.body.style.overflow='hidden'; }
  function closePopup() { document.getElementById('offertePopup').classList.remove('open'); document.body.style.overflow=''; }
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closePopup(); });
</script>
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script src="assets/emailjs-forms.js"></script>
"""

def make_page(filename, title, seo_desc, seo_kw, category, date, readtime, article_html, related):
    head = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{seo_desc}" />
  <meta name="keywords" content="{seo_kw}" />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="Dakbedrijf 'T Noorden" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title} | Dakbedrijf 'T Noorden" />
  <meta property="og:description" content="{seo_desc}" />
  <meta property="og:image" content="logo.png" />
  <meta property="og:locale" content="nl_NL" />
  <meta property="og:site_name" content="Dakbedrijf 'T Noorden" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title} | Dakbedrijf 'T Noorden" />
  <meta name="twitter:description" content="{seo_desc}" />
  <link rel="icon" href="favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />
  <title>{title} | Dakbedrijf 'T Noorden</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fjalla+One&family=Bitter:ital,wght@0,400;0,600;0,700;1,400&family=Barlow+Condensed:wght@400;600;700;900&display=swap" rel="stylesheet" />
  <style>{SHARED_CSS}</style>
</head>
<body>
"""
    rel_html = '\n'.join([f'<a class="rel-card" href="{r[0]}"><div class="rel-cat">{r[1]}</div><div class="rel-title">{r[2]}</div><div class="rel-meta">{r[3]}</div></a>' for r in related])

    return head + SHARED_NAV + f"""
<!-- HERO -->
<div class="art-hero">
  <div class="art-hero-inner">
    <div class="art-breadcrumb">
      <a href="index.html">Home</a>
      <span>/</span>
      <a href="blog.html">Blog</a>
      <span>/</span>
      <span style="color:var(--steel)">{category}</span>
    </div>
    <span class="art-cat">{category}</span>
    <h1 class="art-title">{title}</h1>
    <div class="art-meta">
      <span>&#128197; {date}</span>
      <span class="art-meta-dot">&bull;</span>
      <span>&#9201; {readtime} minuten lezen</span>
      <span class="art-meta-dot">&bull;</span>
      <span>Door Dakbedrijf 'T Noorden</span>
    </div>
  </div>
</div>

<!-- ARTICLE -->
<div class="art-body">
  <div class="art-body-inner">
{article_html}
    <div class="art-cta">
      <h3>Heeft u vragen over uw dak?</h3>
      <p>Onze dakspecialisten helpen u graag persoonlijk. Vraag vandaag nog een gratis en vrijblijvende inspectie aan.</p>
      <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
        <a class="btn-primary" href="#" onclick="event.preventDefault();openPopup()">Gratis Offerte Aanvragen &rarr;</a>
        <a class="btn-ghost" href="tel:+31612370853">&#9742; 06 12 37 08 53</a>
      </div>
    </div>
  </div>
</div>

<!-- RELATED -->
<div class="art-related">
  <div class="art-related-inner">
    <div class="art-related-title">Meer artikelen</div>
    <div class="rel-grid">
      {rel_html}
    </div>
  </div>
</div>
""" + SHARED_FOOTER + SHARED_POPUP + SHARED_WIDGETS + SHARED_JS + "\n</body>\n</html>\n"


# ─────────────────────────────────────────────────────────────────────────────
# BLOG POSTS
# ─────────────────────────────────────────────────────────────────────────────

posts = []

# 1 ── Dakschade na storm
posts.append(("blog-dakschade-storm.html",
  "Hoe herken je dakschade na een storm?",
  "Na een storm kan uw dak beschadigd zijn zonder dat u het direct ziet. Leer hoe u dakschade herkent en wanneer u een vakman inschakelt.",
  "dakschade storm, stormschade dak, dak controleren na storm, beschadigd dak, noord-nederland",
  "Schade", "15 maart 2025", 5,
  """
    <p class="art-lead">Na iedere zware storm is het verstandig om uw dak te inspecteren — ook als er van binnenuit niets te zien is. Schade kan sluimerend zijn en pas weken later leiden tot lekkage.</p>

    <h2>Waarom stormschade zo verraderlijk is</h2>
    <p>Een storm trekt even hard aan uw dak als aan uw tuin. Dakpannen die iets verschoven zijn, losgetrokken lood of een barst in de nokvorst zijn met het blote oog van de straat nauwelijks te zien. Toch kan één kleine beschadiging na verloop van tijd leiden tot vochtinfiltratie, schimmel en structurele problemen in uw woning.</p>
    <p>In Nederland gelden stormen met windkracht 7 of hoger als een risico voor woningdaken. Na extreme weersomstandigheden — zeker in de provincies Groningen, Friesland en Drenthe waar windstoten van 100 km/u geen uitzondering zijn — loont het altijd om uw dak te laten controleren.</p>

    <h2>Wat kunt u zelf controleren?</h2>
    <p>U hoeft niet op het dak te klimmen om een eerste beoordeling te maken. Vanuit de grond of via een bovenslaapkamer kunt u al veel zien:</p>
    <ul>
      <li><strong>Verschoven of ontbrekende dakpannen</strong> — kijk of de rijen nog netjes aansluiten en of er pannen ontbreken</li>
      <li><strong>Kapotte nokvorsten</strong> — de nok (de 'rug' van het dak) is extra kwetsbaar bij storm; kijk of hij nog recht ligt</li>
      <li><strong>Losliggend loodwerk</strong> — rondom schoorstenen en dakramen zit lood dat bij storm kan lostrekken</li>
      <li><strong>Materiaal op de grond</strong> — stukken dakpan, dakgrind of lood rondom uw woning zijn een duidelijk signaal</li>
      <li><strong>Dakgoten</strong> — controleer of de goten nog recht hangen en niet verstopt zijn met afgewaaid materiaal</li>
    </ul>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Tip van de vakman</div>
      <p>Kijk ook na de storm naar uw plafonds en zoldervloer. Vochtplekken, verkleuringen of een muffe geur zijn tekenen dat er al water binnensijpelt &mdash; ook al ziet het dak er van buiten gaaf uit.</p>
    </div>

    <h2>Wanneer schakelt u een dakdekker in?</h2>
    <p>Schakel altijd een professional in wanneer:</p>
    <ol>
      <li>U zichtbare schade ziet die u zelf niet veilig kunt beoordelen</li>
      <li>Er water of vocht binnensijpelt of er al vochtplekken zichtbaar zijn</li>
      <li>Er dakpannen of nokvorsten ontbreken of gebroken zijn</li>
      <li>Het loodwerk rondom schoorsteen of dakraam loshangt</li>
      <li>Uw dak ouder is dan 20 jaar — ouder dak is gevoeliger voor stormschade</li>
    </ol>

    <div class="warn-box">
      <div class="warn-box-label">&#9888; Let op</div>
      <p>Klim nooit zelf op een nat of glibberig dak. Val- en glijrisico's zijn na een storm extra groot. Laat een vakman de inspectie uitvoeren &mdash; dit is bij de meeste verzekeringen ook een vereiste voor schadevergoeding.</p>
    </div>

    <h2>Stormschade en uw verzekering</h2>
    <p>De meeste inboedel- en opstalverzekeringen vergoeden stormschade aan uw dak, mits de windkracht minimaal 7 Beaufort was. Documenteer de schade goed: maak foto's zo snel mogelijk na de storm, noteer de datum en vraag bij het KNMI de windgegevens op voor uw locatie. Lees meer in ons artikel over <a href="blog-stormschade-verzekering.html" style="color:var(--blue-accent)">stormschade en uw verzekering</a>.</p>

    <h2>Conclusie</h2>
    <p>Na iedere storm met windkracht 7 of hoger is een dakcontrole geen overbodige luxe — het is verstandig preventief onderhoud. Vroegtijdige opsporing van schade bespaart u aanzienlijke reparatiekosten later. Twijfelt u? Laat een gratis dakinspectie uitvoeren door een van onze specialisten.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden is actief in Groningen, Friesland, Drenthe, Zwolle en Utrecht. Voor spoedgevallen zijn wij 24/7 bereikbaar via <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("blog-stormschade-verzekering.html","Verzekering","Stormschade aan je dak: wat vergoedt de verzekering?","18 augustus 2025 · 6 min"),
    ("blog-dakonderhoud-checklist.html","Onderhoud","Jaarlijkse dakonderhoud checklist","20 mei 2025 · 5 min"),
    ("blog-daklekkage-oorzaken.html","Lekkage","Lekkend dak: de 6 meest voorkomende oorzaken","10 juni 2025 · 7 min"),
  ]
))

# 2 ── Levensduur dak
posts.append(("blog-levensduur-dak.html",
  "Hoe lang gaat een dak mee? Levensduur per daktype",
  "Elke daksoort heeft een andere levensduur. Van dakpannen tot bitumen en EPDM — ontdek hoe lang uw dak nog meegaat en wanneer renovatie nodig is.",
  "levensduur dak, hoe lang gaat een dak mee, dakpannen levensduur, bitumen dak levensduur, dakrenovatie",
  "Onderhoud", "2 april 2025", 6,
  """
    <p class="art-lead">Een dak gaat niet eeuwig mee. Maar hoe lang precies? Dat hangt sterk af van het materiaal, de kwaliteit van de installatie en het onderhoud. In dit artikel zetten we de meest voorkomende daktypen op een rij.</p>

    <h2>Keramische en betonnen dakpannen</h2>
    <p>Dakpannen zijn het meest toegepaste dakmateriaal in Nederland. Goede kwaliteit keramische pannen gaan gemiddeld 50 tot 75 jaar mee; betonnen pannen 30 tot 50 jaar. De pannen zelf gaan lang mee, maar de onderconstructie, het loodwerk, de nokvorsten en het dakleer hebben een kortere levensduur.</p>
    <div class="sum-grid">
      <div class="sum-item"><h4>Keramische dakpannen</h4><p>50 &ndash; 75 jaar bij goed onderhoud. Nok en lood eerder vervangen.</p></div>
      <div class="sum-item"><h4>Betonnen dakpannen</h4><p>30 &ndash; 50 jaar. Kunnen na verloop van tijd poreus worden.</p></div>
    </div>

    <h2>Bitumen dakbedekking</h2>
    <p>Bitumen is het meest gebruikte materiaal voor platte daken in Nederland. Een kwalitatief goed aangelegd bitumendak gaat 20 tot 30 jaar mee. Goedkopere varianten of daken met gebreken kunnen al na 10 tot 15 jaar problemen geven. Regelmatig onderhoud verlengt de levensduur aanzienlijk.</p>

    <h2>EPDM rubber</h2>
    <p>EPDM (synthetisch rubber) is een modernere keuze voor platte daken. Mits correct aangelegd kan een EPDM-dak 40 tot 50 jaar meegaan zonder grote reparaties. Het is flexibel, bestand tegen UV en temperatuurschommelingen, en relatief onderhoudsvriendelijk.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Wist u dat</div>
      <p>Een bitumendak dat goed onderhouden wordt, kan 5 tot 10 jaar langer meegaan dan een verwaarloosd dak van dezelfde kwaliteit. J&auml;&auml;rlijkse inspectie loont dus altijd.</p>
    </div>

    <h2>Leien daken</h2>
    <p>Leien zijn het meest duurzame dakmateriaal. Natuurleien daken gaan 80 tot 150 jaar mee. Ze zijn duur in aanschaf en onderhoud, maar vormen een monumentale en tijdloze keuze voor woningen in Noord-Nederland.</p>

    <h2>Zinken daken en dakgoten</h2>
    <p>Zink is een populair materiaal voor aansluitingen, dakgoten en speciale dakvormen. Een zinken dak of dakgoot gaat 60 tot 80 jaar mee als het goed is aangebracht en niet in contact komt met agressieve materialen.</p>

    <h2>Wanneer is renovatie nodig?</h2>
    <p>Let op de volgende signalen, ongeacht de leeftijd van uw dak:</p>
    <ul>
      <li>Vochtplekken op plafond of muren binnenshuis</li>
      <li>Gebroken, verschoven of ontbrekende dakpannen</li>
      <li>Mos- of algengroei die niet verdwijnt na reiniging</li>
      <li>Blaasvorming of naadverschuiving op een plat dak</li>
      <li>Loodwerk dat loslaat rondom schoorsteen of dakramen</li>
      <li>Stijgende energiekosten door warmteverlies via het dak</li>
    </ul>

    <h2>Uw dak laten inspecteren</h2>
    <p>Weet u niet zeker hoe oud uw dak is of in welke staat het verkeert? Laat een professionele dakinspectie uitvoeren. Onze specialisten beoordelen het volledige daksysteem en geven u een eerlijk advies — kosteloos en vrijblijvend.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden verzorgt dakinspecties en dakrenovaties in heel Noord-Nederland. Neem contact op via <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("blog-dakonderhoud-checklist.html","Onderhoud","Jaarlijkse dakonderhoud checklist","20 mei 2025 · 5 min"),
    ("blog-dakschade-storm.html","Schade","Hoe herken je dakschade na een storm?","15 maart 2025 · 5 min"),
    ("blog-dakpannen-soorten.html","Materialen","Welke dakpannen zijn het beste voor jouw woning?","1 augustus 2025 · 6 min"),
  ]
))

# 3 ── Dakisolatie besparing
posts.append(("blog-dakisolatie-besparing.html",
  "Dakisolatie: zo bespaar je honderden euro's per jaar",
  "Een slecht geïsoleerd dak is de grootste bron van warmteverlies in uw woning. Ontdek hoe dakisolatie werkt, wat het kost en hoe snel het terugverdient.",
  "dakisolatie, dak isoleren, energiebesparing dak, isolatiewaarden, spouwmuurisolatie dak, plat dak isolatie",
  "Isolatie", "18 april 2025", 7,
  """
    <p class="art-lead">Wist u dat via een slecht geïsoleerd dak tot wel 30 procent van de warmte in uw woning verloren gaat? Dakisolatie is een van de meest effectieve investeringen die u kunt doen voor een lager energieverbruik en meer wooncomfort.</p>

    <img src="tnoordenfoto/dakisolatie.webp" alt="Dakisolatie materialen" class="art-img" />

    <h2>Waarom het dak zo belangrijk is</h2>
    <p>Warmte stijgt altijd op. Dat betekent dat uw dak het eerste aanrakingspunt is waar warmte het huis verlaat. Hoe slechter de isolatie, hoe harder uw verwarmingsinstallatie moet werken om de binnentemperatuur op peil te houden. En dat kost geld — maand na maand.</p>
    <p>Met de sterk gestegen energieprijzen van de afgelopen jaren verdient dakisolatie zich sneller terug dan ooit. Afhankelijk van het type woning en de isolatieoplossing kunt u rekenen op een terugverdientijd van 5 tot 10 jaar — daarna is de besparing pure winst.</p>

    <h2>Soorten dakisolatie</h2>
    <h3>Isolatie van schuine daken</h3>
    <p>Bij schuine daken zijn er drie methoden: isolatie aan de binnenzijde (het meest toegepast bij renovatie), isolatie tussen de gordingen, en isolatie aan de buitenzijde (bij volledige dakrenovatie). De keuze hangt af van uw situatie, budget en de gewenste Rc-waarde.</p>
    <h3>Isolatie van platte daken</h3>
    <p>Bij platte daken wordt isolatie aangebracht boven of onder de dakbedekking. Bovenisolatie (warm dak) is de meest effectieve methode en wordt standaard toegepast bij een nieuwe dakbedekking.</p>

    <div class="sum-grid">
      <div class="sum-item"><h4>Schuind dak isoleren</h4><p>Gemiddeld &euro;30 &ndash; &euro;60 per m&sup2;. Afhankelijk van methode en materiaal.</p></div>
      <div class="sum-item"><h4>Plat dak isoleren</h4><p>Gemiddeld &euro;40 &ndash; &euro;80 per m&sup2;, inclusief nieuwe dakbedekking.</p></div>
    </div>

    <h2>Welke Rc-waarde heeft u nodig?</h2>
    <p>De Rc-waarde geeft de thermische weerstand van isolatie aan: hoe hoger, hoe beter. Voor nieuwbouw geldt momenteel een minimum van Rc 6,0 voor daken. Voor bestaande woningen adviseert het Rijk minimaal Rc 3,5 bij renovatie. Wij adviseren altijd om te streven naar Rc 5,0 of hoger voor optimale energiebesparing en een comfortabel binnenklimaat.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Subsidies en regelingen</div>
      <p>Vraag altijd naar de actuele ISDE-subsidie (Investeringssubsidie Duurzame Energie en Energiebesparing) en eventuele gemeentelijke regelingen. Dakisolatie komt hiervoor in aanmerking en kan de investering tot 20% verlagen.</p>
    </div>

    <h2>Hoeveel bespaart u?</h2>
    <p>Een gemiddeld Nederlands rijtjeshuis met een ongeïsoleerd of slecht geïsoleerd dak verliest jaarlijks voor &euro;300 tot &euro;600 aan energie via het dak. Met goede isolatie kunt u dit bijna volledig elimineren. Bij een investering van &euro;3.000 is de terugverdientijd dus 5 tot 10 jaar — en daarna bespaart u elk jaar.</p>

    <h2>Combineer dakisolatie met andere maatregelen</h2>
    <p>Dakisolatie rendeert nog beter als u het combineert met vloerisolatie, gevelisolatie en HR++ beglazing. Door de woning als systeem te benaderen, bereikt u het beste resultaat voor het laagste gecombineerde budget.</p>

    <h2>Laat uw dak gratis inspecteren</h2>
    <p>Weet u niet zeker of uw dak al voldoende geïsoleerd is of wilt u weten welke opties er zijn? Onze specialisten beoordelen uw dak gratis en geven u een eerlijk advies op maat.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden plaatst dakisolatie in Groningen, Friesland, Drenthe, Zwolle en Utrecht. Bel ons op <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a> voor meer informatie.</p>
  """,
  [
    ("dak-isolatie.html","Dienst","Bekijk onze isolatiedienst","Gratis offerte · Noord-Nederland"),
    ("blog-plat-dak-problemen.html","Plat dak","5 veelvoorkomende problemen met platte daken","5 mei 2025 · 6 min"),
    ("blog-levensduur-dak.html","Onderhoud","Hoe lang gaat een dak mee?","2 april 2025 · 6 min"),
  ]
))

# 4 ── Plat dak problemen
posts.append(("blog-plat-dak-problemen.html",
  "5 veelvoorkomende problemen met platte daken",
  "Platte daken zijn gevoelig voor specifieke problemen zoals waterophoping, blaasvorming en naadverschuiving. Leer hoe u ze herkent en voorkomt.",
  "plat dak problemen, waterophoping plat dak, blaasvorming bitumen, plat dak lekkage, onderhoud plat dak",
  "Plat dak", "5 mei 2025", 6,
  """
    <p class="art-lead">Een plat dak heeft veel voordelen — ruimtebesparend, modern en functioneel. Maar het stelt ook specifieke eisen aan onderhoud en materiaalgebruik. Wij zetten de vijf meest voorkomende problemen op een rij.</p>

    <h2>1. Waterophoping (ponding)</h2>
    <p>Een plat dak is nooit echt plat: het heeft altijd een lichte helling (minimaal 1%) om hemelwater naar de afvoer te leiden. Als die helling te klein is, de afvoer verstopt raakt of de constructie is doorgebogen, blijft water op het dak staan. Dit heet "ponding".</p>
    <p>Waterophoping is gevaarlijk omdat het extra gewicht de constructie belast, de dakbedekking sneller slijt en vocht bij temperatuurwisselingen in het materiaal dringt. Controleer na zware regenval altijd of er water blijft staan.</p>

    <div class="warn-box">
      <div class="warn-box-label">&#9888; Gevaar</div>
      <p>Meer dan 10 cm waterophoping op een plat dak kan leiden tot constructieve schade. Schakel bij twijfel meteen een vakman in.</p>
    </div>

    <h2>2. Blaasvorming in bitumen</h2>
    <p>Blaren of bollen in de dakbedekking ontstaan doordat lucht of vocht tussen de lagen bitumen is terechtgekomen. Dit kan gebeuren door een slechte verlijming of hechting tijdens de installatie, of door vocht dat na verloop van tijd door de dakbedekking is gedrongen.</p>
    <p>Kleine blaren zijn soms acceptabel, maar grote of groeiende blaren moeten worden gerepareerd. Ze scheuren open bij extreme temperaturen en maken het dak kwetsbaar voor lekkage.</p>

    <h2>3. Naadverschuiving en scheurvorming</h2>
    <p>Bitumen en andere dakbedekkingen zetten uit bij warmte en krimpen bij kou. Over de jaren kan dit leiden tot naadverschuiving — de overlappingen van de dakbaan schuiven op elkaar. Zichtbare scheuren of openstaande naden zijn een duidelijk teken dat reparatie nodig is.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Preventie</div>
      <p>Laat een plat dak minimaal elke 2 tot 3 jaar controleren door een dakspecialist. Kleine naadverschuivingen zijn eenvoudig te repareren; wacht u te lang, dan is de kans groot dat het dak volledig vernieuwd moet worden.</p>
    </div>

    <h2>4. Verstopte dakafvoeren</h2>
    <p>Bladeren, mos, dakgrind en stof kunnen de dakafvoer verstopt raken. Een verstopte afvoer leidt direct tot waterophoping en verhoogt het risico op lekkage aanzienlijk. Maak de afvoer minimaal twee keer per jaar schoon — in het najaar na de bladval en in het voorjaar.</p>

    <h2>5. Loslating van folie of detaillering</h2>
    <p>Rondom opstaande randen, doorvoeren (voor dakramen, ventilatiekanalen of schoorstenen) en aansluitingen op muren is de dakbedekking het meest kwetsbaar. Hier moet het materiaal omhoog worden gevoerd en vastgezet. Wind, uitzetting en krimp zorgen ervoor dat deze aansluitingen na verloop van tijd kunnen loslaten — met lekkage als gevolg.</p>

    <h2>Hoe houdt u uw platte dak gezond?</h2>
    <ul>
      <li>Laat het dak jaarlijks of tweejaarlijks professioneel inspecteren</li>
      <li>Houd de afvoer vrij van verstoppingen</li>
      <li>Verwijder mos en algengroei tijdig</li>
      <li>Laat kleine scheuren of loslating snel repareren — uitstel verergert altijd</li>
      <li>Kies bij renovatie voor kwalitatieve materialen met garantie</li>
    </ul>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Problemen met uw platte dak? Dakbedrijf 'T Noorden helpt u snel en vakkundig. Actief in Noord-Nederland &mdash; bel <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("bitumen-daken.html","Dienst","Bitumen Daken Noord-Nederland","Gratis offerte · Platte daken"),
    ("blog-bitumen-epdm-verschil.html","Materialen","Bitumen of EPDM: wat past bij jouw plat dak?","28 juni 2025 · 8 min"),
    ("blog-dakisolatie-besparing.html","Isolatie","Dakisolatie: zo bespaar je honderden euro's","18 april 2025 · 7 min"),
  ]
))

# 5 ── Dakonderhoud checklist
posts.append(("blog-dakonderhoud-checklist.html",
  "Jaarlijkse dakonderhoud checklist voor woningeigenaren",
  "Met deze handige checklist weet u precies wat u jaarlijks moet controleren aan uw dak om dure reparaties te voorkomen. Inclusief tips van dakspecialisten.",
  "dakonderhoud checklist, jaarlijks dak controleren, dakonderhoud tips, preventief dakonderhoud, dak inspecteren",
  "Onderhoud", "20 mei 2025", 5,
  """
    <p class="art-lead">Goed dakonderhoud begint met regelmatige controle. Een dak dat jaarlijks wordt geïnspecteerd, gaat gemiddeld 10 tot 15 jaar langer mee dan een verwaarloosd dak. Gebruik deze checklist als leidraad.</p>

    <img src="tnoordenfoto/2025-10-07 (1).webp" alt="Dakonderhoud door specialist" class="art-img" />

    <h2>Voorjaarsinspectie (april – mei)</h2>
    <p>Na de winter is het ideale moment om uw dak te controleren. Vorst, sneeuw en storm kunnen schade hebben aangericht die u in de zomer wilt herstellen.</p>
    <ul>
      <li><strong>Dakpannen</strong> — zijn er verschoven, gebroken of ontbrekende pannen?</li>
      <li><strong>Nokvorsten</strong> — liggen ze nog vast en zijn er geen barsten zichtbaar?</li>
      <li><strong>Dakgoten</strong> — vrij van bladeren en vuil? Hangen ze nog recht?</li>
      <li><strong>Loodwerk</strong> — zit het lood rondom schoorsteen en dakramen nog vast?</li>
      <li><strong>Mos en algen</strong> — zijn er groene of zwarte aangroeiingen zichtbaar?</li>
      <li><strong>Plat dak</strong> — zijn er blaren, scheuren of waterophoping?</li>
    </ul>

    <h2>Najaarscontrole (oktober – november)</h2>
    <p>Vóór de winter controleert u of uw dak de koudste maanden goed kan doorstaan.</p>
    <ul>
      <li><strong>Dakgoten reinigen</strong> — verwijder blad en takken na de bladval</li>
      <li><strong>Afvoerpunten</strong> — zijn alle afvoeren vrij zodat regenwater goed wegloopt?</li>
      <li><strong>Dakramen en kitranden</strong> — zijn de kitranden intact en niet uitgedroogd?</li>
      <li><strong>Zolder of vliering</strong> — zijn er vochtplekken, schimmel of daglichtkieren zichtbaar?</li>
      <li><strong>Sneeuwlading</strong> — is uw dakconstructie berekend op eventuele zware sneeuwval?</li>
    </ul>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Tip</div>
      <p>Controleer uw dak altijd vanuit de grond of met een verrekijker &mdash; klim er niet zelf op. Voor een grondige inspectie schakelt u een vakman in die het veilig en vakkundig kan beoordelen.</p>
    </div>

    <h2>Na elke storm (windkracht 7+)</h2>
    <ul>
      <li>Controleer of er materiaal op de grond rondom uw woning ligt</li>
      <li>Kijk vanuit de straat of alle pannen en nokvorsten nog op hun plek liggen</li>
      <li>Controleer zolder en plafonds op vocht of daglichtkieren</li>
    </ul>

    <h2>Wanneer schakelt u een professional in?</h2>
    <p>Sommige onderhoudswerkzaamheden kunt u zelf uitvoeren, zoals het schoonmaken van dakgoten. Maar voor alles dat te maken heeft met het dak zelf — pannen, lood, bitumen, isolatie — geldt: schakel een gecertificeerde dakdekker in. Werken op hoogte is gevaarlijk en verkeerd uitgevoerd dakwerk leidt al snel tot grotere schade.</p>

    <h2>Dakonderhoud laten uitvoeren</h2>
    <p>Wilt u uw dak vakkundig laten onderhouden? Dakbedrijf 'T Noorden biedt preventief dakonderhoud aan in heel Noord-Nederland. Wij stellen een onderhoudsplan op maat op, zodat uw dak altijd in topconditie blijft.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden &mdash; uw betrouwbare dakspecialist in Groningen, Friesland, Drenthe, Zwolle en Utrecht. <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a></p>
  """,
  [
    ("dakinspectie.html","Dienst","Gratis Dakinspectie Noord-Nederland","Vrijblijvend · Inclusief rapport"),
    ("blog-dakschade-storm.html","Schade","Hoe herken je dakschade na een storm?","15 maart 2025 · 5 min"),
    ("blog-levensduur-dak.html","Onderhoud","Hoe lang gaat een dak mee?","2 april 2025 · 6 min"),
  ]
))

# 6 ── Daklekkage oorzaken
posts.append(("blog-daklekkage-oorzaken.html",
  "Lekkend dak: de 6 meest voorkomende oorzaken",
  "Daklekkage heeft altijd een oorzaak — maar die is niet altijd zichtbaar. Ontdek de zes meest voorkomende oorzaken en wat u eraan kunt doen.",
  "daklekkage oorzaken, lekkend dak, daklek repareren, oorzaak lekkage dak, vochtschade dak",
  "Lekkage", "10 juni 2025", 7,
  """
    <p class="art-lead">Een lekkend dak is een van de meest vervelende problemen voor woningeigenaren. Het goede nieuws: lekkage heeft altijd een specifieke oorzaak. Als u weet waar u op moet letten, kunt u snel en doelgericht ingrijpen.</p>

    <h2>1. Beschadigd of losliggend loodwerk</h2>
    <p>Lood wordt gebruikt rondom schoorstenen, dakramen, muurvoeten en aansluitingen. Het is een van de meest kwetsbare plekken op het dak, omdat lood uitzet en krimpt door temperatuurverschillen. Na jaren van gebruik kan het lood loslaten, scheuren of versleten raken — met lekkage als direct gevolg.</p>
    <p>Kenmerkend: loodlekkage is vaak zichtbaar als een watervlek dicht bij een schoorsteen of dakraam, aan het plafond direct eronder.</p>

    <h2>2. Kapotte of verschoven dakpannen</h2>
    <p>Dakpannen beschermen de onderconstructie van uw dak. Als een pan breekt, verschuift of gewoon ontbreekt, kan regenwater direct doordringen in de houten constructie en isolatie. Dit type schade is vaak het gevolg van storm, vorst of gewoon slijtage na tientallen jaren gebruik.</p>

    <div class="warn-box">
      <div class="warn-box-label">&#9888; Belangrijk</div>
      <p>Wacht niet tot u lekkage ziet binnenshuis. Water dat door een kapotte pan binnendringt, beschadigt de dakconstructie soms al maanden voordat er vochtplekken op uw plafond verschijnen.</p>
    </div>

    <h2>3. Verstopte of beschadigde dakgoten</h2>
    <p>Dakgoten die verstopt zijn met bladeren, takken of mos kunnen water niet goed afvoeren. Het water loopt dan over de rand of drukt terug onder de dakpannen. Op den duur kan dit leiden tot vochtschade aan de dakrand, de gevelplank en de fundering van uw woning.</p>

    <h2>4. Verouderde dakbedekking op een plat dak</h2>
    <p>Bitumen en andere bedekkingsmaterialen voor platte daken verouderen na verloop van tijd. Scheuren, naadverschuiving en het lostrekken van randen zijn tekenen dat de dakbedekking aan het einde van zijn levensduur is. Gemiddeld is een bitumendak na 20 tot 25 jaar aan vervanging toe.</p>

    <h2>5. Beschadigde kitrand rondom dakramen</h2>
    <p>Dakramen worden afgedicht met kitringen en rubber afdichtingen. Na jaren van blootstelling aan zon, regen en temperatuurwisselingen worden deze materialen hard en bros. Een gescheurde kitrand is een van de meest voorkomende oorzaken van lekkage rondom dakramen.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Snelle controle</div>
      <p>Controleer de kitrand rondom uw dakramen jaarlijks. Als de kit hard, gebarsten of verkleurd is, laat hem dan professioneel vervangen. Dit is een kleine ingreep die grote wateroverlast voorkomt.</p>
    </div>

    <h2>6. Condensatie en binnenklimaat</h2>
    <p>Niet elke "lekkage" komt van buiten. Als de dakisolatie onvoldoende is of als er geen dampscherm aanwezig is, kan warme vochtige lucht van binnenuit condenseren in de dakconstructie. Dit kan leiden tot schimmelgroei, houtrot en dezelfde vochtplekken die u ziet bij een echte lekkage. Een bouwfysische inspectie kan uitsluitsel geven.</p>

    <h2>Wat te doen bij een lekkend dak?</h2>
    <ol>
      <li>Beperk de binnenkomende schade: zet emmers neer en leg handdoeken op het vloerkleed</li>
      <li>Documenteer de schade met foto's (belangrijk voor uw verzekeraar)</li>
      <li>Neem direct contact op met een dakspecialist — bij acute lekkage staat onze 24/7 spoedservice voor u klaar</li>
      <li>Laat de oorzaak professioneel vaststellen voordat u zelf iets repareert</li>
    </ol>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden verhelpt daklekkages in heel Noord-Nederland. 24/7 spoedservice beschikbaar. Bel <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("daklekkage.html","Dienst","Daklekkage Oplossen Noord-Nederland","24/7 spoedservice beschikbaar"),
    ("spoed.html","Spoedservice","Spoed Dakservice 24/7","Direct beschikbaar · Noord-Nederland"),
    ("blog-dakschade-storm.html","Schade","Hoe herken je dakschade na een storm?","15 maart 2025 · 5 min"),
  ]
))

# 7 ── Bitumen vs EPDM
posts.append(("blog-bitumen-epdm-verschil.html",
  "Bitumen of EPDM: wat past het beste bij jouw plat dak?",
  "Twee populaire materialen voor platte daken vergeleken: bitumen en EPDM. We bespreken prijs, levensduur, onderhoud en welk materiaal past bij uw situatie.",
  "bitumen vs EPDM, plat dak materiaal, bitumen dakbedekking, EPDM rubber dak, plat dak renovatie",
  "Materialen", "28 juni 2025", 8,
  """
    <p class="art-lead">Als u uw platte dak wilt renoveren of vernieuwen, heeft u de keuze uit twee hoofdmaterialen: bitumen en EPDM. Beide zijn populair in Nederland, maar ze hebben elk hun eigen voor- en nadelen. Wij helpen u de juiste keuze te maken.</p>

    <h2>Wat is bitumen?</h2>
    <p>Bitumen is een derivaat van aardolie en wordt al tientallen jaren gebruikt als dakbedekking voor platte daken. Het wordt aangebracht in twee of drie lagen die met branders worden samengeweld, waardoor een waterdichte aaneengesloten laag ontstaat. De meest gebruikte variant in Nederland is SBS-gemodificeerd bitumen, dat flexibeler en duurzamer is dan traditioneel bitumen.</p>

    <h2>Wat is EPDM?</h2>
    <p>EPDM (Ethyleen-Propyleen-Dieen-Monomeer) is een synthetisch rubber dat in één grote folie over het dak wordt aangebracht. Het wordt vastgezet met lijm of mechanisch bevestigd. EPDM is relatief jong als dakmateriaal maar wint snel aan populariteit vanwege zijn lange levensduur en duurzame eigenschappen.</p>

    <div class="sum-grid">
      <div class="sum-item"><h4>Bitumen</h4><p>Levensduur: 20&ndash;30 jaar. Vertrouwd materiaal, breed toepasbaar, repareerbaar. Installatie vereist open vuur.</p></div>
      <div class="sum-item"><h4>EPDM</h4><p>Levensduur: 40&ndash;50 jaar. Duurzaam, flexibel, geen open vuur nodig. Hogere aanschafprijs.</p></div>
    </div>

    <h2>Vergelijking op de belangrijkste punten</h2>
    <h3>Prijs</h3>
    <p>Bitumen is doorgaans goedkoper in aanschaf dan EPDM. Voor een eenvoudig plat dak kunt u rekenen op &euro;30 tot &euro;60 per m&sup2; voor bitumen versus &euro;40 tot &euro;75 per m&sup2; voor EPDM. De langere levensduur van EPDM maakt het over de totale gebruikstermijn echter vaak voordeliger.</p>

    <h3>Levensduur</h3>
    <p>Een goed aangelegd bitumendak gaat 20 tot 30 jaar mee. EPDM heeft een bewezen levensduur van 40 tot 50 jaar. Bij een groot dak kan dit verschil in levensduur een complete renovatie schelen.</p>

    <h3>Onderhoud</h3>
    <p>Beide materialen vereisen minimaal onderhoud als ze goed zijn aangelegd. Bitumen kan na verloop van tijd blaasvorming of naadverschuiving vertonen, wat professionele reparatie vereist. EPDM is minder gevoelig voor dit soort problemen maar heeft specifieke lijm en reparatietape nodig bij eventuele schade.</p>

    <h3>Duurzaamheid</h3>
    <p>EPDM wint het duurzaamheidsdebat: het materiaal bevat geen zware metalen, is UV-bestendig en is aan het einde van zijn levensduur recycleerbaar. Bitumen bevat aardoliederivaten en wordt minder duurzaam geacht.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Advies van de vakman</div>
      <p>Kiest u voor een langetermijninvestering en een duurzamere oplossing? Ga dan voor EPDM. Heeft u een kleiner budget of een ouder pand waarbij bitumen al aanwezig is? Dan is hoogwaardig SBS-bitumen een uitstekende en betrouwbare keuze.</p>
    </div>

    <h2>Wanneer kiest u voor welk materiaal?</h2>
    <ul>
      <li><strong>Kies bitumen</strong> als uw dak al een bitumenconstructie heeft (uitbreiding of renovatie is eenvoudiger), bij een kleiner budget, of bij complexe dakvormen met veel details</li>
      <li><strong>Kies EPDM</strong> als u lang wilt genieten zonder onderhoud, als duurzaamheid voor u zwaar weegt, of bij een nieuwbouwproject</li>
    </ul>

    <h2>Gratis advies op maat</h2>
    <p>Weet u niet welk materiaal het beste bij uw situatie past? Onze specialisten kijken graag mee en geven u een eerlijk advies — zonder verplichtingen.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden is specialist in zowel bitumen als EPDM platte daken in Noord-Nederland. Neem contact op via <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("bitumen-daken.html","Dienst","Bitumen Daken Noord-Nederland","Gratis offerte · Platte daken"),
    ("blog-plat-dak-problemen.html","Plat dak","5 veelvoorkomende problemen met platte daken","5 mei 2025 · 6 min"),
    ("blog-levensduur-dak.html","Onderhoud","Hoe lang gaat een dak mee?","2 april 2025 · 6 min"),
  ]
))

# 8 ── Vogeloverlast
posts.append(("blog-vogeloverlast-dak.html",
  "Vogeloverlast op je dak: oorzaken en oplossingen",
  "Duiven, meeuwen en spreeuwen op het dak zorgen voor schade en rommel. Ontdek hoe u vogels effectief en diervriendelijk kunt weren van uw dak.",
  "vogeloverlast dak, duiven weren, meeuw dak, spreeuwen dak, vogelwering dak, anti-vogel systeem",
  "Vogelwering", "15 juli 2025", 5,
  """
    <p class="art-lead">Vogels op uw dak klinken misschien onschuldig, maar kunnen serieuze schade aanrichten. Uitwerpselen die de dakbedekking aantasten, nesten die afvoeren verstopt raken en de geluidsoverlast — vogelwering is geen luxe, maar een verstandige investering.</p>

    <img src="tnoordenfoto/vogelwering.webp" alt="Vogels op dak" class="art-img" />

    <h2>Welke vogels zijn het grootste probleem?</h2>
    <h3>Duiven</h3>
    <p>Duiven zijn de meest voorkomende plaagvogel op daken in Noord-Nederland. Ze nestelen graag op platte daken, in dakgoten en achter dakpannen. Duivenmest is sterk zuur en tast bitumen, lood en hout aan. Bovendien verspreidt duivenmest ziektekiemen die gevaarlijk kunnen zijn voor mensen.</p>
    <h3>Meeuwen</h3>
    <p>In kustgebieden en steden nestelen meeuwen graag op platte daken. Ze zijn luidruchtig, agressief bij het verdedigen van hun nest en produceren grote hoeveelheden mest. Meeuwen staan onder de Wet Natuurbescherming, wat betekent dat actieve verstoring van nesten zonder vergunning verboden is.</p>
    <h3>Spreeuwen</h3>
    <p>Spreeuwen nestelen graag in spleten en kieren onder dakpannen. Ze trekken grote zwermen aan en hun nesten kunnen houtrot veroorzaken. Ze zijn ook beschermd.</p>

    <div class="warn-box">
      <div class="warn-box-label">&#9888; Let op: beschermde soorten</div>
      <p>Veel vogels in Nederland staan onder de Wet Natuurbescherming. Het verwijderen van actieve nesten of eieren is strafbaar. Laat vogelwering altijd installeren door een specialist die op de hoogte is van de regelgeving.</p>
    </div>

    <h2>Hoeveel schade veroorzaken vogels?</h2>
    <p>De schade die vogels aan uw dak aanrichten is groter dan veel mensen denken:</p>
    <ul>
      <li>Vogeluitwerpselen bevatten zuren die bitumen, lood en dakpannen aantasten</li>
      <li>Nesten in dakgoten blokkeren de waterafvoer, wat leidt tot waterophoping</li>
      <li>Spleten die vogels vergroten om toegang te krijgen, leiden tot vochtinfiltratie</li>
      <li>Organisch nestmateriaal houdt vocht vast en versnelt houtrot</li>
    </ul>

    <h2>Effectieve vogelweringsmethoden</h2>
    <h3>Vogelspikes (anti-nestpinnen)</h3>
    <p>Roestvrijstalen of kunststof pinnen worden aangebracht op dakranden, nokvorsten en andere landingsplekken. Ze voorkomen dat vogels kunnen landen en nestelen zonder hen te beschadigen.</p>
    <h3>Vogelnet</h3>
    <p>Een fijnmazig polypropyleen net wordt gespannen over het te beschermen gebied. Ideaal voor grote platte daken en gebieden waar vogels toegang zoeken tot constructiedelen.</p>
    <h3>Elektrische afschrikkingssystemen</h3>
    <p>Een lage, pijnloze elektrische stroom schrikt vogels af zonder hen te verwonden. Dit is een van de meest effectieve methoden voor hardnekkige plaagvogels.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Preventie is goedkoper</div>
      <p>Vogelwering installeren voordat er nestvorming plaatsvindt is altijd goedkoper dan het verwijderen van nesten, reinigen van dakbedekking en repareren van vogelschade achteraf.</p>
    </div>

    <h2>Wat kost vogelwering?</h2>
    <p>De kosten voor vogelwering hangen af van het type systeem, de omvang van het te beschermen gebied en de bereikbaarheid. Een eenvoudige anti-nestpin installatie op een nokvorst begint rond &euro;150 tot &euro;400. Een volledig net over een plat dak kan oplopen tot &euro;1.000 of meer. Laat altijd een vrijblijvende offerte opmaken.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden installeert vogelwering in heel Noord-Nederland. Gratis inspectie aanvragen via <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("vogelwering.html","Dienst","Vogelwering Noord-Nederland","Gratis inspectie · Diervriendelijk"),
    ("blog-dakonderhoud-checklist.html","Onderhoud","Jaarlijkse dakonderhoud checklist","20 mei 2025 · 5 min"),
    ("blog-plat-dak-problemen.html","Plat dak","5 veelvoorkomende problemen met platte daken","5 mei 2025 · 6 min"),
  ]
))

# 9 ── Dakpannen soorten
posts.append(("blog-dakpannen-soorten.html",
  "Welke dakpannen zijn het beste voor jouw woning?",
  "Keramisch, beton, leisteen of staal — de keuze in dakpannen is groot. Wij vergelijken de populairste soorten op prijs, levensduur en uitstraling.",
  "soorten dakpannen, keramische dakpannen, betonnen dakpannen, leistenen dak, dakpannen kiezen, dakrenovatie materialen",
  "Materialen", "1 augustus 2025", 6,
  """
    <p class="art-lead">De keuze in dakpannen is groter dan ooit. Van klassiek keramiek tot moderne betonpannen en duurzame leien — elk type heeft zijn eigen voor- en nadelen op het gebied van prijs, levensduur, gewicht en uitstraling.</p>

    <img src="tnoordenfoto/2025-05-20.webp" alt="Dakpannen op een woning" class="art-img" />

    <h2>1. Keramische dakpannen</h2>
    <p>Keramische dakpannen zijn gemaakt van gebakken klei en zijn al eeuwen het meest toegepaste dakmateriaal in Nederland. Ze zijn duurzaam, onderhoudsarm en beschikbaar in tientallen kleuren en vormen. De levensduur is 50 tot 75 jaar bij goed onderhoud.</p>
    <div class="sum-grid">
      <div class="sum-item"><h4>Voordelen</h4><p>Lange levensduur, kleurecht, vorstbestendig, bewezen kwaliteit, hoge brandveiligheid.</p></div>
      <div class="sum-item"><h4>Nadelen</h4><p>Hogere prijs dan beton, zwaarder gewicht vraagt om sterke dakconstructie.</p></div>
    </div>

    <h2>2. Betonnen dakpannen</h2>
    <p>Betonnen dakpannen zijn een goedkoper alternatief voor keramiek. Ze zijn solide, sterk en verkrijgbaar in diverse kleuren. De levensduur is korter dan keramiek (30 tot 50 jaar) en na verloop van tijd kunnen ze poreus worden, waardoor mos en algen sneller vat krijgen.</p>

    <h2>3. Leien (Leisteen)</h2>
    <p>Leien zijn het meest exclusieve en duurzame dakmateriaal. Natuurleien gaan 80 tot 150 jaar mee en geven een woning een tijdloze, monumentale uitstraling. Ze zijn populair bij rijksmonumenten en historische panden, maar ook bij moderne luxewoningen.</p>
    <p>Het nadeel: leien zijn duur in aanschaf en installatie, en er zijn weinig vakspecialisten die dit ambacht nog beheersen.</p>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Monumentale panden</div>
      <p>Heeft u een rijksmonument of gemeentelijk monument? Dan kunt u verplicht zijn om het originele dakmateriaal terug te plaatsen. Vraag altijd advies bij de gemeente voordat u kiest voor een ander type dakpan.</p>
    </div>

    <h2>4. Zinken dakplaten</h2>
    <p>Zink is een populaire keuze voor speciale dakvormen, mansardedaken en moderne architectuur. Zink is zeer duurzaam (60 tot 80 jaar), veroudert mooi en is volledig recycleerbaar. Het is echter duurder in aanschaf en vakkundig plaatsen is een specialisme.</p>

    <h2>5. Betaalbare alternatieven: staal en composiet</h2>
    <p>Stalen dakpannen (gegalvaniseerd of gecoat) zijn licht van gewicht, goedkoop en snel te installeren. Ze zijn populair in de agrarische sector en bij bijgebouwen. Composiet dakpannen combineren het uiterlijk van leisteen met het gewicht van kunststof — een opkomend materiaal met een verwachte levensduur van 40 tot 60 jaar.</p>

    <h2>Welke dakpan past bij uw woning?</h2>
    <p>Bij het kiezen van dakpannen spelen meerdere factoren een rol:</p>
    <ul>
      <li><strong>Draagvermogen</strong> — keramiek en leien zijn zwaarder dan beton of staal; controleer of uw dakconstructie dit aankan</li>
      <li><strong>Dakhelling</strong> — niet elk type pan is geschikt voor elke dakhelling; controleer de minimale helling van het gekozen type</li>
      <li><strong>Bestemmingsplan of welstandseisen</strong> — sommige gemeenten schrijven voor welk type of kleur dakpan gebruikt mag worden</li>
      <li><strong>Budget</strong> — keramiek en leien zijn duurder, maar betalen zich terug in levensduur en woningwaarde</li>
      <li><strong>Uitstraling</strong> — kies een pan die past bij de architectuur van uw woning en de buurt</li>
    </ul>

    <h2>Advies op maat</h2>
    <p>Wilt u weten welke dakpannen het beste passen bij uw woning? Onze specialisten adviseren u graag en laten u ook materiaalmonsterstalen zien tijdens de gratis inspectie.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Dakbedrijf 'T Noorden verzorgt dakrenovaties en pannenvervanging in heel Noord-Nederland. Vraag een gratis offerte aan via <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("dakrenovatie.html","Dienst","Dakrenovatie Noord-Nederland","Gratis inspectie · Op maat"),
    ("blog-levensduur-dak.html","Onderhoud","Hoe lang gaat een dak mee?","2 april 2025 · 6 min"),
    ("blog-bitumen-epdm-verschil.html","Materialen","Bitumen of EPDM: wat past bij jouw plat dak?","28 juni 2025 · 8 min"),
  ]
))

# 10 ── Stormschade verzekering
posts.append(("blog-stormschade-verzekering.html",
  "Stormschade aan je dak: wat vergoedt de verzekering?",
  "Storm heeft uw dak beschadigd? Leer hoe u een claim indient, welk bewijs u nodig heeft en wat uw opstalverzekering vergoedt bij dakschade.",
  "stormschade verzekering, opstalverzekering dak, stormschade claimen, dakschade vergoeding, windkracht 7 verzekering",
  "Verzekering", "18 augustus 2025", 6,
  """
    <p class="art-lead">Een storm heeft uw dak beschadigd. Behalve het regelen van een vakman wilt u weten wat uw verzekeraar vergoedt. Wij leggen uit hoe de claim werkt, wat u moet documenten en waar u op moet letten.</p>

    <h2>Wanneer vergoedt uw verzekering dakschade?</h2>
    <p>De meeste opstalverzekeringen vergoeden schade door storm, maar er zijn voorwaarden. De belangrijkste: er moet sprake zijn van stormschade, wat doorgaans gedefinieerd wordt als wind met een snelheid van minimaal 14 meter per seconde (Beaufort 7) of hoger.</p>
    <p>Schade door gewone regen, normaal gebruik of achterstallig onderhoud wordt niet vergoed. Verzekeraars kijken kritisch of de schade inderdaad storm-gerelateerd is en of u uw dak redelijk heeft onderhouden.</p>

    <div class="warn-box">
      <div class="warn-box-label">&#9888; Let op: onderhoudplicht</div>
      <p>Als uw verzekeraar kan aantonen dat de schade mede veroorzaakt is door achterstallig onderhoud, kan de uitkering worden gekort of geweigerd. Houd uw dak goed onderhouden &mdash; ook als preventie richting uw verzekeraar.</p>
    </div>

    <h2>Stap voor stap: uw claim indienen</h2>
    <ol>
      <li><strong>Documenteer de schade direct</strong> — maak zo snel mogelijk na de storm foto's van alle zichtbare schade, zowel van buitenaf als binnen (vochtplekken, gevallen materiaal)</li>
      <li><strong>Noteer datum en tijd</strong> — voor uw verzekeraar is dit essentieel om de windgegevens te verifiëren</li>
      <li><strong>Vraag windgegevens op bij het KNMI</strong> — via knmi.nl kunt u de windsnelheid op uw locatie opvragen voor een specifieke datum en tijd</li>
      <li><strong>Meld de schade zo snel mogelijk</strong> — de meeste verzekeraars vereisen dat u schade binnen een bepaalde termijn meldt (vaak 3 tot 5 werkdagen)</li>
      <li><strong>Laat een offerte opstellen</strong> — uw verzekeraar heeft een professionele offerte of schaderapport nodig van een dakdekker</li>
      <li><strong>Werk samen met de schade-expert</strong> — uw verzekeraar stuurt soms een eigen expert; zorg dat u erbij bent en wijs op alle schade</li>
    </ol>

    <div class="tip-box">
      <div class="tip-box-label">&#128161; Noodafdekking</div>
      <p>Begrenzend water tegengaan is ook uw eigen belang. Als u tijdelijk een folie of nooddak laat plaatsen om verdere schade te voorkomen, worden de kosten daarvoor doorgaans ook vergoed door uw verzekeraar. Bewaar altijd de bonnen.</p>
    </div>

    <h2>Wat wordt vergoed, wat niet?</h2>
    <p>Doorgaans vergoed bij stormschade:</p>
    <ul>
      <li>Beschadigde of weggewaaide dakpannen, nokvorsten en dakgoten</li>
      <li>Schade aan loodwerk en aansluitingen</li>
      <li>Waterinfiltratie als direct gevolg van de storm</li>
      <li>Noodafdekking en spoedmaatregelen</li>
      <li>Opruimkosten van gevallen materiaal</li>
    </ul>
    <p>Doorgaans <em>niet</em> vergoed:</p>
    <ul>
      <li>Schade door normaal gebruik en slijtage</li>
      <li>Schade aan een dak dat aantoonbaar slecht onderhouden was</li>
      <li>Schade onder het eigen risico</li>
      <li>Gevolgschade door langdurig uitstel van reparatie</li>
    </ul>

    <h2>Eigen risico</h2>
    <p>Let op uw eigen risico. Bij de meeste opstalverzekeringen geldt een eigen risico van &euro;100 tot &euro;500. Bij kleinere schades — zoals een paar gebroken dakpannen — is het soms niet de moeite waard om een claim in te dienen als dit uw premie verhoogt.</p>

    <h2>Schade laten herstellen door een erkend bedrijf</h2>
    <p>Uw verzekeraar hecht veel waarde aan reparaties uitgevoerd door een erkend en gecertificeerd dakbedrijf. Een professionele factuur en garantiecertificaat versterken uw dossier. Dakbedrijf 'T Noorden stelt desgewenst een volledig schade- en reparatierapport op voor uw verzekeraar.</p>

    <div class="art-divider"></div>
    <p style="font-size:0.85rem;color:var(--text-muted);">Stormschade aan uw dak? Dakbedrijf 'T Noorden staat 24/7 voor u klaar met spoedservice in heel Noord-Nederland. Bel <a href="tel:+31612370853" style="color:var(--blue-accent)">06 12 37 08 53</a>.</p>
  """,
  [
    ("spoed.html","Spoedservice","Spoed Dakservice 24/7","Direct beschikbaar · Noord-Nederland"),
    ("blog-dakschade-storm.html","Schade","Hoe herken je dakschade na een storm?","15 maart 2025 · 5 min"),
    ("blog-dakonderhoud-checklist.html","Onderhoud","Jaarlijkse dakonderhoud checklist","20 mei 2025 · 5 min"),
  ]
))

# ── Write all files ──────────────────────────────────────────────────────────
for args in posts:
    filename = args[0]
    html = make_page(*args)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Written: {filename}')

print(f'\nDone - {len(posts)} blog posts created.')
