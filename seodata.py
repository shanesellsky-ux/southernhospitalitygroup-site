# SEO copy: titles, descriptions, ideal guests, and destination/guide pages.
# Facts only from the property data already on the site.

TITLE = {
 'bootleggers': "Bootlegger's Retreat: Red River Gorge Cabin with Hot Tub & Game Room",
 'neo': 'NEO: Modern Red River Gorge Cabin with Private Hot Tub',
 'trinity': 'Trinity A-Frame: Red River Gorge Cabin with Hot Tub, Sleeps 6',
 'bourbon-street': 'Bourbon Street: Frankfort Mansion for 14 Near Buffalo Trace',
 'woodleigh': 'The Woodleigh: Versailles, KY Home Near Keeneland, Sleeps 8',
 'bourbon-loft': 'Bourbon Trail Loft: Downtown Frankfort Loft Near Buffalo Trace',
 'historic-loft': 'Historic Loft: Frankfort, KY Loft for Two with King Bed',
 'herrington-haven': 'Herrington Haven: Herrington Lake House with Dock & Hot Tub',
}

DESC = {
 'bootleggers': '4-bedroom Red River Gorge cabin near Slade with a private hot tub, game room and arcade, fire pit and EV charger. Sleeps 8, pets welcome. Book direct.',
 'neo': 'Modern 2-bedroom cabin 10 minutes from Slade with a private hot tub, wall of windows, fire pit and free EV charger. Sleeps 5, dogs welcome. Book direct.',
 'trinity': '3-bedroom A-frame near Slade and Natural Bridge with a sunken hot tub, shuffleboard, arcade and fire pit. Sleeps 6, pets welcome. Book direct.',
 'bourbon-street': '1904 mansion in downtown Frankfort for groups up to 14: 7 bedrooms, speakeasy bar, billiards, theater. About 5 minutes to Buffalo Trace. Book direct.',
 'woodleigh': '1903 home in downtown Versailles, KY with 4 bedrooms and a covered patio with fire pit, about 15 minutes to Keeneland. Sleeps 8. Book direct.',
 'bourbon-loft': "Two-story brick loft on St. Clair Street in downtown Frankfort, 1.6 miles from Buffalo Trace. Two queen beds, sleeps 4. Walk to dinner. Book direct.",
 'historic-loft': "Remodeled loft for two in Frankfort's entertainment district: king bed, exposed brick, dedicated parking, close to Buffalo Trace. Book direct.",
 'herrington-haven': 'Lakefront home on Herrington Lake near Harrodsburg with a private dock and boat slip, hot tub and game room. 3 bedrooms, sleeps 10. Book direct.',
}

BEST = {
 'bootleggers': 'Families and friend groups up to 8 who want a game room for downtime; dog owners',
 'neo': 'Couples, honeymooners and small families up to 5; dog owners',
 'trinity': 'Families and small groups up to 6; hikers and climbers who want a hot tub after a day in the Gorge',
 'bourbon-street': "Bourbon Trail groups, family reunions and friends' weekends up to 14",
 'woodleigh': 'Families and Keeneland or Bourbon Trail groups up to 8; remote workers (dedicated workspace)',
 'bourbon-loft': 'Couples or two couples touring distilleries who want to walk to dinner',
 'historic-loft': 'Couples on a bourbon weekend',
 'herrington-haven': 'Families and groups up to 10 who want time on the water',
}

HOTTUB = {'bootleggers', 'neo', 'trinity', 'herrington-haven'}

# Short "highlight" per home for comparison tables
HL = {
 'bootleggers': 'Hot tub, game room with arcade, fire pit, EV charger',
 'neo': 'Private hot tub, wall of windows, fire pit, EV charger',
 'trinity': 'Sunken hot tub, shuffleboard and arcade, fire pit, EV charger',
 'bourbon-street': 'Speakeasy bar, billiards, poker room, theater, walk to dinner',
 'woodleigh': 'Covered patio with fire pit and outdoor TV, 1903 hardwoods',
 'bourbon-loft': 'Exposed brick, two queen beds, walk to restaurants and live music',
 'historic-loft': 'King bed, exposed brick, dedicated parking space',
 'herrington-haven': 'Private dock and boat slip, hot tub, game room with pool table',
}

