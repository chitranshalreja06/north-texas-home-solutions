#!/usr/bin/env python3
import os

cities = [
    # (slug, display_name, county, county_seat, nearby_city, zip_example, distress_detail)
    ("dallas", "Dallas", "Dallas County", "Dallas", "Garland", "75201", "Whether you're in Oak Cliff, South Dallas, Pleasant Grove, or anywhere in between - we know Dallas neighborhoods and can move fast."),
    ("garland", "Garland", "Dallas County", "Dallas", "Mesquite", "75040", "From downtown Garland to Firewheel, we buy houses throughout the city and can close on your timeline."),
    ("irving", "Irving", "Dallas County", "Dallas", "Grand Prairie", "75061", "From Las Colinas to Valley Ranch to South Irving, we help homeowners across the city get a fast cash offer."),
    ("richardson", "Richardson", "Dallas County", "Dallas", "Plano", "75080", "From Spring Valley to UTD area neighborhoods, we buy houses throughout Richardson quickly and as-is."),
    ("mesquite", "Mesquite", "Dallas County", "Dallas", "Garland", "75149", "From Mesquite's older established neighborhoods to newer subdivisions, we buy houses fast across the city."),
    ("duncanville", "Duncanville", "Dallas County", "Dallas", "DeSoto", "75116", "We help Duncanville homeowners move quickly - no repairs, no listings, no waiting on buyer financing."),
    ("farmers-branch", "Farmers Branch", "Dallas County", "Dallas", "Carrollton", "75234", "Conveniently located between Dallas and Carrollton, we buy houses throughout Farmers Branch fast."),
    ("cedar-hill", "Cedar Hill", "Dallas County", "Dallas", "Duncanville", "75104", "From Joe Pool Lake area homes to established Cedar Hill neighborhoods, we buy houses as-is."),
    ("lancaster", "Lancaster", "Dallas County", "Dallas", "DeSoto", "75146", "We buy houses throughout Lancaster and can often close within 7-14 days with a fair cash offer."),
    ("desoto", "DeSoto", "Dallas County", "Dallas", "Lancaster", "75115", "DeSoto homeowners facing tough situations have options. We buy houses in any condition throughout the city."),
    ("rowlett", "Rowlett", "Dallas County", "Dallas", "Garland", "75088", "From lakefront properties to inland neighborhoods, we buy houses throughout Rowlett quickly for cash."),
    ("sachse", "Sachse", "Dallas County", "Dallas", "Wylie", "75048", "Sachse is one of DFW's fastest growing areas and we're actively buying houses throughout the city."),
    ("sunnyvale", "Sunnyvale", "Dallas County", "Dallas", "Mesquite", "75182", "We buy houses in Sunnyvale and can work around your timeline - close in 7 days or whenever you're ready."),
    ("balch-springs", "Balch Springs", "Dallas County", "Dallas", "Mesquite", "75180", "We help Balch Springs homeowners in difficult situations sell fast for a fair cash price."),
    ("seagoville", "Seagoville", "Dallas County", "Dallas", "Mesquite", "75159", "From established Seagoville neighborhoods to rural properties in the area, we buy houses as-is."),
    ("hutchins", "Hutchins", "Dallas County", "Dallas", "Lancaster", "75141", "We buy houses in Hutchins and surrounding areas quickly - any condition, any situation."),
    ("wilmer", "Wilmer", "Dallas County", "Dallas", "Hutchins", "75172", "We help Wilmer homeowners get a fast cash offer regardless of the property's condition or situation."),
    ("cockrell-hill", "Cockrell Hill", "Dallas County", "Dallas", "Irving", "75211", "We buy houses in Cockrell Hill fast - no repairs needed, no fees, cash offer in 24 hours."),
    ("addison", "Addison", "Dallas County", "Dallas", "Farmers Branch", "75001", "From Addison's townhomes to single-family properties, we buy houses throughout the area for cash."),
    ("fort-worth", "Fort Worth", "Tarrant County", "Fort Worth", "Arlington", "76101", "From the Stockyards to the Southside to East Fort Worth - we know every neighborhood and buy houses fast across the city."),
    ("arlington", "Arlington", "Tarrant County", "Fort Worth", "Grand Prairie", "76010", "From entertainment district homes to established East Arlington neighborhoods, we buy houses throughout Arlington fast."),
    ("grapevine", "Grapevine", "Tarrant County", "Fort Worth", "Southlake", "76051", "We buy houses in Grapevine and surrounding areas - any condition, close on your timeline."),
    ("southlake", "Southlake", "Tarrant County", "Fort Worth", "Keller", "76092", "We buy houses in Southlake including higher-value properties that need work or face difficult situations."),
    ("keller", "Keller", "Tarrant County", "Fort Worth", "North Richland Hills", "76248", "From Keller's newer subdivisions to established neighborhoods, we buy houses throughout the city quickly."),
    ("hurst", "Hurst", "Tarrant County", "Fort Worth", "Euless", "76053", "We help Hurst homeowners get a fair cash offer fast - no repairs, no agent fees, no stress."),
    ("euless", "Euless", "Tarrant County", "Fort Worth", "Bedford", "76039", "Euless homeowners facing foreclosure, inherited properties, or tough situations have options. We buy houses fast."),
    ("bedford", "Bedford", "Tarrant County", "Fort Worth", "Hurst", "76021", "We buy houses throughout Bedford quickly - fair cash offer in 24 hours, close in as little as 7 days."),
    ("north-richland-hills", "North Richland Hills", "Tarrant County", "Fort Worth", "Hurst", "76180", "From older NRH neighborhoods to newer developments, we buy houses throughout North Richland Hills fast."),
    ("haltom-city", "Haltom City", "Tarrant County", "Fort Worth", "Fort Worth", "76117", "We help Haltom City homeowners sell fast for cash - any condition, any situation, close on your schedule."),
    ("colleyville", "Colleyville", "Tarrant County", "Fort Worth", "Southlake", "76034", "We buy houses in Colleyville including higher-value properties facing difficult situations."),
    ("watauga", "Watauga", "Tarrant County", "Fort Worth", "North Richland Hills", "76148", "Watauga homeowners can get a fair cash offer within 24 hours - no repairs, no fees, close fast."),
    ("richland-hills", "Richland Hills", "Tarrant County", "Fort Worth", "North Richland Hills", "76118", "We buy houses in Richland Hills fast - any condition, any situation, cash offer on the spot."),
    ("white-settlement", "White Settlement", "Tarrant County", "Fort Worth", "Fort Worth", "76108", "We help White Settlement homeowners sell fast for a fair cash price with zero fees or commissions."),
    ("benbrook", "Benbrook", "Tarrant County", "Fort Worth", "Fort Worth", "76126", "From Benbrook Lake area properties to established neighborhoods, we buy houses throughout the city."),
    ("plano", "Plano", "Collin County", "McKinney", "Allen", "75023", "From West Plano to East Plano to Legacy area - we know the market and buy houses throughout Plano fast."),
    ("mckinney", "McKinney", "Collin County", "McKinney", "Frisco", "75069", "Historic downtown McKinney to newer subdivisions - we buy houses throughout one of DFW's fastest growing cities."),
    ("frisco", "Frisco", "Collin County", "McKinney", "Plano", "75034", "We buy houses in Frisco fast - including newer construction that may be underwater or facing difficult situations."),
    ("allen", "Allen", "Collin County", "McKinney", "Plano", "75002", "We help Allen homeowners sell fast for cash - any condition, any situation, close in as little as 7 days."),
    ("wylie", "Wylie", "Collin County", "McKinney", "Sachse", "75098", "From downtown Wylie to newer Lake Lavon area developments, we buy houses throughout the city quickly."),
    ("murphy", "Murphy", "Collin County", "McKinney", "Wylie", "75094", "We buy houses in Murphy fast - fair cash offer in 24 hours, no repairs needed, close on your schedule."),
    ("prosper", "Prosper", "Collin County", "McKinney", "Frisco", "75078", "We buy houses in Prosper including newer higher-value properties facing foreclosure or difficult equity situations."),
    ("celina", "Celina", "Collin County", "McKinney", "Prosper", "75009", "Celina is booming and we actively buy houses throughout the area - fast cash, any condition."),
    ("anna", "Anna", "Collin County", "McKinney", "Melissa", "75409", "We buy houses in Anna and surrounding Collin County communities quickly for a fair cash price."),
    ("melissa", "Melissa", "Collin County", "McKinney", "Anna", "75454", "We help Melissa homeowners sell fast for cash - any condition, close in as little as 7 days."),
    ("denton", "Denton", "Denton County", "Denton", "Lewisville", "76201", "From TWU and UNT area rentals to established Denton neighborhoods - we buy houses throughout the city fast."),
    ("lewisville", "Lewisville", "Denton County", "Denton", "Carrollton", "75029", "From Old Town Lewisville to Lake Lewisville area properties, we buy houses throughout the city for cash."),
    ("flower-mound", "Flower Mound", "Denton County", "Denton", "Lewisville", "75022", "We buy houses in Flower Mound including higher-value properties facing tough situations."),
    ("carrollton", "Carrollton", "Denton County", "Denton", "Farmers Branch", "75006", "From Old Downtown Carrollton to Hebron corridor neighborhoods, we buy houses throughout the city fast."),
    ("the-colony", "The Colony", "Denton County", "Denton", "Lewisville", "75056", "We help The Colony homeowners sell fast for a fair cash price - no repairs, no fees, no stress."),
    ("highland-village", "Highland Village", "Denton County", "Denton", "Flower Mound", "75077", "We buy houses in Highland Village including lakefront and higher-value properties in difficult situations."),
    ("corinth", "Corinth", "Denton County", "Denton", "Lewisville", "76210", "We buy houses in Corinth fast - fair cash offer within 24 hours, close on your timeline."),
    ("little-elm", "Little Elm", "Denton County", "Denton", "Frisco", "75068", "From Paloma Creek to Little Elm's lake communities, we buy houses throughout one of DFW's fastest growing cities."),
    ("aubrey", "Aubrey", "Denton County", "Denton", "Little Elm", "76227", "We buy houses in Aubrey and the surrounding fast-growing North Denton County area quickly for cash."),
    ("pilot-point", "Pilot Point", "Denton County", "Denton", "Aubrey", "76258", "We help Pilot Point homeowners sell fast for a fair cash price - any condition, any situation."),
    ("justin", "Justin", "Denton County", "Denton", "Keller", "76247", "We buy houses in Justin and surrounding Denton County communities fast - cash offer in 24 hours."),
    ("argyle", "Argyle", "Denton County", "Denton", "Flower Mound", "76226", "We buy houses in Argyle including higher-value properties facing foreclosure or difficult equity situations."),
    ("rockwall", "Rockwall", "Rockwall County", "Rockwall", "Heath", "75087", "From downtown Rockwall to Lake Ray Hubbard waterfront properties, we buy houses throughout the county fast."),
    ("heath", "Heath", "Rockwall County", "Rockwall", "Rockwall", "75032", "We buy houses in Heath including higher-value lakefront and estate properties facing tough situations."),
    ("fate", "Fate", "Rockwall County", "Rockwall", "Rockwall", "75132", "Fate is one of the fastest growing DFW cities and we actively buy houses throughout the area."),
    ("royse-city", "Royse City", "Rockwall County", "Rockwall", "Fate", "75189", "We buy houses in Royse City and the surrounding fast-growing East DFW area quickly for cash."),
    ("mclendon-chisholm", "McLendon-Chisholm", "Rockwall County", "Rockwall", "Rockwall", "75032", "We buy houses in McLendon-Chisholm and surrounding Rockwall County communities for a fair cash price."),
]

