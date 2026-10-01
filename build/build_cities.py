#!/usr/bin/env python3
"""Regenerate all 61 city pages: unified navy/white trust-funnel template.

Run from repo root:  python3 build/build_cities.py
"""
import json, os, re, html as htmlmod, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from city_data import CITY_COUNTY, COUNTY_BLURB, NEIGHBORHOODS, TOP10, CITY_INTRO, CITY_FAQ

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STREETS = json.load(open(os.path.join(ROOT, "..", "deal_streets.json")))
CITY_DIR = os.path.join(ROOT, "cities")
PHONE = "+1 (972) 665-6599"
PHONE_TEL = "+19726656599"
DOMAIN = "https://northtexashomesolutions.com"

def slug_to_name(slug):
    return " ".join(w.capitalize() for w in slug.replace("-", " ").split())

def streets_for(city_name, n=6):
    return STREETS.get(city_name, [])[:n]

def nearby_cities(slug, county):
    """Same-county cities (excluding self), up to 6."""
    from city_data import COUNTIES
    out = []
    for s in COUNTIES[county]:
        if s != slug and s not in out:
            out.append(s)
        if len(out) == 6:
            break
    return out

def situation_cards():
    cards = [
        ("/foreclosure/", "Facing Foreclosure", "Texas moves fast on foreclosure. We can close before the auction date and you keep what's left."),
        ("/tax-liens/", "Behind on Property Taxes", "Back taxes get paid off at closing. You sell with a clear title and walk away with cash."),
        ("/inherited-property/", "Inherited a Property", "Probate is confusing and the house sits costing you money. We buy inherited homes as-is, paperwork and all."),
        ("/divorce/", "Going Through Divorce", "A house you both need gone, sold fast, split clean, no showings, no awkward open houses."),
    ]
    out = []
    for href, t, d in cards:
        out.append(f'''<a class="sit-card" href="{href}"><h3>{t}</h3><p>{d}</p><span class="sit-link">How it works &rarr;</span></a>''')
    return "\n".join(out)

def street_proof_section(city, county, streets):
    if streets:
        chips = "".join(f'<span class="street-chip">{htmlmod.escape(s)}</span>' for s in streets)
        sub = (f"We've bought homes on streets like these across {city}. Same story every time: "
               f"a homeowner who needed a fast, fair, no-repair sale and got one.")
        return f"""
<section class="sec alt">
  <div class="wrap">
    <span class="eyebrow">Local Proof</span>
    <h2 class="sec-h2">We've Bought Homes on These <em>{city}</em> Streets</h2>
    <p class="sec-lead">{sub}</p>
    <div class="street-chips">{chips}</div>
    <p class="street-note">Your street could be next. Get a cash offer with zero obligation and see what your home is worth today.</p>
  </div>
</section>"""
    return ""

def neighborhood_section(city, slug):
    nb = NEIGHBORHOODS.get(slug)
    if not nb:
        return ""
    items = "".join(f"<li>{n}</li>" for n in nb)
    return f"""
<section class="sec">
  <div class="wrap">
    <span class="eyebrow">Where We Buy</span>
    <h2 class="sec-h2">Neighborhoods We Know in <em>{city}</em></h2>
    <p class="sec-lead">We don't just buy in {city}, we know the blocks. Foundation issues near the lake, hail damage on older roofs, 1970s builds needing everything, we've seen it and bought it.</p>
    <ul class="nb-list">{items}</ul>
  </div>
</section>"""

