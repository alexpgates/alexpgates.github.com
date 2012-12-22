"""Fabric tasks for generating HTML"""
from __future__ import with_statement

from fabric.api import lcd, local, settings

def html():
    """Re-generates the output."""
    local('pelican . -o ../ -s settings.py')

def dev():
	"""Live-update after changes."""
	local('pelican -r -o ../ -s settings.py')
