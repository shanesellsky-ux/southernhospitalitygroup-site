import json, html, os
from faqdata import SITE_FAQ, PROP_FAQ, LOC, PHONE
from urllib.parse import quote_plus
from localdata import LOCAL, SITES, TOWN, QUERY
from articles import ARTICLES
from seodata import TITLE, DESC, BEST, HOTTUB, HL, G, BT, WHERE, SITE_DIRECT_FAQ, BOOK_Q
SITE = 'https://www.southernhospitalitygroup.co'
import hashlib
CSSV=hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'out','style.css'),'rb').read()).hexdigest()[:8]
OUT = '/home/claude/site/out'
E = html.escape
BASE = 'https://www.southernhospitalitygroup.co/property/'

HOSP_SITE='a26e49a1-a0e0-4b96-b0d3-1078465552b5'
HOSP_ID={'bourbon-loft':'836610','bourbon-street':'1709872','historic-loft':'1182872','herrington-haven':'2483446','bootleggers':'836612','trinity':'1709870','neo':'1709868','woodleigh':'1830842'}
SEARCH_ID='d8ed439f-02cc-4e94-abba-fdd152aae2c2'
SEARCH_JS='https://hospitable.b-cdn.net/direct-property-search-widget/hospitable-search-widget.prod.js'
PERK = 'Complimentary early check-in or late checkout (up to 2 hours), when available'

P = {
 'bootleggers': dict(name="Bootlegger's Retreat", market='red-river-gorge', town='Stanton · Red River Gorge',
   tag='Hot tub · game room · arcade · sleeps 8', br=4, ba=2, guests=8, beds=5, pets=True, n=16,
   book=BASE+'661714854670765222/sale-rrg-cabin-whot-tub-game-room-ev-charger',
   lede="Three levels of cabin in the woods, about 10 minutes from Slade. A private hot tub deck, a downstairs game room with ping pong, foosball and a multicade arcade, and a fire pit for s'mores under the stars.",
   feats=['Private hot tub deck','Game room: ping pong, foosball, arcade','Fire pit, grill & upper deck','EV charging on site','Pet friendly','Loft sleeping area the kids will fight over'],
   note='4WD or AWD recommended; required in ice or snow.',
   caps=['Lit up at dusk','Under the stars','Hot tub on the deck','Fall in the great room','Deck time','Dinner with a view of the leaves','The game room','Arcade machine','Fire pit at night','Bunk room','King bedroom','Grill on the deck','Pet corner','EV charger','Kitchen','Sunset from the deck'],
   rev=[("Brandon H.","The house was great and worked well for our trip! We enjoyed the hot tub and making s'mores around the fire pit. Our youngest daughter loved sleeping in the loft."),
        ("Danny S.","Shane, the host, is very hospitable and proactive. We enjoyed our visit to his cabin. We loved the game room and spent much of our time together playing the games and listening to music."),
        ("Kari D.","The cabin was exactly as advertised and close to all the things to do in the area! We would stay here again and the games/ping pong table were used a lot!")]),
 'neo': dict(name='NEO', market='red-river-gorge', town='Rosslyn · Red River Gorge',
   tag='Private hot tub · big windows · sleeps 5', br=2, ba=1, guests=5, beds=2, pets=True, n=17,
   book=BASE+'661715337158331627/hot-tub-ev-charger-firepit-10-minutes-from-slade-holiday-home',
   lede='A modern black cabin with vaulted wood ceilings and floor-to-ceiling windows that pull the forest inside. King loft, queen bedroom, a private hot tub on the deck and a fire pit out back, about 10 minutes from Slade.',
   feats=['Private hot tub on the deck','King loft + queen bedroom','Fire pit & grill','Full kitchen & coffee bar','Free Level 2 EV charger','Pet friendly, dog bed included'],
   note='',
   caps=['Red door in the fall leaves','NEO in the woods','The deck and hot tub','Living room','Loft bedroom','King loft','Hot tub','The red door','Queen bedroom','Living and dining','Dining for four','Kitchen','EV charger','Pup corner','Bedroom','Loft lounge','From above'],
   rev=[("Rachel M.","Best BnB… EVER. This place is gorgeous and the location is perfect for a quiet getaway. Shane is an incredible host and was always communicative and all around very pleasant to converse with. I can't recommend this place enough. We LOVED it."),
        ("Claire R.","This was a great place to stay for a quick honeymoon getaway! The cabin was beautiful and clean. I also really appreciated being able to bring my puppy so we could have a full family getaway!"),
        ("Myra S.","Shane's cabin was excellent! The space is beautiful and the cabin is peacefully nestled in the woods. Everything was easy to find and use. The kitchen was well stocked with seasonings and cooking needs. The EV charger worked excellently.")]),
 'trinity': dict(name='Trinity A-Frame', market='red-river-gorge', town='Rosslyn · Red River Gorge',
   tag='Sunken hot tub · shuffleboard · sleeps 5', br=3, ba=2, guests=5, beds=2, pets=True, n=16,
   book=BASE+'661715636182846734/10-minutes-from-slade-hottub-arcade-ev-charger',
   lede='A Scandinavian-inspired A-frame with soaring wood ceilings, a wall of glass and a sunken hot tub on the deck. Light-up shuffleboard and an arcade inside, a fire pit ring with red Adirondacks outside, and hidden trails to wander.',
   feats=['Sunken hot tub','Light-up shuffleboard & arcade','Fire pit with Adirondack chairs','3 bedrooms, 2 baths','Free Level 2 EV charger','Pet friendly'],
   note='4WD or AWD recommended; required in ice or snow.',
   caps=['Tucked in the trees','Trinity in the trees','Living room','Dining table','Shuffleboard','Loft bedroom','Fire pit circle','Loft','Dining under the stairs','Kitchen','Fire pit garden','Loft with ladder','EV charger','Deck dining','Game and dining room','The A-frame'],
   rev=[("Leslie F.","We loved the modern design of this cabin. We felt right at home in the heart of the mountains. Don't think twice….book it!!!!!"),
        ("Dillon P.","We had a wonderful stay! The cabin was clean, comfortable, and surrounded by beautiful nature. Shane was a great host and very responsive. We really enjoyed our time here and would definitely love to come back. Highly recommended!"),
        ("Megan A.","Our family had a wonderful stay at the A frame cabin! The host was very quick to respond to messages and the cabin was so clean and comfortable. We had everything we needed and it was in a great location.")]),
 'bourbon-street': dict(name='Bourbon Street', market='bourbon-trail', town='Downtown Frankfort',
   tag='1904 mansion · speakeasy · theater · sleeps 14', br=7, ba=3.5, guests=14, beds=7, pets=False, n=22,
   book=BASE+'661715874222181687/downtown-mansion-15-miles-to-buffalo-trace',
   lede="A 1904 mansion in downtown Frankfort built for Bourbon Trail groups. A speakeasy bar made from barrel lids and live-edge wood, a billiard parlor with an 8' slate table, a poker room, a theater with an 85\" TV, an arcade and a piano. Walk to dinner; Buffalo Trace is about five minutes away.",
   feats=['Speakeasy wet bar','Billiard parlor, 8\' slate table','Poker room','Theater with 85" TV','Arcade with 15,000 games','Dining for 10 + home gym'],
   note='All bedrooms and full baths are upstairs.',
   caps=['Bourbon Street at twilight','The speakeasy bar','The 1904 facade','The parlor','Billiard parlor','The Bulleit lounge','Music room with 1920s piano','Kitchen island','Dining for 10','Poker room','Theater lounge','Home gym','Navy fireplace suite','Rust fireplace suite','Green bedroom','Navy bedroom with reading chair','Blue accent bedroom','Slate blue bedroom','Teal bedroom','Spa-style bath','Front porch','Downtown Frankfort from above'],
   video=True,
   rev=[("Scott W.","Great visit. Perfect for the Bourbon Trail. Our group of 8 enjoyed all the amenities and appreciated the cleanliness and the location in the middle of Frankfort. Would highly recommend for a group trip."),
        ("Lisa H.","The house worked well for our group of 8. We enjoyed the pool table, bar and home gym. The location downtown was wonderful and we were able to walk to the restaurants and bars nearby. I would highly recommend this house for anyone visiting."),
        ("Ben B.","Shane's place is very close and walkable to downtown Frankfort. Easy parking and access to the rental. More spacious than the photos give it credit. Rooms and bathrooms were clean and Shane was always responsive.")]),
 'woodleigh': dict(name='The Woodleigh', market='bourbon-trail', town='Versailles',
   tag='1903 home · covered patio · sleeps 8', br=4, ba=2, guests=8, beds=4, pets=False, n=8,
   book=BASE+'661716251483049337/the-woodleigh',
   lede="A 1903 home in Versailles with original hardwoods, high ceilings and a covered patio with a fire pit and outdoor TV. Minutes from Keeneland and the Bourbon Trail, about 15 minutes to Lexington.",
   feats=['Covered patio with fire pit','Grill & outdoor dining','Original 1903 hardwoods','Dedicated workspace','Crib available','Minutes to Keeneland'],
   note='',
   caps=['The Woodleigh','Covered patio','Living room','Dining room','Kitchen','Primary bedroom','Bath','Bedroom'],
   rev=[("John P.","The house was great and the location was perfect. Perfectly located for the Bourbon Trail, Keeneland or exploring Lexington. The House is spacious and has a lot of gathering areas and a great kitchen. Perfect for Labor Day weekend family gathering."),
        ("Lou L.","Overall a very nice, comfortable and spacious place, very attentive and responsive, even checking on us during a storm to make sure all was good. Would stay again if in the area.")]),
 'bourbon-loft': dict(name='Bourbon Trail Loft', market='bourbon-trail', town='St. Clair Street · Frankfort',
   tag='2-story loft · sleeps 4', br=1, ba=1.5, guests=4, beds=2, pets=False, n=12,
   book=BASE+'661714732994006054/1-bedroom-ky-bourbon-trail-loft-in-horse-country',
   lede="A renovated two-story loft with exposed brick and restored wood in Frankfort's St. Clair entertainment district. Walk to restaurants and live music; Buffalo Trace is 1.6 miles away and Woodford Reserve about 11.",
   feats=['Exposed brick & restored wood','Two queen beds','Full kitchen','Washer & dryer','Walk to dinner & live music','1.6 miles to Buffalo Trace'],
   note='Second-floor unit with about 25 steps and no elevator.',
   caps=['Living room','St. Clair Street','Living room from the stairs','Two queen beds','Living and dining','Dining nook','Kitchen','Bedroom','Stairs to the bedroom','Bath','Sidewalk cafés out front','Your private entrance'],
   rev=[("Jan R.","Very cool loft, loved all the old wood that had been restored. Located by the old capital buildings. Short walk to the riverside trail."),
        ("Donna B.","Shane was a super host and answered all our questions. The place is super clean and very nice. Location is perfect. Close walking distance to anywhere in downtown Frankfort. Highly recommend!")]),
 'historic-loft': dict(name='Historic Loft', market='bourbon-trail', town='St. Clair Street · Frankfort',
   tag='King loft for two · sleeps 2', br=1, ba=1.5, guests=2, beds=1, pets=False, n=13,
   book=BASE+'661715189573356756/historic-loft-in-frankfort-entertainment-district',
   lede="A freshly remodeled loft for two with a king bed, brick walls and a dedicated parking space, right in Frankfort's entertainment district. Park once and walk to dinner, bars and the river.",
   feats=['King bed','Exposed brick & fireplace mantel','Dedicated parking space','Well-stocked kitchen & coffee bar','Walk to bars & restaurants','Close to Buffalo Trace'],
   note='',
   caps=['Living room with fireplace','Living room from the stairs','King bedroom','Living room','Bedroom with fireplace','Living room','Kitchen pass-through','Kitchen','Bedroom suite','Bath','Walk-in shower','Walk-in closet','St. Clair Street, right out the door'],
   rev=[("Rax D.","We had a great stay! The loft was freshly remodeled, clean, and comfortable. Its central location made it the perfect home base for exploring multiple bourbon distilleries. There were also plenty of great restaurants and bars nearby, many featuring live music."),
        ("Christa H.","Great stay in Frankfort. Super clean and exactly as pictured. Comfy king sized bed. Will definitely look to stay here again when visiting this area. Bars and restaurants right out the front door. Close to many distilleries.")]),
 'herrington-haven': dict(name='Herrington Haven', market='herrington-lake', town='Harrodsburg · Herrington Lake',
   tag='Lakefront · dock · hot tub · sleeps 10', br=3, ba=3.5, guests=10, beds=4, pets=False, n=24,
   book=BASE+'705116711627522693/lakefront-escape-on-herrington-dock-views',
   lede='A three-story lake house right on Herrington Lake with a private dock and boat slip, sunrise views from the deck, a fire pit on the lawn, a hot tub and a game room with a pool table. Room for 10 to spread out.',
   feats=['Private dock & boat slip','Big deck over the water','Hot tub & fire pit','Game room with pool table','3 bedrooms, 3.5 baths','Sleeps 10'],
   note='Steps down to the dock are steep and narrow.',
   caps=['Herrington Haven at dusk','The private dock','Hot tub with a lake view','Fire pit by the lake','From the lawn','Lake view from the deck','Living room','Dining','Kitchen','Kitchen','Bath','Dining for the whole crew','Kitchen','Entry','Game room with pool table','Pool table in the game room','Game room lounge','Primary suite','Primary suite','Bedroom','Bedroom','Full bath','Full bath','Full bath'],
   rev=[("Jeannie M.","Beautiful lake home with great views, comfortable accommodations and plenty of things to do if you want to just stay at the house. Pool table, fire pit, hot tub, games, TV's and more. Loved our stay!"),
        ("Beth W.","Loved staying here. The house is amazing and the view is fabulous. Loved spending time on the chaise lounges at the dock. We had a very relaxing time. Beds are super comfy."),
        ("Ali A.","What a gem! Our family of five had a lovely time! Very clean, linens were fresh, and private dock was amazing! The location on Herrington was beautiful, and clean.")]),
}

