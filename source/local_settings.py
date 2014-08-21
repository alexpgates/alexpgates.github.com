"""Settings for pelican."""
from __future__ import unicode_literals

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = '/Applications/MAMP/htdocs/alexpgates.github.com/themes/apg/'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'America/Chicago'


# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'
USE_FOLDER_AS_CATEGORY = True

AUTHOR = 'Alex P. Gates'
SITENAME = 'Alex P. Gates'
SITESUBTITLE = 'works on the internet'
SUBTWO = 'lives in Omaha.'
SITEURL = 'http://alexpgates.com'
RELATIVE_URLS = True
TYPOGRIFY = True


DISPLAY_PROJECTS_ON_MENU = False

WITH_PAGINATION = False
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True
REVERSE_CATEGORY_ORDER = True

# Settings for articles.
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARCHIVES_URL = 'blog/archives.html'
TAGS_SAVE_AS = 'blog/tags.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''

# Settings for pages. 
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
#DISQUS_SITENAME = 'yourdisqushandle'
#GITHUB_URL = 'http://github.com/username/username.github.com'
#TWITTER_USERNAME = 'username'
