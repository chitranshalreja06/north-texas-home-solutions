# City -> county mapping (from homepage service-area section), plus hand-written
# local extras for the top-10 money cities. Everything else falls back to
# county-level content so no page ships generic.
COUNTIES = {
 "Dallas County": ["dallas","garland","irving","richardson","mesquite","addison","duncanville","farmers-branch","cedar-hill","lancaster","desoto","hutchins","balch-springs","cockrell-hill","seagoville","wilmer","rowlett","sunnyvale","sachse"],
 "Tarrant County": ["fort-worth","arlington","grapevine","southlake","keller","hurst","euless","bedford","north-richland-hills","haltom-city","colleyville","watauga","richland-hills","white-settlement","benbrook"],
 "Collin County": ["plano","mckinney","frisco","allen","wylie","murphy","prosper","celina","anna","melissa","sachse"],
 "Denton County": ["denton","lewisville","flower-mound","carrollton","the-colony","highland-village","corinth","little-elm","aubrey","pilot-point","justin","argyle"],
 "Rockwall County": ["rockwall","heath","fate","royse-city","mclendon-chisholm"],
}
CITY_COUNTY = {}
for county, slugs in COUNTIES.items():
    for s in slugs:
        CITY_COUNTY.setdefault(s, county)  # Sachse keeps Dallas County first listing

COUNTY_BLURB = {
 "Dallas County": "Dallas County holds its tax sales on the first Tuesday of every month. If you're behind on property taxes, that date is the real deadline, and a cash sale before it stops the auction cold.",
 "Tarrant County": "Tarrant County holds its tax sales on the first Tuesday of every month in downtown Fort Worth. Behind on taxes? A cash sale before that date keeps your home off the auction list.",
 "Collin County": "Collin County's tax sales happen on the first Tuesday of every month in McKinney. If back taxes are piling up, selling before the sale date means you walk away with money instead of losing the house.",
 "Denton County": "Denton County runs its tax sales on the first Tuesday of every month. Owe back taxes? We handle the payoff at closing, so the county gets paid and you still walk away with cash.",
 "Rockwall County": "Rockwall County holds tax sales on the first Tuesday of every month. If you're behind, a fast cash sale before that date is the cleanest way out.",
}
# Hand-written neighborhood proof for top-10 cities only
NEIGHBORHOODS = {
 "dallas": ["Oak Cliff", "Lakewood", "Pleasant Grove", "Far North Dallas", "Bishop Arts", "Preston Hollow"],
 "fort-worth": ["Stop Six", "Como", "Riverside", "Diamond Hill", "Ridglea", "East Fort Worth"],
 "garland": ["Duck Creek", "Club Hill", "Firewheel", "Travis College Hill", "Northridge"],
 "arlington": ["East Arlington", "North Arlington", "South Cooper corridor", "Dalworthington Gardens area"],
 "mesquite": ["Town East area", "Lawson Road corridor", "Creek Crossing", "Rutherford Place"],
 "plano": ["East Plano", "Old Plano", "Douglass", "Park Forest", "Parker Road corridor"],
 "irving": ["Valley Ranch", "Las Colinas", "south Irving", "Plymouth Park", "Shady Grove"],
 "rowlett": ["Lake Ray Hubbard shoreline", "downtown Rowlett", "Springfield Lakes", "Toler Bay"],
 "mckinney": ["historic downtown McKinney", "Eldorado", "Stonebridge Ranch", "Craig Ranch"],
 "denton": ["historic Denton", "the UNT area", "Robson Ranch corridor", "Southridge"],
}
TOP10 = list(NEIGHBORHOODS.keys())