M = {
 'red-river-gorge': dict(name='Red River Gorge', kicker='Stanton · Slade · Rosslyn', homes=['bootleggers','neo','trinity'], hero='bootleggers/15.jpg',
   blurb='Three cabins in the woods about 10 minutes from Slade. Every one has a hot tub, a fire pit and free EV charging. Climb, hike and paddle all day, then soak.',
   long='The Gorge is Kentucky at its wildest: sandstone arches, cliffs for climbing, the Red River for paddling and Natural Bridge just down the road. Our three cabins sit in the woods close to Slade and Miguel\'s, with hot tubs on every deck and game rooms for rainy days.',
   todo=[('Natural Bridge State Resort Park','Hike to the arch or ride the skylift.'),('Rock climbing','World-class sport routes; Miguel\'s Pizza is base camp.'),('Gorge Underground','Kayak a flooded mine by headlamp.'),('Sky Bridge & Auxier Ridge','Two of the best short hikes for views.')]),
 'bourbon-trail': dict(name='The Bourbon Trail', kicker='Frankfort · Versailles', homes=['bourbon-street','woodleigh','bourbon-loft','historic-loft'], hero='bourbon-street/00.jpg',
   blurb="A 1904 mansion with a speakeasy and theater, a Versailles home minutes from Keeneland, and two lofts in Frankfort's entertainment district.",
   long="Frankfort is the capital of bourbon country. Buffalo Trace is minutes from downtown, Castle & Key and Woodford Reserve are a short drive, and Keeneland is about 20 minutes away. Stay walkable downtown or settle into a historic home in Versailles.",
   todo=[('Buffalo Trace Distillery','About five minutes from downtown Frankfort.'),('Castle & Key','A restored castle distillery on McCracken Pike.'),('Woodford Reserve','Rolling horse country, about 11 miles from Frankfort.'),('Keeneland','Live racing in April and October.')]),
 'herrington-lake': dict(name='Herrington Lake', kicker='Harrodsburg', homes=['herrington-haven'], hero='herrington-haven/01.jpg',
   blurb='Herrington Haven sits right on the water with a private dock, a hot tub, big lake views and room for 10.',
   long="Herrington Lake is one of Kentucky's deepest lakes, with limestone bluffs and quiet coves. Spend the day boating, fishing or swimming off your own dock, and the evening around the fire pit. Historic Harrodsburg and Shaker Village are close by.",
   todo=[('Boat, swim & fish','Right from your private dock.'),('Shaker Village of Pleasant Hill','Trails, farm-to-table dining and history.'),('Historic Harrodsburg','Kentucky\'s oldest town.'),('Bourbon Trail','Danville and Lawrenceburg distilleries within reach.')]),
}

