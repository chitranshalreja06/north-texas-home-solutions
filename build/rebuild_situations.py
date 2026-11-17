#!/usr/bin/env python3
"""Rebuild the 4 situation pages on the navy/white theme, preserving all copy."""
import re, html

PAGES = {
    "foreclosure": {
        "slug": "foreclosure",
        "badge": "Time-Sensitive Situation",
        "h1": 'Facing Foreclosure in <em>Dallas-Fort Worth?</em> You Still Have Options.',
        "sub": "Texas has one of the fastest foreclosure timelines in the country - but you can often still sell before the auction date and walk away with cash instead of losing everything. Time matters. We can move fast.",
        "form_title": "Get Your Free Cash Offer",
        "checks": ["Can stop the foreclosure process", "Close in as little as 7 days", "Protect your credit from a 7-year hit", "Walk away with cash, not zero"],
        "eyebrow": "Foreclosure Help in DFW",
        "faq_title": "Foreclosure Questions <em>Answered</em>",
        "faq_lead": "Straight answers about your foreclosure situation in Texas.",
        "cta_h": "Stop the Clock <em>Today</em>",
        "cta_p": "Every day matters in foreclosure. Tell us where things stand and we'll tell you honestly what we can do.",
    },
    "divorce": {
        "slug": "divorce",
        "badge": "Divorce Property Sale",
        "h1": 'Need to Sell Your House During a <em>Divorce in DFW?</em>',
        "sub": "When you're going through a divorce in Dallas-Fort Worth, the family home is often the largest and most complicated asset to deal with. A fast clean cash sale removes a major source of conflict, gives both parties clarity, and lets everyone move forward - without the delays and uncertainty of a traditional listing.",
        "form_title": "Get Your Free Cash Offer",
        "checks": ["Zero fees or commissions", "Close in as little as 7 days", "We buy as-is, no repairs", "Cash offer within 24 hours"],
        "eyebrow": "Divorce Property Sales in DFW",
        "faq_title": "Divorce Sale Questions <em>Answered</em>",
        "faq_lead": "Straight answers about selling a house during divorce in Texas.",
        "cta_h": "Find Out Your <em>Options</em>",
        "cta_p": "No obligation. No pressure. No cost. Just an honest conversation about what's possible.",
    },
    "tax-liens": {
        "slug": "tax-liens",
        "badge": "Property Tax & Lien Issues",
        "h1": 'Behind on Property Taxes in <em>Dallas-Fort Worth?</em> We Can Help.',
        "sub": "Delinquent property taxes in Texas accumulate fast - penalties, interest, and attorney fees can pile on quickly. But back taxes don't have to mean losing your home. A cash sale can often resolve everything from the proceeds at closing, with no money out of pocket on your end.",
        "form_title": "Get Your Free Cash Offer",
        "checks": ["Back taxes paid off at closing", "No money out of pocket", "Stop penalties and interest", "Close in as little as 7 days"],
        "eyebrow": "Tax Lien Help in DFW",
        "faq_title": "Tax Lien Questions <em>Answered</em>",
        "faq_lead": "Straight answers about property tax problems in Texas.",
        "cta_h": "Resolve It <em>Before It Grows</em>",
        "cta_p": "Penalties and interest grow every month. Tell us what you owe and we'll show you a clean way out.",
    },
    "inherited-property": {
        "slug": "inherited-property",
        "badge": "Inherited Property & Probate",
        "h1": 'Inherited a House in <em>Dallas-Fort Worth?</em> We Can Help.',
        "sub": "Inheriting a property you didn't plan for - especially one that needs work, is going through probate, or has multiple heirs involved - is overwhelming. We work with inherited properties and estates throughout DFW regularly and can help you find the cleanest path forward.",
        "form_title": "Get Your Free Cash Offer",
        "checks": ["We buy as-is, any condition", "Help with probate confusion", "Multiple heirs? We handle it", "Close in as little as 7 days"],
        "eyebrow": "Inherited Property Help in DFW",
        "faq_title": "Inherited Property Questions <em>Answered</em>",
        "faq_lead": "Straight answers about inherited houses and probate in Texas.",
        "cta_h": "Turn It Into <em>Cash</em>",
        "cta_p": "That inherited house is costing you money every month it sits. Let's talk about the cleanest way forward.",
    },
}

