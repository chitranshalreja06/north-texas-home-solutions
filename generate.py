#!/usr/bin/env python3
"""Generate all DFW wholesaling website pages"""

import os

# ── CITIES ────────────────────────────────────────────────────────────────────
CITIES = [
    # Dallas County
    {"name": "Dallas", "county": "Dallas", "zip": "75201", "pop": "1.3 million", "note": "the heart of DFW"},
    {"name": "Garland", "county": "Dallas", "zip": "75040", "pop": "240,000", "note": "one of DFW's largest suburbs"},
    {"name": "Irving", "county": "Dallas", "zip": "75061", "pop": "256,000", "note": "home to Las Colinas and DFW Airport"},
    {"name": "Richardson", "county": "Dallas", "zip": "75080", "pop": "120,000", "note": "part of the Telecom Corridor"},
    {"name": "Mesquite", "county": "Dallas", "zip": "75149", "pop": "143,000", "note": "a growing East Dallas suburb"},
    {"name": "Duncanville", "county": "Dallas", "zip": "75116", "pop": "39,000", "note": "a close-in southwest Dallas suburb"},
    {"name": "Farmers Branch", "county": "Dallas", "zip": "75234", "pop": "41,000", "note": "a well-established northwest Dallas city"},
    {"name": "Cedar Hill", "county": "Dallas", "zip": "75104", "pop": "48,000", "note": "a southwest DFW suburb with strong community roots"},
    {"name": "Lancaster", "county": "Dallas", "zip": "75134", "pop": "40,000", "note": "a south Dallas suburb with deep history"},
    {"name": "DeSoto", "county": "Dallas", "zip": "75115", "pop": "54,000", "note": "a fast-growing south Dallas city"},
    {"name": "Rowlett", "county": "Dallas", "zip": "75088", "pop": "66,000", "note": "a lakeside suburb on Lake Ray Hubbard"},
    {"name": "Sachse", "county": "Dallas", "zip": "75048", "pop": "27,000", "note": "a rapidly growing northeast suburb"},
    {"name": "Balch Springs", "county": "Dallas", "zip": "75180", "pop": "25,000", "note": "an east Dallas suburb"},
    {"name": "Seagoville", "county": "Dallas", "zip": "75159", "pop": "17,000", "note": "a southeast Dallas suburb"},
    # Tarrant County
    {"name": "Fort Worth", "county": "Tarrant", "zip": "76101", "pop": "950,000", "note": "the cultural capital of North Texas"},
    {"name": "Arlington", "county": "Tarrant", "zip": "76010", "pop": "400,000", "note": "home to AT&T Stadium and Globe Life Field"},
    {"name": "Grapevine", "county": "Tarrant", "zip": "76051", "pop": "55,000", "note": "a historic lakeside city near DFW Airport"},
    {"name": "Keller", "county": "Tarrant", "zip": "76248", "pop": "48,000", "note": "one of DFW's top-rated family suburbs"},
    {"name": "Hurst", "county": "Tarrant", "zip": "76053", "pop": "40,000", "note": "a mid-cities suburb between Dallas and Fort Worth"},
    {"name": "Euless", "county": "Tarrant", "zip": "76039", "pop": "57,000", "note": "a diverse mid-cities community"},
    {"name": "Bedford", "county": "Tarrant", "zip": "76021", "pop": "49,000", "note": "a well-established mid-cities suburb"},
    {"name": "North Richland Hills", "county": "Tarrant", "zip": "76180", "pop": "72,000", "note": "a large northeast Tarrant County suburb"},
    {"name": "Haltom City", "county": "Tarrant", "zip": "76117", "pop": "45,000", "note": "a working-class north Fort Worth suburb"},
    {"name": "Colleyville", "county": "Tarrant", "zip": "76034", "pop": "28,000", "note": "one of DFW's most affluent suburbs"},
    {"name": "Benbrook", "county": "Tarrant", "zip": "76126", "pop": "24,000", "note": "a southwest Fort Worth suburb on Benbrook Lake"},
    {"name": "White Settlement", "county": "Tarrant", "zip": "76108", "pop": "17,000", "note": "a west Fort Worth suburb"},
    # Collin County
    {"name": "Plano", "county": "Collin", "zip": "75023", "pop": "290,000", "note": "one of the largest and most prosperous DFW suburbs"},
    {"name": "McKinney", "county": "Collin", "zip": "75069", "pop": "200,000", "note": "one of the fastest-growing cities in America"},
    {"name": "Frisco", "county": "Collin", "zip": "75034", "pop": "220,000", "note": "consistently ranked among the best places to live in the US"},
    {"name": "Allen", "county": "Collin", "zip": "75002", "pop": "105,000", "note": "a thriving Collin County suburb"},
    {"name": "Wylie", "county": "Collin", "zip": "75098", "pop": "57,000", "note": "a fast-growing east Collin County city"},
    {"name": "Murphy", "county": "Collin", "zip": "75094", "pop": "22,000", "note": "a small but growing Collin County suburb"},
    {"name": "Prosper", "county": "Collin", "zip": "75078", "pop": "36,000", "note": "one of DFW's fastest-growing luxury suburbs"},
    {"name": "Celina", "county": "Collin", "zip": "75009", "pop": "25,000", "note": "a rapidly expanding north Collin County city"},
    {"name": "Anna", "county": "Collin", "zip": "75409", "pop": "18,000", "note": "a growing north Collin County community"},
    {"name": "Melissa", "county": "Collin", "zip": "75454", "pop": "16,000", "note": "a small but fast-growing Collin County city"},
    # Denton County
    {"name": "Denton", "county": "Denton", "zip": "76201", "pop": "148,000", "note": "home to two major universities and a vibrant arts scene"},
    {"name": "Lewisville", "county": "Denton", "zip": "75029", "pop": "115,000", "note": "a large and diverse Denton County suburb"},
    {"name": "Flower Mound", "county": "Denton", "zip": "75022", "pop": "80,000", "note": "a master-planned community and top-rated family suburb"},
    {"name": "Carrollton", "county": "Denton", "zip": "75006", "pop": "135,000", "note": "a large diverse city straddling Dallas and Denton counties"},
    {"name": "The Colony", "county": "Denton", "zip": "75056", "pop": "42,000", "note": "a lakeside Denton County suburb on Lewisville Lake"},
    {"name": "Highland Village", "county": "Denton", "zip": "75077", "pop": "16,000", "note": "an affluent lakeside community"},
    {"name": "Corinth", "county": "Denton", "zip": "76210", "pop": "22,000", "note": "a growing Denton County suburb"},
    {"name": "Little Elm", "county": "Denton", "zip": "75068", "pop": "55,000", "note": "a rapidly growing lakeside community"},
    {"name": "Aubrey", "county": "Denton", "zip": "76227", "pop": "10,000", "note": "a fast-growing small town north of Denton"},
    {"name": "Argyle", "county": "Denton", "zip": "76226", "pop": "7,000", "note": "a small upscale Denton County community"},
    # Rockwall County
    {"name": "Rockwall", "county": "Rockwall", "zip": "75087", "pop": "50,000", "note": "the county seat of the smallest county in Texas"},
    {"name": "Heath", "county": "Rockwall", "zip": "75032", "pop": "9,000", "note": "an upscale lakeside community on Lake Ray Hubbard"},
    {"name": "Fate", "county": "Rockwall", "zip": "75132", "pop": "18,000", "note": "one of the fastest-growing cities in Rockwall County"},
    {"name": "Royse City", "county": "Rockwall", "zip": "75189", "pop": "22,000", "note": "a fast-growing east DFW community"},
]