STARS = '★★★★★'

def fmt(x): return ('%g' % x)

BOOKMENU = ('<div class="dd"><button class="btn ddb" type="button" aria-haspopup="true" aria-expanded="false">Book direct &#9662;</button><div class="ddm"><p class="ddh">Pick a home to see open dates</p>'
  + ''.join(f'<span class="ddg">{E(m["name"])}</span>' + ''.join(f'<a href="{k}.html#book">{E(P[k]["name"])}<small>Sleeps {P[k]["guests"]}</small></a>' for k in m['homes']) for m in M.values())
  + '<a class="ddall" href="search.html">Search all homes by date &rarr;</a></div></div>')

def head(title, desc, depth='', ld=None):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="p:domain_verify" content="579e0f4fb4aa7a1666019bee12486320"/>
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={CSSV}">{"".join('<script type="application/ld+json">'+json.dumps(x)+'</script>' for x in (ld or []))}</head><body>
<header class="top"><a class="brand" href="index.html"><span>SOUTHERN HOSPITALITY</span><small>GROUP · KENTUCKY</small></a>
<button class="menu" aria-label="Menu" onclick="document.body.classList.toggle('nav-open')">☰</button>
<nav><a href="red-river-gorge.html">Red River Gorge</a><a href="bourbon-trail.html">Bourbon Trail</a><a href="herrington-lake.html">Herrington Lake</a><a href="trip-guides.html">Trip guides</a><a href="faq.html">FAQ</a><a href="index.html#host">About us</a>{BOOKMENU}</nav></header>'''

FOOT = '''<section class="perk-band"><div class="wrap"><div><p class="kick">BOOK DIRECT PERK</p><h2>Two extra hours of Kentucky.</h2>
<p>Book on our site and get a complimentary early check-in or late checkout, up to 2 hours, when available. Same homes, same hosts, always a lower price than Airbnb or Vrbo.</p></div>
<a class="btn big" href="index.html#homes">Find your stay</a></div></section>
<footer><div class="wrap fgrid"><div><a class="brand" href="index.html"><span>SOUTHERN HOSPITALITY</span><small>GROUP · KENTUCKY</small></a>
<p>Locally hosted short-term rentals in the Red River Gorge, on the Bourbon Trail and on Herrington Lake. Hosted by Shane and the Southern Hospitality Group team.</p></div>
<div><h4>Stays</h4><a href="red-river-gorge.html">Red River Gorge</a><a href="bourbon-trail.html">Bourbon Trail</a><a href="herrington-lake.html">Herrington Lake</a></div>
<div><h4>Trip guides</h4><a href="large-group-rentals.html">Large group rentals</a><a href="buffalo-trace-lodging.html">Stays near Buffalo Trace</a><a href="red-river-gorge.html">Red River Gorge cabins</a><a href="bourbon-trail.html">Frankfort &amp; Bourbon Trail</a></div>
<div><h4>Contact</h4><a href="tel:+18592291524">Call or text 859-229-1524</a><a href="faq.html">FAQ</a><a href="terms.html">Terms of Stay</a><a href="https://www.instagram.com/southern_hospitalityky/">Instagram</a><a href="https://www.facebook.com/people/Southern-Hospitality-Group/100076536140013/">Facebook</a><a href="https://www.pinterest.com/southernhospitalityky/">Pinterest</a></div></div>
<div class="wrap fine">© 2026 Southern Hospitality Group · Red River Gorge cabin photography by Kylie Whiseman, PoppyCoast Photography</div></footer>
<div class="lb" id="lb" onclick="if(event.target===this)lbClose()"><button class="lbx" onclick="lbClose()" aria-label="Close">✕</button><button class="lbp" onclick="lbGo(-1)" aria-label="Previous">‹</button><img id="lbi" alt=""><button class="lbn" onclick="lbGo(1)" aria-label="Next">›</button><p id="lbc"></p></div>
<script>let G=[],gi=0;function lbOpen(i){G=[...document.querySelectorAll('[data-lb]')];gi=i;lbShow();document.getElementById('lb').classList.add('on')}
function lbShow(){const a=G[gi];document.getElementById('lbi').src=a.dataset.lb;document.getElementById('lbc').textContent=a.dataset.cap||''}
function lbGo(d){gi=(gi+d+G.length)%G.length;lbShow()}function lbClose(){document.getElementById('lb').classList.remove('on')}
document.addEventListener('keydown',e=>{if(!document.getElementById('lb').classList.contains('on'))return;if(e.key==='Escape')lbClose();if(e.key==='ArrowRight')lbGo(1);if(e.key==='ArrowLeft')lbGo(-1)});
document.querySelectorAll('[data-lb]').forEach((a,i)=>a.addEventListener('click',e=>{e.preventDefault();lbOpen(i)}));</script>
<script>(function(){var b=document.body;function c(){b.classList.remove('nav-open')}document.querySelectorAll('.top nav a').forEach(function(a){a.addEventListener('click',c)});var y=window.scrollY;window.addEventListener('scroll',function(){if(b.classList.contains('nav-open')&&!document.querySelector('.dd.open')&&Math.abs(window.scrollY-y)>40)c();y=window.scrollY},{passive:true});document.addEventListener('click',function(e){if(b.classList.contains('nav-open')&&!e.target.closest('.top'))c()});window.addEventListener('hashchange',c);document.querySelectorAll('.dd .ddb').forEach(function(x){x.addEventListener('click',function(e){e.stopPropagation();var d=x.parentElement,o=!d.classList.contains('open');document.querySelectorAll('.dd.open').forEach(function(y){y.classList.remove('open')});d.classList.toggle('open',o);x.setAttribute('aria-expanded',o)})});document.addEventListener('click',function(e){if(!e.target.closest('.dd'))document.querySelectorAll('.dd.open').forEach(function(y){y.classList.remove('open')})});})();</script>
<script>(function(){var n=0,t=setInterval(function(){n++;document.querySelectorAll('hospitable-direct-mps').forEach(function(w){var r=w.shadowRoot;if(!r||!r.children.length)return;w.parentElement.classList.add('hs-live');if(!r.querySelector('style[data-shg]')){var s=document.createElement('style');s.setAttribute('data-shg','');s.textContent='.search-bar-container{width:100%!important;margin-left:0!important;left:auto!important;right:auto!important;transform:none!important}.search-bar{width:100%!important;max-width:100%!important;box-sizing:border-box}'+(w.closest('.hresults')?'.hospitable-mps,.results-container,.left{height:auto!important;max-height:none!important;overflow:visible!important}':'');r.appendChild(s)}});if(n>60)clearInterval(t)},500)})();</script>
</body></html>'''

def faq_html(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in items) + '</div>'

def faq_ld(items):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in items]}

def card(k):
    p = P[k]
    return f'''<a class="card" href="{k}.html"><div class="ph"><img loading="lazy" src="img/{k}/t00.jpg" alt="{E(p['name'])}, {E(p['tag'].split(' · ')[0].lower())} in {E(M[p['market']]['name'])}, Kentucky"><span class="pill">{E(M[p['market']]['name'])}</span></div>