# Hand-written local intros for top-10 money cities (genuinely local, no filler)
CITY_INTRO = {
 "dallas": "Dallas is huge and every pocket sells different. A 1950s pier-and-beam in Oak Cliff with foundation movement is a totally different sale than a teardown lot in Preston Hollow. We price off what investors are actually paying on your street, not a Zillow guess.",
 "fort-worth": "Fort Worth's east and south sides are full of 1940s to 60s homes that need everything, and that is exactly what we buy. An inherited house in Stop Six, a rental in Diamond Hill that became a headache, we make cash offers based on real Fort Worth investor sales.",
 "garland": "Garland's Duck Creek and Club Hill areas are full of 1970s and 80s brick homes with aging roofs and foundations shifting in the clay. We buy them as-is, hail damage and all.",
 "arlington": "Arlington sits between two big cities and its housing stock shows it, from mid-century ranches in East Arlington to 80s builds along South Cooper. Arlington code enforcement does not mess around, so if citations are piling up, a fast cash sale stops the fines.",
 "mesquite": "Mesquite's Town East corridor and the older neighborhoods near Lawson Road hold thousands of 1960s and 70s homes. When the repairs outrun the value, listing does not make sense. We buy them for cash: no repairs, no cleanout.",
 "plano": "Even in Plano, not every house fits the MLS. East Plano's older homes, divorce situations, inherited properties with title issues, we buy the ones that need a fast, private sale.",
 "irving": "Irving's south side has some of the oldest housing stock in DFW, and the condos and townhomes around Valley Ranch come with their own headaches. We buy houses, townhomes, and condos across Irving for cash.",
 "rowlett": "Rowlett's lake-area homes take a beating from storms and shifting soil near the water. If your house needs more work than it is worth on the open market, we buy it as-is.",
 "mckinney": "Historic downtown McKinney's older homes come with charm and expensive problems: foundation, old electrical, cast-iron plumbing, you name it. We buy them without asking you to fix a thing.",
 "denton": "Denton's mix of college rentals, historic homes, and new builds means every sale is different. Tired landlords near UNT, inherited homes sitting empty for a year, we buy them all as-is.",
}
# One extra localized FAQ per top-10 city
CITY_FAQ = {
 "dallas": ("My Dallas house needs foundation work. Will that kill the offer?",
            "No. Foundation issues are the single most common problem we see in Dallas, thanks to the clay soil. We get a foundation bid, factor it into our numbers, and still make you a fair cash offer. You don't lift a finger."),
 "fort-worth": ("I inherited a house in Fort Worth but the title isn't in my name. Can you still buy it?",
            "Usually yes. Heirship and probate issues are routine for us. We work with the title company to sort out who can legally sell, and we buy the house as-is while that's happening."),
 "garland": ("My Garland roof was damaged in a hail storm. Do I need to replace it first?",
            "No. We buy hail-damaged houses all the time in Garland. Replacing a roof costs thousands you may never get back in sale price; we price the damage in and buy as-is."),
 "arlington": ("Arlington code enforcement is fining me. Can you close fast enough to stop it?",
            "Often yes. We can close in as little as 7 days on a clean title, and the day we close, the violations become our problem, not yours. Tell us about the citations when you reach out so we plan around them."),
 "mesquite": ("My Mesquite house is dated and needs everything. Is it even worth selling as-is?",
            "If the repair bill is bigger than the payoff, listing it usually means months of showings and lowball offers. We buy dated, worn-out Mesquite homes for cash based on the lot and structure value, no repairs needed."),
 "plano": ("I need to sell my Plano house privately because of a divorce. Is that possible?",
            "Yes. We handle divorce sales discreetly: no yard sign, no showings, no open houses. We coordinate with both parties and the title company so the sale and split happen cleanly."),
 "irving": ("Do you buy condos and townhomes in Irving, or just houses?",
            "We buy condos and townhomes too, including the ones with high HOA dues or special assessments coming. If the HOA situation makes a traditional sale painful, a cash sale is usually the clean exit."),
 "rowlett": ("My insurance won't cover the storm damage on my Rowlett home. What are my options?",
            "This happens a lot around the lake. If the repair cost doesn't make sense, we buy the house as-is with the damage disclosed. You walk away with cash instead of a repair bill."),
 "mckinney": ("My McKinney home is in a historic area. Does that complicate a cash sale?",
            "Not for us. We buy older and historic-area homes regularly and handle any extra title or survey quirks with the title company. The age of the house is never a dealbreaker."),
 "denton": ("I'm a tired landlord near UNT and my rental is trashed. Will you still buy it?",
            "Absolutely. Tenant damage, deferred maintenance, leases you don't want to deal with, we buy Denton rentals as-is, tenants and all if needed. You don't have to clean or evict anyone first."),
}