BOOK_Q = ('Can I book directly instead of through Airbnb or Vrbo?',
  "Yes. Every home on this site has a live calendar and secure checkout, so you can book directly with us. Booking here is always cheaper than the same stay on Airbnb or Vrbo, and direct guests get a complimentary early check-in or late checkout of up to 2 hours when available.")

# Destination and guide pages. 'col' = extra column for the comparison table.
G = {
 'red-river-gorge': dict(
   title='Red River Gorge Cabin Rentals with Hot Tubs | Book Direct',
   desc='Three pet-friendly Red River Gorge cabins near Slade and Natural Bridge, each with a private hot tub, fire pit and free EV charger. Sleep 5 to 8. Book direct.',
   h1='Red River Gorge cabin rentals', kicker='Stanton · Slade · Rosslyn', hero='bootleggers/15.jpg',
   sub='Three cabins in the woods about 10 minutes from Slade. Every one has a private hot tub, a fire pit and free EV charging.',
   homes=['bootleggers', 'trinity', 'neo'],
   intro=["The Red River Gorge is in the Daniel Boone National Forest in eastern Kentucky, known for its natural sandstone arches, high cliffs and some of the best sport climbing in the country. Natural Bridge State Resort Park sits just south of Slade, and Miguel's Pizza is the climbers' base camp.",
          "Our three cabins, Bootlegger's Retreat, Trinity A-Frame and NEO, are in Birch Hollow between Stanton and Slade, about 10 minutes from the Gorge. Every one has a private hot tub, a fire pit, a free Level 2 EV charger and room for up to two pets."],
   callout="Traveling with a bigger crew? All three cabins are in Birch Hollow and sleep 19 together (8 + 6 + 5). Book each on its page, or call or text 859-229-1524 and we'll help you line up the dates.",
   todo=[('Natural Bridge State Resort Park', 'Hike up to the arch or ride the skylift. A short drive from the cabins.'),
         ('Rock climbing', "World-class sport routes, with Miguel's Pizza as base camp."),
         ('Gorge Underground', 'Kayak a flooded mine by headlamp.'),
         ('Sky Bridge & Auxier Ridge', 'Two of the best short hikes for big views.'),
         ('Nada Tunnel', 'The one-lane tunnel on the scenic drive into the Gorge.')],
   best=['Hikers and climbers who want a hot tub at the end of the day', 'Couples and honeymooners (NEO)', 'Families (Trinity A-Frame and Bootlegger\'s Retreat)', 'Dog owners: all three cabins are pet friendly', 'EV drivers: free Level 2 charger at every cabin'],
   faq=[('Where should a group stay when visiting the Red River Gorge?', "Bootlegger's Retreat sleeps 8 across 4 bedrooms and has a game room for downtime. For a bigger group, book all three of our cabins: they're in the same hollow between Stanton and Slade and sleep 19 together."),
        ('Are there family cabins near Natural Bridge State Resort Park?', "Yes. All three cabins are about 10 minutes from Slade, with Natural Bridge a short drive beyond. Trinity A-Frame (3 bedrooms, sleeps 6) and Bootlegger's Retreat (4 bedrooms, sleeps 8, with a gated kids' loft) work well for families."),
        ('Do the Red River Gorge cabins have hot tubs?', 'Yes. Every cabin has its own private hot tub on the deck. Our Herrington Lake house has one too.'),
        ('Can I bring my dog?', 'Yes. All three Gorge cabins welcome up to 2 pets for $50 per pet per stay.'),
        ('Do I need 4WD to reach the cabins?', 'The cabins sit up a gravel road in Birch Hollow. AWD or 4WD is recommended in good weather and required in ice or snow.'),
        ('Is there cell service?', 'Cell signal can be spotty in the Gorge. Every cabin has Wi-Fi, so turn on Wi-Fi calling.'),
        BOOK_Q]),
 'bourbon-trail': dict(
   title='Frankfort, KY & Bourbon Trail Vacation Rentals | Book Direct',
   desc='Stay in downtown Frankfort minutes from Buffalo Trace or in historic Versailles near Keeneland: a 1904 mansion for 14, a home for 8 and two lofts. Book direct.',
   h1='Frankfort & Bourbon Trail vacation rentals', kicker='Frankfort · Versailles', hero='bourbon-street/00.jpg',
   sub="A 1904 mansion with a speakeasy and theater, two lofts in Frankfort's entertainment district, and a 1903 home in Versailles near Keeneland.",
   homes=['bourbon-street', 'woodleigh', 'bourbon-loft', 'historic-loft'],
   intro=["Frankfort, Kentucky's capital, sits on the Kentucky River in the middle of bourbon country. Buffalo Trace is at the edge of downtown, Castle & Key is a short drive up McCracken Pike, Woodford Reserve is in neighboring Woodford County, and Keeneland is just outside Lexington.",
          "We host four homes here. Bourbon Street is a 1904 mansion on Main Street for groups up to 14. The Bourbon Trail Loft and Historic Loft are on St. Clair Street, a short walk from restaurants, bars and live music. The Woodleigh is a 1903 home in downtown Versailles, about 15 minutes from Keeneland."],
   callout='Three of the four homes are in walkable downtown Frankfort, so after a day of tastings you can leave the car parked and walk to dinner.',
   todo=[('Buffalo Trace Distillery', 'About five minutes from downtown Frankfort. Tours are popular, so reserve ahead.'),
         ('Castle & Key', 'A restored castle distillery on McCracken Pike.'),
         ('Woodford Reserve', 'Rolling horse country, about 11 miles from Frankfort.'),
         ('Keeneland', 'Live racing in April and October, about 15 minutes from The Woodleigh.'),
         ('Downtown Frankfort', 'Restaurants, bars, the Old State Capitol and a riverside trail.')],
   best=["Bourbon Trail groups and family reunions up to 14 (Bourbon Street)", 'Keeneland weekends and families up to 8 (The Woodleigh)', 'Couples and small groups who want to walk everywhere (the lofts)'],
   faq=[('What are good vacation rentals for a Bourbon Trail trip?', 'It depends on your group. Bourbon Street sleeps 14 in downtown Frankfort, about 5 minutes from Buffalo Trace. The Woodleigh in Versailles sleeps 8 and is close to Woodford Reserve and Keeneland. The Bourbon Trail Loft (sleeps 4) and Historic Loft (sleeps 2) put couples within walking distance of restaurants and bars.'),
        ('Can I walk to restaurants and bars?', 'Yes from Bourbon Street and both lofts, which are in downtown Frankfort. The Woodleigh is in downtown Versailles.'),
        ('How far is Buffalo Trace?', 'About 5 minutes from Bourbon Street and about 1.6 miles from the two lofts. From The Woodleigh in Versailles it is roughly a 25-minute drive.'),
        ('Which home is closest to Keeneland?', 'The Woodleigh in Versailles, about 15 minutes away.'),
        ('Are the Bourbon Trail homes pet friendly?', 'No. Our Bourbon Trail homes are pet free. Our three Red River Gorge cabins welcome pets.'),
        BOOK_Q]),
 'herrington-lake': dict(
   title='Herrington Lake Rental with Private Dock & Hot Tub | Book Direct',
   desc='Herrington Haven is a lakefront home near Harrodsburg, KY with a private dock and boat slip, hot tub, fire pit and game room. 3 bedrooms, sleeps 10. Book direct.',
   h1='Herrington Lake vacation rental', kicker='Harrodsburg', hero='herrington-haven/01.jpg',
   sub='Herrington Haven sits right on the water with a private dock, a hot tub, big lake views and room for 10.',
   homes=['herrington-haven'],
   intro=["Herrington Lake is one of Kentucky's deepest lakes, with limestone bluffs and quiet coves. Spend the day boating, fishing or swimming off your own dock, and the evening around the fire pit. Historic Harrodsburg and Shaker Village of Pleasant Hill are close by.",
          'Herrington Haven is a three-story lake house right on the water, with a private dock and boat slip, a hot tub, a fire pit on the lawn and a game room with a pool table. It has 3 bedrooms and 3.5 baths and sleeps 10.'],
   callout='Bring the boat: Herrington Haven has its own slip at the private dock.',
   todo=[('Boat, swim & fish', 'Right from your private dock.'),
         ('Shaker Village of Pleasant Hill', 'Trails, farm-to-table dining and history.'),
         ('Historic Harrodsburg', "Kentucky's oldest town."),
         ('Bourbon Trail', 'Danville and Lawrenceburg distilleries within reach.')],
   best=['Families and groups up to 10', 'Boaters and anglers', 'Anyone who wants a hot tub with a lake view'],
   faq=[('Does Herrington Haven have a private dock?', 'Yes, a private dock with a boat slip and chaise lounges. The steps down to the dock are steep and narrow.'),
        ('Is there a hot tub?', 'Yes, plus a fire pit on the lawn and a game room with a pool table.'),
        ('How many people does it sleep?', 'Up to 10, with 3 bedrooms and 3.5 baths.'),
        ('How far is it from Lexington?', 'Within about an hour.'),
        ('Are pets allowed?', 'No. Herrington Haven is pet free.'),
        BOOK_Q]),
 'large-group-rentals': dict(
   title='Large Group Vacation Rentals in Kentucky | Sleeps 8 to 14',
   desc='Kentucky homes for big groups: a 1904 Frankfort mansion for 14, a Herrington Lake house for 10, and Red River Gorge cabins that sleep 19 together. Book direct.',
   h1='Large group vacation rentals in Kentucky', kicker='Groups of 8 or more', hero='bourbon-street/01.jpg',
   sub='Family reunions, friend trips and Bourbon Trail weekends: our homes for 8 to 14 guests, plus three Gorge cabins that sleep 19 together.',
   homes=['bourbon-street', 'herrington-haven', 'bootleggers', 'woodleigh'], col='where',
   intro=["Planning a family reunion, a friends' trip to the Bourbon Trail or a big weekend in the Red River Gorge? These are our homes built for groups of 8 or more. Each has room to gather and enough beds and baths to go around.",
          "Bourbon Street is the biggest: a 1904 mansion in downtown Frankfort with 7 bedrooms, a speakeasy bar, billiards, a poker room and a theater. Herrington Haven puts 10 people on the lake with a private dock. Bootlegger's Retreat and The Woodleigh each sleep 8."],
   callout="Need room for more than 14? Our three Red River Gorge cabins, Bootlegger's Retreat, Trinity A-Frame and NEO, are in the same hollow and sleep 19 together. Call or text 859-229-1524 and we'll help you line up the dates.",
   todo=[('No parties or events', 'Our homes are for groups staying together, not parties or events.'),
         ('Stairs at Bourbon Street', 'All bedrooms and full baths are upstairs.'),
         ('Gorge driving', 'AWD or 4WD is recommended for the cabins, and required in ice or snow.'),
         ('Pets', 'Only the three Red River Gorge cabins are pet friendly.')],
   todo_head='Good to know for groups',
   best=['Family reunions', "Friends' trips and milestone birthdays", 'Bourbon Trail and Keeneland groups', 'Lake weekends'],
   faq=[('What is the largest home?', 'Bourbon Street in downtown Frankfort: 7 bedrooms and 3.5 baths for up to 14 guests.'),
        ('Where can a large family stay near Buffalo Trace?', 'Bourbon Street sleeps 14 and is about 5 minutes from Buffalo Trace, in walkable downtown Frankfort.'),
        ('Where can a big group stay in the Red River Gorge?', "Book our three cabins in Birch Hollow together for up to 19 guests, or Bootlegger's Retreat alone for up to 8."),
        ('Are parties or events allowed?', 'No. Our homes are not available for parties or events.'),
        ('Can I book more than one home directly?', 'Yes. Book each home on its own page, or call or text 859-229-1524 and we will help you coordinate dates.'),
        BOOK_Q]),
 'buffalo-trace-lodging': dict(
   title='Vacation Rentals Near Buffalo Trace Distillery | Frankfort, KY',
   desc='Stay minutes from Buffalo Trace in Frankfort, KY: a 1904 mansion for 14 about 5 minutes away and two downtown lofts 1.6 miles away. Book direct.',
   h1='Vacation rentals near Buffalo Trace Distillery', kicker='Frankfort, Kentucky', hero='bourbon-street/21.jpg',
   sub='Three homes in walkable downtown Frankfort, a few minutes from Buffalo Trace, plus a historic home in Versailles.',
   homes=['bourbon-street', 'bourbon-loft', 'historic-loft', 'woodleigh'], col='bt',
   intro=["Buffalo Trace Distillery sits on the Kentucky River at the north edge of Frankfort. Three of our homes are a few minutes from it in downtown Frankfort, so you can tour in the afternoon and walk to dinner at night.",
          'Bourbon Street, a 1904 mansion for up to 14, is about 5 minutes away. The Bourbon Trail Loft (sleeps 4) and Historic Loft (sleeps 2) are on St. Clair Street, about 1.6 miles away. The Woodleigh in Versailles is roughly 25 minutes by car and closer to Woodford Reserve and Keeneland.'],
   callout='Tours at Buffalo Trace are popular. Reserve yours before you book your dates, and plan a designated driver or a ride for tasting days.',
   todo=[('Buffalo Trace Distillery', 'About 5 minutes from Bourbon Street.'),
         ('Castle & Key', 'A restored castle distillery on McCracken Pike.'),
         ('Woodford Reserve', 'About 11 miles from Frankfort.'),
         ('Lawrenceburg distilleries', 'Four Roses and Wild Turkey are a short drive southwest.')],
   todo_head='Make it a bourbon weekend',
   best=['Large families and groups up to 14 (Bourbon Street)', 'Couples (Historic Loft)', 'Two couples (Bourbon Trail Loft)'],
   faq=[('How close are your homes to Buffalo Trace?', 'Bourbon Street is about 5 minutes away. The two lofts on St. Clair Street are about 1.6 miles away. The Woodleigh in Versailles is roughly 25 minutes by car.'),
        ('Where can a large family stay near Buffalo Trace?', 'Bourbon Street: 7 bedrooms, 3.5 baths, sleeps 14, in downtown Frankfort.'),
        ('What is a good place for a couple near Buffalo Trace?', 'The Historic Loft: a remodeled loft for two with a king bed and a dedicated parking space, in walking distance of restaurants and bars.'),
        ('What other distilleries are nearby?', 'Castle & Key is a short drive up McCracken Pike, Woodford Reserve is about 11 miles from Frankfort, and Four Roses and Wild Turkey are in nearby Lawrenceburg.'),
        BOOK_Q]),
}

# Distance-to-Buffalo-Trace column text
BT = {'bourbon-street': 'About 5 minutes', 'bourbon-loft': 'About 1.6 miles', 'historic-loft': 'About 1.6 miles', 'woodleigh': 'Roughly 25 minutes'}
WHERE = {'bourbon-street': 'Downtown Frankfort', 'herrington-haven': 'Herrington Lake', 'bootleggers': 'Red River Gorge', 'woodleigh': 'Versailles'}

SITE_DIRECT_FAQ = [
 ('Can I book these homes directly?', 'Yes. Every home on this site has a live calendar and secure checkout. Booking direct is always cheaper than the same stay on Airbnb or Vrbo.'),
 ('What are the benefits of booking directly with Southern Hospitality Group?', 'Our best price, a complimentary early check-in or late checkout of up to 2 hours when available, and a direct line to your local hosts instead of a call center.'),
 ('Is booking direct secure?', 'Yes. Reservations and payments on this site run through Hospitable, the same system that manages our calendars on Airbnb and Vrbo, with secure online payment.'),
]