<div class="cb"><p class="town">{E(p['town'])}</p><h3>{E(p['name'])}</h3><p class="meta">{p['br']} bd · {fmt(p['ba'])} ba · sleeps {p['guests']}{' · pets ok' if p['pets'] else ''}</p><p class="tag">{E(p['tag'])}</p><span class="go">View home →</span></div></a>'''

def quote(name, text, prop=None):
    sub = f' · {E(P[prop]["name"])}' if prop else ''
    return f'<figure class="q"><div class="st">{STARS}</div><blockquote>“{E(text)}”</blockquote><figcaption>{E(name)}{sub}</figcaption></figure>'

# ---------- HOME
def home():
    org = {"@context":"https://schema.org","@type":"Organization","@id":SITE+"/#org","name":"Southern Hospitality Group","url":SITE+"/",
           "description":"Locally hosted vacation rentals in Kentucky: three hot tub cabins in the Red River Gorge, four homes in Frankfort and Versailles on the Bourbon Trail, and a lake house with a hot tub on Herrington Lake, all bookable directly.",
           "telephone":"+1-859-229-1524","areaServed":[{"@type":"Place","name":n} for n in ["Red River Gorge, Kentucky","Frankfort, Kentucky","Versailles, Kentucky","Herrington Lake, Kentucky"]],
           "address":{"@type":"PostalAddress","addressRegion":"KY","addressCountry":"US"},
           "founder":{"@type":"Person","name":"Shane O'Donley"},
           "contactPoint":{"@type":"ContactPoint","telephone":"+1-859-229-1524","contactType":"reservations","areaServed":"US"},
           "sameAs":["https://www.instagram.com/southern_hospitalityky/","https://www.facebook.com/profile.php?id=100076536140013","https://www.pinterest.com/southernhospitalityky/"]}
    web = {"@context":"https://schema.org","@type":"WebSite","@id":SITE+"/#website","name":"Southern Hospitality Group","url":SITE+"/","publisher":{"@id":SITE+"/#org"}}
    hfaq = SITE_DIRECT_FAQ + SITE_FAQ[:3]
    h = head('Kentucky Vacation Rentals | Red River Gorge, Bourbon Trail & Lake | Book Direct', 'Book direct with local hosts: hot tub cabins in the Red River Gorge, a 1904 mansion and lofts in Frankfort near Buffalo Trace, and a Herrington Lake house.', ld=[org, web, faq_ld(hfaq)])
    h += '''<section class="hero"><img src="img/bootleggers/00.jpg" alt="Bootlegger's Retreat lit up at dusk in the Red River Gorge woods"><div class="shade"></div>
<div class="wrap hc"><p class="kick">CABINS · MANSIONS · LAKE HOUSES</p><h1>Kentucky vacation rentals, done right.</h1>
<p class="sub">Three ways to do Kentucky: hot tub cabins in the Red River Gorge. A 1904 mansion with a speakeasy on the Bourbon Trail. A private dock and hot tub on Herrington Lake. Booked direct with the local hosts who run them.</p>
<div class="hsearch"><script src="'''+SEARCH_JS+'''"></script><hospitable-direct-mps identifier="'''+SEARCH_ID+'''" type="custom" results-url="/search"></hospitable-direct-mps><div class="hs-ph"><span>Where</span><span>Check-in</span><span>Checkout</span><span>Guests</span><a class="btn" href="#homes">Search</a></div></div><div class="row"><a class="btn ghost big" href="#book-direct">Why book direct</a></div></div></section>
<section class="stats"><div class="wrap sg"><div><b>3</b><span>MARKETS</span></div><div><b>8</b><span>HOMES</span></div><div><b>4.96</b><span>AVG. GUEST RATING</span></div><div><b>4</b><span>HOMES WITH HOT TUBS</span></div></div></section>
<section class="sec" id="markets"><div class="wrap"><p class="kick">CHOOSE YOUR KENTUCKY</p><h2>Three markets. One standard.</h2>'''
    for i, (mk, m) in enumerate(M.items()):
        n = len(m['homes']); gs = [P[k]['guests'] for k in m['homes']]
        rng = f'sleep {min(gs)} to {max(gs)}' if n > 1 else f'sleeps {gs[0]}'
        h += f'''<a class="mk {'rev' if i%2 else ''}" href="{mk}.html"><div class="mph">{('<video autoplay muted loop playsinline poster="img/'+m['hero']+'" src="video/bourbon-street-loop.mp4"></video>') if mk=='bourbon-trail' else ('<img loading="lazy" src="img/'+m['hero']+'" alt="'+E(m['name'])+'">')}</div>
<div class="mt"><span class="num">0{i+1} · {E(m['kicker'].upper())}</span><h3>{E(m['name'])}</h3><p>{E(m['blurb'])}</p><span class="meta">{n} {'homes' if n>1 else 'home'} · {rng}</span><span class="go">Explore {E(m['name'])} →</span></div></a>'''
    h += '<div class="guides"><span>Trip guides:</span><a href="large-group-rentals.html">Large groups (8 to 19)</a><a href="buffalo-trace-lodging.html">Near Buffalo Trace</a><a href="red-river-gorge.html">Gorge cabins with hot tubs</a><a href="bourbon-trail.html">Frankfort &amp; Bourbon Trail</a><a href="herrington-lake.html">Lake house with a dock</a></div>'
    h += '</div></section><section class="sec alt" id="homes"><div class="wrap"><p class="kick">ALL 8 HOMES</p><h2>Find your stay.</h2>'
    h += '<div class="filters"><button class="on" data-f="all">All</button><button data-f="red-river-gorge">Red River Gorge</button><button data-f="bourbon-trail">Bourbon Trail</button><button data-f="herrington-lake">Herrington Lake</button><button data-f="pets">Pet friendly</button><button data-f="big">Groups of 8+</button></div><div class="grid" id="hg">'
    for k, p in P.items():
        h += f'<div class="gi" data-m="{p["market"]}" data-p="{int(p["pets"])}" data-g="{p["guests"]}">{card(k)}</div>'
    h += '''</div></div></section>
