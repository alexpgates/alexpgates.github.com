"""Settings for pelican."""
from __future__ import unicode_literals

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = '/Applications/MAMP/htdocs/alexpgates.github.com/themes/bootstrap-apg/'

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


# Settings for articles. We're putting them all in "blog" because that's my preference
ARTICLE_DIR = 'blog/'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'

# Settings for pages. We're putting them all in "projects" because that's my preference
PAGE_DIR = 'projects/'
PAGE_URL = 'projects/{slug}.html'
PAGE_SAVE_AS = 'projects/{slug}.html'

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
#DISQUS_SITENAME = 'yourdisqushandle'
#GITHUB_URL = 'http://github.com/username/username.github.com'
#TWITTER_USERNAME = 'username'
