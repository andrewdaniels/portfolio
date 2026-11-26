---
title: "ChurchCalls.ai"
client: "ChurchCalls.ai"
years: "2025–26"
year: 2025
category: "Product design, site & app · Claude, GitHub, Cloudflare"
summary: "An AI phone agent for small churches. It picks up when the office can't, answers from the church's own website, texts the details, and sends the calls that need a person straight to staff."
overview: "Every call to your church, answered."
outcome: "Live for churches at one flat price, 9.99 a month."
tagline: "Every call to your church, answered."
cover: "/media/churchcalls-ai/desktop.jpg"
thumbs: ["/media/churchcalls-ai/dashboard.jpg", "/media/churchcalls-ai/value.jpg"]
shots: ["/media/churchcalls-ai/466_2x_shots_so.webp", "/media/churchcalls-ai/530_2x_shots_so.webp", "/media/churchcalls-ai/mobile.jpg", "/media/churchcalls-ai/m1.jpg"]
gallery: "squares"
order: 5
featured: false
link: "https://churchcalls.ai"
draft: false
---

Setup takes an afternoon: forward the church's number, add its website, and the agent is answering calls.

## The problem

Most small churches run on a pastor with six jobs and a part-time office manager, and the phone rings during all of them. When it goes to voicemail, most callers hang up without leaving a message. A first-time visitor who never hears back tries the church down the road. A receptionist or an answering service costs more than a small church can spend.

## What I built

- **An agent that knows the church.** Add the website and it pulls in service times, ministries and staff.
- **Routing from the staff list.** A hospital visit or a crisis rings straight through to the right person, and sales calls are filtered out.
- **Texts during the call.** Addresses, sign-up links and service times arrive while the caller is still talking.
- **A summary after every call.** Who called, what they needed and what to follow up on.

## How it was built

I designed and directed the marketing site and built it with **Claude**. The code and every change live in **GitHub**, and **Cloudflare** puts each push live in seconds. The app itself is built in FlutterFlow with custom APIs. [Read how I build sites with Claude →](/blog/build-your-website-with-claude)

## The homepage, section by section

The hero puts the real dashboard on the page: calls this week, recent calls with written summaries and the minutes meter.

![The ChurchCalls dashboard on desktop and phone](/media/churchcalls-ai/dashboard.jpg)

Six before-and-after pairs describe a week in a small church office, so a pastor sees their own problem before they see a feature.

![Life in a small church office, before and after](/media/churchcalls-ai/before-after.jpg)

Each feature is shown as a small working piece of the product: the call summary, live transfer, the text sent mid-call, question trends, the coverage schedule and Priority Instructions.

![What changes on Monday morning](/media/churchcalls-ai/value.jpg)

Three setup steps, each with the screen it happens on, so setup looks as short as it is.

![Answering calls by this afternoon](/media/churchcalls-ai/setup.jpg)

One plan and one price, with everything it includes.

![One plan, $19.99 a month](/media/churchcalls-ai/pricing.jpg)
