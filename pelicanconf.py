#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vibek Raj Maurya'
SITENAME = u'rvibek'
SITEURL = ''

PATH = 'content'
THEME = 'output/theme/pelicanium'
COVER_IMG_URL = 'http://res.cloudinary.com/rvibek-com-np/image/upload/v1486821421/ghostium800_y3y8pa.jpg'
PROFILE_IMG_URL = 'http://res.cloudinary.com/rvibek-com-np/image/upload/v1486821422/logo_dpmyds.png'
DISQUS_SITENAME = ''
AUTHOR_EMAIL = 'rvibek@gmail.com'

TIMEZONE = 'Africa/Cairo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
    ('Facebook', 'http://facebook.com/rvibek'),
    ('Instagram', 'http://instagram.com/rvibek'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PAGINATED_DIRECT_TEMPLATES = ['index', 'archives']
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# PLUGIN_PATH = 'src/pelican-plugins'
# PLUGINS = (
#     # 'pelican_edit_url',
#     'pelican_extended_authors',
#     # 'summary',
# )
ARTICLE_EXCLUDES = ('pages', 'authors')
# PAGE_EXCLUDES = ('authors',)
PLUGINS = ('pelican_extended_authors',)
