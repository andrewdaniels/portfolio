---
title: "Coffee Notes"
client: "Optimal Coffee Notes"
years: "2021–now"
year: 2021
category: "Personal product · iOS"
summary: "Coffee Notes is a brew journal for specialty-coffee people on iOS. You log each brew with its dose, water, ratio, grind and time, and rate it. The app shows how your brewing is trending and what your friends are brewing. Version 2 is a full redesign: an AI recap of your recent brews, deeper stats, better brewing tools and adding a coffee from a photo of the bag."
overview: "A brew journal for dialing in coffee, and for seeing what your friends are brewing."
outcome: "Live on iOS. Version 2 is being redesigned and rebuilt now."
cover: "/media/coffeenotes/dashboard.webp"
thumbs: ["/media/coffeenotes/stats.webp", "/media/coffeenotes/brew-ratio.webp"]
shots: ["/media/coffeenotes/friends-feed.webp", "/media/coffeenotes/for-you.webp", "/media/coffeenotes/add-coffee.webp", "/media/coffeenotes/scan-bag.webp", "/media/coffeenotes/review-coffee.webp", "/media/coffeenotes/extraction.webp", "/media/coffeenotes/year-in-review.webp", "/media/coffeenotes/dashboard-light.webp"]
gallery: "phones"
order: 8
featured: false
status: "past"
link: ""
draft: false
---

Coffee Notes started as a side project to help me dial in my own brews and grew into a small social app. Version 2 rethinks the whole thing.

- **Dashboard:** an AI recap of your last five brews with one tip, plus a dot-grid chart of each day's ratings and quick stats.
- **Stats:** averages, your best coffees and roasters, your mix of brew methods, and a calendar of the month.
- **Tools:** a brew ratio calculator with measuring-tape sliders, a pour timer, and an extraction calculator that plots EY% and TDS on a brew control chart.
- **Add a coffee:** snap the front and back of the bag and Claude reads the label. You can also paste the roaster's link or search the catalog. Any field it isn't sure about is flagged so you can check it.
- **Friends:** a feed of what friends are brewing. "Brew it like this" copies their recipe into your timer, and you get recommendations from friends.
- **Year in Review:** shareable story cards with your year in brews, your top coffee and a short summary of your palate.

The first version was built in FlutterFlow on Firebase. Version 2 moves the app to plain Flutter, with Claude running in Cloud Functions.