NAV = """<nav class="nav" role="navigation">
  <div class="wrap">
    <div class="nav-in">
      <a href="/" class="logo">[Company<span>Name</span>]</a>
      <div class="nav-r">
        <a href="/#how-it-works" class="nav-lk">How It Works</a>
        <a href="/#situations" class="nav-lk">Situations</a>
        <a href="/#areas" class="nav-lk">Areas</a>
        <a href="/#faq" class="nav-lk">FAQ</a>
        <a href="tel:[YOUR-PHONE-NUMBER]" class="nav-btn">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg>
          Call Now - Free
        </a>
      </div>
    </div>
  </div>
</nav>"""

TBAR = """<div class="tbar">
  <div class="wrap"><div class="tbar-in">
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Zero Fees or Commissions</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Close in 7 Days</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Buy As-Is</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Cash Offer in 24 Hours</div>
  </div></div>
</div>"""

FOOTER = """<footer class="footer">
  <div class="wrap"><div class="footer-in">
    <div class="flogo">[Company<span>Name</span>]</div>
    <p class="fcopy">© 2025 [Company Name] · Serving Dallas-Fort Worth, TX · All rights reserved.</p>
    <div class="flinks">
      <a href="/privacy.html">Privacy</a>
      <a href="/#faq">FAQ</a>
      <a href="/#get-offer">Get Offer</a>
    </div>
  </div></div>
</footer>
<div class="mcta">
  <a href="tel:[YOUR-PHONE-NUMBER]" class="mc">Call Now</a>
  <a href="#get-offer" class="mf">Get Cash Offer</a>
</div>"""