def extract(path):
    s = open(path, encoding="utf-8").read()
    out = {}
    out["title"] = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    m = re.search(r'<meta name="description" content="(.*?)"', s)
    out["desc"] = m.group(1) if m else ""
    m = re.search(r'<link rel="canonical" href="(.*?)"', s)
    out["canonical"] = m.group(1) if m else ""
    out["jsonld"] = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    # body content
    m = re.search(r'<div class="content-body rv">(.*?)</div>\s*</div>\s*</section>', s, re.S)
    body = m.group(1) if m else ""
    # convert old classes to navy equivalents
    body = body.replace('class="slbl"', 'class="eyebrow"')
    body = body.replace('class="sh2"', 'class="sec-h2" style="text-align:left"')
    body = re.sub(r'<div class="alert-box"><p>(.*?)</p></div>',
                  r'<div class="callout"><p>\1</p></div>', body, flags=re.S)
    out["body"] = body.strip()
    # FAQs
    faqs = []
    for qm, am in re.findall(
            r'<button class="faq-q"[^>]*>(.*?)</button>\s*<div class="faq-a">(.*?)</div>',
            s, re.S):
        q = re.sub(r"<svg.*?</svg>", "", qm, flags=re.S).strip()
        q = re.sub(r"\s+", " ", q)
        a = re.sub(r"\s+", " ", am).strip()
        faqs.append((q, a))
    out["faqs"] = faqs
    return out

CHECK_SVG = '<div class="hero-check-mark"><svg viewBox="0 0 10 10" fill="none"><path d="M2 5.5l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
FAQ_ICON = '<span class="faq-icon"><svg viewBox="0 0 12 12" fill="none"><path d="M6 1v10M1 6h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>'

TIMELINE_HTML = """
<section class="sec alt">
  <div class="wrap">
    <span class="eyebrow rv">Why Speed Matters</span>
    <h2 class="sec-h2 rv">The Texas Foreclosure <em>Timeline</em></h2>
    <p class="sec-lead rv">Texas is a non-judicial foreclosure state. No court required, and the clock runs fast.</p>
    <div class="tl-grid">
      <div class="tl-card"><div class="tl-day">Day 1</div><div class="tl-label">Missed payment. Lender sends notice.</div></div>
      <div class="tl-card"><div class="tl-day">Day 20</div><div class="tl-label">Notice of default and acceleration.</div></div>
      <div class="tl-card"><div class="tl-day">Day 41</div><div class="tl-label">Notice of sale posted publicly.</div></div>
      <div class="tl-card danger"><div class="tl-day">Day 61+</div><div class="tl-label">First Tuesday auction. You lose the home.</div></div>
    </div>
  </div>
</section>"""

EXTRA_CSS = """
.rich h2{font-family:var(--fh);font-size:1.6rem;font-weight:700;letter-spacing:-.02em;margin:2.2rem 0 .9rem;color:var(--navy)}
.rich h2:first-child{margin-top:0}
.rich h3{font-family:var(--fh);font-size:1.15rem;font-weight:700;margin:1.6rem 0 .6rem;color:var(--navy)}
.rich p{font-size:.95rem;color:var(--text2);line-height:1.8;margin-bottom:1rem}
.rich ul{margin:0 0 1.2rem 1.2rem;display:grid;gap:.5rem}
.rich li{font-size:.93rem;color:var(--text2);line-height:1.75}
.rich li strong,.rich p strong{color:var(--navy)}
.callout{background:#fff7ed;border:1px solid #fed7aa;border-left:4px solid #ea580c;border-radius:12px;padding:20px 24px;margin:1.8rem 0}
.callout p{margin:0;font-size:.93rem;color:#9a3412;font-weight:500;line-height:1.7}
.tl-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:36px}
.tl-card{background:var(--white);border:1px solid var(--border);border-radius:14px;padding:26px 20px;text-align:center}
.tl-day{font-family:var(--fh);font-size:1.6rem;font-weight:800;color:var(--navy);margin-bottom:8px}
.tl-label{font-size:.85rem;color:var(--text2);line-height:1.6}
.tl-card.danger{background:#fef2f2;border-color:#fecaca}
.tl-card.danger .tl-day{color:#dc2626}
@media(max-width:900px){.tl-grid{grid-template-columns:1fr 1fr}}
"""

def build(slug, cfg, ext):
    checks = "\n".join(
        f'      <div class="hero-check">{CHECK_SVG}{c}</div>' for c in cfg["checks"])
    faqs = "\n".join(
        f'<div class="faq-item rv"><button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">{q}{FAQ_ICON}</button><div class="faq-a"><p>{a}</p></div></div>'
        for q, a in ext["faqs"])
    jsonld = "\n".join(f'<script type="application/ld+json">{j}</script>' for j in ext["jsonld"])
    timeline = TIMELINE_HTML if slug == "foreclosure" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ext['title']}</title>
