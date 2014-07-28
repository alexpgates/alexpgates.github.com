Title: Working Smarter with Alfred: Workflows
Date: 2014-07-27
Summary: Learn how to use Alfred workflows help you automate tasks and get your work done quicker.
Slug: working-smarter-with-alfred-workflows
Tags: Alfred, Productivity, Mac

<div class="row text-center">
    <img src="/static/images/alfred-logo.png" alt="Alfred logo">
</div>

### Hello again, Alfred!

This is the second post in a series on <a href="http://alfredapp.com">Alfred</a>, a productivity application for Mac OS X.

For an overview of Alfred, and to learn about using Custom Web Searches to work smarter and faster, <a href="/blog/2014/07/working-smarter-with-alfred-custom-web-searches">read my first post in this series here</a>.

In this post, I'm assuming you're already familiar with Alfred and have <a href="https://buy.alfredapp.com/">purchased the Powerpack</a>.

### Understanding Workflows

An Alfred Workflow is basically a chain of things that you want to do on your Mac incredibly quickly. 

The possibilities are honestly unlimited, so this makes it a bit complicated to actually explain what a Workflow _is_ and how powerful they are. Instead, I'll just _show_ you a few of the Alfred Workflows I use to make my day-to-day tasks easier and more efficient.

These are just a few examples that barely scratch the surface, but it should be enough to help you grasp the general idea of Alfred Workflows and get excited about downloading or creating your own Workflows to make your job easier.

### Don't reinvent the wheel

There are many super smart Alfred users who have created many wonderful Workflows and shared them on the web. Websites like <a href="http://www.alfredworkflow.com/">alfredworkflow.com</a> and <a href="http://www.packal.org/">Packal</a> have hundreds of available Workflows to download for free. You can also find lots of great resources in the <a href="http://www.alfredforum.com/forum/3-share-your-workflows/">Alfred Forum</a>.

If you search around, you'll likely find something that will shave off some time for things you frequently do on your Mac. I've downloaded a few of these, and the following list are Workflows I use quite frequently.

<br>
#### Super fast GIF Workflow!

Pack's team is distributed, so we rely on <a href="https://campfirenow.com/">Campfire</a> as a central place for communication. Sometimes text just isn't the best avenue to convey emotion, so we (perhaps too frequently) harness the power of animated gifs.

<div class="row text-center">
    <img src="/static/images/alfred-dog-pug-wut.gif" class="margin" alt="pug wut">
</div>

It's <a href="https://dl.dropboxusercontent.com/u/2227623/gifs/obama-kidding-me.gif">a proven fact</a> that the hilarity of a gif reply diminishes over time, so it's absolutely essential to be quick with your response. <a href="http://destroytoday.com/blog/gif-workflow/">Jonnie Hallman's GIF Workflow</a> can help.

This Workflow allows you to harvest your own GIFs and store them in a public folder on Dropbox. Just add keywords in the filename when you save a GIF, then search for them when you run the Workflow. <a href="https://dl.dropboxusercontent.com/u/2227623/gifs/kim-yes-clapping-good-joke.gif">Brilliant</a>!

<hr>

#### Don't forget about emoji!

<a href="https://github.com/carlosgaldino/alfred-emoji-workflow">Carlos Galdino's Alfred Emoji Workflow</a> is the emoji equivalent of the gif Workflow. Sometimes a reply just calls for something small, so Carlos has you covered.

<div class="row text-center">
    <a href="https://github.com/carlosgaldino/alfred-emoji-workflow"><img src="/static/images/alfred-emoji-workflow.png" alt="emoji workflow"></a>
</div>

<hr>

#### iMessage to a friend

<a href="http://eay.cc/projects/alfred-workflow-imessage-to-friend/">Stefan Grund</a> made a really handy iMessage Workflow to quickly send an iMessage right from Alfred. It's not directly integrated to your Address Book, so you need to manually set up the Workflow for contacts that you message frequently.

<div class="row text-center">
    <a href="http://eay.cc/projects/alfred-workflow-imessage-to-friend/"><img src="/static/images/alfred-imessage.png" alt="imessage workflow"></a>
</div>

Like some other plugins, a little setup in the beginning saves lots of time down the road.

<hr>

#### Phillips Hue Controller

<a href="https://github.com/benknight">Benjamin Knight</a> wrote a Workflow to control <a href="http://meethue.com/">Phillips Hue lights</a>. I've written <a href="/blog/tag/philips-hue.html"> a couple posts</a> about Philips Hue bulbs, and anyone who knows me knows I get really excited about these things.

