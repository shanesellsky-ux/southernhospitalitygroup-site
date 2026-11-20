# Local favorites per property. Sourced from Shane's Folio guidebooks (gorge, Frankfort)
# and research (Versailles, Herrington). No exact distances: they could reveal the address.
GORGE = {
 'intro': "Our go-to spots around the Gorge, the same list we send booked guests.",
 'eat': [
  ("Miguel's Pizza", "The legendary climbers' pizza stop near Slade", "About 15 min"),
  ("Red River Rockhouse", "Burgers and craft beer, a Gorge favorite", "About 20 min"),
  ("Thatcher Barbecue Company", "Smoked meats, close to the cabins", "About 10 min"),
  ("Toad's BARn & Grill", "Casual bar and grill, the closest dinner option", "About 10 min"),
  ("La Cabana", "Mexican, a reliable family dinner", "About 15 min"),
  ("Sky Bridge Station", "Food and drinks near the Sky Bridge trailhead", "About 25 min"),
  ("RedPoint Barbeque", "Barbecue on the far side of the Gorge", "About 30 min"),
 ],
 'do': [
  ("Red River Gorge", "Natural arches, ridge hikes, climbing and the Sky Bridge", "About 20 min"),
  ("Natural Bridge Sky Lift", "Chairlift up to Natural Bridge State Resort Park", "About 15 min"),
  ("Gorge Underground", "Kayak tours through a flooded limestone mine", "About 20 min"),
  ("Red River Gorge Ziplines", "Zipline canopy tours", "About 25 min"),
  ("Hollerwood Park", "Outdoor park in the Gorge area", "About 15 min"),
 ]}
FRANKFORT = {
 'intro': "Downtown Frankfort is walkable, and Buffalo Trace is five minutes away. These come straight from our guest guidebook.",
 'eat': [
  ("Bourbon on Main", "Bourbon bar and restaurant in the heart of downtown", "Walkable"),
  ("House of Commons: A Bourbon Library", "Cozy bourbon bar", "Walkable"),
  ("The Kentucky Hug", "Bourbon bar with live music", "Walkable"),
  ("Serafini", "Upscale dinner and cocktails", "Walkable"),
  ("The Brown Barrel", "Southern comfort food and bourbon", "Walkable"),
  ("Goodwood Frankfort", "Brewpub and burgers", "Walkable"),
  ("Sig Luscher Brewery", "Local craft brewery", "Walkable"),
  ("The Ashbrook", "Dinner spot downtown", "Walkable"),
  ("Dicey Riley's Irish Pub", "Pub food and pints", "Walkable"),
  ("Buddy's Pizza", "Pizza, an easy family night", "Walkable"),
  ("Mi Fiesta", "Mexican", "Walkable"),
  ("Main Street Diner", "Breakfast and lunch", "Walkable"),
  ("Hoggy's Ice Cream", "Dessert after dinner", "Walkable"),
  ("Cypress & Oak", "Dinner a short drive away", "About 5 min"),
  ("The Stave", "Restaurant near Castle & Key on the Glenns Creek road", "About 15 min"),
 ],
 'do': [
  ("Buffalo Trace Distillery", "Tours at one of the most famous distilleries anywhere", "About 5 min"),
  ("J. Mattingly 1845 Distillery", "Craft distillery with blending experiences", "About 5 min"),
  ("Castle & Key Distillery", "A restored castle distillery with gardens", "About 15 min"),
  ("Woodford Reserve Distillery", "Classic Bourbon Trail stop in horse country", "About 20 min"),
  ("Whiskey Thief Distilling Co.", "Craft distillery near Lawrenceburg", "About 20 min"),
  ("The Bourbon Boat", "Kentucky River cruises from downtown", "Walkable"),
  ("River View Park", "Riverfront walking path", "Walkable"),
  ("Daniel Boone's Grave", "Frankfort Cemetery overlook above the river", "About 5 min"),
  ("Salato Wildlife Education Center", "Easy trails and native wildlife", "About 10 min"),
  ("Keeneland", "Live racing in April and October", "About 35 min"),
  ("Horse Farm Tours", "Guided visits to Thoroughbred farms", "About 40 min"),
 ]}
VERSAILLES = {
 'intro': "Downtown Versailles is right outside, with Midway and the distilleries a short drive away.",
 'eat': [
  ("Black Squirrel", "Breakfast and lunch on Main Street", "Downtown"),
  ("Amsden Station", "Restaurant and bar in the old police station", "Downtown"),
  ("Vallozzi's", "Italian, good for a nicer night out", "Downtown"),
  ("Wallace Station Deli & Bakery", "Sandwiches and baked goods in horse country", "About 15 min"),
  ("Heirloom", "Contemporary dinner in historic Midway", "About 15 min"),
  ("Castle Farm at The Kentucky Castle", "Farm-to-table dining at the castle", "About 10 min"),
 ],
 'do': [
  ("Woodford Reserve Distillery", "Tours and tastings at one of the Bourbon Trail's best-known stops", "About 15 min"),
  ("Keeneland", "Live racing in April and October, and morning workouts", "About 15 min"),
  ("Rail Explorers", "Pedal rail bikes past the Kentucky River and horse farms", "About 10 min"),
  ("Castle & Key Distillery", "A restored castle distillery with gardens", "About 20 min"),
  ("Downtown Midway", "Shops, antiques and restaurants along the railroad", "About 15 min"),
  ("Equus Run Vineyards", "Winery in Midway", "About 20 min"),
 ]}