# ── SITUATIONS ────────────────────────────────────────────────────────────────
SITUATIONS = [
    {
        "slug": "foreclosure",
        "title": "Sell Your House Before Foreclosure in DFW",
        "h1": "Facing Foreclosure in <em>Dallas–Fort Worth?</em>",
        "badge": "Stop Foreclosure Fast",
        "desc": "If you've received a notice of default or a foreclosure sale date, you may have more options than you think. A fast cash sale can stop the process - and potentially let you walk away with money instead of losing everything to the bank.",
        "icon": "🏚️",
        "meta_title": "Sell House Before Foreclosure Dallas TX | Stop Foreclosure DFW | [COMPANY NAME]",
        "meta_desc": "Facing foreclosure in Dallas-Fort Worth? A fast cash sale can stop the process and help you walk away with cash. We close in 7 days. No fees. Serving all of DFW.",
        "faqs": [
            ("How quickly can you close to stop a foreclosure?", "In most cases we can close in 7-10 days, which is often fast enough to stop a scheduled foreclosure sale. As soon as you contact us we will assess your timeline and tell you exactly what's possible."),
            ("What if the foreclosure sale date is very close?", "Even if the sale date is days away, it's worth calling us immediately. Depending on the timeline there may still be options available including postponing the sale date while we close. Don't assume it's too late - call first."),
            ("Will selling stop the foreclosure from showing on my credit?", "If we close before the foreclosure completes, it generally does not appear as a foreclosure on your credit report. This can make a significant difference for your financial future compared to letting the foreclosure proceed."),
            ("What if I owe more than the house is worth?", "We can still potentially help through a short sale, where the lender agrees to accept less than what's owed. This requires lender cooperation but is often preferable for all parties compared to a full foreclosure."),
        ],
    },
    {
        "slug": "inherited-property",
        "title": "Sell an Inherited House Fast in DFW",
        "h1": "Inherited a House in <em>Dallas–Fort Worth?</em>",
        "badge": "Inherited Property Specialists",
        "desc": "Inheriting a property you didn't plan for - especially one that needs work, is going through probate, or is located far from where you live - can be overwhelming. We help heirs and estates find a clean, fast exit with no repairs and no hassle.",
        "icon": "⚖️",
        "meta_title": "Sell Inherited House Fast Dallas TX | Probate Property Buyers DFW | [COMPANY NAME]",
        "meta_desc": "Inherited a house in Dallas-Fort Worth? We buy inherited properties and probate homes as-is for cash. Fast closing, no repairs, no fees. Serving all of DFW.",
        "faqs": [
            ("Do I need to wait for probate to finish before selling?", "Not always. In Texas there are several ways to sell property during or after probate depending on the circumstances. We work with estates regularly and can help you understand what's possible for your specific situation."),
            ("The inherited house needs a lot of repairs - is that a problem?", "Not at all. We buy inherited properties in any condition - even those that have been vacant for years or need significant work. You don't spend a single dollar on repairs or cleanup."),
            ("There are multiple heirs - can you still buy?", "Yes. We regularly purchase properties with multiple heirs. All heirs will need to agree to the sale, and we work through the title company to ensure everyone is properly handled."),
            ("What if the property is still going through probate in Dallas County?", "We work with probate attorneys and can often close once the executor has authority to sell. We are patient and understand that the probate process has its own timeline."),
        ],
    },
    {
        "slug": "divorce",
        "title": "Sell Your House Fast During Divorce in DFW",
        "h1": "Selling a House During <em>Divorce</em> in DFW",
        "badge": "Divorce Property Solutions",
        "desc": "When a marriage ends, the family home is often the largest shared asset - and the hardest to deal with. A fast cash sale removes one of the biggest sources of conflict and lets both parties move forward with cash in hand.",
        "icon": "💔",
        "meta_title": "Sell House During Divorce Dallas TX | Fast Cash Home Sale DFW | [COMPANY NAME]",
        "meta_desc": "Selling a house during divorce in Dallas-Fort Worth? We make it simple - fair cash offer, fast closing, zero fees. Both parties get paid and move on. Serving all of DFW.",
        "faqs": [
            ("Do both spouses need to agree to sell?", "In Texas, both spouses generally need to agree to sell community property. We work with both parties and can coordinate with attorneys when needed to make the process as smooth as possible."),
            ("How quickly can we close?", "As fast as 7 days once both parties agree. We understand that speed matters when you're trying to finalize a divorce - every week the house sits is a week you're still financially connected."),
            ("What if my spouse is being uncooperative?", "We understand this is a difficult situation. If a divorce decree has been issued that gives one party the right to sell, we can often proceed on that basis. We work with your attorney to navigate the specifics."),
            ("Can you close after the divorce is finalized?", "Absolutely. We work on whatever timeline the legal process requires - before, during, or after finalization."),
        ],
    },
    {
        "slug": "tax-liens",
        "title": "Sell Your House With Back Taxes or Tax Liens in DFW",
        "h1": "Behind on Property Taxes in <em>Dallas–Fort Worth?</em>",
        "badge": "Tax Lien & Back Tax Specialists",
        "desc": "Delinquent property taxes in Texas can escalate fast - penalties and interest pile up, and the county can eventually seize the property. A cash sale can resolve everything at closing from the proceeds, without you paying a single dollar upfront.",
        "icon": "📋",
        "meta_title": "Sell House With Back Taxes Dallas TX | Tax Lien Property Buyers DFW | [COMPANY NAME]",
        "meta_desc": "Owe back property taxes in Dallas-Fort Worth? We buy houses with tax liens and delinquent taxes. Resolved at closing from proceeds. No upfront cost. Close in 7 days.",
        "faqs": [
            ("Do I have to pay the back taxes before you can buy?", "No. In most cases the delinquent taxes, penalties, and interest are paid directly from the sale proceeds at closing through the title company. You don't need to come up with money upfront."),
            ("How much time do I have before Dallas County takes my property?", "Texas law requires the county to wait until taxes are at least 2 years delinquent before starting a tax foreclosure lawsuit. However, penalties and interest accumulate quickly. The sooner you act, the more you preserve."),
            ("What if there are multiple years of back taxes?", "Multiple years of delinquent taxes is something we handle regularly. As long as there is enough equity in the property to cover the taxes and our offer, the sale can proceed normally."),
            ("Are there other liens besides taxes that you handle?", "Yes. Judgment liens, HOA liens, code violation liens, and mechanic's liens can all often be resolved at closing from proceeds. We work with experienced title companies who handle these situations routinely."),
        ],
    },
    {
        "slug": "repairs",
        "title": "Sell Your House As-Is Without Repairs in DFW",
        "h1": "House Needs Major Repairs? <em>We Buy As-Is.</em>",
        "badge": "Any Condition - No Repairs Needed",
        "desc": "Foundation problems, roof damage, fire damage, mold, or just decades of deferred maintenance - we buy houses in any condition anywhere in DFW. You don't spend a dollar on repairs and you don't have to lift a finger to clean it out.",
        "icon": "🔨",
        "meta_title": "Sell House As-Is Dallas TX | We Buy Houses Any Condition DFW | [COMPANY NAME]",
        "meta_desc": "Need to sell a house that needs major repairs in Dallas-Fort Worth? We buy homes in any condition - as-is, no repairs, no cleaning. Fair cash offer in 24 hours.",
        "faqs": [
            ("What kinds of damage or conditions do you buy?", "Foundation issues, roof problems, fire damage, water damage, mold, code violations, structural problems, outdated systems, hoarder situations - we've seen it all and buy regardless of condition."),
            ("Will the condition affect your offer?", "Yes, the condition factors into our offer because we account for the cost of repairs. But we are transparent about how we arrive at our number and you are never obligated to accept."),
            ("Do I need to remove belongings or trash?", "No. Leave anything you don't want. We handle all cleanout after closing. You can take what you want and walk away from the rest - no judgment, no hassle."),
            ("What about properties with code violations from the city?", "Code violations are common in properties we buy. They can often be resolved after closing or factored into our offer. They are rarely a dealbreaker."),
        ],
    },
    {
        "slug": "vacant-property",
        "title": "Sell a Vacant or Abandoned House Fast in DFW",
        "h1": "Vacant Property in <em>Dallas–Fort Worth?</em>",
        "badge": "Vacant & Abandoned Property Buyers",
        "desc": "A vacant property is a liability - it attracts vandalism, racks up maintenance costs, and can draw code violations from the city. Whether it's been empty for months or years, we can take it off your hands quickly in any condition.",
        "icon": "🔒",
        "meta_title": "Sell Vacant House Fast Dallas TX | Abandoned Property Buyers DFW | [COMPANY NAME]",
        "meta_desc": "Selling a vacant or abandoned house in Dallas-Fort Worth? We buy vacant properties in any condition for cash. Fast closing, no repairs, no fees. Serving all of DFW.",
        "faqs": [
            ("Does the property need to have utilities on?", "No. We buy properties with utilities off, disconnected, or never established. We do our own assessment of the property's condition."),
            ("The property has been broken into and vandalized - does that matter?", "We buy vandalized properties regularly. The condition factors into our offer but is never a reason we can't proceed."),
            ("What if there are squatters or unauthorized occupants?", "This is a situation we have experience with. Depending on the circumstances there are legal processes to handle this and we can guide you through what needs to happen."),
            ("I've been paying taxes on a vacant property for years - can I recover any of that?", "If there is equity in the property after taxes, liens, and our offer, you walk away with that equity at closing. A sale is often the fastest way to stop the bleeding on a vacant property you're maintaining."),
        ],
    },
]

