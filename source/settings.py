"""Settings for pelican."""

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = 'notmyidea'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'America/Chicago'


# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'
USE_FOLDER_AS_CATEGORY = True;


AUTHOR = 'Alex P. Gates'
SITENAME = 'Alex P. Gates'
SITESUBTITLE = 'works on the internet'
SUBTWO = 'lives in Omaha.'
SITEURL = 'http://alexpgates.com'
RELATIVE_URLS = True
TYPOGRIFY = True


# I like to have ``Archives`` in the main menu.
# MENUITEMS = (
#     ('Archives', '/archives.html'.format(SITEURL)),
# )


WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
#DISQUS_SITENAME = 'yourdisqushandle'
#GITHUB_URL = 'http://github.com/username/username.github.com'
#TWITTER_USERNAME = 'username'