def local_section(city, county):
    blurb = COUNTY_BLURB[county]
    return f"""
<section class="sec">
  <div class="wrap split">
    <div>
      <span class="eyebrow">{city}, {county}</span>
      <h2 class="sec-h2">Local Knowledge That <em>Actually Matters</em></h2>
      <p class="sec-lead">{blurb}</p>
      <ul class="check-list">
        <li><b>Foundation movement:</b> North Texas clay soil wrecks foundations. We buy houses with foundation issues as-is, no inspection games.</li>
        <li><b>Hail and roof damage:</b> Every DFW storm season leaves a trail of worn roofs. We price it in and still make you a strong offer.</li>
        <li><b>Older housing stock:</b> 1960s-80s homes with original everything? That's our bread and butter. No updates needed, ever.</li>
        <li><b>Code violations:</b> City of {city} citations piling up? We buy with violations open and deal with the city ourselves.</li>
      </ul>
    </div>
    <div class="local-card">
      <h3>Sell your {city} house in 3 steps</h3>
      <ol class="steps">
        <li><b>Tell us about the house.</b> Fill out the form or call {PHONE}. Takes about a minute.</li>
        <li><b>Get your cash offer.</b> We look at the property and bring you a fair, no-pressure offer, usually within 24 hours.</li>
        <li><b>Close on your schedule.</b> As fast as 7 days, or take your time. You pick the date. We cover all closing costs.</li>
      </ol>
      <a class="btn-gold" href="#get-offer">Get My Free Cash Offer</a>
    </div>
  </div>
</section>"""

def faq_items(city, slug):
    qa = [
        (f"Is this a scam? How do I know you're legit?",
         f"Fair question, there are a lot of we-buy-houses flyers out there. We're a local DFW company, we close through a licensed Texas title company, and you pay zero fees or commissions. If our offer doesn't work for you, you walk away and owe us nothing."),
        (f"How fast can you actually close in {city}?",
         f"As fast as 7 days when the title is clean. If there are liens, back taxes, or probate issues, we work through them with the title company and keep you updated. You choose the closing date, not us."),
        (f"Do I need to make any repairs first?",
         "No. We buy as-is, which means as it sits right now. Don't clean, don't fix, don't haul anything out. Leave what you don't want and take what you do."),
        (f"What will you offer for my house?",
         f"It depends on the condition, location, and what fixed-up homes nearby are selling for. Our offers are based on real comparable sales in {city}, and we'll show you how we got to the number. No obligation to accept."),
        (f"Are there any fees or commissions?",
         "None. No realtor commissions, no closing costs, no hidden fees. The offer we make is the amount you get at closing, minus any mortgage or liens you already owe."),
        (f"My house has liens or back taxes. Can you still buy it?",
         f"Yes, this is one of the most common situations we handle. Liens and back taxes get paid off at the closing table from the sale proceeds, so you don't need cash up front to clear them."),
    ]
    if slug in CITY_FAQ:
        q, a = CITY_FAQ[slug]
        qa.insert(1, (q, a))
    items = []
    for q, a in qa:
        items.append(f'''<div class="faq-item rv"><button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">{q}<span class="faq-icon"><svg viewBox="0 0 12 12" fill="none"><path d="M6 1v10M1 6h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span></button><div class="faq-a"><p>{a}</p></div></div>''')
    return "\n".join(items)

def form_html(city):
    return f'''<form id="lead-form" name="lead-form" data-netlify="true" netlify-honeypot="bot-field" onsubmit="submitLeadForm(event)" novalidate>
        <input type="hidden" name="form-name" value="lead-form">
        <input type="hidden" name="city-page" value="{htmlmod.escape(city)}">
        <div style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden" aria-hidden="true"><label>Leave this field empty<input type="text" name="bot-field" tabindex="-1" autocomplete="off"></label></div>
        <div class="fg-2">
          <div class="fg"><label for="fn">First Name</label><input type="text" id="fn" name="fname" placeholder="John" autocomplete="given-name" required/></div>
          <div class="fg"><label for="ln">Last Name</label><input type="text" id="ln" name="lname" placeholder="Smith" autocomplete="family-name" required/></div>
        </div>
        <div class="fg"><label for="ph">Phone Number</label><input type="tel" id="ph" name="phone" placeholder="(214) 555-0000" autocomplete="tel" required/></div>
        <div class="fg"><label for="addr">Property Address</label><input type="text" id="addr" name="address" placeholder="123 Main St, {htmlmod.escape(city)} TX" required/></div>
        <div class="fg">
          <label for="sit">Your Situation</label>
          <select id="sit" name="situation" required>
            <option value="" disabled selected>What's going on?</option>
            <option>Facing Foreclosure</option>
            <option>Behind on Property Taxes</option>
            <option>Inherited Property / Probate</option>
            <option>Going Through Divorce</option>
            <option>Too Many Repairs Needed</option>
            <option>Tired Landlord</option>
            <option>Relocating Fast</option>
            <option>Vacant Property</option>
            <option>Other</option>
          </select>
        </div>
        <button type="submit" class="form-btn">Get My Free Cash Offer</button>
      </form>'''

