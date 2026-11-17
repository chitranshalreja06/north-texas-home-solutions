#!/usr/bin/env python3
"""Rebuild blog posts on navy/white theme, preserving content."""
import re, glob

ARTICLE_CSS = """
.article-hero{background:var(--navy);color:#fff;padding:120px 0 60px}
.article-hero .breadcrumb{font-size:.82rem;color:rgba(255,255,255,.6);margin-bottom:20px}
.article-hero .breadcrumb a{color:rgba(255,255,255,.8);text-decoration:none}
.article-hero .breadcrumb span{margin:0 8px}
.article-tag{display:inline-block;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);color:#fff;padding:5px 14px;border-radius:100px;font-size:.72rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;margin-bottom:18px}
.article-hero h1{font-family:var(--fh);font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;letter-spacing:-.02em;line-height:1.2;max-width:720px;margin-bottom:16px}
.article-hero p{color:rgba(255,255,255,.7);font-size:1rem;max-width:640px;line-height:1.7;margin:0}
.prose{max-width:720px;margin:0 auto}
.prose h2{font-family:var(--fh);font-size:1.5rem;font-weight:700;color:var(--navy);margin:2.2rem 0 .8rem;letter-spacing:-.02em}
.prose h3{font-family:var(--fh);font-size:1.15rem;font-weight:700;color:var(--navy);margin:1.6rem 0 .6rem}
.prose p{font-size:.96rem;color:var(--text2);line-height:1.85;margin-bottom:1.1rem}
.prose ul,.prose ol{margin:0 0 1.2rem 1.3rem;display:grid;gap:.5rem}
.prose li{font-size:.94rem;color:var(--text2);line-height:1.75}
.prose li strong,.prose p strong{color:var(--navy)}
.prose a{color:var(--navy);font-weight:600}
.prose blockquote{border-left:4px solid var(--navy);background:var(--bg-alt);padding:18px 22px;border-radius:0 12px 12px 0;margin:1.6rem 0;font-size:.93rem;color:var(--text2);line-height:1.7}
"""

def build_post(path, title, desc, canon, schema_tag, h1, cat, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/theme.css">
<style>{ARTICLE_CSS}</style>
{schema_tag}
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
<a href="/#get-offer" class="btn-nav">Get Cash Offer</a>
</div></nav>

<div class="article-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="/">Home</a><span>&rsaquo;</span><a href="/blog/">Blog</a><span>&rsaquo;</span>{cat}</div>
    <div class="article-tag">{cat}</div>
    <h1>{h1}</h1>
    <p>{desc}</p>
  </div>
</div>

<section class="sec">
  <div class="wrap">
    <article class="prose">
{body}
    </article>
  </div>
</section>

<section class="sec alt">
  <div class="wrap sec-center">
    <span class="eyebrow rv">Ready When You Are</span>
    <h2 class="sec-h2 rv">Get Your Free <em>Cash Offer</em></h2>
    <p class="sec-lead rv">No repairs. No fees. No obligation. Just a fair cash offer and a closing date you choose.</p>
    <div class="final-btns">
      <a href="/#get-offer" class="btn-gold">Get My Free Cash Offer</a>
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
        <a href="/#get-offer">Get Offer</a>
      </div>
    </div>
  </div>
</footer>
<div class="sticky-cta"><a href="/#get-offer">Text Us Now</a></div>
<script>
document.addEventListener('DOMContentLoaded',function(){{
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{threshold:.12}});
  document.querySelectorAll('.rv').forEach(function(el){{io.observe(el);}});
}});
</script>
</body>
</html>"""

for f in glob.glob("blog/*.html"):
    if f.endswith("blog/index.html"):
        continue
    s = open(f, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)"', s).group(1)
    canon = re.search(r'<link rel="canonical" href="(.*?)"', s).group(1)
    am = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', s, re.S)
    schema_tag = f'<script type="application/ld+json">{am.group(1)}</script>' if am else ""
    h1m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    h1 = re.sub(r"<[^>]+>", "", h1m.group(1)).strip() if h1m else title
    h1 = h1.replace("\u2014", "-")
    bm = re.search(r'<article class="prose[^"]*">(.*?)</article>', s, re.S)
    body = bm.group(1).strip() if bm else ""
    # clean gold remnants from body
    body = re.sub(r'style="[^"]*var\(--(gold|cream|ink)[^"]*"', '', body)
    catm = re.search(r'text-transform:uppercase">(.*?)</span>', s)
    cat = catm.group(1).strip() if catm else "Guide"
    html = build_post(f, title, desc, canon, schema_tag, h1, cat, body)
    open(f, "w", encoding="utf-8").write(html)
    print(f"rebuilt: {f} ({len(html)} bytes)")