JS = """<script>
function toggleFaq(btn){
  const a=btn.nextElementSibling,open=btn.getAttribute('aria-expanded')==='true';
  document.querySelectorAll('.faq-q').forEach(b=>{b.setAttribute('aria-expanded','false');b.nextElementSibling.classList.remove('open')});
  if(!open){btn.setAttribute('aria-expanded','true');a.classList.add('open')}
}
function handleSubmit(e){
  e.preventDefault();
  const form=document.getElementById('lead-form'),success=document.getElementById('form-success');
  let valid=true;
  form.querySelectorAll('[required]').forEach(f=>{if(!f.value.trim()){valid=false;f.style.borderColor='#a63d2f'}else{f.style.borderColor=''}});
  if(!valid)return;
  form.style.display='none';
  success.style.display='block';
}
const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target)}})},{threshold:.1,rootMargin:'0px 0px -36px 0px'});
document.querySelectorAll('.rv').forEach(el=>obs.observe(el));
document.querySelectorAll('a[href^="#"]').forEach(a=>{a.addEventListener('click',e=>{const t=document.querySelector(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'})}})});
const ph=document.getElementById('ph');
if(ph){ph.addEventListener('input',function(){let v=this.value.replace(/\\D/g,'');if(v.length>=6)v='('+v.substring(0,3)+') '+v.substring(3,6)+'-'+v.substring(6,10);else if(v.length>=3)v='('+v.substring(0,3)+') '+v.substring(3);this.value=v;})}
</script>"""

