# Southern Hospitality Group website: source

This branch holds the generator. The `main` branch holds the published site (GitHub Pages, www.southernhospitalitygroup.co).

## Rebuild and publish
```
git clone -b source https://github.com/shanesellsky-ux/southernhospitalitygroup-site site
git clone -b main   https://github.com/shanesellsky-ux/southernhospitalitygroup-site site/out   # style.css and img/ live here
cd site && python3 build.py          # rewrites the HTML, sitemap, llms.txt, redirects in out/
cd out && git add -A && git commit -m "..." && git push          # publish
```
Commit changes to build.py / *data.py back to this `source` branch too.

## Files
- build.py: page templates, nav, schema, redirects, sitemap. Hand-edited CSS is out/style.css (main branch).
- seodata.py: titles, descriptions, destination/guide pages. faqdata.py: FAQs. localdata.py: local favorites + their links (SITES).
- src/: original photos per home; out/img/ holds the web-sized copies.

## Rules
- No exact addresses, door codes or Wi-Fi on the site. Pets only at the 3 Gorge cabins. No Booking.com.
- Don't say Shane owns all 8 homes ("my team and I host"). Don't use stay@southernhospitalitygroup.co.
- Herrington Haven has a hot tub (4 hot tub homes). Photos: Kylie Whiseman (PoppyCoast Photography).
