"""Fabric tasks for generating HTML"""
from __future__ import with_statement

from fabric.api import lcd, local, settings

def pub():
    """Re-generates the output using absolute urls."""
    local('pelican . -o /Applications/MAMP/htdocs/alexpgates.github.com -s settings.py')

def dev():
    """Re-generates the output using relative urls."""
    local('pelican . -o /Applications/MAMP/htdocs/alexpgates.github.com -s local_settings.py')

def pubnocache():
    """Re-generates the output using absolute urls."""
    local('pelican . -o /Applications/MAMP/htdocs/alexpgates.github.com -s settings.py --ignore-cache')

def devnocache():
    """Re-generates the output using relative urls."""
    local('pelican . -o /Applications/MAMP/htdocs/alexpgates.github.com -s local_settings.py --ignore-cache')