# ── BLOG POSTS ────────────────────────────────────────────────────────────────
BLOG_POSTS = [
    {
        "slug": "how-to-stop-foreclosure-dallas-tx",
        "title": "How to Stop Foreclosure in Dallas TX - Your Options Explained",
        "meta_desc": "Facing foreclosure in Dallas TX? Here are your real options - from loan modification to a fast cash sale - and how to decide which is right for your situation.",
        "category": "Foreclosure",
        "read_time": "6 min read",
        "intro": "Receiving a foreclosure notice in Texas can feel like the floor dropping out from under you. But foreclosure is a process - not an instant event - and there is almost always more time and more options than homeowners realize.",
        "sections": [
            ("Understanding the Texas Foreclosure Timeline", "Texas is a non-judicial foreclosure state, which means lenders can foreclose without going through the court system. Once you miss payments, your lender must send a Notice of Default and give you 20 days to cure the default. If you don't, they can send a Notice of Sale, which gives you at least 21 additional days before the foreclosure auction.\n\nIn Texas, foreclosure sales happen on the first Tuesday of every month at the county courthouse. Dallas County auctions are held at the George Allen Courts Building. This means the entire process from first missed payment to auction can happen in as little as 60-90 days, though it often takes longer."),
            ("Option 1: Loan Modification", "Contact your lender's loss mitigation department as soon as possible. Lenders often prefer to modify a loan rather than foreclose - foreclosure is expensive for them too. A modification might reduce your interest rate, extend your loan term, or add the missed payments to the end of your loan. This works best if your financial hardship is temporary and you can afford modified payments going forward."),
            ("Option 2: Forbearance Agreement", "A forbearance temporarily reduces or pauses your payments. You'll still owe the missed payments eventually, but it can buy you time if you're facing a short-term hardship like job loss or medical bills. Call your lender's loss mitigation department directly - not the general customer service line."),
            ("Option 3: Sell the House Before the Auction", "If you have equity in your home - meaning it's worth more than what you owe - selling before the foreclosure auction is often your best financial outcome. You keep the equity instead of losing it to the bank. A traditional listing takes 60-90 days, which may be too slow. A cash sale to a direct buyer can close in 7-14 days, which is often fast enough to stop the auction."),
            ("Option 4: Short Sale", "If you owe more than the house is worth, a short sale allows you to sell for less than the mortgage balance with lender approval. It's better for your credit than a full foreclosure and can eliminate the deficiency judgment in some cases. This requires lender cooperation and takes longer than a regular sale."),
            ("Option 5: Bankruptcy", "Filing for Chapter 13 bankruptcy triggers an automatic stay that immediately halts all foreclosure proceedings. It's a serious step that affects your credit for 7-10 years, but it can give you time to reorganize your finances and catch up on missed payments. Speak with a bankruptcy attorney before pursuing this option."),
            ("The Bottom Line", "The worst thing you can do when facing foreclosure is nothing. Every week you wait narrows your options. If you have equity in the property, a fast cash sale is usually the cleanest and most financially beneficial exit. If you'd like to know what your home is worth in cash and how quickly we could close, reach out - there's no obligation and the conversation costs you nothing."),
        ],
    },
    {
        "slug": "selling-inherited-house-texas-probate",
        "title": "How to Sell an Inherited House in Texas - Probate, Title, and Your Options",
        "meta_desc": "Inherited a house in Texas? This guide explains the probate process, how title transfer works, and the fastest ways to sell - including as-is cash sales.",
        "category": "Inherited Property",
        "read_time": "7 min read",
        "intro": "Inheriting a house in Texas can be both a gift and a burden. Whether the property is paid off or still has a mortgage, whether it's in great shape or needs major work, the path to selling it runs through Texas probate law - and understanding the process makes everything easier.",
        "sections": [
            ("Does the Estate Have to Go Through Probate?", "In Texas, whether probate is required depends on how the property was held. If the deceased had a will, Texas has a relatively simple probate process. If there was no will (intestate), the court determines heirs under Texas intestacy law.\n\nTexas also has two simplified options that avoid full probate: a Muniment of Title (for estates with a valid will and no debts other than the mortgage) and a Small Estate Affidavit (for estates under $75,000 excluding the homestead). An estate attorney can tell you which applies to your situation."),
            ("How Long Does Texas Probate Take?", "A standard Texas probate takes 6-9 months for a straightforward estate. More complex estates - multiple heirs, disputes, title issues - can take 12-24 months or longer. During this time, the executor has authority to manage the property but may need court approval to sell it depending on the will's terms."),
            ("Who Has Authority to Sell the Property?", "The executor named in the will (or administrator appointed by the court in an intestate estate) has legal authority to sell estate property. If there are multiple heirs, all heirs generally must agree to a sale unless the executor has independent administration authority under the will."),
            ("Selling During Probate vs. After", "You don't always have to wait for probate to complete before selling. If the executor has independent administration authority, the sale can proceed during probate. Closing will require the title company to verify the executor's authority and the estate's clear title. Cash buyers are often more flexible on timeline than buyers using bank financing."),
            ("What About the Mortgage?", "If the inherited property still has a mortgage, it becomes a debt of the estate. In most cases the estate must continue making payments or sell the property to pay off the loan. An inherited property that is behind on mortgage payments or heading toward foreclosure needs to be dealt with quickly."),
            ("The Fastest Way to Sell an Inherited Property", "If you want to sell quickly - especially if the property needs repairs, has title complications, or is going through probate - a cash sale to a direct buyer is usually the fastest and simplest route. There are no bank appraisals, no repair contingencies, and no financing fall-throughs. The buyer works around the estate's timeline. If you're dealing with an inherited property in the DFW area, we buy estates and probate properties regularly and can work at whatever pace the process requires."),
        ],
    },
    {
        "slug": "we-buy-houses-dfw-how-it-works",
        "title": "How 'We Buy Houses' Companies Actually Work in DFW - The Honest Truth",
        "meta_desc": "Wondering how cash home buyers in DFW actually work? This honest guide explains the process, how offers are calculated, and what to watch out for.",
        "category": "How It Works",
        "read_time": "5 min read",
        "intro": "If you've seen 'We Buy Houses' signs on telephone poles or received a postcard from a cash buyer, you probably have questions. How does the process work? How are offers calculated? Is it legitimate? Here's the straight answer.",
        "sections": [
            ("What Is a Cash Home Buyer?", "A cash home buyer - sometimes called a real estate investor or wholesaler - is someone who purchases houses directly from homeowners without using bank financing. Because there's no lender involved, the process is much faster and has far fewer conditions than a traditional sale.\n\nIn the DFW market there are individual investors, small local companies, and large national 'iBuyer' platforms like Opendoor and Offerpad. The local operators typically offer more flexibility and personal service than the national platforms."),
            ("How Are Cash Offers Calculated?", "Cash buyers use a formula that starts with the After Repair Value (ARV) - what the house would sell for on the open market in fully repaired condition. From that number they subtract the estimated repair costs and their profit margin.\n\nA typical formula looks like: Offer = (ARV × 70-75%) minus repair costs. This means a house with a $300,000 ARV and $40,000 in repairs might receive an offer around $185,000. The offer reflects the buyer's risk and the cost of repairs, not a reflection of the homeowner's situation."),
            ("What Happens After You Accept?", "Once you accept an offer, both parties sign a purchase agreement. A licensed title company opens the transaction, verifies title, and handles all the paperwork. There's no home inspection contingency that can kill the deal. No appraisal. No bank underwriting. The title company closes the transaction and wires or hands you a check. The whole process typically takes 7-30 days."),
            ("Is It Legitimate?", "Yes - cash home buying is a legitimate, legal transaction that closes through a licensed title company the same way any real estate sale does. Reputable buyers will never ask you to sign over your deed directly to them or transfer title outside of a title company. That's a red flag. Every legitimate cash sale closes through a neutral third-party title company."),
            ("When Does It Make Sense?", "A cash sale makes financial sense when: the property needs significant repairs you can't afford; you're facing a time-sensitive situation like foreclosure; you're dealing with a difficult title situation; you need to close quickly due to relocation or divorce; or the property is vacant and costing you money every month. For properties in great condition with no time pressure, a traditional listing often nets more money. A good cash buyer will tell you honestly which option makes more sense for your situation."),
        ],
    },
    {
        "slug": "sell-house-during-divorce-texas",
        "title": "Selling a House During Divorce in Texas - What You Need to Know",
        "meta_desc": "Selling a house during a Texas divorce involves community property laws, timing, and both spouses' agreement. Here's what you need to know and your options.",
        "category": "Divorce",
        "read_time": "5 min read",
        "intro": "The family home is often the largest and most emotionally charged asset in a Texas divorce. Understanding how Texas law treats marital property - and knowing your options for selling - can reduce conflict and help both parties move forward faster.",
        "sections": [
            ("Texas Community Property Law", "Texas is a community property state, which means any property acquired during the marriage is generally owned equally by both spouses. The family home - unless it was owned before marriage or received as a gift or inheritance - is typically community property that both spouses must agree to sell."),
            ("Do Both Spouses Have to Sign?", "In Texas, both spouses must sign the deed to transfer title on community property. This means both parties must agree to sell and agree on the terms. If one spouse refuses to cooperate, the other may need to seek a court order through the divorce proceedings - a process that can add significant time and legal fees."),
            ("Selling Before vs. After Divorce is Finalized", "You can sell the home before the divorce is finalized, during the proceedings, or after. Selling during the proceedings can simplify the final property division since there's cash to divide rather than a shared asset to argue over. Selling after finalization is also common, particularly if the divorce decree specifies how the proceeds are to be divided."),
            ("The Practical Case for a Fast Cash Sale", "A traditional listing requires both spouses to cooperate on showings, price reductions, and negotiations - which can be extremely difficult during an adversarial divorce. A cash sale simplifies everything: one offer, one closing, proceeds split per the divorce agreement. It's often the cleanest way to sever the financial connection to the property and let both parties move on."),
            ("What Happens to the Mortgage?", "Until the house is sold or refinanced into one spouse's name, both parties remain liable for the mortgage. If payments are being missed during the divorce proceedings, the credit damage affects both spouses and a foreclosure could result. A fast sale resolves this exposure immediately."),
        ],
    },
    {
        "slug": "property-taxes-delinquent-dallas-county",
        "title": "Behind on Property Taxes in Dallas County? Here's What Happens Next",
        "meta_desc": "Delinquent property taxes in Dallas County escalate fast. Here's the timeline, the penalties, and your options - including a fast cash sale that resolves everything at closing.",
        "category": "Tax Liens",
        "read_time": "5 min read",
        "intro": "If you've fallen behind on property taxes in Dallas County, you're not alone - and you're not without options. But time matters. Here's exactly what happens when Texas property taxes go unpaid and what you can do about it.",
        "sections": [
            ("The Dallas County Tax Delinquency Timeline", "January 31: Taxes are due. February 1: Taxes become delinquent. A 6% penalty plus 1% interest is added immediately. July 1: An additional 20% attorney collection fee is added, bringing the total penalty to roughly 27-47% of the original bill depending on timing. The penalties continue to compound each month taxes remain unpaid."),
            ("When Can Dallas County Seize Your Property?", "Texas law allows the taxing authority to file a tax lien lawsuit after taxes have been delinquent for at least 180 days. In practice, Dallas County typically waits 1-2 years before filing suit. Once a judgment is obtained, the property can be sold at a tax foreclosure auction. This process can take 2-4 years total, but the penalties accumulate throughout."),
            ("Your Options When Taxes Are Delinquent", "You have several options: pay the taxes in full and eliminate the lien; set up a payment plan with the Dallas County Tax Office (available to some homeowners); apply for a deferral if you are 65+ or disabled; sell the property and pay the taxes at closing from the proceeds."),
            ("How a Cash Sale Resolves Delinquent Taxes", "When you sell the property, the title company calculates the total amount owed - including all penalties, interest, and attorney fees - and pays it directly from the sale proceeds at closing. You don't pay anything upfront. Whatever is left after taxes, any mortgage balance, and the purchase price is your cash at closing."),
            ("What If the Taxes Are More Than the Property Is Worth?", "This is rare but possible, particularly on properties that have declined in value or been neglected. In this situation, options are more limited. A short sale or negotiation with the tax authority may be possible. An attorney who specializes in Texas tax law can advise on the specific options available."),
        ],
    },
]

