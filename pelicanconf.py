#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vibek Raj Maurya'
SITENAME = u'rvibek'
SITESUBTITLE = u'..in the making'
SITEURL = 'http://rvibek.com.np'

PATH = 'content'
THEME = 'output/theme/pelicanium'
COVER_IMG_URL = 'http://res.cloudinary.com/rvibek-com-np/image/upload/v1486821421/ghostium800_y3y8pa.jpg'
PROFILE_IMG_URL = 'http://res.cloudinary.com/rvibek-com-np/image/upload/v1486821422/logo_dpmyds.png'
AUTHOR_EMAIL = 'rvibek@gmail.com'

DISQUS_SITENAME = 'rvibekblog'
GOOGLE_ANALYTICS = "UA-177774-1"


TIMEZONE = 'Africa/Cairo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
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
    ('Flickr', 'http://flickr.com/rvibek'),
    ('Github', 'http://github.com/rvibek'),

    ('Instagram', 'http://instagram.com/rvibek'),
    ('Twitter', 'http://twitter.com/rvibek')

)

DEFAULT_PAGINATION = 10

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