<script>document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');const f=b.dataset.f;
document.querySelectorAll('#hg .gi').forEach(g=>{let s=f==='all'||g.dataset.m===f||(f==='pets'&&g.dataset.p==='1')||(f==='big'&&+g.dataset.g>=8);g.style.display=s?'':'none'})})</script>
<section class="sec" id="book-direct"><div class="wrap bd"><div><p class="kick">BOOK DIRECT</p><h2>Same homes. Better deal.</h2>
<p class="lead">When you book here instead of on Airbnb or Vrbo, you deal straight with us, and you get a little extra.</p></div>
<div class="bdg"><div><b>⏰</b><h4>2 extra hours</h4><p>Complimentary early check-in or late checkout, up to 2 hours, when available.</p></div>
<div><b>💲</b><h4>Our best price</h4><p>Booking here is always cheaper than the same stay on Airbnb or Vrbo.</p></div>
<div><b>💬</b><h4>Talk to your host</h4><p>Questions go straight to Shane and the team, not a call center.</p></div>
<div><b>🔒</b><h4>Secure checkout</h4><p>Live calendars and secure payment on every home.</p></div></div></div></section>
<section class="sec"><div class="wrap two"><div><p class="kick">GOOD TO KNOW</p><h2>Booking direct, explained.</h2><p class="lead">Live calendars, secure checkout and our best price on every home. Contactless check-in, and a checkout list you can finish in two minutes. No stripping beds, no laundry.</p><p style="margin-top:22px"><a class="btn ghost" href="faq.html">Read the FAQ</a></p></div>'''+faq_html(hfaq)+'''</div></section>
<section class="sec" id="host"><div class="wrap host"><img src="img/shane.jpg" alt="Shane O'Donley, host of Southern Hospitality Group" loading="lazy"><div><p class="kick">MEET YOUR HOST</p><h2>A local who picks up the phone.</h2>
<p class="lead">My team and I host all eight Southern Hospitality Group homes, from hot tub cabins in the Red River Gorge to a 1904 mansion on the Bourbon Trail. I&rsquo;m a Kentucky local, I&rsquo;ve been hosting for four years, and I&rsquo;m an Airbnb Superhost with more than 850 reviews and a 4.96 out of 5 average. If anything comes up during your stay, you&rsquo;ll hear back quickly from someone who knows the home, not a call center.</p>
<p>Opening up these homes has been a true pleasure. Knowing families and friends are making memories in them, whether that&rsquo;s s&rsquo;mores around the fire pit, a toast in the speakeasy or coffee on the dock at sunrise, never gets old.</p>
<p class="inv"><em>Thinking about owning a short-term rental yourself?</em> I also help investors find, buy and set up vacation rentals in Kentucky, from choosing the right market to getting the property guest-ready. Happy to talk shop anytime: <a href="tel:+18592291524">859-229-1524</a>.</p>
<p class="sig">Shane O&rsquo;Donley<span>Realtor, Keller Williams Legacy Group</span></p></div></div></section>
<section class="sec alt"><div class="wrap"><p class="kick">FROM OUR GUESTS</p><h2>850+ reviews. 4.96 average.</h2><div class="qg">'''
    for k, i in [('neo',0),('bourbon-street',0),('herrington-haven',0),('trinity',0),('historic-loft',0),('bootleggers',0)]:
        n, t = P[k]['rev'][i]; h += quote(n, t, k)
    h += '</div></div></section>'
    h += FOOT
    return h

# ---------- DESTINATION / GUIDE PAGES
def crumbs_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(items)]}

def guide(slug):
    g = G[slug]
    url = f"{SITE}/{slug}"
    items = {"@context":"https://schema.org","@type":"ItemList","name":g['h1'],"itemListElement":[{"@type":"ListItem","position":i+1,"url":f"{SITE}/{k}","name":P[k]['name']} for i,k in enumerate(g['homes'])]}
    page = {"@context":"https://schema.org","@type":"CollectionPage","name":g['h1'],"url":url,"description":g['desc'],"isPartOf":{"@id":SITE+"/#website"},"about":{"@type":"Place","name":g['kicker'] if slug in M else "Kentucky"}}
    h = head(g['title'], g['desc'], ld=[page, items, crumbs_ld([("Home",SITE+"/"),(g['h1'],url)]), faq_ld(g['faq'])])
    h += f'''<section class="hero short"><img src="img/{g['hero']}" alt="{E(g['h1'])}"><div class="shade"></div><div class="wrap hc"><p class="crumb"><a href="index.html">Home</a> / {E(g['h1'])}</p>
<p class="kick">{E(g['kicker'].upper())}</p><h1>{E(g['h1'])}</h1><p class="sub">{E(g['sub'])}</p></div></section>
<section class="sec"><div class="wrap two"><div><p class="kick">THE AREA</p><h2>Why stay here</h2>''' + ''.join(f'<p class="lead"{" style=margin-top:18px" if i else ""}>{E(t)}</p>' for i,t in enumerate(g['intro'])) + f'''<p class="callout">{E(g['callout'])}</p></div>
<div><h3 class="todoh">{E(g.get('todo_head','Things to do nearby'))}</h3><div class="todo">''' + ''.join(f'<div><h4>{E(t)}</h4><p>{E(d)}</p></div>' for t,d in g['todo']) + '</div></div></div></section>'
    # comparison table
    col = g.get('col')
    colh = {'bt':'To Buffalo Trace','where':'Where'}.get(col,'')
    h += f'<section class="sec alt" id="ghomes"><div class="wrap"><p class="kick">{"OUR HOMES" if len(g["homes"])>1 else "THE HOME"}</p><h2>{("Compare the " + str(len(g["homes"])) + " homes") if len(g["homes"])>1 else ("Meet " + E(P[g["homes"][0]]["name"]))}</h2>'
    if len(g['homes'])>1:
        h += '<div class="cmp"><table><thead><tr><th>Home</th>' + (f'<th>{colh}</th>' if col else '') + '<th>Bedrooms</th><th>Baths</th><th>Sleeps</th><th>Pets</th><th>Highlights</th></tr></thead><tbody>'
        for k in g['homes']:
            p = P[k]; extra = (BT if col=='bt' else WHERE).get(k,'') if col else None
            h += f'<tr><td><a href="{k}.html">{E(p["name"])}</a></td>' + (f'<td>{E(extra)}</td>' if col else '') + f'<td>{p["br"]}</td><td>{fmt(p["ba"])}</td><td>{p["guests"]}</td><td>{"Yes" if p["pets"] else "No"}</td><td>{E(HL[k])}</td></tr>'
        if slug=='large-group-rentals':
            h += '<tr><td><a href="red-river-gorge.html">All 3 Gorge cabins</a></td><td>Red River Gorge</td><td>9</td><td>5</td><td>19</td><td>Yes</td><td>Three neighboring cabins in Birch Hollow, each with a hot tub</td></tr>'
        h += '</tbody></table></div>'
    h += '<div class="grid">' + ''.join(card(k) for k in g['homes']) + '</div></div></section>'
    h += f'<section class="sec"><div class="wrap two"><div><p class="kick">BEST FOR</p><h2>{"Who these homes suit" if len(g["homes"])>1 else "Who it suits"}</h2><ul class="feats one">' + ''.join(f'<li>{E(b)}</li>' for b in g['best']) + '</ul>'
    h += ('<p style="margin-top:26px"><a class="btn big" href="' + g['homes'][0] + '.html#book">Check dates &amp; book direct</a></p></div>') if len(g['homes'])==1 else '<p style="margin-top:26px"><a class="btn big" href="#ghomes">Pick a home &amp; check dates</a></p></div>'
    h += '<div><h3 class="todoh">Questions travelers ask</h3>' + faq_html(g['faq']) + '</div></div></section>'
    if slug in M:
        h += '<section class="sec alt"><div class="wrap"><p class="kick">GUESTS SAY</p><div class="qg">'
        for k in g['homes']:
            for n, t in P[k]['rev'][:2 if len(g['homes'])>1 else 3]: h += quote(n, t, k)
        h += '</div></div></section>'
    h += FOOT
    return h

# ---------- PROPERTY
PLANS={'bourbon-street':('About 6,000 sq ft over three floors. Main floor: parlor, music room, billiard room, speakeasy bar, poker room, kitchen, dining for 10, office and gym. Second floor: five bedrooms. Third floor: two more bedrooms and a sitting room.',[('plan1.jpg','Main floor'),('plan2.jpg','Second floor: 5 bedrooms'),('plan3.jpg','Third floor: 2 bedrooms')]),'bourbon-loft':'Two floors, about 900 sq ft. Downstairs: kitchen, living room, dining area and half bath. Upstairs: a 17 x 19 ft bedroom, full bath, laundry and walk-in closet.','historic-loft':'Two floors. Downstairs: kitchen, living room, dining area and half bath. Upstairs: an 18 x 20 ft bedroom, full bath, laundry and walk-in closet.'}
def glance(k, city):
    p = P[k]; area, mq, drives = LOC[k]
    rows = [('Location', f"{area}, Kentucky"), ('Space', f"{p['br']} bedrooms · {fmt(p['ba'])} baths · {p['beds']} beds"), ('Sleeps', f"Up to {p['guests']} guests"),
            ('Pets', 'Welcome (up to 2, $50 each)' if p['pets'] else 'Not allowed'), ('Hot tub', 'Yes, private' if k in HOTTUB else 'No'),
            ('Check-in / checkout', ('4:00 pm' if k=='trinity' else '3:00 pm') + ' / ' + ('11:00 am' if k=='woodleigh' else '10:00 am')), ('Best for', BEST[k]), ('Nearby', '; '.join(drives)),
            ('Book direct', 'Live calendar on this page, always cheaper than Airbnb or Vrbo')]
    return ''.join(f'<dt>{E(a)}</dt><dd>{E(b)}</dd>' for a,b in rows)

def prop(k):
    p = P[k]; m = M[p['market']]
    from faqdata import CANCEL
    pf = PROP_FAQ[k] + [CANCEL]
    city = {'red-river-gorge':'Stanton','bourbon-trail':'Frankfort' if 'Frankfort' in p['town'] else 'Versailles','herrington-lake':'Harrodsburg'}[p['market']]
    url = f"{SITE}/{k}"
    amen = p['feats']
    vr = {"@context":"https://schema.org","@type":"VacationRental","@id":url+"#rental","name":p['name'],"url":url,"identifier":HOSP_ID[k],"description":p['lede'],
          "image":[f"img/{k}/{i:02d}.jpg" for i in range(min(10,p['n']))],
          "amenityFeature":[{"@type":"LocationFeatureSpecification","name":a,"value":True} for a in amen],
          "knowsLanguage":"en",
          "address":{"@type":"PostalAddress","addressLocality":city,"addressRegion":"KY","addressCountry":"US"},
          "containsPlace":{"@type":"Accommodation","occupancy":{"@type":"QuantitativeValue","maxValue":p['guests']},"numberOfBedrooms":p['br'],"numberOfBathroomsTotal":p['ba']},
          "petsAllowed":p['pets'],"checkinTime":"15:00","checkoutTime":"11:00" if k=='woodleigh' else "10:00",
          "brand":{"@id":SITE+"/#org"}}
    bc = crumbs_ld([("Home",SITE+"/"),(G[p['market']]['h1'],f"{SITE}/{p['market']}"),(p['name'],url)])
    h = head(TITLE[k], DESC[k], ld=[vr, bc, faq_ld(pf)])
    imgs = [f'img/{k}/{i:02d}.jpg' for i in range(p['n'])]
    caps = p['caps'] + [''] * 20
    h += f'''<section class="pwrap"><div class="wrap"><p class="crumb dark"><a href="index.html">Home</a> / <a href="{p['market']}.html">{E(m['name'])}</a> / {E(p['name'])}</p>
