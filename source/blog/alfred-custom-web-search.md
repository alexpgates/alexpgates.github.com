Title: Working Smarter with Alfred: Custom Web Searches
Date: 2014-07-03
Summary: Use custom web searches to quickly launch websites and efficiently search any site, including your own custom admin tools.
Slug: working-smarter-with-alfred-custom-web-searches
Tags: Alfred, Productivity, Mac

<div class="row text-center">
    <img src="/static/images/alfred-logo.png" alt="Alfred logo">
</div>

### Meet Alfred!

<a href="http://alfredapp.com">Alfred</a> is a productivity application for Mac OS X.

Out of the box, it's a tremendously useful tool that helps you quickly launch apps with a few keystrokes or self-assigned hotkeys. 
<div class="row text-center">
    <img src="/static/images/alfred-launch-chrome.png" alt="Launching apps with Alfred">
</div>
You can use Alfred to search all sorts of websites.

<div class="row text-center">
    <img src="/static/images/alfred-search-youtube.png" alt="Search YouTube with Alfred">
</div>

You can even do lots of little things right inside Alfred, like perform quick calculations

<div class="row text-center">
    <img src="/static/images/alfred-calculator.png" alt="Alfred calculator">
</div>

### Step one: buy the Powerpack

To create custom web searches (and get the most out of Alfred), you need to <a href="http://www.alfredapp.com/powerpack/">buy the Powerpack</a>. In addition to creating custom web searches, the Powerpack gives you the ability to create create and import workflows, access clipboard history, manage a snippet library, and import beautiful custom themes.

We'll get to all those other things in later articles in this series. For now, I'll show you how to use custom web searches to make opening and searching _any site_, including your own custom admin tools, much more efficient. 

### Use a custom web search to quickly launch any website

While working on <a href="http://packdog.com">Pack</a>, I frequently open our admin site. Instead of _cmd+tabing_ to Chrome and clicking a bookmark or typing the URL, I simply invoke Alfred (_option+space_) and begin typing _packadmin_. As soon as Alfred recognizes what I'm typing, I hit enter and Chrome brings up the admin site. Like magic.

<div class="row text-center">
    <img src="/static/images/alfred-pack-admin.png" alt="Alfred Pack Admin">
</div>

#### Set it up

To set this up for any website, click on _Web Search_ under the _Features_ tab in Alfred Preferences. Then click _Add Custom Search_ at the bottom right.

Add a URL in the _Search URL_ text box, then assign a title (this will appear in Alfred when you start typing). Then set a keyword (this is what you start typing after invoking Alfred to open the website.) Finally, add a nice icon to keep everything looking fancy.

<div class="row text-center">
    <img src="/static/images/alfred-custom-search-launch-site.png" class="margin" alt="Set up Alfred to quickly launch any website">
</div>

After you click _save_, test it out by invoking Alfred and typing your keyword. Now you'll be able to quickly launch this website no matter where you are on your Mac, even if your browser is closed.

---

### Search in a jiffy

The Pack admin site gives us a search tool to find dogs by name and users by name or email address. This is something I do multiple times per day.

Instead of opening the admin site and performing a search from a search field, Alfred allows me to skip the middleman and go directly to the search results.

To search for a dog, I simply invoke Alfred and type _dog_ followed by a tab, and the name of the dog I'm looking for.

<div class="row text-center">
    <img src="/static/images/alfred-pack-dogs.png" alt="Alfred Pack Dog Search">
</div>

To search for a user, I start typing _human_ then tab, then the name or email address of the Pack user I want to find. After hitting enter, I'm taken directly to the search results.

<div class="row text-center">
    <img src="/static/images/alfred-pack-humans.png" alt="Alfred Pack Human Search">
</div>

#### Set it up

Setting up a custom web search is easy. In order for this to work, though, you need the name of the query parameter used in your search results. In my case, it's <code>search</code>. YouTube, for example, uses <code>search_query</code>. The easiest way to find this is to perform a search using the regular search field, then look at everything that comes after the <code>?</code> in the URL on your results page. You'll find it.

Like the first example, add this in the _Web Search_ pane under the _Features_ tab in Alfred Preferences. Click Add Custom Search on the bottom right of the screen. Then add the URL for your results page in the _Search URL_ field. Use <code>{query}</code> as the variable that is passed from the Alfred window. Finally, set your title, keyword, and icon.

<div class="row text-center">
    <img src="/static/images/alfred-custom-search-setup.png" class="margin" alt="Alfred Pack Admin">
</div>

That's it! Adding custom web searches is a great way to save keystrokes, mouse clicks, and page loads. Plus, when your co-workers notice what you've done, they'll think you're super smart.

<hr>

### Go!

Alfred can do _a lot_ of things to help speed up your workflow. The trick is to take things slowly and add these improvements to your workflow over time. If you try to cram too many things in at once, you'll never remember them all, and you'll easily fall back into old, wasteful habits.

Custom web searches are a perfect first step to learning Alfred. Master this, then you'll be ready for the next article in the _Working Smarter with Alfred_ series: _Workflows._ 