# DFW Home Solutions — Project Brief
> Drop this file in the project root. Reference it at the start of every Claude Code session.

---

## What This Is
A **128-page static HTML/CSS/JS lead generation website** for a DFW real estate wholesaling business. The goal is seller lead capture — homeowners in difficult situations (foreclosure, back taxes, divorce, inherited property) who need to sell fast. The site also serves as a trust signal during cold calls.

**Live URL:** sellhousetrial.netlify.app  
**Host:** Netlify (drag-and-drop deploy)  
**Stack:** Pure HTML + CSS + vanilla JS — no frameworks, no build tools  

---

## File Structure
```
dfw-site/
├── index.html              ← Homepage (primary conversion page)
├── style.css               ← Shared styles for inner pages (city, blog, situational)
├── sitemap.xml             ← 66 URLs, submit to Google Search Console
├── robots.txt
├── PROJECT_BRIEF.md        ← This file
├── cities/                 ← 61 city pages (individual HTML files)
│   └── sell-house-fast-[city].html
├── blog/                   ← 5 blog posts + index
│   ├── index.html
│   ├── how-to-stop-foreclosure-dallas-tx.html
│   ├── selling-inherited-house-texas-probate.html
│   ├── sell-house-during-divorce-texas.html
│   ├── property-taxes-delinquent-dallas-county.html
│   └── we-buy-houses-dfw-how-it-works.html
├── foreclosure/index.html  ← Situational landing page
├── inherited-property/index.html
├── divorce/index.html
└── tax-liens/index.html
```

---

## Design System

### Typography
- **Display/Headlines:** `Cormorant Garamond` — luxury editorial serif (Google Fonts)
- **Body/UI:** `Outfit` — clean geometric sans (Google Fonts)
- Inner pages (blog, city) currently use `Playfair Display` + `DM Sans` — being unified to match homepage

### Color Tokens (defined in index.html `<style>` block)
```css
--ink: #0e0d0b        /* near-black, primary text */
--ink2: #0f0e0c       /* hero/dark section backgrounds */
--cream: #f7f3ec      /* page background */
--warm: #f0ebe1       /* alternate section background */
--panel: #e8e1d6      /* card backgrounds */
--gold: #b8812a       /* primary accent — NO glow/box-shadow on buttons */
--gold-lt: #d4a044    /* gold hover state */
--gold-pale: #f2e3c4  /* gold tint backgrounds */
--rust: #8f3324       /* negative/warning */
--sage: #3a5636       /* positive/check marks */
--muted: #7a7266      /* secondary text */
--border: #ddd6ca     /* dividers */
--white: #fff
```

### Critical CSS Rules
- `.btn-gold` — gold CTA button. **No box-shadow glow** (removed intentionally — looked too shiny on mobile)
- `.rv` — scroll reveal class. Starts `opacity:0`, becomes visible via IntersectionObserver
- `.rv.vis` — triggered state. JS adds this class on scroll
- IntersectionObserver options must be `{threshold:.1}` — NOT `{{'threshold':.1}}` (double braces = JS syntax error, content invisible)
- Nav has NO `backdrop-filter:blur()` — causes iOS Safari blur bug when bottom bar appears
- Nav has `-webkit-transform:translateZ(0)` — forces GPU compositing layer
- `html{background:var(--cream)}` set on html element, not just body — prevents iOS transparent gap

---

## Homepage Sections (index.html scroll order)
1. **Nav** — fixed, solid cream background, mobile hamburger menu
2. **Hero** — dark split layout: left (headline + bullet checks + stats) / right (embedded lead form). No grain overlay, no radial glow (both caused yellow tint)
3. **Trust Bar** — horizontally scrollable single row on mobile (`overflow-x:auto`, `flex-wrap:nowrap`, scrollbar hidden). 5 trust signals
4. **How It Works** — 3 process cards with gold-ringed numbered circles
5. **Situations** — dark `#0f0e0c` section, 6 cards with uniform `#1a1917` background, `rgba(247,243,236,.18)` separators between cards
6. **Compare Table** — Us vs Agent listing, 7 rows each
7. **Testimonials** — 3 cards
8. **City Grid** — organized by county (Dallas/Tarrant/Collin/Denton/Rockwall), city tags link to city pages
9. **FAQ** — accordion. "Call Us — We Pick Up" button sits above the accordion list
10. **Final CTA** — dark section, zero-pressure copy
11. **Footer**

---

## Placeholders To Replace (find & replace across all 128 files)
- `[COMPANY NAME]` → business DBA name (TBD — "Home Solutions" style, e.g. "Lone Star Home Solutions")
- `[YOUR-PHONE-NUMBER]` → OpenPhone DFW local number (not yet set up)
- `https://www.yourwebsite.com` → final domain (being purchased ~$10 on Namecheap)

---

## Pending Tasks (priority order)

### Immediate
- [ ] **Wire up lead form with Netlify Forms** — add `data-netlify="true"` attribute to `<form id="lead-form">` in index.html. Submissions appear in Netlify dashboard + email alerts. Zero cost, zero backend needed
- [ ] **Google Places Autocomplete** on property address field (`id="addr"`) — needs Google Maps API key with Places API enabled. Free under $200/month. console.cloud.google.com
- [ ] **Replace all placeholders** — company name, phone number, domain URL (sed command can do all 128 files at once)
- [ ] **Google Business Profile** — set up as Service Area Business (no physical address needed)

