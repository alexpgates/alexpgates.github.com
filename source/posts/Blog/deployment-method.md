Date: 2012-12-17
Title: Deployment method
Slug: deployment-method
Tags: Python, Makefile, Pelican, Fabric

# Whizzamo!

I managed to get a lot working. This is how it's all shaking out.

## make sure you are in the right environment

	:::bash
	$ workon blog

## I don't think I need that Makefile

When I first set up Pelican, I used the quick setup which created a make file that worked well with the /output directory

	:::bash
	$ pelican-quickstart

This created a few files for me (probably a few handy things). One of them was the Makefile that allowed me to generate HTML with:

	:::bash
	$ make html
	
After following the [this tutorial](http://martinbrochhaus.com/2012/02/pelican.html), though, I had to generate my HTML using this command:

	:::bash
	$ pelican . -o ../ -s settings.py
	

That isn't as nice.
	
So, in my attempts to create a Makefile that worked well with the structure of what I have here, I managed to delete my entire directory a few times. I gave up on the Makefile.

## Oh hai fabric!

The author of that tutorial also had set up a fabric file to help with publishing. This seems to save the day, and it seems I can probaly do some other neat stuff with this. (*I trimmed out the other tasks in the fab file because I don't really feel the need to deploy to github without first previewing locally*)

	:::bash
	"""Fabric tasks for generating HTML"""
	from __future__ import with_statement

	from fabric.api import lcd, local, settings

	def html():
	    """Re-generates the output."""
	    local('pelican . -o ../ -s settings.py')
	)
	

## tl;dr

	:::bash
	$ cd /Applications/MAMP/htdocs/alexpgates.github.com/source/
	$ fab html
	
Then preview my site locally before using the Github app to publish to the live site.