# ── TEMPLATE FUNCTIONS ─────────────────────────────────────────────────────────

NAV = """<nav class="nav" role="navigation">
  <div class="wrap">
    <div class="nav-in">
      <a href="../index.html" class="logo">[Company<span>Name</span>]</a>
      <div class="nav-r">
        <a href="../index.html#how-it-works" class="nav-lk">How It Works</a>
        <a href="../index.html#situations" class="nav-lk">Situations</a>
        <a href="../index.html#areas" class="nav-lk">Areas</a>
        <a href="../index.html#faq" class="nav-lk">FAQ</a>
        <a href="tel:[YOUR-PHONE-NUMBER]" class="nav-btn">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" style="width:14px;height:14px"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg>
          Call Now - Free
        </a>
      </div>
    </div>
  </div>
</nav>"""

TBAR = """<div class="tbar">
  <div class="wrap"><div class="tbar-in">
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Cash Offer in 24 Hours</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Close in 7 Days</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Zero Fees or Commissions</div>
    <div class="ti"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>Any Condition - As-Is</div>
  </div></div>
</div>"""

MINI_FORM = """<div class="mini-form-wrap">
  <div class="mf-title">Get a Free Cash Offer</div>
  <div class="mf-sub">No obligation. Usually same-day response.</div>
  <form onsubmit="handleSubmit(event)" novalidate>
    <div class="mfg"><input type="text" placeholder="Your Name" required /></div>
    <div class="mfg"><input type="tel" id="mfph" placeholder="(214) 555-0000" required /></div>
    <div class="mfg"><input type="text" placeholder="Property Address" required /></div>
    <div class="mfg">
      <select required>
        <option value="" disabled selected>Your situation</option>
        <option>Facing Foreclosure</option>
        <option>Behind on Property Taxes</option>
        <option>Inherited Property</option>
        <option>Going Through Divorce</option>
        <option>Needs Major Repairs</option>
        <option>Tired Landlord</option>
        <option>Relocating</option>
        <option>Vacant Property</option>
        <option>Other</option>
      </select>
    </div>
    <button type="submit" class="mf-btn">Get My Free Cash Offer →</button>
  </form>
  <div id="mf-success" style="display:none;text-align:center;padding:20px 0">
    <div style="font-size:2rem;margin-bottom:8px">✅</div>
    <p style="color:rgba(246,241,233,.7);font-size:.85rem">Got it! We'll be in touch within hours.</p>
  </div>
</div>"""

