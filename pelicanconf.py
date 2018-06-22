#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kris De Decker'
SITENAME = u'LOW&larr;TECH MAGAZINE'
SITEURL = ''
SITESUBTITLE = u'Doubts on progress and technology'
ARTICLE_PATHS = ['posts']

PATH = 'content'

THEME = 'themes/zero'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'
DEFAULT_METADATA = {
    'status': 'draft',
}
FORMATTED_FIELDS = ['editor','translator']

# URLS
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

ARTICLE_LANG_URL = '{lang}/{date:%Y}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{date:%Y}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ["neighbors", "dither"]
TYPOGRIFY = True

# CATEGORIES
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False

#DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Subscribe via RSS', 'http://feeds2.feedburner.com/typepad/krisdedecker/lowtechmagazineenglish'),
          ('Twitter', 'http://twitter.com/lowtechmagazine'),
          ('Facebook', 'https://www.facebook.com/Lowtechmagazine'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
