Title: What's Under the Hood?
Date: 2013-06-22
Summary: From Markdown to static HTML, by way of Pelican, Jinja2, Bootstrap, and more.
Slug: whats-under-the-hood
Tags: Pelican, Bootstrap, Github

Many months ago, [a buddy](http://christopherkollars.com) sent me [this article](http://kylerush.net/blog/meet-the-obama-campaigns-250-million-fundraising-platform/) written by [Kyle Rush](http://kylerush.net/) about the technology stack behind the Obama campaign's fundraising platform. Kyle mentioned [Jekyll](http://jekyllrb.com/), a static site generator written in Ruby, and recommended giving it a whirl to create fast, simple websites without the need for a bloated CMS.

I'm not a Ruby guy, and despite making an attempt to get things working properly on my Mac, I backed out of the rabbit hole and instead decided to give [Pelican](http://docs.getpelican.com/en/latest/) a try. It's written in Python, and uses the [Jinja2](http://jinja.pocoo.org/docs/) templating language.  

To get up and running, I followed [this](http://martinbrochhaus.com/pelican.html) handy (but now outdated) guide by [Martin Brochhaus](http://martinbrochhaus.com). <small>(Note: Here's Martin's [updated guide](http://martinbrochhaus.com/pelican2.html).)</small>

After getting everything configured and deployed to [Github Pages](http://pages.github.com/), I started working on an *ugly* theme based off the default Pelican template. I never finished it. Then, [What Cheer](http://whatcheer.com) announced our [transition](http://whatcheer.com/pack/) to [Pack](http://packlove.com), and things got pretty busy for a while.

### Fast-forward six months

I picked things up again a couple weeks ago after reading about the [updates](http://blog.getpelican.com/pelican-3.2-released.html) to Pelican. I began piecing together this current theme using <a href="http://twitter.github.io/bootstrap/">Bootstrap</a>. (I haven't worked with any other front-end frameworks, but I've been using it on [some stuff](http://news.packlove.com/admin/) I'm building with Pack, and also a [Yearbook project](http://yearbooks.edison-pta.org) for the PTA.) I like it. Since the bulk of my front-end development happened between 1996 and 2004, it's allowed me get back in the game pretty quickly.

### A complete list of tools

* [Pelican](http://docs.getpelican.com/en/latest/) - A static site generator written in Python
* [Jinja2](http://jinja.pocoo.org/docs/) - A templating language for Python used to create Pelican themes
* [Markdown](http://daringfireball.net/projects/markdown/) - A lightweight markup language to quickly write content
* [Bootstrap](http://twitter.github.io/bootstrap/) - A  front-end framework - helpful for responsive development
* [Google Fonts](http://www.google.com/fonts/) - For nicer fonts
* [Pygments](http://pygments.org/) - For syntax highlighting
* [Typogrify](https://github.com/getpelican/pelican-typogrify) - To fancy up the text a bit
* [Fabric](http://docs.fabfile.org/en/1.6/) - To streamline deployment
* [Github Pages](http://pages.github.com/) - Fast, reliable hosting 

### The process

####Install Pelican

Again, here's Martin Brochhaus' [updated guide](http://martinbrochhaus.com/pelican2.html).


####Create your first post

Include your metadata at the top. <small>(More [here](http://docs.getpelican.com/en/latest/getting_started.html#writing-content-using-pelican))</small>

	:::Text
	Title: What's Under the Hood?
	Date: 2013-06-22
	Summary: From Markdown to static HTML, by way of Pelican, Jinja2, Bootstrap, and more.
	Slug: whats-under-the-hood
	Tags: Pelican, Boostrap, Github

	Many months ago, [a buddy](http://christopherkollars.com) sent me ...

####Preview!

I use two separate config files for Pelican. One uses relative URLs (so I can preview locally), and the other generates absolute URLs for production. To avoid typing the full Pelican commands to generate the output, I use this fabfile.py:

	:::bash
	"""Fabric tasks for generating HTML"""
	from __future__ import with_statement

	from fabric.api import lcd, local, settings

	def pub():
	    """Re-generates the output using absolute urls."""
	    local('pelican . -o ../ -s settings.py')

	def dev():
	    """Re-generates the output using relative urls."""
	    local('pelican . -o ../ -s local_settings.py')

####Preview locally

	:::bash
	fab dev

Then I check it out on my local vhost.

####Deploy

If everything looks okay, I generate the HTML with absolute URLs.

	:::bash
	fab pub


Then simply commit my changes to Github.

###So far, so good

I'm the kind of guy who will spend 15 hours hacking my Wii to play 15 minutes of old NES games. I'm optimistic that an easy, fast, and fun way to manage a new blog will encourage me to get my act together and finally start writing somewhat regularly.

###Get the theme
Fork the current version of this theme on [Github](https://github.com/alexpgates/alexpgates.github.com/tree/master/themes/apg). It really wasn't built with with sharing in mind, but you're free to use what you can!

<div class="row text-center top-padding download">
    <a class="btn btn-large" href="https://github.com/alexpgates/alexpgates.github.com/tree/master/themes/apg">Download this theme <i class="fa fa-arrow-circle-right"></i></a>
</div>