<meta name="description" content="{ext['desc']}">
<link rel="canonical" href="{ext['canonical']}">
<meta property="og:title" content="{ext['title']}">
<meta property="og:description" content="{ext['desc']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{ext['canonical']}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/theme.css">
<style>{EXTRA_CSS}</style>
{jsonld}
</head>
<body>
<nav class="nav"><div class="wrap nav-in">
<a href="/" class="logo">North Texas <b>Home Solutions</b></a>
<div class="nav-links">
<a href="/#how-it-works">How It Works</a>
<a href="/#situations">Situations</a>
<a href="/#areas">Areas</a>
<a href="/blog/">Blog</a>
</div>
<a class="nav-phone" href="tel:+19726656599">+1 (972) 665-6599</a>
<a href="#get-offer" class="btn-nav">Get Cash Offer</a>
</div></nav>

<!-- HERO -->
<section class="hero" id="get-offer">
  <div class="wrap hero-l">
    <div class="hero-tag"><span class="hero-tag-dot"></span>{cfg['badge']}</div>
    <h1 class="hero-h1">{cfg['h1']}</h1>
    <p class="hero-h1-sub">{cfg['sub']}</p>
    <div class="hero-checks">
{checks}
    </div>
    <div class="hero-cta-row">
      <a href="#get-offer" class="btn-gold" onclick="document.getElementById('fn').focus();return false;">Get My Free Cash Offer</a>
      <div class="hero-or-call">or call <a href="tel:+19726656599">+1 (972) 665-6599</a></div>
    </div>
  </div>
  <div class="hero-r">
    <div class="form-card">
      <span class="form-eyebrow">Free, No Obligation Whatsoever</span>
      <h2 class="form-title">{cfg['form_title']}</h2>
      <p class="form-sub">Fill this out and someone from our local team reaches out within a few hours, usually same day.</p>
      <form id="lead-form" name="lead-form" data-netlify="true" netlify-honeypot="bot-field" onsubmit="submitLeadForm(event)" novalidate>
        <input type="hidden" name="form-name" value="lead-form">
        <input type="hidden" name="situation-page" value="{slug}">
        <div style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden" aria-hidden="true"><label>Leave this field empty<input type="text" name="bot-field" tabindex="-1" autocomplete="off"></label></div>
        <div class="fg-2">
          <div class="fg"><label for="fn">First Name</label><input type="text" id="fn" name="fname" placeholder="John" autocomplete="given-name" required/></div>
          <div class="fg"><label for="ln">Last Name</label><input type="text" id="ln" name="lname" placeholder="Smith" autocomplete="family-name" required/></div>
        </div>
        <div class="fg"><label for="ph">Phone Number</label><input type="tel" id="ph" name="phone" placeholder="(214) 555-0000" autocomplete="tel" required/></div>
        <div class="fg"><label for="addr">Property Address</label><input type="text" id="addr" name="address" placeholder="123 Main St, Dallas TX" autocomplete="street-address" required/></div>
        <button type="submit" class="form-btn">Get My Free Cash Offer</button>
      </form>
      <div id="form-success">
        <div class="success-ico"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.75" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
        <h3 class="success-h">We Got It.</h3>
        <p class="success-p">Someone from our team will reach out shortly. Keep your phone nearby.</p>
      </div>
      <div class="form-secure">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z" clip-rule="evenodd"/></svg>
        Private and secure. Your info is never shared or sold.
      </div>
    </div>
  </div>
</section>

{timeline}
<!-- CONTENT -->
<section class="sec">
  <div class="wrap">
    <span class="eyebrow rv">{cfg['eyebrow']}</span>
    <div class="rich rv" style="max-width:780px;margin-top:18px">
{ext['body']}
    </div>
  </div>
</section>