FORM = """<div style="background:var(--ink);border-radius:16px;padding:40px;max-width:560px;margin:0 auto;position:relative;overflow:hidden">
  <div style="position:absolute;top:-100px;right:-100px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(200,146,42,.12) 0%,transparent 65%);pointer-events:none"></div>
  <div style="position:relative;z-index:1">
    <p style="font-size:.72rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Free - No Obligation</p>
    <h3 style="font-family:var(--fh);font-size:1.6rem;font-weight:700;color:var(--cream);margin-bottom:6px">Get Your Cash Offer</h3>
    <p style="font-size:.87rem;color:rgba(246,241,233,.5);margin-bottom:24px">We'll be in touch within hours - usually the same day.</p>
    <form id="lead-form" onsubmit="handleSubmit(event)" novalidate>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
        <div><label style="display:block;font-size:.74rem;font-weight:600;color:rgba(246,241,233,.5);letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px">First Name</label><input type="text" id="fn" name="fname" placeholder="John" required style="width:100%;background:rgba(246,241,233,.07);border:1px solid rgba(246,241,233,.15);color:var(--cream);padding:11px 14px;border-radius:var(--r);font-family:var(--fb);font-size:.92rem;outline:none"></div>
        <div><label style="display:block;font-size:.74rem;font-weight:600;color:rgba(246,241,233,.5);letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px">Last Name</label><input type="text" id="ln" name="lname" placeholder="Smith" required style="width:100%;background:rgba(246,241,233,.07);border:1px solid rgba(246,241,233,.15);color:var(--cream);padding:11px 14px;border-radius:var(--r);font-family:var(--fb);font-size:.92rem;outline:none"></div>
      </div>
      <div style="margin-bottom:12px"><label style="display:block;font-size:.74rem;font-weight:600;color:rgba(246,241,233,.5);letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px">Phone Number</label><input type="tel" id="ph" name="phone" placeholder="(214) 555-0000" required style="width:100%;background:rgba(246,241,233,.07);border:1px solid rgba(246,241,233,.15);color:var(--cream);padding:11px 14px;border-radius:var(--r);font-family:var(--fb);font-size:.92rem;outline:none"></div>
      <div style="margin-bottom:12px"><label style="display:block;font-size:.74rem;font-weight:600;color:rgba(246,241,233,.5);letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px">Property Address</label><input type="text" id="addr" name="address" placeholder="123 Main St" required style="width:100%;background:rgba(246,241,233,.07);border:1px solid rgba(246,241,233,.15);color:var(--cream);padding:11px 14px;border-radius:var(--r);font-family:var(--fb);font-size:.92rem;outline:none"></div>
      <div style="margin-bottom:16px"><label style="display:block;font-size:.74rem;font-weight:600;color:rgba(246,241,233,.5);letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px">Your Situation</label><select id="sit" name="situation" required style="width:100%;background:rgba(246,241,233,.07);border:1px solid rgba(246,241,233,.15);color:var(--cream);padding:11px 14px;border-radius:var(--r);font-family:var(--fb);font-size:.92rem;outline:none;-webkit-appearance:none"><option value="" disabled selected>Select situation</option><option value="foreclosure">Facing Foreclosure</option><option value="tax">Behind on Property Taxes</option><option value="inherited">Inherited Property / Probate</option><option value="divorce">Going Through Divorce</option><option value="repairs">Too Many Repairs Needed</option><option value="landlord">Tired Landlord</option><option value="moving">Relocating Fast</option><option value="vacant">Vacant Property</option><option value="other">Other</option></select></div>
      <button type="submit" style="width:100%;background:var(--gold);color:var(--ink);border:none;border-radius:var(--r);padding:15px;font-family:var(--fb);font-size:.97rem;font-weight:700;cursor:pointer;transition:all .2s;box-shadow:0 4px 20px rgba(200,146,42,.3)">Get My Free Cash Offer →</button>
    </form>
    <div id="form-success" style="display:none;text-align:center;padding:32px 0">
      <div style="font-size:2.5rem;margin-bottom:12px">✅</div>
      <h3 style="font-family:var(--fh);color:var(--cream);font-size:1.3rem;margin-bottom:8px">Got It - We'll Be In Touch!</h3>
      <p style="color:rgba(246,241,233,.5);font-size:.87rem">Someone will reach out within a few hours. Keep an eye on your phone.</p>
    </div>
    <p style="font-size:.74rem;color:rgba(246,241,233,.3);margin-top:12px;text-align:center">🔒 Your info is private and never shared.</p>
  </div>
</div>"""