FOOTER_CTA = """<section class="fcta">
  <div class="wrap fcta-in">
    <h2>Ready to Get Your <em>Free Cash Offer?</em></h2>
    <p>No obligation, no pressure, no cost. The worst outcome is you have more information than you do right now.</p>
    <div class="fcta-btns">
      <a href="../index.html#get-offer" class="btn-g">Get My Free Cash Offer</a>
      <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-ink">Call [YOUR-PHONE-NUMBER]</a>
    </div>
  </div>
</section>"""

FOOTER = """<footer class="footer">
  <div class="wrap"><div class="footer-in">
    <div class="flogo">[Company<span>Name</span>]</div>
    <p class="fcopy">© 2025 [Company Name] · Serving Dallas-Fort Worth, TX</p>
    <div class="flinks">
      <a href="../index.html">Home</a>
      <a href="../index.html#faq">FAQ</a>
      <a href="../index.html#get-offer">Get Offer</a>
    </div>
  </div></div>
</footer>"""

MOBILE_CTA = """<div class="mcta">
  <a href="tel:[YOUR-PHONE-NUMBER]" class="mc">📞 Call Now</a>
  <a href="../index.html#get-offer" class="mf">Get Cash Offer</a>
</div>"""

JS = """<script>
  function handleSubmit(e){
    e.preventDefault();
    e.target.style.display='none';
    document.getElementById('mf-success').style.display='block';
  }
  function toggleFaq(btn){
    const a=btn.nextElementSibling,open=btn.getAttribute('aria-expanded')==='true';
    document.querySelectorAll('.faq-q').forEach(b=>{b.setAttribute('aria-expanded','false');b.nextElementSibling.classList.remove('open')});
    if(!open){btn.setAttribute('aria-expanded','true');a.classList.add('open')}
  }
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target)}})
  },{threshold:.1,rootMargin:'0px 0px -30px 0px'});
  document.querySelectorAll('.rv').forEach(el=>obs.observe(el));
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click',e=>{const t=document.querySelector(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'})}})
  });
  const ph=document.getElementById('mfph');
  if(ph){ph.addEventListener('input',function(){let v=this.value.replace(/\D/g,'');if(v.length>=6)v='('+v.substring(0,3)+') '+v.substring(3,6)+'-'+v.substring(6,10);else if(v.length>=3)v='('+v.substring(0,3)+') '+v.substring(3);this.value=v})}
</script>"""

CHECK_ICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" style="width:16px;height:16px;color:#3d5c3a;flex-shrink:0"><path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/></svg>'


def city_slug(name):
    return name.lower().replace(" ", "-").replace("'", "")


def other_cities_html(current_name):
    links = []
    for c in CITIES:
        if c["name"] != current_name:
            links.append(f'<a href="sell-house-fast-{city_slug(c["name"])}.html" class="city-lnk">Sell House Fast {c["name"]}</a>')
    return "\n".join(links)


def situation_links_html():
    links = []
    for s in SITUATIONS:
        links.append(f'<a href="../situation/{s["slug"]}.html" class="city-lnk">{s["title"]}</a>')
    return "\n".join(links)


# ── GENERATE CITY PAGES ────────────────────────────────────────────────────────
def generate_city_page(city):
    name = city["name"]
    county = city["county"]
    slug = city["slug"] if "slug" in city else city_slug(name)
    pop = city["pop"]
    note = city["note"]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sell My House Fast {name} TX | Cash Home Buyers {name} | [COMPANY NAME]</title>
  <meta name="description" content="Sell your house fast for cash in {name}, TX. Fair cash offer in 24 hours. No repairs, no fees, no agents. Close in 7 days. Any situation - foreclosure, divorce, inherited, tax issues. Serving {name} and all of {county} County." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.yourwebsite.com/city/sell-house-fast-{slug}.html" />
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"RealEstateAgent","name":"[COMPANY NAME]","description":"We buy houses fast for cash in {name}, TX. Fair cash offer in 24 hours, close in 7 days, no repairs, no fees.","url":"https://www.yourwebsite.com/city/sell-house-fast-{slug}.html","telephone":"[YOUR-PHONE-NUMBER]","areaServed":"{name}, TX","address":{{"@type":"PostalAddress","addressLocality":"{name}","addressRegion":"TX","addressCountry":"US"}}}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
</head>
<body>

{NAV}

<main>
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-in">
      <div>
        <div class="breadcrumb">
          <a href="../index.html">Home</a><span>›</span>
          <a href="../index.html#areas">Cities</a><span>›</span>
          <span>{name}, TX</span>
        </div>
        <div class="hero-badge"><span class="badge-dot"></span>{county} County · {name}, TX</div>
        <h1 class="page-h1">Sell Your House Fast in <em>{name}, TX</em></h1>
        <p class="page-desc">
          We buy houses fast for cash in {name} - {note} with a population of {pop}.
          Fair cash offer within 24 hours, close in as little as 7 days. No repairs needed, no agent fees, no commissions.
          Any situation, any condition.
        </p>
        <div class="hero-acts">
          <a href="../index.html#get-offer" class="btn-g">Get My Free Cash Offer</a>
          <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-dk">Call [YOUR-PHONE-NUMBER]</a>
        </div>
      </div>
      {MINI_FORM}
    </div>
  </div>
</section>

{TBAR}