def schema_faq(city, slug):
    qa = [
        (f"Is North Texas Home Solutions legit?",
         f"Yes. North Texas Home Solutions is a local DFW home buying company. We close through licensed Texas title companies and charge zero fees or commissions."),
        (f"How fast can you buy my house in {city}?",
         f"We can close in as little as 7 days in {city}, Texas, or on whatever timeline works for you."),
        (f"Do I need to repair my {city} house before selling?",
         "No. We buy houses as-is in any condition, no repairs, cleaning, or showings needed."),
    ]
    if slug in CITY_FAQ:
        qa.append(CITY_FAQ[slug])
    items = ",\n".join(f'''{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}''' for q, a in qa)
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"North Texas Home Solutions","url":"{DOMAIN}/","telephone":"{PHONE_TEL}","areaServed":{{"@type":"City","name":"{city}","address":{{"@type":"PostalAddress","addressLocality":"{city}","addressRegion":"TX","addressCountry":"US"}}}},"priceRange":"$$"}}
</script>'''

JS = """<script>
function maskPhone(v){var d=v.replace(/\\D/g,'').slice(0,10);var p=d;if(d.length>6)p='('+d.slice(0,3)+') '+d.slice(3,6)+'-'+d.slice(6);else if(d.length>3)p='('+d.slice(0,3)+') '+d.slice(3);return p;}
document.addEventListener('DOMContentLoaded',function(){
  var ph=document.getElementById('ph');
  if(ph){ph.addEventListener('input',function(){ph.value=maskPhone(ph.value);});}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{threshold:.12});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});
});
function toggleFaq(btn){
  var open=btn.getAttribute('aria-expanded')==='true';
  btn.setAttribute('aria-expanded',open?'false':'true');
  var a=btn.nextElementSibling;
  a.style.display=open?'none':'block';
}
async function submitLeadForm(e){
  e.preventDefault();
  var form=e.target;
  var btn=form.querySelector('.form-btn');
  if(!form.checkValidity()){form.reportValidity();return;}
  btn.disabled=true;btn.textContent='Sending...';
  try{
    var data=new FormData(form);
    var res=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(data).toString()});
    if(!res.ok)throw new Error('submit failed');
    form.style.display='none';
    document.getElementById('form-success').style.display='block';
    window.scrollTo({top:0,behavior:'smooth'});
  }catch(err){
    btn.disabled=false;btn.textContent='Get My Free Cash Offer';
    alert('Something went wrong sending your request. Please call or text """ + PHONE + """ and we will help you right away.');
  }
  return false;
}
</script>"""

EXTRA_CSS = """<style>
.sec{padding:72px 0}
.sec.alt{background:var(--bg-alt)}
.split{display:grid;grid-template-columns:1.2fr .8fr;gap:48px;align-items:start}
.check-list{list-style:none;padding:0;margin:24px 0 0;display:grid;gap:14px}
.check-list li{font-size:.9rem;color:var(--text2);line-height:1.7;padding-left:28px;position:relative}
.check-list li:before{content:"✓";position:absolute;left:0;color:var(--navy);font-weight:700}
.check-list b{color:var(--text)}
.local-card{background:var(--white);border:1px solid var(--border);border-radius:var(--r);padding:32px;box-shadow:var(--sh)}
.local-card h3{font-family:var(--fh);font-size:1.25rem;margin-bottom:18px;letter-spacing:-.02em}
.steps{list-style:none;padding:0;margin:0 0 24px;display:grid;gap:16px;counter-reset:st}
.steps li{font-size:.88rem;color:var(--text2);line-height:1.7;padding-left:40px;position:relative;counter-increment:st}
.steps li:before{content:counter(st);position:absolute;left:0;top:0;width:28px;height:28px;border-radius:50%;background:var(--navy);color:#fff;font-size:.75rem;font-weight:700;display:flex;align-items:center;justify-content:center}
.steps b{color:var(--text)}
.sit-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:40px}
.sit-card{background:var(--white);border:1px solid var(--border);border-radius:var(--r);padding:26px;text-decoration:none;color:inherit;display:block;transition:box-shadow .2s,transform .2s}
.sit-card:hover{box-shadow:var(--sh);transform:translateY(-3px)}
.sit-card h3{font-family:var(--fh);font-size:1.02rem;margin-bottom:10px;letter-spacing:-.01em;color:var(--text)}
.sit-card p{font-size:.84rem;color:var(--text2);line-height:1.7;margin-bottom:12px}
.sit-link{font-size:.84rem;font-weight:600;color:var(--navy)}
.street-chips{display:flex;flex-wrap:wrap;gap:10px;margin:28px 0 20px}
.street-chip{background:var(--white);border:1px solid var(--border);border-radius:999px;padding:9px 18px;font-size:.85rem;font-weight:500;color:var(--text)}
.street-note{font-size:.88rem;color:var(--text2)}
.nb-list{list-style:none;padding:0;margin:28px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.nb-list li{background:var(--white);border:1px solid var(--border);border-radius:var(--r);padding:14px 18px;font-size:.88rem;font-weight:500}
.nearby{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
@media(max-width:900px){.split{grid-template-columns:1fr}.sit-grid{grid-template-columns:1fr 1fr}.nb-list{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.sit-grid{grid-template-columns:1fr}.nb-list{grid-template-columns:1fr}}
</style>"""

def nav_html():
    return f"""<nav class="nav"><div class="wrap nav-in">
<a href="/" class="logo">North Texas <b>Home Solutions</b></a>
<div class="nav-links">
<a href="/#how-it-works">How It Works</a>
<a href="/#situations">Situations</a>
<a href="/#areas">Areas</a>
<a href="/blog/">Blog</a>
</div>
<a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE}</a>
<a href="#get-offer" class="btn-nav">Get Cash Offer</a>
</div></nav>"""

def footer_html():
    return f"""<footer class="footer">
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
</footer>"""

def intro_section(city, slug):
    intro = CITY_INTRO.get(slug)
    if not intro:
        return ""
    return f"""
<section class="sec">
  <div class="wrap">
    <span class="eyebrow rv">Selling in {city}</span>
    <h2 class="sec-h2 rv">Why {city} Homeowners <em>Sell to Us</em></h2>
    <p class="sec-lead rv" style="max-width:680px">{intro}</p>
  </div>
</section>"""

def build_page(slug):
    city = slug_to_name(slug)
    county = CITY_COUNTY.get(slug, "Dallas County")
    streets = streets_for(city)
    nearby = nearby_cities(slug, county)
    nearby_links = "".join(f'<a href="/cities/{s}.html" class="city-tag">{slug_to_name(s)}</a>' for s in nearby)
    title = f"We Buy Houses in {city}, TX | Sell Your House Fast for Cash"
    desc = (f"Sell your house fast in {city}, TX. North Texas Home Solutions buys homes as-is for cash, "
            f"closes in as little as 7 days, and charges zero fees. Get your free cash offer today.")
    url = f"{DOMAIN}/cities/{slug}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)}</title>
<meta name="description" content="{htmlmod.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{htmlmod.escape(title)}">
<meta property="og:description" content="{htmlmod.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/theme.css">
{EXTRA_CSS}
{schema_faq(city, slug)}
</head>
<body>
{nav_html()}
<!-- HERO -->
<section class="hero" id="get-offer">
  <div class="wrap hero-l">
    <div class="hero-tag"><span class="hero-tag-dot"></span>{city}, Texas &middot; {county}</div>
    <h1 class="hero-h1">We Buy Houses<br>in <em>{city}</em></h1>
    <p class="hero-h1-sub">Fast. Fair. As-is. On your terms.</p>
    <div class="hero-checks">
      <div class="hero-check"><div class="hero-check-mark"><svg viewBox="0 0 10 10" fill="none"><path d="M2 5.5l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>Cash offer within 24 hours of seeing your property</div>
      <div class="hero-check"><div class="hero-check-mark"><svg viewBox="0 0 10 10" fill="none"><path d="M2 5.5l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>Close in as little as 7 days, or on your timeline</div>
      <div class="hero-check"><div class="hero-check-mark"><svg viewBox="0 0 10 10" fill="none"><path d="M2 5.5l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>Zero fees, zero commissions, we cover closing costs</div>
      <div class="hero-check"><div class="hero-check-mark"><svg viewBox="0 0 10 10" fill="none"><path d="M2 5.5l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>Buy as-is, no repairs, no cleaning, no showings</div>
    </div>
    <div class="hero-cta-row">
      <a href="#get-offer" class="btn-gold" onclick="document.getElementById('fn').focus();return false;">Get My Free Cash Offer</a>
      <div class="hero-or-call">or call <a href="tel:{PHONE_TEL}">{PHONE}</a></div>
    </div>
  </div>
  <div class="hero-r">
    <div class="form-card">
      <span class="form-eyebrow">Free, No Obligation Whatsoever</span>
      <h2 class="form-title">Get Your {city} Cash Offer</h2>
      <p class="form-sub">Fill this out and someone from our local team reaches out within a few hours, usually same day.</p>
      {form_html(city)}
      <div id="form-success">
        <div class="success-ico"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.75" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
        <h3 class="success-h">We Got It.</h3>
        <p class="success-p">Someone from our team will reach out shortly. Keep your phone nearby.</p>
      </div>
      <div class="form-secure">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z" clip-rule="evenodd"/></svg>
        Private &amp; secure, your info is never shared or sold
      </div>
    </div>
  </div>
</section>

{street_proof_section(city, county, streets)}
{intro_section(city, slug)}

<!-- SITUATIONS -->
<section class="sec">
  <div class="wrap">
    <span class="eyebrow rv">We Can Help</span>
    <h2 class="sec-h2 rv">Whatever Your Situation in <em>{city}</em>, There's a Way Out</h2>
    <p class="sec-lead rv">Most of our sellers aren't choosing between five great options. They're dealing with something hard. Here's how a cash sale helps.</p>
    <div class="sit-grid">
      {situation_cards()}
    </div>
  </div>
</section>

{neighborhood_section(city, slug)}
{local_section(city, county)}

<!-- FAQ -->
<section class="sec alt" id="faq">
  <div class="wrap sec-center">
    <span class="eyebrow rv">Common Questions</span>
    <h2 class="sec-h2 rv">{city} Homeowners <em>Ask Us</em></h2>
    <p class="sec-lead rv">Straight answers, no sales pitch.</p>
    <div class="faq-list">
      {faq_items(city, slug)}
    </div>
  </div>
</section>

<!-- NEARBY -->
<section class="sec">
  <div class="wrap">
    <span class="eyebrow rv">Nearby Cities</span>
    <h2 class="sec-h2 rv">Also Buying in <em>{county}</em></h2>
    <div class="nearby">
      {nearby_links}
    </div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="sec alt">
  <div class="wrap sec-center">
    <span class="eyebrow rv">Ready When You Are</span>
    <h2 class="sec-h2 rv">Get Your Free Cash Offer for Your <em>{city}</em> Home</h2>
    <p class="sec-lead rv">No repairs. No fees. No obligation. Just a fair cash offer and a closing date you choose.</p>
    <div class="final-btns">
      <a href="#get-offer" class="btn-gold">Get My Free Cash Offer</a>
      <a href="tel:{PHONE_TEL}" class="btn-outline">Call {PHONE}</a>
    </div>
  </div>
</section>

{footer_html()}
{JS}
</body>
</html>
"""

def main():
    from city_data import COUNTIES
    slugs = sorted({s for lst in COUNTIES.values() for s in lst})
    os.makedirs(CITY_DIR, exist_ok=True)
    for slug in slugs:
        path = os.path.join(CITY_DIR, slug + ".html")
        open(path, "w").write(build_page(slug))
    print(f"wrote {len(slugs)} city pages")

if __name__ == "__main__":
    main()