<div class="ptitle"><div><p class="kick">{E(p['town'].upper())}</p><h1>{E(p['name'])}</h1><p class="meta">{p['br']} bedrooms · {fmt(p['ba'])} baths · {p['beds']} beds · sleeps {p['guests']}{' · pet friendly' if p['pets'] else ''}</p></div>
<a class="btn big" href="#book">Check dates &amp; book</a></div>
<div class="mosaic">'''
    for i in range(min(5, p['n'])):
        h += f'<a href="{imgs[i]}" data-lb="{imgs[i]}" data-cap="{E(caps[i])}" class="m{i}"><img {"" if i==0 else "loading=lazy "}src="{imgs[i]}" alt="{E(caps[i] or p["name"])}"></a>'
    h += f'<button class="all" onclick="lbOpen(0)">View all {p["n"]} photos</button></div></div></section>'
    h += f'''<section class="sec tight"><div class="wrap pgrid"><div class="pmain"><p class="lead">{E(p['lede'])}</p>
<h2 class="ph2">At a glance</h2><dl class="glance">{glance(k, city)}</dl>
<h2 class="ph2">What you'll love</h2><ul class="feats">''' + ''.join(f'<li>{E(f)}</li>' for f in p['feats']) + '</ul>'
    if p['note']: h += f'<p class="note">Good to know: {E(p["note"])}</p>'
    if p.get('video'):
        h += '<h2 class="ph2">Take the walkthrough</h2><div class="vid"><video controls playsinline preload="none" poster="video/bs-poster.jpg" src="video/bourbon-street-walkthrough.mp4"></video><p class="meta">A 70-second tour, from the front porch to a bird&rsquo;s-eye view of downtown.</p></div>'
    h += '<h2 class="ph2">More photos</h2><div class="thumbs">'
    for i in range(5, p['n']):
        h += f'<a href="{imgs[i]}" data-lb="{imgs[i]}" data-cap="{E(caps[i])}"><img loading="lazy" src="{imgs[i]}" alt="{E(caps[i] or p["name"])}"></a>'
    area, mq, drives = LOC[k]
    h += '</div>'
    if k in PLANS:
        text, files = PLANS[k] if isinstance(PLANS[k], tuple) else (PLANS[k], [('plan.jpg','Floor plan')])
        h += '<h2 class="ph2">Floor plan</h2><div class="plans">' + ''.join(f'<figure><a class="plan" href="img/{k}/{f}" data-lb="img/{k}/{f}" data-cap="{E(c)}"><img loading="lazy" src="img/{k}/{f}" alt="{E(p["name"])} {E(c.lower())}"></a>' + (f'<figcaption>{E(c)}</figcaption>' if len(files)>1 else '') + '</figure>' for f,c in files) + f'</div><p class="meta">{E(text)} Measurements are approximate.</p>'
    h += f'<h2 class="ph2">Where it is</h2><div class="loc"><div><p class="lead" style="font-size:17px">{E(area)}</p><ul class="feats one">' + ''.join(f'<li>{E(d)}</li>' for d in drives) + f'</ul><p class="note">For your privacy and ours, the exact address and arrival directions are sent after you book.</p></div><a class="maplink" href="https://www.google.com/maps/search/?api=1&query={quote_plus(mq)}"><span class="pin">📍</span><b>{E(area)}</b><span>View the area on Google Maps →</span></a></div>'
    if k in LOCAL:
        L = LOCAL[k]
        town = TOWN['gorge' if p['market']=='red-river-gorge' else 'herrington' if p['market']=='herrington-lake' else ('versailles' if k=='woodleigh' else 'frankfort')]
        def href(n): return SITES.get(n) or 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(QUERY.get(n, f'{n} {town}'))
        def lst(items): return '<ul class="fav">' + ''.join(f'<li><b><a href="{E(href(n))}" target="_blank" rel="noopener">{E(n)}</a></b><span>{E(d)}</span><em>{E(t)}</em></li>' for n,d,t in items) + '</ul>'
        h += f'<h2 class="ph2">Local favorites</h2><p class="meta">{E(L["intro"])}</p><div class="favs"><div><h4>Eat &amp; drink</h4>{lst(L["eat"])}</div><div><h4>See &amp; do</h4>{lst(L["do"])}</div></div>'
    h += '<h2 class="ph2">Good to know</h2>' + faq_html(pf)
    h += '<h2 class="ph2">Guest reviews</h2><div class="qg one">' + ''.join(quote(n, t) for n, t in p['rev']) + '</div></div>'
    h += f'''<aside class="book"><div class="bx"><p class="kick">BOOK DIRECT</p><h3>{E(p['name'])}</h3><p class="meta">{p['br']} bd · {fmt(p['ba'])} ba · sleeps {p['guests']}</p>
<div class="perk">✓ {E(PERK)}</div><div class="perk">✓ Always cheaper than Airbnb or Vrbo</div><div class="perk">✓ Message your host directly</div>
<div class="hwidget" id="book"><script src="https://cdn.hsptb.com/direct-booking-widget/widget-loader.prod.js" data-site-uuid="{HOSP_SITE}" data-property-id="{HOSP_ID[k]}" data-theme="multi"></script><div class="hw-ph"><b>Pick your dates</b><div class="hw-row"><span>Check-in</span><span>Checkout</span></div><div class="hw-row"><span>Guests</span></div><p>Live calendar, pricing and secure checkout load here on the live site.</p></div></div>
<p class="fine">Live calendar and secure checkout by Hospitable.</p></div><a class="hostcard" href="index.html#host"><img src="img/shane-sm.jpg" alt="Shane O'Donley"><span><b>Hosted by Shane O&rsquo;Donley</b><small>Kentucky local · 4 years hosting · replies fast</small></span></a></aside></div></section>'''
    others = [x for x in m['homes'] if x != k] or [x for x in P if x != k][:3]
    h += f'<section class="sec alt"><div class="wrap"><p class="kick">{"MORE IN " + E(m["name"].upper()) if len(m["homes"])>1 else "MORE KENTUCKY STAYS"}</p><div class="grid">' + ''.join(card(x) for x in others[:3]) + '</div></div></section>'
    h += f'<a class="mbar" href="#book"><span><b>{E(p["name"])}</b><small>{p["br"]} bd · sleeps {p["guests"]} · book direct</small></span><em>Check dates</em></a><script>(function(){{var b=document.querySelector(".mbar"),t=document.getElementById("book");if(b&&t&&"IntersectionObserver" in window){{new IntersectionObserver(function(e){{b.style.display=e[0].isIntersecting?"none":""}}).observe(t)}}}})()</script>'
    h += FOOT
    return h