<!-- WHY US IN {name.upper()} -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv">Why {name} Homeowners Choose Us</p>
    <h2 class="sh2 rv">The Fastest Way to Sell Your {name} House</h2>
    <p class="ssub rv">Selling a house in {name} the traditional way takes 60-90+ days, costs 5-6% in commissions, and requires repairs and showings. Here's what's different when you sell to us.</p>
    <div class="steps">
      <div class="step rv">
        <div class="snum">01</div>
        <h3>Tell Us About Your Property</h3>
        <p>Fill out the short form or call us directly. Tell us your situation and your address. No judgment, no pressure - just a conversation about your options.</p>
      </div>
      <div class="step rv">
        <div class="snum">02</div>
        <h3>We Visit Your {name} Property</h3>
        <p>We schedule a quick walkthrough at your convenience. No cleaning, no repairs. We assess the property as-is and provide a fair written cash offer on the spot.</p>
      </div>
      <div class="step rv">
        <div class="snum">03</div>
        <h3>Close on Your Timeline</h3>
        <p>If the offer works for you, we close through a licensed Texas title company on your schedule - as fast as 7 days. You receive cash at closing. No surprises.</p>
      </div>
    </div>
  </div>
</section>

<!-- SITUATIONS -->
<section class="sec sec-dk">
  <div class="wrap">
    <p class="slbl rv">We Help {name} Homeowners In Every Situation</p>
    <h2 class="sh2 lt rv">Whatever Your Situation -<br>We Have a Solution</h2>
    <p class="ssub lt rv">We've helped {name} homeowners navigate some of the most difficult real estate situations imaginable. Here's what we deal with every day.</p>
    <div class="benefits">
      <div class="benefit rv"><span class="ben-ico">🏚️</span><h3>Facing Foreclosure</h3><p>A fast cash sale can stop foreclosure before it completes and help you walk away with cash instead of losing everything.</p></div>
      <div class="benefit rv"><span class="ben-ico">📋</span><h3>Behind on Property Taxes</h3><p>Back taxes owed to {county} County can be resolved directly from sale proceeds at closing. No upfront cost.</p></div>
      <div class="benefit rv"><span class="ben-ico">⚖️</span><h3>Inherited Property</h3><p>We buy inherited and probate properties in {name} in any condition and work at whatever pace the estate requires.</p></div>
      <div class="benefit rv"><span class="ben-ico">💔</span><h3>Going Through Divorce</h3><p>A fast clean sale removes the biggest shared asset and lets both parties move forward with cash instead of conflict.</p></div>
      <div class="benefit rv"><span class="ben-ico">🔨</span><h3>Needs Major Repairs</h3><p>Foundation problems, roof damage, fire or water damage - we buy {name} properties in any condition, as-is.</p></div>
      <div class="benefit rv"><span class="ben-ico">🏠</span><h3>Tired Landlord</h3><p>Done being a landlord in {name}? We buy rental properties occupied or vacant and let you step away for good.</p></div>
    </div>
  </div>
</section>

<!-- ABOUT {name.upper()} -->
<section class="sec sec-alt">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start">
      <div class="rv">
        <p class="slbl">About {name}, TX</p>
        <h2 class="sh2">We Know the {name} Market</h2>
        <div class="prose">
          <p>{name} is {note} in {county} County, Texas, with a population of approximately {pop}. The {name} real estate market has seen significant changes in recent years, with property values shifting alongside broader DFW trends.</p>
          <p>We are local - we know {county} County property values, the local title companies, and the specific challenges that come with selling a house in this market. When you work with us you're working with someone who understands the neighborhood, not a national call center.</p>
          <p>We've helped homeowners throughout {name} in foreclosure, probate, divorce, and dozens of other situations. We understand what {name} properties are worth and make offers that reflect local market reality.</p>
        </div>
      </div>
      <div class="rv">
        <p class="slbl">What You Get</p>
        <h2 class="sh2">Your Benefits</h2>
        <div style="display:flex;flex-direction:column;gap:14px;margin-top:8px">
          {"".join(f'<div style="display:flex;align-items:center;gap:10px;font-size:.9rem;font-weight:500">{CHECK_ICON}{item}</div>' for item in [
            "Cash offer within 24 hours of seeing the property",
            "Close in as little as 7 days - or on your schedule",
            "Zero agent commissions - save 5-6%",
            "We cover all closing costs",
            "No repairs or cleaning required",
            "No open houses or strangers in your home",
            "Guaranteed sale - no financing fall-through",
            "Licensed title company handles everything",
          ])}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv" style="text-align:center">Common Questions</p>
    <h2 class="sh2 rv" style="text-align:center;margin-bottom:8px">Questions About Selling Your {name} House</h2>
    <p class="ssub rv" style="text-align:center;margin:0 auto 40px">Straight answers about how this works in {name}.</p>
    <div class="faq-list rv">
      <div class="faq-item"><button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">How fast can you buy my house in {name}?<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg></button><div class="faq-a">We can close in as little as 7 days in {name}. In most cases we provide a cash offer within 24 hours of seeing your property. We work around your timeline completely.</div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">Do I need to make repairs before selling in {name}?<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg></button><div class="faq-a">No repairs, no cleaning, no staging. We buy {name} houses completely as-is. Leave whatever you don't want - we handle everything after closing.</div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">Are there any fees or commissions?<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg></button><div class="faq-a">Zero. No commissions, no fees, no closing costs on your end. The offer we make is exactly what you receive at closing.</div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">Do you buy houses anywhere in {county} County?<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg></button><div class="faq-a">Yes - we serve all of {county} County and the entire DFW metroplex. Any city, any neighborhood.</div></div>
    </div>
  </div>
</section>

<!-- OTHER CITIES -->
<section class="sec sec-alt">
  <div class="wrap">
    <p class="slbl rv">Other DFW Cities We Serve</p>
    <h2 class="sh2 rv">We Buy Houses Across All of DFW</h2>
    <p class="ssub rv" style="margin-bottom:32px">We serve the entire Dallas-Fort Worth Metroplex. Click any city to learn more.</p>
    <div class="city-grid rv">
      {other_cities_html(name)}
    </div>
  </div>
</section>

{FOOTER_CTA}
</main>

{FOOTER}
{MOBILE_CTA}
{JS}
</body>
</html>"""
    return html


# ── GENERATE SITUATION PAGES ───────────────────────────────────────────────────
def generate_situation_page(sit):
    slug = sit["slug"]
    title = sit["title"]
    h1 = sit["h1"]
    badge = sit["badge"]
    desc = sit["desc"]
    meta_title = sit["meta_title"]
    meta_desc = sit["meta_desc"]
    faqs = sit["faqs"]

    faq_html = ""
    for q, a in faqs:
        faq_html += f"""      <div class="faq-item"><button class="faq-q" aria-expanded="false" onclick="toggleFaq(this)">{q}<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 3a.75.75 0 01.75.75v10.638l3.96-4.158a.75.75 0 111.08 1.04l-5.25 5.5a.75.75 0 01-1.08 0l-5.25-5.5a.75.75 0 111.08-1.04l3.96 4.158V3.75A.75.75 0 0110 3z" clip-rule="evenodd"/></svg></button><div class="faq-a">{a}</div></div>\n"""

    # Nav/footer need one less ../ since situation pages are one level deep
    nav_sit = NAV.replace('href="../index.html"', 'href="../index.html"')
    footer_cta_sit = FOOTER_CTA
    footer_sit = FOOTER
    mobile_cta_sit = MOBILE_CTA

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.yourwebsite.com/situation/{slug}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
</head>
<body>