HERRINGTON = {
 'intro': "The lake is the main event, but there's plenty within a short drive.",
 'eat': [
  ("Beaumont Inn", "Historic inn in Harrodsburg known for Kentucky country ham", "About 20 min"),
  ("Downtown Harrodsburg", "Kentucky's oldest town, with cafés and shops", "About 20 min"),
  ("Downtown Danville", "Restaurants and the Norton Center for the Arts", "About 25 min"),
 ],
 'do': [
  ("Herrington Lake", "Boating, fishing, swimming and kayaking from your own dock", "Out back"),
  ("Pandora Marina", "Boat rentals near Kennedy Bridge", "Short drive"),
  ("Kamp Kennedy Marina", "Marina on the lake", "Short drive"),
  ("Shaker Village of Pleasant Hill", "Restored Shaker village with trails, farm and dining", "About 25 min"),
  ("Old Fort Harrod State Park", "Pioneer fort replica in Harrodsburg", "About 20 min"),
  ("Wild Turkey Distillery", "Bourbon Trail stop in Lawrenceburg", "About 35 min"),
 ]}
LOCAL = {'bootleggers':GORGE,'neo':GORGE,'trinity':GORGE,'bourbon-loft':FRANKFORT,'historic-loft':FRANKFORT,'bourbon-street':FRANKFORT,'woodleigh':VERSAILLES,'herrington-haven':HERRINGTON}

# Links for local favorites: official sites where confirmed, otherwise a Google Maps search
# (Maps listings carry the business's own website, hours and phone, and don't go stale).
SITES = {
 'Red River Gorge': 'https://www.fs.usda.gov/r08/danielboone/recreation/red-river-gorge',
 'Red River Gorge Ziplines': 'https://www.redrivergorgezipline.com',
 'Hollerwood Park': 'https://www.hollerwoodpark.com',
 'Buffalo Trace Distillery': 'https://www.buffalotracedistillery.com',
 'Castle & Key Distillery': 'https://castleandkey.com',
 'Woodford Reserve Distillery': 'https://www.woodfordreserve.com',
 'Keeneland': 'https://www.keeneland.com',
 'Horse Farm Tours': 'https://www.horsefarmtours.com',
 'Castle Farm at The Kentucky Castle': 'https://thekentuckycastle.com',
 'Rail Explorers': 'https://railexplorers.net',
 'Wallace Station Deli & Bakery': 'https://www.wallacestation.com',
 'Equus Run Vineyards': 'https://www.equusrunvineyards.com',
 'Beaumont Inn': 'https://www.beaumontinn.com',
 'Shaker Village of Pleasant Hill': 'https://shakervillageky.org',
 'Wild Turkey Distillery': 'https://wildturkeybourbon.com',
}
TOWN = {'gorge': 'Slade KY', 'frankfort': 'Frankfort KY', 'versailles': 'Versailles KY', 'herrington': 'Harrodsburg KY'}
QUERY = {
 'Red River Rockhouse': 'Red River Rockhouse Campton KY',
 'Sky Bridge Station': 'Sky Bridge Station Pine Ridge KY',
 'RedPoint Barbeque': 'RedPoint Barbeque Campton KY',
 'Gorge Underground': 'Gorge Underground Rogers KY',
 'Natural Bridge Sky Lift': 'Natural Bridge Sky Lift Slade KY',
 'Cypress & Oak': 'Cypress and Oak restaurant near Frankfort KY',
 'Whiskey Thief Distilling Co.': 'Whiskey Thief Distilling Co Frankfort KY',
 'Daniel Boone\'s Grave': 'Daniel Boone grave Frankfort Cemetery KY',
 'Salato Wildlife Education Center': 'Salato Wildlife Education Center Frankfort KY',
 'Heirloom': 'Heirloom restaurant Midway KY',
 'Downtown Midway': 'Downtown Midway KY',
 'Downtown Harrodsburg': 'Downtown Harrodsburg KY',
 'Downtown Danville': 'Downtown Danville KY',
 'Herrington Lake': 'Herrington Lake KY',
 'Pandora Marina': 'Pandora Marina Herrington Lake KY',
 'Kamp Kennedy Marina': 'Kamp Kennedy Marina Herrington Lake KY',
 'Old Fort Harrod State Park': 'Old Fort Harrod State Park Harrodsburg KY',
 'J. Mattingly 1845 Distillery': 'J. Mattingly 1845 Distillery Frankfort KY',
}