TERMS = [
 ('Booking and payment', ["These terms apply to stays booked directly on southernhospitalitygroup.co. Stays booked through Airbnb or Vrbo follow that platform's terms and the policies shown on its listing.", "Reservations and payments are processed securely through Hospitable. The total shown at checkout, including the nightly rate, cleaning fee, service fee and taxes, is the amount you pay. By completing a booking you agree to these terms and to the house rules for your home.", "The person who books is responsible for everyone in their group and for following these terms and the house rules."]),
 ('Cancellations', ["Cancel at least 30 days before check-in for a full refund.", "Cancel 7 to 30 days before check-in and 50% of the nightly total is refunded.", "Cancellations less than 7 days before check-in are non-refundable.", "We strongly recommend travel insurance. Kentucky weather can change quickly, and we can't offer refunds for weather, road conditions or travel delays outside our control."]),
 ('Changes', ["To change your dates or number of guests, message us or call or text 859-229-1524. Changes depend on availability and may change the price."]),
 ('Check-in and checkout', ["Check-in is 3:00 pm (4:00 pm at the Trinity A-Frame). Checkout is 10:00 am, except The Woodleigh, which checks out at 11:00 am.", "Early check-in or late checkout depends on the calendar. Direct bookings get a complimentary early check-in or late checkout of up to 2 hours when available; anything beyond that must be agreed with us in advance.", "Check-in is contactless. Your door code and arrival directions are sent before your stay. Please don't share your code with anyone outside your group."]),
 ('Length of stay and occupancy', ["The maximum stay is 28 nights.", "The number of guests may not exceed the maximum occupancy listed for your home, and only registered guests may stay overnight. Visitors beyond your registered group need our approval in advance."]),
 ('House rules', ["No parties or events.", "No smoking or vaping inside any home. You're welcome to smoke outside on a deck or porch; please dispose of butts properly. Evidence of smoking inside may result in a cleaning fee (for example, $300 at the Trinity A-Frame).", "Please be respectful of neighbors, and leave furniture where you found it.", "Follow any posted rules for hot tubs, fire pits, docks, game rooms and other amenities."]),
 ('Pets', ["Pets are welcome only at our three Red River Gorge cabins (Bootlegger's Retreat, NEO and Trinity A-Frame): up to 2 pets, $50 per pet per stay. Please include pets in your booking.", "Pets must be crated if left alone inside, kept off the furniture and never left unattended outside. Owners are responsible for any damage caused by their pets.", "Our Bourbon Trail homes and Herrington Haven are pet free."]),
 ('Damage and responsibility', ["You are responsible for any damage to the home or its contents caused by you, your guests or your pets beyond normal wear and tear, and for any extra cleaning needed beyond a normal turnover. Please tell us right away if something breaks; accidents happen and we'd rather know.", "Amenities such as hot tubs, fire pits, grills, docks, stairs and game equipment are used at your own risk. Please supervise children at all times. Some homes have steep driveways, gravel roads, ladders or steep steps; these are noted on each home's page.", "We're not responsible for lost or stolen belongings, or for interruptions to utilities, Wi-Fi, cell service or streaming services outside our control. We'll always do our best to fix any problem quickly."]),
 ('Access and maintenance', ["We or our team may need to enter the home during your stay for urgent maintenance or safety reasons. Whenever possible, we'll contact you first."]),
 ('Contact', ["Questions about these terms or your booking? Call or text Shane at 859-229-1524."]),
]

def termspage():
    h = head('Terms of Stay | Southern Hospitality Group', 'Booking, payment, cancellation, check-in, pet and house-rule terms for stays booked directly with Southern Hospitality Group in Kentucky.')
    h += '<section class="sec"><div class="wrap" style="max-width:860px"><p class="crumb dark"><a href="index.html">Home</a> / Terms of Stay</p><p class="kick">TERMS OF STAY</p><h1 style="font-size:clamp(38px,5vw,60px);margin-bottom:18px">The fine print, in plain words.</h1><p class="meta">Last updated November 20, 2026</p>'
    for t, ps in TERMS:
        h += f'<h2 style="font-size:clamp(22px,2.6vw,30px);margin:40px 0 14px">{E(t)}</h2>' + ''.join(f'<p class="lead" style="font-size:17px;margin-bottom:12px">{E(x)}</p>' for x in ps)
    h += '</div></section>' + FOOT
    return h

def faqpage():
    h = head('FAQ | Southern Hospitality Group', 'Check-in, checkout, pets, cancellations and more for our Red River Gorge cabins, Bourbon Trail homes and Herrington Lake house.', ld=[faq_ld(SITE_FAQ)])
    h += '<section class="sec"><div class="wrap two"><div><p class="crumb dark"><a href="index.html">Home</a> / FAQ</p><p class="kick">FREQUENTLY ASKED</p><h1 style="font-size:clamp(40px,5vw,64px);margin-bottom:22px">Good to know.</h1><p class="lead">Short answers to the questions guests ask most. Each home\'s page has its own details too.</p>'
    h += f'<p class="lead" style="margin-top:22px">Still have a question? Call or text <a href="tel:+18592291524">{PHONE}</a>.</p></div>' + faq_html(SITE_FAQ) + '</div></section>'
    h += FOOT
    return h

def searchpage():
    h = head('Search available stays | Southern Hospitality Group', 'Search live availability across our Red River Gorge cabins, Bourbon Trail homes and Herrington Lake house.')
    h += f'<section class="sec"><div class="wrap"><p class="kick">AVAILABLE STAYS</p><h1 style="font-size:clamp(36px,5vw,60px);margin-bottom:28px">Find your dates.</h1><div class="hresults"><script src="{SEARCH_JS}"></script><hospitable-direct-mps identifier="{SEARCH_ID}" type="custom"></hospitable-direct-mps><p class="hs-note">Live search loads here on the live site. Browse <a href="index.html#homes">all 8 homes</a> in the meantime.</p></div></div></section>'
    h += FOOT
    return h

os.makedirs(OUT, exist_ok=True)
open(f'{OUT}/search.html','w').write(searchpage())
open(f'{OUT}/faq.html','w').write(faqpage())
open(f'{OUT}/terms.html','w').write(termspage())
open(f'{OUT}/index.html','w').write(home())
for g in G: open(f'{OUT}/{g}.html','w').write(guide(g))
for k in P: open(f'{OUT}/{k}.html','w').write(prop(k))

# ---------- ARTICLES (trip guides)
def article(a):
    url = f"{SITE}/{a['slug']}"
    ld = {"@context":"https://schema.org","@type":"Article","headline":a['h1'],"description":a['desc'],"datePublished":a['date'],"dateModified":a['date'],"image":f"img/{a['hero']}","author":{"@type":"Organization","name":"Southern Hospitality Group"},"publisher":{"@type":"Organization","name":"Southern Hospitality Group"},"mainEntityOfPage":url}
    h = head(a['title'], a['desc'], ld=[ld, crumbs_ld([("Home",SITE+"/"),("Trip guides",SITE+"/trip-guides"),(a['h1'],url)])])
    h += f'''<section class="hero short"><img src="img/{a['hero']}" alt="{E(a['h1'])}"><div class="shade"></div><div class="wrap hc"><p class="crumb"><a href="index.html">Home</a> / <a href="trip-guides.html">Trip guides</a></p>
<p class="kick">{E(a['kicker'].upper())}</p><h1>{E(a['h1'])}</h1><p class="sub">{E(a['sub'])}</p></div></section>
<section class="sec"><div class="wrap" style="max-width:820px">'''
    for i,(hd, paras) in enumerate(a['body']):
        h += f'<h2{" style=margin-top:40px" if i else ""}>{E(hd)}</h2>' + ''.join(f'<p class="lead" style="margin-top:14px">{E(t)}</p>' for t in paras)
    h += '</div></section>'
    if a.get('homes'):
        h += '<section class="sec alt"><div class="wrap"><p class="kick">WHERE TO STAY</p><h2>Our homes for this trip</h2><div class="grid">' + ''.join(card(k) for k in a['homes']) + '</div></div></section>'
    h += FOOT
    return h