{nav_sit}

<main>
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-in">
      <div>
        <div class="breadcrumb">
          <a href="../index.html">Home</a><span>›</span>
          <span>{title}</span>
        </div>
        <div class="hero-badge"><span class="badge-dot"></span>{badge}</div>
        <h1 class="page-h1">{h1}</h1>
        <p class="page-desc">{desc}</p>
        <div class="hero-acts">
          <a href="../index.html#get-offer" class="btn-g">Get My Free Cash Offer</a>
          <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-dk">Call [YOUR-PHONE-NUMBER]</a>
        </div>
      </div>
      {MINI_FORM}
    </div>
  </div>
</section>

{TBAR}

<!-- HOW IT WORKS -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv">Simple Process</p>
    <h2 class="sh2 rv">How It Works</h2>
    <p class="ssub rv">Three straightforward steps from where you are right now to cash in your hand.</p>
    <div class="steps">
      <div class="step rv"><div class="snum">01</div><h3>Tell Us Your Situation</h3><p>Call us or fill out the form. Tell us about your property and what you're dealing with. There is no judgment here - just a straight conversation about your options.</p></div>
      <div class="step rv"><div class="snum">02</div><h3>We See the Property</h3><p>We schedule a quick visit at your convenience. No cleaning, no repairs. We assess the property as-is and make a fair written cash offer on the spot.</p></div>
      <div class="step rv"><div class="snum">03</div><h3>Close and Get Paid</h3><p>If the offer works, we close through a licensed Texas title company on your schedule. As fast as 7 days. You receive cash at closing. Done.</p></div>
    </div>
  </div>
</section>

<!-- WHY FAST SALE -->
<section class="sec sec-dk">
  <div class="wrap">
    <p class="slbl rv">Why a Cash Sale Makes Sense</p>
    <h2 class="sh2 lt rv">What You Get When You<br>Sell to Us</h2>
    <p class="ssub lt rv">Here's exactly what's different about selling to a cash buyer compared to listing on the market.</p>
    <div class="benefits">
      <div class="benefit rv"><span class="ben-ico">⚡</span><h3>Speed</h3><p>Close in 7 days instead of 60-90+ days. When you're in a difficult situation, speed is often the most valuable thing we can offer.</p></div>
      <div class="benefit rv"><span class="ben-ico">💰</span><h3>No Fees or Commissions</h3><p>Zero agent commissions, zero closing costs, zero transaction fees. The offer is what you walk away with.</p></div>
      <div class="benefit rv"><span class="ben-ico">🔨</span><h3>Any Condition</h3><p>No repairs, no cleaning, no staging. We buy the property exactly as it sits today.</p></div>
      <div class="benefit rv"><span class="ben-ico">🔒</span><h3>Guaranteed Sale</h3><p>No financing contingencies that can fall through. When we make an offer and you accept, it closes.</p></div>
      <div class="benefit rv"><span class="ben-ico">📅</span><h3>Your Timeline</h3><p>7 days or 90 days - we close when you're ready. You control the schedule completely.</p></div>
      <div class="benefit rv"><span class="ben-ico">🤝</span><h3>Licensed Title Company</h3><p>Every transaction closes through a licensed Texas title company for full legal protection.</p></div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="sec">
  <div class="wrap">
    <p class="slbl rv" style="text-align:center">Common Questions</p>
    <h2 class="sh2 rv" style="text-align:center;margin-bottom:8px">Frequently Asked Questions</h2>
    <p class="ssub rv" style="text-align:center;margin:0 auto 40px">Straight answers about your specific situation.</p>
    <div class="faq-list rv">
{faq_html}
    </div>
  </div>
</section>

<!-- OTHER SITUATIONS -->
<section class="sec sec-alt">
  <div class="wrap">
    <p class="slbl rv">Other Situations We Handle</p>
    <h2 class="sh2 rv">Every Situation Welcome</h2>
    <p class="ssub rv" style="margin-bottom:32px">We help DFW homeowners through all kinds of difficult real estate situations.</p>
    <div class="sit-grid rv">
      {"".join(f'<div class="sit-card"><div class="sit-card-ico">{s["icon"]}</div><div><h3>{s["title"]}</h3><p>{s["desc"][:120]}...</p><a href="{s["slug"]}.html">Learn more →</a></div></div>' for s in SITUATIONS if s["slug"] != slug)}
    </div>
  </div>
</section>

{footer_cta_sit}
</main>