<div class="row text-center">
    <a href="https://github.com/benknight"><img src="/static/images/alfred-hue-overview.png" alt="hue workflow"></a>
</div>

With Ben's Workflow, I'm able to control the lights in my house right inside Alfred. 

<hr>

### Custom Alfred Workflows

Clearly, most of the Workflows that I've downloaded really don't do too much to make my _work_ more efficient. But that doesn't mean _all_ Workflows are just for fun and games.

Here are a few Workflows I've put together to help around the office.

<br>
#### Email the Pack Team

<div class="row text-center">
    <img src="/static/images/alfred-workflow-setup.png" alt="Alfred Workflow Setup">
</div>

There are five us on the Pack team, so every time I wanted to send an email to everyone on the team, I'd _cmd+tab_ to my mail program (Sparrow), _cmd+n_ to open a new email. Then I'd start typing each team member's name, followed by tab, until all four were in the _To_ field. _At best_, that's 14 keystrokes. 

With Alfred, I've reduced it to 2.

I just invoke quicksilver, and begin typing _emailpack_.

<div class="row text-center">
    <img src="/static/images/alfred-email-pack.png" alt="Alfred Email Pack">
</div>

Once Alfred detects what I'm typing, (it usually just takes the _e_) I just hit enter.

Immediately, a new message window is opened with everyone's email address in the _To_ field.

<div class="row text-center">
    <img src="/static/images/alfred-email-pack-sparrow.png" alt="Alfred Email Pack">
</div>

I can invoke this Workflow from _anywhere_ on my Mac. In other words, I don't need to be in Sparrow (or even have Sparrow open, for that matter).

This Workflow is a bit more complicated to set up, since it requires a little Applescript to make it happen. 

Begin by creating a new blank Workflow, then set your keyword input. For your action, choose _Run Script_. Choose <code>/usr/bin/osascript</code> from the Language dropdown. Then, use this as a guide for creating your own email list:

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

At Pack, we use a task collaboration app we built at <a href="http://whatcheer.com">What Cheer</a> called <a href="http://peprallyapp.com">Pep Rally</a>. Unfortunately Pep Rally isn't available to the public, but it's a tool that we rely on heavily.

One feature of Pep Rally I frequently use is the inbox. Adding an item to my inbox is a quick way to document a task quickly when I'm in the middle of completing another task. 

Instead of opening Pep Rally and clicking on my inbox tab, I simply invoke Alfred, begin typing _inbox_, then hit tab and start typing what I need to remember. 

<div class="row text-center">
    <img src="/static/images/alfred-peprally-inbox.png" alt="Alfred Pep Rally Inbox">
</div>

<a href="http://velvetcache.org">Hobbs</a> added a Python command line tool to interact with Pep Rally, so for this Workflow action I execute a BASH script to use it by selecting <code>/bin/bash</code> from the Language dropdown.

    :::bash
    created=`/Applications/MAMP/htdocs/Pep-Rally/peprally_python/scripts/peprally inbox:create "{query}"`

    if [[ $created == *TRUE* ]]
    then
    echo "{query}"
    fi

For this Workflow, I added a Post Notification output so Growl alerts me that my task was successfully added. To do this, I clicked the _+_ symbol, then clicked _Outputs_ &#10142; _Post Notification_. With Alfred, you can output to Growl or Notification Center, and set a custom title and text for the notification. Using <code>{query}</code> in either of these fields will use the output from the previous action.

<div class="row text-center">
    <img src="/static/images/alfred-growl-peprally.png" alt="Alfred Growl">
</div>

This one is a little vague, I know. But I chose to include it so you can see an example of extending Alfred to a CLI and to your own tools.

<hr>



### Go!

As I mentioned in <a href="/blog/2014/07/working-smarter-with-alfred-custom-web-searches">my first post about Alfred Custom Web Searches</a>, you should add helpful Workflows slowly. If you add too many new tools at once, you'll never keep track of them all and all the potential efficiencies will be lost.

Soon these new tools will become second nature, and all the seconds you save in your day-to-day will definitely add up.

Do you have an Alfred Workflow you'd like me to check out? <a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#97;&#108;&#101;&#120;&#64;&#119;&#104;&#97;&#116;&#99;&#104;&#101;&#101;&#114;&#46;&#99;&#111;&#109;">Let me know</a>!