### UX / Visual (Desktop focus)
- [ ] **GSAP + ScrollTrigger** — replace basic CSS fadeUp with scroll-triggered sequences on hero headline, section cards, stats counter animation
- [ ] **Lenis smooth scroll** — replaces native browser scroll. Single CDN script. Makes entire site feel more premium instantly
- [ ] **Splitting.js** — animate hero h1 word by word or letter by letter on load
- [ ] **Desktop hero layout** — form panel proportions need work at 1200px+, typography scale
- [ ] **Custom cursor** on desktop — immediately signals "not a template site"
- [ ] **About/Who We Are page** — photo + short bio. Critical trust signal for cold calls ("look us up while we're talking")
- [ ] **Unify fonts across inner pages** — blog/city pages still use Playfair Display + DM Sans, should match homepage Cormorant Garamond + Outfit

### SEO / Infrastructure
- [ ] **Submit sitemap.xml** to Google Search Console after custom domain connected
- [ ] **Virtual mailbox** for Dallas address (~$10-20/mo: Anytime Mailbox, PostScan Mail, iPostal1)
- [ ] **Set up GitHub repo** → connect to Netlify for auto-deploy on push (replaces manual drag-and-drop)

---

## Libraries to Add (all via CDN — no npm, no build step)

```html
<!-- Lenis smooth scroll — add before closing </body> -->
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>

<!-- GSAP core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

<!-- GSAP ScrollTrigger plugin -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Splitting.js (text split animation) -->
<link rel="stylesheet" href="https://unpkg.com/splitting/dist/splitting.css">
<script src="https://unpkg.com/splitting/dist/splitting.min.js"></script>

<!-- Google Places Autocomplete (replace YOUR_API_KEY) -->
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initAutocomplete" async defer></script>
```

**Lenis init pattern:**
```js
const lenis = new Lenis({ lerp: 0.1, smooth: true })
function raf(time) { lenis.raf(time); requestAnimationFrame(raf) }
requestAnimationFrame(raf)
// If using GSAP ScrollTrigger, add:
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add((time) => lenis.raf(time * 1000))
```

**Google Places Autocomplete pattern:**
```js
function initAutocomplete() {
  const input = document.getElementById('addr')
  const autocomplete = new google.maps.places.Autocomplete(input, {
    componentRestrictions: { country: 'us' },
    fields: ['formatted_address'],
    types: ['address']
  })
}
```

---

## Business Context
- **Model:** Real estate wholesaling — find distressed sellers, get property under contract, assign contract to cash buyer for assignment fee
- **Owner:** Currently 1099 at RFP Homes (finds buyers for company deals) + building own independent pipeline simultaneously
- **Market:** Dallas-Fort Worth — highly competitive, 60+ cities across 5 counties (Dallas, Tarrant, Collin, Denton, Rockwall)
- **Positioning:** "Problem solver who helps homeowners in difficult situations" — NOT investor/cash buyer framing
- **Primary lead gen:** Cold calling scored leads from county public records (lis pendens, tax delinquent rolls, probate filings)
- **Site's dual role:** (1) Passive SEO — rank for city + situation searches. (2) Active trust signal — share URL during cold calls

### Language Rules
**Never say:** investor, cash buyer, flip houses, make you an offer, what's your bottom line  
**Always say:** "I work with homeowners in difficult situations", "I help people find options they might not know they have", "We help you find a way forward"

### Target Seller Situations
- Facing foreclosure (lis pendens filed)
- Behind on property taxes (2+ years delinquent)
- Inherited property / probate
- Going through divorce
- Too many repairs, can't afford them
- Tired/burnt-out landlord
- Vacant property

---

## Competitor Research Notes
- **Ninebird Properties (ninebp.com)** — most sophisticated local competitor. BBB accredited, Google 5-star in nav, "as seen on" Yahoo Finance / This Old House / Better Homes & Gardens. Weakness: Wix template feel, generic fonts, form on separate page
- **Southern Hills Home Buyers** — strong Google reviews (293, 5.0 stars)
- **Cash House Buyers DFW** — BBB A+ since 2019, known for being "never pushy"
- **Key differentiator to build toward:** Professional design (already ahead), local DFW knowledge, personal face/bio page, fast response time

---

## Deployment Process
**Current:** Download zip → unzip → drag `dfw-site` folder into Netlify deploy dropzone → live in ~30 seconds  
**Future:** GitHub repo → Netlify connected → push to main branch → auto-deploys  

**Netlify site:** sellhousetrial.netlify.app  
Once custom domain purchased: point nameservers to Netlify, add domain in Netlify dashboard

---

## Known Bugs Fixed (don't re-introduce)
| Bug | Cause | Fix |
|-----|-------|-----|
| Blog content invisible | `{{'threshold':.1}}` double braces in IntersectionObserver | Fixed to `{threshold:.1}` |
| Blog CSS not loading | `../../style.css` wrong path from `/blog/` subfolder | Fixed to `../style.css` |
| Hero yellow tint | SVG feTurbulence grain + radial gold glow overlay | Both removed entirely |
| Gold buttons shimmering | `box-shadow: 0 6px 28px rgba(184,129,42,.38)` | Removed, buttons now flat |
| iOS Safari nav blur | `backdrop-filter:blur(14px)` on nav | Removed, nav is solid `var(--cream)` |
| iOS bottom bar transparent gap | Body background not on html element | Added `html{background:var(--cream)}` |
| First sit-card different color | `.rv` paint timing caused flash | All cards set to uniform `#1a1917` |
| Trust bar wrapping on mobile | `flex-wrap:wrap` | Changed to `flex-wrap:nowrap` + `overflow-x:auto` |
EOF