{footer_sit}
{mobile_cta_sit}
{JS}
</body>
</html>"""
    return html


# ── GENERATE BLOG PAGES ────────────────────────────────────────────────────────
def generate_blog_page(post):
    slug = post["slug"]
    title = post["title"]
    meta_desc = post["meta_desc"]
    category = post["category"]
    read_time = post["read_time"]
    intro = post["intro"]
    sections = post["sections"]

    sections_html = ""
    for heading, body in sections:
        paragraphs = "".join(f"<p>{p.strip()}</p>" for p in body.split("\n\n") if p.strip())
        sections_html += f"<h2>{heading}</h2>{paragraphs}\n"

    nav_blog = NAV.replace('href="../index.html"', 'href="../../index.html"').replace('href="../style.css"', 'href="../../style.css"')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | [COMPANY NAME]</title>
  <meta name="description" content="{meta_desc}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.yourwebsite.com/blog/{slug}.html" />
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{meta_desc}","author":{{"@type":"Organization","name":"[COMPANY NAME]"}},"publisher":{{"@type":"Organization","name":"[COMPANY NAME]"}}}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../style.css" />
</head>
<body>

<nav class="nav" role="navigation">
  <div class="wrap">
    <div class="nav-in">
      <a href="../../index.html" class="logo">[Company<span>Name</span>]</a>
      <div class="nav-r">
        <a href="../../index.html#how-it-works" class="nav-lk">How It Works</a>
        <a href="../../index.html#situations" class="nav-lk">Situations</a>
        <a href="../../index.html#areas" class="nav-lk">Areas</a>
        <a href="../../index.html#faq" class="nav-lk">FAQ</a>
        <a href="tel:[YOUR-PHONE-NUMBER]" class="nav-btn">Call Now - Free</a>
      </div>
    </div>
  </div>
</nav>

<main>
<section class="page-hero" style="padding:100px 0 60px">
  <div class="wrap">
    <div class="breadcrumb">
      <a href="../../index.html">Home</a><span>›</span>
      <a href="index.html">Blog</a><span>›</span>
      <span>{category}</span>
    </div>
    <div style="display:inline-flex;align-items:center;gap:10px;margin:16px 0">
      <span style="background:rgba(200,146,42,.15);border:1px solid rgba(200,146,42,.4);color:#e8b84b;padding:4px 12px;border-radius:100px;font-size:.72rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase">{category}</span>
      <span style="color:rgba(246,241,233,.35);font-size:.8rem">{read_time}</span>
    </div>
    <h1 class="page-h1" style="font-size:clamp(1.8rem,3vw,3rem)">{title}</h1>
    <p class="page-desc">{intro}</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 340px;gap:60px;align-items:start">
      <article class="prose rv">
        {sections_html}
        <div style="margin-top:40px;padding:28px;background:var(--gold-pale);border:1px solid var(--gold);border-radius:12px">
          <strong style="font-family:var(--fh);font-size:1.1rem;display:block;margin-bottom:8px">Need to Sell Your DFW House Fast?</strong>
          <p style="color:var(--muted);margin-bottom:16px">We help DFW homeowners find a way out of difficult situations. Fair cash offer in 24 hours, close in 7 days, zero fees.</p>
          <a href="../../index.html#get-offer" class="btn-ink" style="font-size:.88rem;padding:12px 24px">Get My Free Cash Offer →</a>
        </div>
      </article>
      <aside style="position:sticky;top:80px" class="rv">
        <div style="background:var(--ink);border-radius:12px;padding:28px;margin-bottom:20px">
          <p style="font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:10px">Free - No Obligation</p>
          <h3 style="font-family:var(--fh);color:var(--cream);font-size:1.2rem;margin-bottom:8px">Get a Cash Offer Today</h3>
          <p style="font-size:.82rem;color:rgba(246,241,233,.45);margin-bottom:18px">Any DFW city. Any condition. Any situation.</p>
          <a href="../../index.html#get-offer" class="btn-g" style="width:100%;justify-content:center;font-size:.9rem;padding:13px">Get My Free Cash Offer</a>
          <a href="tel:[YOUR-PHONE-NUMBER]" style="display:block;text-align:center;margin-top:12px;font-size:.8rem;color:rgba(246,241,233,.4);font-weight:500">[YOUR-PHONE-NUMBER]</a>
        </div>
        <div>
          <p style="font-size:.76rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:12px">Related Situations</p>
          {"".join(f'<a href="../situation/{s["slug"]}.html" style="display:flex;align-items:center;gap:8px;padding:10px 0;border-bottom:1px solid var(--border);font-size:.85rem;font-weight:500;color:var(--ink);transition:color .2s" onmouseover="this.style.color=\'#c8922a\'" onmouseout="this.style.color=\'#0d0c0a\'">{s["icon"]} {s["title"]}</a>' for s in SITUATIONS)}
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="fcta">
  <div class="wrap fcta-in">
    <h2>Ready to Get Your <em>Free Cash Offer?</em></h2>
    <p>No obligation, no pressure, no cost. The worst outcome is you have more information than you do right now.</p>
    <div class="fcta-btns">
      <a href="../../index.html#get-offer" class="btn-g">Get My Free Cash Offer</a>
      <a href="tel:[YOUR-PHONE-NUMBER]" class="btn-ink">Call [YOUR-PHONE-NUMBER]</a>
    </div>
  </div>
</section>
</main>

<footer class="footer">
  <div class="wrap"><div class="footer-in">
    <div class="flogo">[Company<span>Name</span>]</div>
    <p class="fcopy">© 2025 [Company Name] · Serving Dallas-Fort Worth, TX</p>
    <div class="flinks">
      <a href="../../index.html">Home</a>
      <a href="../../index.html#faq">FAQ</a>
      <a href="../../index.html#get-offer">Get Offer</a>
    </div>
  </div></div>
</footer>

<div class="mcta">
  <a href="tel:[YOUR-PHONE-NUMBER]" class="mc">📞 Call Now</a>
  <a href="../../index.html#get-offer" class="mf">Get Cash Offer</a>
</div>

<script>
  const obs=new IntersectionObserver(entries=>{{entries.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('vis');obs.unobserve(e.target)}}}});}},{{{{'threshold':.1}}}});
  document.querySelectorAll('.rv').forEach(el=>obs.observe(el));
</script>
</body>
</html>"""
    return html


# ── BLOG INDEX ─────────────────────────────────────────────────────────────────
def generate_blog_index():
    cards = ""
    for post in BLOG_POSTS:
        cards += f"""    <a href="{post['slug']}.html" style="background:var(--white);border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:all .2s;display:block" onmouseover="this.style.boxShadow='0 8px 32px rgba(13,12,10,.12)';this.style.transform='translateY(-3px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
      <div style="padding:28px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">
          <span style="background:var(--gold-pale);color:var(--gold);padding:3px 10px;border-radius:100px;font-size:.71rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase">{post['category']}</span>
          <span style="font-size:.76rem;color:var(--muted)">{post['read_time']}</span>
        </div>
        <h2 style="font-family:var(--fh);font-size:1.15rem;font-weight:700;color:var(--ink);margin-bottom:10px;line-height:1.3">{post['title']}</h2>
        <p style="font-size:.85rem;color:var(--muted);line-height:1.65">{post['intro'][:160]}...</p>
        <div style="margin-top:16px;font-size:.82rem;font-weight:600;color:var(--gold)">Read article →</div>
      </div>
    </a>\n"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DFW Real Estate Resources & Guides | [COMPANY NAME]</title>
  <meta name="description" content="Helpful guides for Dallas-Fort Worth homeowners facing foreclosure, probate, divorce, tax liens, and more. Learn your options before you decide." />
  <link rel="canonical" href="https://www.yourwebsite.com/blog/" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
</head>
<body>
<nav class="nav">
  <div class="wrap"><div class="nav-in">
    <a href="../index.html" class="logo">[Company<span>Name</span>]</a>
    <div class="nav-r">
      <a href="../index.html#how-it-works" class="nav-lk">How It Works</a>
      <a href="../index.html#areas" class="nav-lk">Areas</a>
      <a href="../index.html#faq" class="nav-lk">FAQ</a>
      <a href="tel:[YOUR-PHONE-NUMBER]" class="nav-btn">Call Now - Free</a>
    </div>
  </div></div>
</nav>
<main>
<section style="padding:120px 0 60px;background:var(--ink)">
  <div class="wrap">
    <div class="breadcrumb"><a href="../index.html">Home</a><span>›</span><span>Blog</span></div>
    <h1 class="page-h1" style="margin-top:16px">DFW Homeowner <em>Resources</em></h1>
    <p class="page-desc">Helpful guides for Dallas-Fort Worth homeowners navigating difficult real estate situations.</p>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:20px">
{cards}
    </div>
  </div>
</section>
</main>
<footer class="footer">
  <div class="wrap"><div class="footer-in">
    <div class="flogo">[Company<span>Name</span>]</div>
    <p class="fcopy">© 2025 [Company Name] · Serving Dallas-Fort Worth, TX</p>
    <div class="flinks"><a href="../index.html">Home</a><a href="../index.html#get-offer">Get Offer</a></div>
  </div></div>
</footer>
</body>
</html>"""


# ── MAIN ───────────────────────────────────────────────────────────────────────
def main():
    base = "/home/claude/dfw-site"

    # City pages
    city_count = 0
    for city in CITIES:
        slug = city_slug(city["name"])
        path = os.path.join(base, "city", f"sell-house-fast-{slug}.html")
        with open(path, "w") as f:
            f.write(generate_city_page(city))
        city_count += 1

    # Situation pages
    sit_count = 0
    for sit in SITUATIONS:
        path = os.path.join(base, "situation", f"{sit['slug']}.html")
        with open(path, "w") as f:
            f.write(generate_situation_page(sit))
        sit_count += 1

    # Blog pages
    blog_count = 0
    for post in BLOG_POSTS:
        path = os.path.join(base, "blog", f"{post['slug']}.html")
        with open(path, "w") as f:
            f.write(generate_blog_page(post))
        blog_count += 1

    # Blog index
    with open(os.path.join(base, "blog", "index.html"), "w") as f:
        f.write(generate_blog_index())

    print(f"✅ {city_count} city pages")
    print(f"✅ {sit_count} situation pages")
    print(f"✅ {blog_count} blog posts + index")
    print(f"✅ Total: {city_count + sit_count + blog_count + 1} pages generated")


if __name__ == "__main__":
    main()
