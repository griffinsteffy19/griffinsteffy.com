---
type: post
title: Investing Alfred Workflow v1
date: 2022-08-21T17:00:00
description: Finding ways to merge my loves of productivity, finance, and technology is always at the front of my mind. I found a way to do that using an app called Alfred.
tags: 
weight: 1
showTableOfContents: false
draft: false
---
After I got my first personal apple computer, I quickly found out about the productivity tool [Alfred](https://www.alfredapp.com). At first I thought it was just a slightly faster spotlight, but after trying to use it as my main source of navigating my computer I realized the benefits of what this tool can provide.

One of the main activities I do on my computer is do investing research. Typically this is looking at financial statements, or browsing through other articles for a company. One site that I frequent the most is the Rule One Toolbox. I found that the time it was taking me to navigate to a specific ticker from whatever other app I was using was consuming more time than I would like. I then set out to create an Alfred workflow that would speed up searching on the toolbox.

If you are familiar with Alfred, you might wonder why I didn’t use the web query feature that comes with the application. In short the reason is that the queries aren’t as simple as they are for other common sites like google.

Example:

TKR: AAPL

RO: https://ruleonetoolbox.com/ticker/NAS:AAPL/company/brief

In order to query both of these websites, it takes knowledge of their trading exchange, which is easily google-able, but for the 10k possible company tickers, I wanted a more automated way of generating the specific URLs. With those requirements I set out to create a script that would generate a JSON file, as well as a CSV file that I would use to populate the argument suggestions for my workflow. The script pulls info from a file downloaded from the SEC, and then searches Yahoo! Finance using a free python package to get the company name, and exchange.

I’ve noticed after using it a bit, that the exchange reported on Yahoo can sometimes be different than the one used for Rule One. However, this isn’t typical with common companies in the US, so for now I ignored those situations and recorded which ones I didn’t process in case I wanted to refer to them later.

The final challenge I had was actually executing the script to process the ten thousand different tickers. At first I was running it on my local PC, but the downside was that I needed to have an internet connection, and be powered on until it finished. Since I was pulling Yahoo! Finance from a free package, it wasn’t the fastest API integration, so it took up to 10 seconds for some companies. After a few days of trying to keep it running on my local machine, I bit the bullet and bought a remote droplet on Digital Ocean to run the script. Turns out once I figured out how to run it in the background there it was a much easier process to generate the data I needed. I simply committed the final results to my repository, and walla! I was ready to go!

If you are interested in using the workflow you can view the code on GitHub here.