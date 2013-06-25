Title: What's Under the Hood?
Date: 2013-06-22
Summary: Markdown, Pelican, Jinja2, Twitter Bootstrap, &amp; Github Pages (oh my!)
Slug: whats-under-the-hood
Tags: Markdown, Pelican, Jinja2, Boostrap, Github

Many months ago, [a buddy](http://christopherkollars.com) sent me [this article](http://kylerush.net/blog/meet-the-obama-campaigns-250-million-fundraising-platform/) written by [Kyle Rush](http://kylerush.net/) about the technology stack behind the Obama campaign's (incredible) fundraising platform. Kyle mentioned [Jekyll](http://jekyllrb.com/), a static site generator written in Ruby, and recommended giving it a whirl to create fast, simple websites without the need for a bloated CMS.

I'm not a Ruby guy, and despite making an attempt to get things working properly on my Mac, I backed out of the rabbit hole and instead decided to give [Pelican](http://docs.getpelican.com/en/latest/) a try. It's based on Python, and uses the [Jinja2](http://jinja.pocoo.org/docs/) templating language.  

To get up and running, I followed [this](http://martinbrochhaus.com/pelican.html) handy (but now outdated) guide by [Martin Brochhaus](http://martinbrochhaus.com). (Note: Here's Martin's [updated guide](http://martinbrochhaus.com/pelican2.html). It isn't the same process I'm using now, but it looks nice!)

After getting everything configured and deployed to [Github Pages](http://pages.github.com/), I started working on an *ugly* theme based off the default Pelican template. I never finished it. Then, [What Cheer](http://whatcheer.com) announced our [transition](http://whatcheer.com/pack/) to [Pack](http://packlove.com), and things got pretty busy for a while.

### Fast-forward six months

I picked things up again a couple weeks ago after reading about the [updates](http://blog.getpelican.com/pelican-3.2-released.html) to Pelican. I began piecing together this current theme using <a href="http://twitter.github.io/bootstrap/">Bootstrap</a>. (I haven't worked with any other front-end frameworks, but I've been using it on [some stuff](http://news.packlove.com/admin/) I'm building with Pack, and also a [Yearbook project](http://yearbooks.edison-pta.org) for the PTA.) I like it. Since the bulk of my front-end development happened between 1996 and 2004, it's allowed me get back in the game pretty quickly.

### A complete list of tools

* [Markdown](http://daringfireball.net/projects/markdown/) - A lightweight markup language to quickly write content
* [Pelican](http://docs.getpelican.com/en/latest/) - A static site generator written in Python
* [Jinja2](http://jinja.pocoo.org/docs/) - A templating language for Python used to create Pelican themes
* [Bootstrap](http://twitter.github.io/bootstrap/) - A  nice front-end framework made by the folks at Twitter
* [Pygments](http://pygments.org/) - For syntax highlighting
* [Typogrify](https://github.com/getpelican/pelican-typogrify) - To fancy up the text a bit
* [Fabric](http://docs.fabfile.org/en/1.6/) - To streamline deployment
* [Github Pages](http://pages.github.com/) - Fast, reliable hosting 

### The process

####Create a Markdown file and include some metadata at the top.

	:::Text
	Title: What's Under the Hood?
	Date: 2013-06-22
	Summary: Markdown, Pelican, Jinja2, Bootstrap, &amp; Github Pages (oh my!)
	Slug: whats-under-the-hood
	Tags: Markdown, Pelican, Boostrap, Github

####Write! (using Markdown)

	:::text
	Many months ago, [a buddy](http://christopherkollars.com) sent me [this article](http://kylerush.net/blog/meet-the-obama-campaigns-250-million-fundraising-platform/) written by [Kyle Rush](http://kylerush.net/) about the technology stack behind the Obama campaign's (incredible) fundraising platform. Kyle mentioned [Jekyll](http://jekyllrb.com/), a static site generator written in Ruby, and recommended giving it a whirl to create fast, simple websites without the need for a bloated CMS. ...

####Preview!

I use two separate config files for Pelican. One uses relative URLs (so I can preview locally), and the other generates absolute URLs for production. To avoid typing the full Pelican commands to generate the output, I use this fabfile.py:

	:::Bash
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

	:::Bash
	fab dev

Then I check it out on my local vhost.

####Deploy

If everything looks okay, I generate the HTML with absolute URLs.

	:::Bash
	fab pub


Then simply commit my changes to Github.

###So far, so good

I'm the kind of guy who will spend 15 hours hacking my Wii to play 15 minutes of old NES games. I'm optimistic that an easy, fast, and fun way to manage a new blog will encourage me to get my act together and finally start writing somewhat regularly.


 