def guides_index():
    t = 'Kentucky Trip Guides | Southern Hospitality Group'
    d = 'Trip ideas and local tips for Red River Gorge, the Kentucky Bourbon Trail, horse country and Herrington Lake, from the hosts at Southern Hospitality Group.'
    h = head(t, d, ld=[crumbs_ld([("Home",SITE+"/"),("Trip guides",SITE+"/trip-guides")])])
    h += '<section class="sec"><div class="wrap"><p class="kick">TRIP GUIDES</p><h1>Kentucky trip ideas from your hosts</h1><div class="grid" style="margin-top:28px">'
    for a in ARTICLES:
        h += f'<a class="card" href="{a["slug"]}.html"><div class="ph"><img loading="lazy" src="img/{a["hero"]}" alt="{E(a["h1"])}"></div><div class="cb"><p class="town">{E(a["kicker"])}</p><h3>{E(a["h1"])}</h3><p class="tag">{E(a["sub"])}</p><span class="go">Read the guide →</span></div></a>'
    h += '</div></div></section>' + FOOT
    return h

for a in ARTICLES: open(f'{OUT}/{a["slug"]}.html','w').write(article(a))
open(f'{OUT}/trip-guides.html','w').write(guides_index())
print('ok', os.listdir(OUT))

# ---- SEO post-processing: clean URLs, canonical, Open Graph, sitemap, robots ----
import re, glob, datetime
pages = []
from PIL import Image
_dims = {}
def _dim(src):
    if src not in _dims:
        try: _dims[src] = Image.open(f'{OUT}/{src}').size
        except Exception: _dims[src] = None
    return _dims[src]
for fp in sorted(f for f in glob.glob(f'{OUT}/*.html') if not os.path.basename(f).startswith(('google','404'))):
    slug = os.path.basename(fp)[:-5]
    url = SITE + '/' if slug == 'index' else f'{SITE}/{slug}'
    h = open(fp).read()
    h = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1) or ""}"', h)
    h = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1)}{m.group(2) or ""}"', h)
    title = re.search(r'<title>(.*?)</title>', h).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    _A = {a['slug']:a for a in ARTICLES}
    img = (f"img/{_A[slug]['hero']}" if slug in _A else f'img/{slug}/00.jpg' if slug in P else (f"img/{G[slug]['hero']}" if slug in G else 'img/bootleggers/00.jpg'))
    tags = (f'<link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="Southern Hospitality Group">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{img}">'
            f'<meta name="twitter:card" content="summary_large_image">')
    if slug == 'search': tags += '<meta name="robots" content="noindex">'
    h = h.replace('</title>', '</title>' + tags, 1)
    def _ld(m):
        j = m.group(0).replace('"img/', f'"{SITE}/img/')
        return j
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', _ld, h, flags=re.S)
    def _wh(m):
        tag = m.group(0)
        if ' width=' in tag: return tag
        sm = re.search(r'src="(img/[^"]+)"', tag)
        d = _dim(sm.group(1)) if sm else None
        return tag.replace('<img ', f'<img width="{d[0]}" height="{d[1]}" ', 1) if d else tag
    h = re.sub(r'<img [^>]*>', _wh, h)
    open(fp, 'w').write(h)
    if slug != 'search': pages.append((url, 'weekly' if slug=='index' else 'monthly', '1.0' if slug=='index' else ('0.9' if slug in P else '0.7')))
today = datetime.date.today().isoformat()
open(f'{OUT}/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n' for u,c,p in pages) + '</urlset>\n')
open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\nDisallow: /search\n\nSitemap: {SITE}/sitemap.xml\n')
print('seo ok', len(pages))

open(f'{OUT}/llms.txt','w').write("""# Southern Hospitality Group

> Locally hosted vacation rentals in Kentucky, bookable directly at https://www.southernhospitalitygroup.co. Booking direct is always cheaper than the same stay on Airbnb or Vrbo. Hosted by Shane O'Donley and team (Airbnb Superhost, 850+ reviews, 4.96 average). Call or text 859-229-1524.

## Homes
""" + "".join(f"- [{p['name']}]({SITE}/{k}): {p['town']}. {p['br']} bedrooms, {fmt(p['ba'])} baths, sleeps {p['guests']}{', pet friendly' if p['pets'] else ''}. {HL[k]}.\n" for k,p in P.items()) + """
## Trip guides
""" + "".join(f"- [{g['h1']}]({SITE}/{s_}): {g['desc']}\n" for s_,g in G.items()) + f"""
## More
- [FAQ]({SITE}/faq): check-in, pets, cancellations, booking direct.
""")
print('llms ok')

# ---- Redirects for URLs from the old Hospitable-hosted site ----
def stub(path, target, title):
    url = SITE + target
    d = os.path.join(OUT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="p:domain_verify" content="579e0f4fb4aa7a1666019bee12486320"/><title>{E(title)} | Southern Hospitality Group</title>
<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url={target}"><meta name="robots" content="noindex,follow">
<script>location.replace("{target}"+location.hash)</script></head><body><p>This page has moved: <a href="{target}">{E(title)}</a>.</p></body></html>''')
OLD = {'about': '/#host', 'contact': '/faq', 'sitemap': '/', 'properties': '/#homes', 'search-results': '/search', 'blog': '/'}
for o, t in OLD.items(): stub(o, t, 'Southern Hospitality Group')
oldmap = {}
for k, p in P.items():
    rest = p['book'].split('/property/')[1]          # "<id>/<slug>"
    pid = rest.split('/')[0]
    oldmap[pid] = k
    for pre in ('property', 'book'):
        stub(f'{pre}/{rest}', f'/{k}', p['name'])
        stub(f'{pre}/{pid}', f'/{k}', p['name'])
# Friendly 404 that also forwards any other old /property/<id>/... or /book/<id>/... link
m = json.dumps(oldmap)
h = head('Page not found | Southern Hospitality Group', 'This page has moved. Browse our Red River Gorge cabins, Bourbon Trail homes and Herrington Lake house.')
h += '''<script>(function(){var m=''' + m + ''',p=location.pathname.split('/').filter(Boolean);if((p[0]==='property'||p[0]==='book')&&m[p[1]]){location.replace('/'+m[p[1]]);return}var o={about:'/#host',contact:'/faq',sitemap:'/',properties:'/#homes'};if(p.length===1&&o[p[0]])location.replace(o[p[0]])})();</script>
<section class="sec"><div class="wrap"><p class="kick">PAGE NOT FOUND</p><h1 style="font-size:clamp(36px,5vw,60px);margin-bottom:22px">That page moved.</h1><p class="lead">We rebuilt our site. Try one of these:</p><div class="guides" style="margin-top:22px"><a href="/">Home</a><a href="/red-river-gorge">Red River Gorge cabins</a><a href="/bourbon-trail">Frankfort &amp; Bourbon Trail</a><a href="/herrington-lake">Herrington Lake</a><a href="/large-group-rentals">Large groups</a><a href="/search">Search dates</a><a href="/faq">FAQ</a></div></div></section>''' + FOOT
h = re.sub(r'href="index\.html(#[^"]*)?"', lambda mm: f'href="/{mm.group(1) or ""}"', h)
h = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda mm: f'href="/{mm.group(1)}{mm.group(2) or ""}"', h)
h = h.replace('href="style.css', 'href="/style.css').replace('<title>', '<meta name="robots" content="noindex"><title>', 1)
open(f'{OUT}/404.html', 'w').write(h)
print('redirects ok', len(oldmap))