def make_city_page(slug, name, county, county_seat, nearby, zipcode, detail):
    depth = "../"
    schema = f"""{{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "[COMPANY NAME]",
  "description": "We buy houses fast in {name}, {county}, TX. Fair cash offer in 24 hours. No repairs, no fees, close in as little as 7 days.",
  "url": "https://www.yourwebsite.com/cities/{slug}.html",
  "telephone": "[YOUR-PHONE-NUMBER]",
  "areaServed": "{name}, {county}, Texas"
}}"""

    faq_items = [
        (f"How fast can you buy my house in {name}?",
         f"We can close in as little as 7 days in {name}. We provide a cash offer within 24 hours of seeing your property. If you need more time we work completely around your schedule."),
        (f"Do I need to repair or clean my {name} house before selling?",
         f"No. We buy houses in {name} completely as-is. No cleaning, no repairs, no staging. Leave behind whatever you don't want to deal with."),
        ("Are there any fees or commissions?",
         "Zero fees, zero commissions. We cover all closing costs. The cash offer we make is the exact amount you walk away with."),
        (f"Can you help if I'm facing foreclosure in {name}?",
         f"Yes. We navigate foreclosure situations in {name} regularly. A fast cash sale can stop the process and potentially help you walk away with money instead of losing the property entirely."),
        (f"Do you buy houses with back taxes or liens in {name}?",
         f"Yes. Back taxes and liens on {name} properties can often be resolved directly from the sale proceeds at closing - no money out of pocket on your end."),
    ]

    faq_html = ""
    for q, a in faq_items:
        faq_html += f"""
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">{q}
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">{a}</div>
      </div>"""

    nearby_cities = [c for c in cities if c[0] != slug and c[3] == county_seat][:8]
    nearby_html = ""
    for nc in nearby_cities:
        nearby_html += f'<a href="{nc[0]}.html" class="city-link">Sell House Fast {nc[1]}</a>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sell My House Fast {name} TX | Cash Home Buyers {name} | [COMPANY NAME]</title>
  <meta name="description" content="Sell your house fast for cash in {name}, TX. Fair cash offer in 24 hours. No repairs, no fees, no agents. Close in 7 days. Foreclosure, divorce, inherited, tax issues - we help with any situation in {name}."/>
  <meta name="robots" content="index, follow"/>
  <link rel="canonical" href="https://www.yourwebsite.com/cities/{slug}.html"/>
  <script type="application/ld+json">{schema}</script>
  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{"@type":"Question","name":"How fast can you buy my house in {name}?","acceptedAnswer":{{"@type":"Answer","text":"We can close in as little as 7 days in {name}, TX. Cash offer within 24 hours."}}}},
      {{"@type":"Question","name":"Do I need repairs before selling in {name}?","acceptedAnswer":{{"@type":"Answer","text":"No. We buy houses in {name} completely as-is. No repairs, no cleaning needed."}}}},
      {{"@type":"Question","name":"Are there fees when selling in {name}?","acceptedAnswer":{{"@type":"Answer","text":"Zero fees, zero commissions. We cover all closing costs in {name}."}}}}
    ]
  }}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="../shared.css"/>
  <style>
    .city-hero{{padding:130px 0 80px;background:var(--ink);position:relative;overflow:hidden}}
    .city-hero::before{{content:'';position:absolute;top:-200px;right:-200px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(200,146,42,.1) 0%,transparent 65%);pointer-events:none}}
    .city-hero-grid{{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:1}}
    .city-hero h1{{font-family:var(--fh);font-size:clamp(2.2rem,3.5vw,3.4rem);font-weight:900;color:var(--cream);line-height:1.1;letter-spacing:-.025em;margin-bottom:18px}}
    .city-hero h1 em{{color:var(--gold);font-style:italic}}
    .city-hero p{{font-size:1rem;color:rgba(246,241,233,.55);line-height:1.72;margin-bottom:28px;max-width:480px}}
    .city-acts{{display:flex;gap:14px;flex-wrap:wrap}}
    .badge{{display:inline-flex;align-items:center;gap:8px;background:var(--gold-pale);border:1px solid var(--gold);color:var(--ink);padding:7px 16px;border-radius:100px;font-size:.74rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;width:fit-content;margin-bottom:24px}}
    .badge-dot{{width:7px;height:7px;border-radius:50%;background:var(--gold);animation:pdot 2s infinite;flex-shrink:0}}
    .pills{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}}
    .pill{{display:inline-flex;align-items:center;gap:6px;background:rgba(246,241,233,.08);border:1px solid rgba(246,241,233,.15);border-radius:100px;padding:6px 14px;font-size:.78rem;font-weight:500;color:var(--cream)}}
    .pill svg{{width:13px;height:13px;color:var(--sage-lt);flex-shrink:0}}
    .sits{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
    .sit{{background:rgba(246,241,233,.05);border:1px solid rgba(246,241,233,.1);border-radius:12px;padding:28px 24px;transition:all .2s}}
    .sit:hover{{background:rgba(200,146,42,.08);border-color:rgba(200,146,42,.3);transform:translateY(-3px)}}
    .sit-ico{{font-size:1.8rem;margin-bottom:12px;display:block}}
    .sit h3{{font-family:var(--fh);font-size:1.05rem;font-weight:700;color:var(--cream);margin-bottom:8px}}
    .sit p{{font-size:.82rem;color:rgba(246,241,233,.45);line-height:1.6}}
    .content-body{{max-width:780px}}
    .content-body h2{{font-family:var(--fh);font-size:1.7rem;font-weight:700;color:var(--ink);margin:36px 0 14px;letter-spacing:-.02em}}
    .content-body h3{{font-family:var(--fh);font-size:1.2rem;font-weight:700;color:var(--ink);margin:24px 0 10px}}
    .content-body p{{font-size:.95rem;color:var(--muted);line-height:1.8;margin-bottom:16px}}
    .content-body ul{{margin:0 0 16px 20px}}
    .content-body li{{font-size:.93rem;color:var(--muted);line-height:1.75;margin-bottom:6px}}
    @media(max-width:1024px){{.city-hero-grid{{grid-template-columns:1fr}}.sits{{grid-template-columns:repeat(2,1fr)}}}}
    @media(max-width:768px){{.sits{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
{NAV}

<!-- BREADCRUMB -->
<div class="breadcrumb" style="padding-top:80px;background:var(--ink)">
  <div class="wrap" style="padding-top:16px;padding-bottom:0">
    <a href="/">Home</a> &rsaquo; <a href="/#areas">Cities</a> &rsaquo; {name}
  </div>
</div>

<!-- HERO -->
<section class="city-hero">
  <div class="wrap">
    <div class="city-hero-grid">
      <div>
        <div class="badge"><span class="badge-dot"></span>{county} · DFW Metroplex</div>
        <h1>Sell Your House Fast in <em>{name}, TX</em></h1>
        <p>We help {name} homeowners who are stuck in a tough spot find a real way out - a fair cash offer within 24 hours, no repairs needed, no agent fees, and a closing timeline that works for you.</p>
        <div class="pills">
          <span class="pill"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Cash offer in 24 hours</span>
          <span class="pill"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Close in 7 days</span>
          <span class="pill"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Zero fees or commissions</span>
          <span class="pill"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Any condition - as-is</span>
        </div>
        <div class="city-acts">
          <a href="#get-offer" class="btn-g">Get My Free Cash Offer</a>
          <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-dk">Call Now - Free</a>
        </div>
      </div>
      <div>{FORM}</div>
    </div>
  </div>
</section>

{TBAR}

<!-- ABOUT THIS CITY -->
<section class="sec">
  <div class="wrap">
    <div class="content-body rv">
      <p class="slbl">We Buy Houses in {name}</p>
      <h2 class="sh2">Cash Home Buyers in {name}, {county}</h2>
      <p>If you need to sell your house fast in {name}, TX, we can help. We are local cash home buyers serving all of {county} and the surrounding DFW area. We buy houses in any condition - no repairs needed, no agent commissions, no closing costs on your end.</p>
      <p>{detail}</p>
      <p>Our process is simple: tell us about your property, we come see it, and we make you a fair cash offer on the spot. You choose the closing date - as fast as 7 days or on whatever timeline works for you. There is no obligation and no pressure to accept.</p>

      <h2>Why {name} Homeowners Choose Us</h2>
      <p>Selling through a traditional real estate agent in {name} can take 60-120 days, cost 5-6% in commissions, and require repairs and showings that many homeowners simply can't afford or don't have time for. We offer a different path:</p>
      <ul>
        <li><strong>Cash offer within 24 hours</strong> of seeing your property</li>
        <li><strong>Close in as little as 7 days</strong> - or on your schedule</li>
        <li><strong>Zero agent commissions</strong> - save 5-6% immediately</li>
        <li><strong>We cover all closing costs</strong> - no deductions at the table</li>
        <li><strong>No repairs or cleaning</strong> - we take it exactly as-is</li>
        <li><strong>Guaranteed sale</strong> - no financing contingencies or fall-throughs</li>
      </ul>

      <h2>Situations We Help {name} Homeowners With</h2>
      <p>We work with homeowners in {name} across a wide range of difficult situations. Whatever is going on with your property - we've likely seen it before and know how to help.</p>
    </div>
  </div>
</section>

<!-- SITUATIONS -->
<section class="sec sec-dk">
  <div class="wrap">
    <p class="slbl rv">Every Situation Welcome</p>
    <h2 class="sh2 lt rv">We Help {name} Homeowners<br>in Any Situation</h2>
    <div class="sits" style="margin-top:8px">
      <div class="sit rv"><span class="sit-ico">🏚️</span><h3>Foreclosure</h3><p>Behind on payments in {name}? A fast cash sale can stop the foreclosure process and help you walk away with money instead of losing everything.</p></div>
      <div class="sit rv"><span class="sit-ico">📋</span><h3>Back Property Taxes</h3><p>Tax liens on your {name} property can often be resolved at closing from the sale proceeds - no money out of pocket required.</p></div>
      <div class="sit rv"><span class="sit-ico">⚖️</span><h3>Inherited Property</h3><p>Inherited a house in {name} you didn't plan for? We work with estates and probate regularly and move at whatever pace the process requires.</p></div>
      <div class="sit rv"><span class="sit-ico">💔</span><h3>Divorce</h3><p>A fast clean cash sale of your {name} property removes conflict and puts money in both parties' hands without the delays of a traditional listing.</p></div>
      <div class="sit rv"><span class="sit-ico">🔨</span><h3>Major Repairs Needed</h3><p>Foundation issues, roof damage, fire, mold - we buy houses in {name} in any condition. Zero dollars spent on repairs.</p></div>
      <div class="sit rv"><span class="sit-ico">🏠</span><h3>Tired Landlord</h3><p>Done managing a rental property in {name}? We buy occupied and vacant rentals and let you step away from the stress permanently.</p></div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv">Simple Process</p>
    <h2 class="sh2 rv">How to Sell Your {name} House Fast</h2>
    <p class="ssub rv">Three steps from where you are today to cash in your hand.</p>
    <div class="steps">
      <div class="step rv">
        <div class="snum">01</div>
        <h3>Tell Us About Your Property</h3>
        <p>Fill out the form or call us. Tell us about your {name} property and your situation. No judgment - the more we know, the better we can help.</p>
      </div>
      <div class="step rv">
        <div class="snum">02</div>
        <h3>We Come See It</h3>
        <p>We schedule a quick walkthrough at your convenience. No cleaning, no repairs. We look at the property as-is and make a fair offer on the spot.</p>
      </div>
      <div class="step rv">
        <div class="snum">03</div>
        <h3>You Pick the Closing Date</h3>
        <p>Accept our offer and choose your closing date - as fast as 7 days or whenever you need. We close through a licensed Texas title company.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="sec sec-alt">
  <div class="wrap">
    <p class="slbl rv" style="text-align:center">Questions</p>
    <h2 class="sh2 rv" style="text-align:center;margin-bottom:8px">Selling Your {name} House - FAQ</h2>
    <p style="text-align:center;color:var(--muted);font-size:.95rem;margin-bottom:44px;max-width:500px;margin-left:auto;margin-right:auto" class="rv">Straight answers about selling your house fast in {name}, TX.</p>
    <div class="faq-list rv">{faq_html}</div>
  </div>
</section>

<!-- NEARBY CITIES -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv">Also Serving</p>
    <h2 class="sh2 rv">We Buy Houses Near {name}</h2>
    <p class="ssub rv" style="margin-bottom:0">We serve all of {county} and surrounding DFW communities.</p>
    <div class="city-grid rv">{nearby_html}</div>
  </div>
</section>

<!-- BOTTOM CTA -->
<section style="background:var(--ink);padding:80px 0;text-align:center;position:relative;overflow:hidden">
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(200,146,42,.1) 0%,transparent 65%);pointer-events:none"></div>
  <div class="wrap" style="position:relative;z-index:1">
    <h2 style="font-family:var(--fh);font-size:clamp(2rem,3.5vw,3rem);font-weight:900;color:var(--cream);letter-spacing:-.025em;line-height:1.15;margin-bottom:16px">Ready to Sell Your <em style="font-style:italic;color:var(--gold)">{name}</em> House?</h2>
    <p style="font-size:.97rem;color:rgba(246,241,233,.5);max-width:440px;margin:0 auto 36px;line-height:1.7">No obligation. No pressure. Just find out what your options are - it costs nothing.</p>
    <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap">
      <a href="#get-offer" class="btn-g">Get My Free Cash Offer</a>
      <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-dk">Call [YOUR-PHONE-NUMBER]</a>
    </div>
  </div>
</section>

{FOOTER}
{JS}
</body>
</html>"""
    return html

# Generate all city pages
output_dir = "/home/claude/dfw-site/cities"
for city_data in cities:
    slug, name, county, county_seat, nearby, zipcode, detail = city_data
    html = make_city_page(slug, name, county, county_seat, nearby, zipcode, detail)
    filepath = os.path.join(output_dir, f"{slug}.html")
    with open(filepath, "w") as f:
        f.write(html)

print(f"Generated {len(cities)} city pages")