<!-- 3 STEPS -->
<section class="sec alt">
  <div class="wrap split">
    <div>
      <span class="eyebrow rv">How It Works</span>
      <h2 class="sec-h2 rv">Sell in <em>3 Simple Steps</em></h2>
      <p class="sec-lead rv">No listings, no showings, no waiting on buyers. Just a straight path from today to cash in hand.</p>
    </div>
    <div class="local-card rv">
      <ol class="steps">
        <li><b>Tell us about the house.</b> Fill out the form or call +1 (972) 665-6599. Takes about a minute.</li>
        <li><b>Get your cash offer.</b> We look at the property and bring you a fair, no-pressure offer, usually within 24 hours.</li>
        <li><b>Close on your schedule.</b> As fast as 7 days, or take your time. You pick the date. We cover all closing costs.</li>
      </ol>
      <a class="btn-gold" href="#get-offer">Get My Free Cash Offer</a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="sec" id="faq">
  <div class="wrap sec-center">
    <span class="eyebrow rv">Common Questions</span>
    <h2 class="sec-h2 rv">{cfg['faq_title']}</h2>
    <p class="sec-lead rv">{cfg['faq_lead']}</p>
    <div class="faq-list">
{faqs}
    </div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="sec alt">
  <div class="wrap sec-center">
    <span class="eyebrow rv">Ready When You Are</span>
    <h2 class="sec-h2 rv">{cfg['cta_h']}</h2>
    <p class="sec-lead rv">{cfg['cta_p']}</p>
    <div class="final-btns">
      <a href="#get-offer" class="btn-gold">Get My Free Cash Offer</a>
      <a href="tel:+19726656599" class="btn-outline">Call +1 (972) 665-6599</a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="wrap">
    <div class="footer-in">
      <div class="footer-logo">North Texas <b>Home Solutions</b></div>
      <p class="footer-copy">&#169; 2026 North Texas Home Solutions &middot; Dallas-Fort Worth, TX &middot; All Rights Reserved</p>
      <div class="footer-links">
        <a href="/blog/">Blog</a>
        <a href="/privacy.html">Privacy Policy</a>
        <a href="#get-offer">Get Offer</a>
      </div>
    </div>
  </div>
</footer>
<script>
function maskPhone(v){{var d=v.replace(/\\D/g,'').slice(0,10);var p=d;if(d.length>6)p='('+d.slice(0,3)+') '+d.slice(3,6)+'-'+d.slice(6);else if(d.length>3)p='('+d.slice(0,3)+') '+d.slice(3);return p;}}
document.addEventListener('DOMContentLoaded',function(){{
  var ph=document.getElementById('ph');
  if(ph){{ph.addEventListener('input',function(){{ph.value=maskPhone(ph.value);}});}}
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{threshold:.12}});
  document.querySelectorAll('.rv').forEach(function(el){{io.observe(el);}});
}});
var GOOGLE_PLACES_KEY="";
(function(){{
  var addr=document.querySelector('input[name="address"]');
  if(!addr||!GOOGLE_PLACES_KEY)return;
  window.nthsInitPlaces=function(){{
    try{{
      var ac=new google.maps.places.Autocomplete(addr,{{types:['address'],componentRestrictions:{{country:'us'}},fields:['formatted_address']}});
      ac.addListener('place_changed',function(){{var p=ac.getPlace();if(p&&p.formatted_address)addr.value=p.formatted_address;}});
    }}catch(e){{}}
  }};
  var s=document.createElement('script');
  s.src='https://maps.googleapis.com/maps/api/js?key='+encodeURIComponent(GOOGLE_PLACES_KEY)+'&libraries=places&callback=nthsInitPlaces';
  s.async=true;s.defer=true;document.head.appendChild(s);
}})();
function toggleFaq(btn){{
  var open=btn.getAttribute('aria-expanded')==='true';
  btn.setAttribute('aria-expanded',open?'false':'true');
  var a=btn.nextElementSibling;
  a.style.display=open?'none':'block';
}}
async function submitLeadForm(e){{
  e.preventDefault();
  var form=e.target;
  var btn=form.querySelector('.form-btn');
  if(!form.checkValidity()){{form.reportValidity();return;}}
  btn.disabled=true;btn.textContent='Sending...';
  try{{
    var data=new FormData(form);
    var res=await fetch('/',{{method:'POST',headers:{{'Content-Type':'application/x-www-form-urlencoded'}},body:new URLSearchParams(data).toString()}});
    if(!res.ok)throw new Error('submit failed');
    form.style.display='none';
    document.getElementById('form-success').style.display='block';
    window.scrollTo({{top:0,behavior:'smooth'}});
  }}catch(err){{
    btn.disabled=false;btn.textContent='Get My Free Cash Offer';
    alert('Something went wrong sending your request. Please call or text +1 (972) 665-6599 and we will help you right away.');
  }}
  return false;
}}
</script>
</body>
</html>
"""

for slug, cfg in PAGES.items():
    ext = extract(f"{slug}/index.html")
    html_out = build(slug, cfg, ext)
    open(f"{slug}/index.html", "w", encoding="utf-8").write(html_out)
    print(f"{slug}: {len(html_out)} bytes, {len(ext['faqs'])} FAQs, body {len(ext['body'])} chars")
