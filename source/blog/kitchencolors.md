Title: Strangers, Please Control my Kitchen Lights
Date: 2014-08-10
Summary: It occurred to me that I should probably let strangers from the internet control the lights in my kitchen. (Because why not?)
Slug: strangers-please-control-my-kitchen-lights
Tags: Philips Hue, Node.js, Raspberry Pi, Twitter
OGImage: http://alexpgates.com/static/images/kitchencolors-header.jpg

<div class="row text-center span12">
    <img src="/static/images/kitchencolors-header.jpg" class="margin" width="650">
</div>

### It occurred to me that I should probably let strangers from the internet control the lights in my kitchen.

_(Because why not?)_ 

#### And now you can, by tweeting to <a href="http://twitter.com/kitchencolors">@kitchencolors</a>.
---

During our recent kitchen remodel, I made a special point to build in power outlets for a couple sets of <a href="http://meethue.com/en-us/friends-of-hue/lightstrips/">Philips Hue LightStrips</a>. 

With the <a href="https://ifttt.com/hue">Philips Hue IFTTT channel</a>, these lights have been set to turn on around sundown and turn off at 11pm.

That's perfectly cool and all, but lately I've been itching to _build_ something fun to take advantage of the bigger RGB color range available with the LightStrips.

Finally last night it dawned on me that I should let the internet choose the colors of my kitchen lights. 

### Before I began, I wrote down these three goals:

<ol>
    <li>Make it fast! (No waiting on IFTTT or anything like that.)</li>
    <li>Step out of my PHP comfort zone.</li>
    <li>Power this with my <a href="http://www.raspberrypi.org/">Raspberry Pi</a>.</li>
</ol>

---

#### Make it fast!

The Philips Hue API works by making HTTP requests to a bridge connected to your local network. That, in itself, created some limitations. 

One thought was to schedule a cron job on a machine in my home network to run every minute and hit an endpoint on a public webserver to check for new color changes. That approach seemed pretty wasteful (and still pretty slow, honestly). That, and it'd require building a front-end interface to interact with the app.

So then I thought about using Twitter to handle the color requests, and realized this would a perfect time to try the <a href="https://dev.twitter.com/docs/streaming-apis/streams/user">user stream API</a>, since it seems to be nearly instantaneous.

--- 

#### Step out of my PHP comfort zone

Next I started thinking about how I'd want people to make the color requests. Since <a href="http://developers.meethue.com/">the Hue API</a> accepts X &amp; Y coordinates from the <a href="http://en.wikipedia.org/wiki/CIE_1931_color_space">CIE color space</a>, I knew we would need an easy way to translate casual color requests without being too limiting. In other words, I didn't want to simply hard-code 20 or so colors, because <a href="http://www.newscenter.philips.com/main/standard/news/press/2013/20130807-philips-expands-the-smart-world-of-hue.wpd#.U-gnuNNdU1g">Hue actually supports _16 million_ colors</a>. 

The <a href="https://github.com/bahamas10/hue-cli">Hue command-line interface by bahamas10</a> accepts CSS color names and also hex color values. This tool runs on Node.js, and I was already familiar with it because I've actually been using it for a few months to control my lights from the command-line. (<a href="/static/images/prof.gif">HOYVIN-GLAVIN!</a>).

**I don't have much experience with Node.js, so this seemed like a perfect opportunity to try something new.**

The next task was to figure out how to consume the Twitter user stream API from Node.js. After a little digging, I came across <a href="https://github.com/outadoc/twitter-mentions-pushover">twitter-mentions-pushover</a> by <a href="http://dev.outadoc.fr/">Baptist Candellier</a>. This provided everything I needed to consume my user stream. I just trimmed off the part in the script that sends the tweet to Pushover, removed any @mentions and # symbols, and added the NPM module <a href="https://www.npmjs.org/package/exec">exec()</a> to send the color command to hue-cli. All said and done, I *maybe* wrote 6 lines of code.

---

#### Power this with my Raspberry Pi

Since the node process needs to be constantly running to consume the Twitter stream and pass requests to the Hue bridge, I wanted to keep my power usage low. The Raspberry Pi runs on a simple 5V power supply, and it's completely silent. It runs headless and sits nicely next to my modem, router, and hue bridge. 

<div class="row text-center">
    <img src="/static/images/rpi.jpg" class="margin" width="500">
</div>

Installing a fresh <a href="http://www.raspberrypi.org/downloads/">Raspbian Wheezy image</a> was a breeze. Then I followed <a href="https://learn.adafruit.com/raspberry-pi-hosting-node-red/setting-up-node-dot-js">this guide</a> to set up Node.js.

From NPM, I installed <a href="https://www.npmjs.org/package/hue-cli">hue-cli</a> and <a href="https://www.npmjs.org/package/exec">exec</a>. The other dependencies (<a href="https://www.npmjs.org/package/entities">entities</a>, <a href="https://www.npmjs.org/package/ntwitter">ntwitter</a>, and <a href="https://www.npmjs.org/package/request">request</a>) shipped with <a href="https://github.com/outadoc/twitter-mentions-pushover">twitter-mentions-pushover</a>.

Finally, I created a fork of twitter-mentions-pushover and renamed the project <a href="https://github.com/alexpgates/kitchencolors">Kitchencolors</a>. 

---

### See it in action!

I made a hilariously dramatic video to show how quickly tweets are processed as color.

<div class="videoWrapper">
<iframe src="//player.vimeo.com/video/103095002?title=0&amp;byline=0&amp;portrait=0" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>
<br>
LOL. It was either that or the sound of my dishwasher running.

---

### Give it a try!

To change the colors of my kitchen lights, just send a tweet to <a href="http://twitter.com/kitchencolors">@kitchencolors</a> with a css color name _or_ a hex value.

<div class="row text-center">
    <img src="/static/images/tweet-to-kitchencolors.png" width="438">
</div>

So far, I've had people from all over the United States, England, Brazil, New Zealand, and Panama decide what color my kitchen should be.

---

### Open up your Hue lights to strangers

It's still pretty rough around the edges, but you can <a href="https://github.com/alexpgates/kitchencolors">download the source here</a>! Future updates will include better color parsing to pull colors out of tweets that contain other text. If that sounds like fun, or if you have other feature ideas, please send me a pull request!