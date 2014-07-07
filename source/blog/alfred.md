Title: Working Smarter, with Alfred
Date: 2014-07-03
Summary: How I use Alfred to make work (and play) more efficient. 
Slug: working-smarter-with-alfred
Tags: Productivity, Mac
Status: draft

<div class="row text-center">
    <img src="/static/images/alfred-logo.png" alt="Alfred logo">
</div>

### Hello Alfred!

<a href="http://alfredapp.com">Alfred</a> is a productivity application for Mac OS X.

Out of the box, it's a tremendously useful tool that helps you quickly launch apps with a few keystrokes or self-assigned hotkeys. You can use Alfred to perform quick web searches other little things, like calculations.

<div class="row text-center">
    <img src="/static/images/alfred-calculator.png" alt="Alfred calculator">
</div>

### Upgrade, seriously

To get the most out of Alfred, you need to <a href="http://www.alfredapp.com/powerpack/">buy the Powerpack</a>. The Powerpack gives you the ability to create and import workflows, access clipboard history, manage a snippet library, create custom web searches, and import beautiful custom themes (basically everything I'm covering in this article). Without question, the Powerpack is absolutely worth it. It will pay for itself with the time you save. 

### Quick results with Custom Web Searches

Alfred makes it very easy to open frequently used websites and perform searches on many popular sites or _any_ site that accepts query parameters for searches. 

<div class="row text-center">
    <img src="/static/images/alfred-web-search.png" alt="Alfred Pack Admin">
</div>
<hr>
#### Quickly access frequently used websites

While working on <a href="http://packdog.com">Pack</a>, I frequently open our admin site. Instead of cmd+tabing to Chrome and clicking a bookmark or typing the URL, I simply invoke Alfred (option+space) and begin typing _packadmin_. As soon as Alfred recognizes what I'm typing, I hit enter and Chrome brings up the admin site. 

<div class="row text-center">
    <img src="/static/images/alfred-pack-admin.png" alt="Alfred Pack Admin">
</div>

Opening frequently-used websites is incredibly fast and simple with Alfred, no matter which app you are currently using on your Mac.
<hr>
#### Perform searches in a jiffy

The Pack admin site gives us a search tool to find dogs by name and users by name or email address. This is something I do multiple times per day.

Instead of opening the admin site and performing a search from a search field, Alfred allows me to skip the middleman and go directly to the search results.

To search for a dog, I simply invoke Alfred using my Alfred hotkey (option+space) and type _dog_ followed by a tab, and the name of the dog I'm looking for.

<div class="row text-center">
    <img src="/static/images/alfred-pack-dogs.png" alt="Alfred Pack Dog Search">
</div>

To search for a user, I start typing _human_ then tab, then the name or email address of the Pack user I want to find.

<div class="row text-center">
    <img src="/static/images/alfred-pack-humans.png" alt="Alfred Pack Human Search">
</div>

After hitting enter, I'm taken directly to the search results page in Pack admin. 
<hr>
#### Create your own Custom Web Search

Setting up a custom web search is easy. From the Web Search setting under the Features tab, just click Add Custom Search on the bottom right of the screen. <code>{query}</code> is the variable that is passed from the Alfred window.

Dropping in an icon will keep things looking nice and fancy, too.

<div class="row text-center">
    <img src="/static/images/alfred-custom-search-setup.png" alt="Alfred Pack Admin">
</div>
<hr>

### Creating Workflows to make your job easier

A workflow is basically a chain of things that you want to do on your Mac incredibly quickly. 

The possibilities are honestly unlimited, so this makes it a bit complicated to actually explain what a workflow _is_ and how powerful they are. Instead, I'll just _show_ you a few of the Alfred workflows I use to make my day-to-day tasks easier and more efficient.

These are just a few examples that barely scratch the surface, but it should be enough to help you grasp the general idea of Alfred workflows and get excited about creating your own workflows to make your job easier.

<div class="row text-center">
    <img src="/static/images/alfred-workflow-setup.png" alt="Alfred Workflow Setup">
</div>

<hr>

#### Email the Pack Team

There are five us on the Pack team, so every time I wanted to send an email to everyone on the team, I'd cmd+tab to my mail program (Sparrow), cmd+n to open a new email. Then I'd start typing each team member's name, followed by tab, until all five were in the TO field. _At best_, that's 14 keystrokes. 

With Alfred, I've reduced it to 2.

I just invoke quicksilver, and begin typing _emailpack_.

<div class="row text-center">
    <img src="/static/images/alfred-email-pack.png" alt="Alfred Email Pack">
</div>

Once Alfred detects what I'm typing (it usually just takes the _e_ I hit enter.

Immediately, a new message window is opened with everyone's email address in the TO field.

I can invoke this workflow from _anywhere_ on my Mac. In other words, I don't need to be in Sparrow (or even have Sparrow open, for that matter).

<div class="row text-center">
    <img src="/static/images/alfred-email-pack-sparrow.png" alt="Alfred Email Pack">
</div>

This workflow is a bit more complicated to set up, since it requires a little Applescript to make it happen. 

Begin by creating a new blank workflow, then set your keyword input. For your action, choose _Run Script_. Choose <code>/usr/bin/osascript</code> from the Language dropdown. Then, use this as a guide for creating your own email list:

    :::AppleScript
    tell application "Sparrow"
        activate
        set theMessage to make new outgoing message with properties {subject:"", content:""}
        tell theMessage
            make new to recipient at end of to recipients with properties {name:"Fred", address:"fred@flintstone.com"}
            make new to recipient at end of to recipients with properties {name:"Wilma", address:"wilma@flintstone.com"}
            make new to recipient at end of to recipients with properties {name:"Barney", address:"barney@rubble.com"}
            make new to recipient at end of to recipients with properties {name:"Betty", address:"betty@rubble.com"}
             compose
        end tell
    end tell

Yes, it takes a bit of time to get this set up initially, but all those saved keystrokes add up over time. Remember, this example is for Sparrow only, but it'd be easy to do something very similar for Mail.app.

<hr>

#### Add an item to my Pep Rally inbox

At Pack, we use a task collaboration app we created at <a href="http://whatcheer.com">What Cheer</a> called <a href="http://peprallyapp.com">Pep Rally</a>. Unfortunately (for you) Pep Rally isn't available to the public, but it's a tool that we rely on heavily.

One feature of Pep Rally I frequently use is the inbox. Adding an item to my inbox is a quick way to document a task quickly when I'm in the middle of completing another task. 

Instead of opening Pep Rally and clicking on my inbox tab, I simply invoke Alfred, begin typing _inbox_, then hit tab and start typing what I need to remember. 

<div class="row text-center">
    <img src="/static/images/alfred-peprally-inbox.png" alt="Alfred Pep Rally Inbox">
</div>

<a href="http://velvetcache.org">Hobbs</a> added a Python command line tool to interact with Pep Rally, so for this workflow action I execute a BASH script to use it by selecting <code>/bin/bash</code> from the Language dropdown.

    :::bash
    created=`/Applications/MAMP/htdocs/Pep-Rally/peprally_python/scripts/peprally inbox:create "{query}"`

    if [[ $created == *TRUE* ]]
    then
    echo "{query}"
    fi

For this workflow, I added a Post Notification output so Growl alerts me that my task was successfully added. To do this, I clicked the _+_ symbol, then clicked _Outputs_ &#10142; _Post Notification_. With Alfred, you can output to Growl or Notification Center, and set a custom title and text for the notification. Using <code>{query}</code> in either of these fields will use the output from the previous action.

<div class="row text-center">
    <img src="/static/images/alfred-growl-peprally.png" alt="Alfred Growl">
</div>

This one is a little vague, I know. But I chose to include it so you can see an example of extending Alfred to a CLI.

<hr>

### Browse and import Workflows shared by other Alfred users

There are many super smart Alfred users who have created many wonderful Workflows and shared them on the web. I haven't spent too much time browsing, but there are a few that I've imported that have been very useful. 

<hr>

#### Super fast GIF Workflow!

Pack's team is distributed, so we rely on <a href="https://campfirenow.com/">Campfire</a> as a central place for communication. Sometimes text just isn't the best avenue to convey emotion, so we (perhaps too frequently) harness the power of animated gifs.

<div class="row text-center">
    <img src="/static/images/alfred-dog-pug-wut.gif" class="margin" alt="pug wut">
</div>

It's <a href="https://dl.dropboxusercontent.com/u/2227623/gifs/obama-kidding-me.gif">a proven fact</a> that the hilarity of a gif reply diminishes over time, so it's absolutely essential to be quick with your response. <a href="http://destroytoday.com/blog/gif-workflow/">Jonnie Hallman's gif Workflow</a> is the right tool for the job.

This Workflow allows you to harvest your own gifs and store them in a public folder on Dropbox. Just add keywords in the filename when you save a gif, then search for them when you run the Workflow. <a href="https://dl.dropboxusercontent.com/u/2227623/gifs/kim-yes-clapping-good-joke.gif">Brilliant</a>! 

<hr>

#### Don't forget about emoji!

<a href="https://github.com/carlosgaldino/alfred-emoji-workflow">Carlos Galdino's Alfred Emoji Workflow</a> is the emoji equivalent of the gif Workflow. Sometimes a reply just calls for something small, so Carlos has you covered.

<div class="row text-center">
    <img src="/static/images/alfred-emoji-workflow.png" alt="emoji workflow">
</div>

<hr>

#### iMessage to a friend

<div class="row text-center">
    <img src="/static/images/alfred-imessage.png" alt="imessage workflow">
</div>

<hr>