#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = u'Vibek Raj Maurya'
SITENAME = u'rvibek'
SITE_TITLE  =  u'rvibek | Vibek Raj Maurya'
SITESUBTITLE = u'..in the making'
SITEURL = 'https://rvibek.com.np'
# GITHUB_URL = 'https://github.com/rvibek'


PATH = 'content'
THEME = 'themes/hyde'

COVER_IMG_URL = 'https://res.cloudinary.com/rvibek-com-np/image/upload/v1486821421/ghostium800_y3y8pa.jpg'
PROFILE_IMG_URL = 'https://res.cloudinary.com/rvibek-com-np/image/upload/v1486821422/logo_dpmyds.png'
AUTHOR_EMAIL = 'rvibek@gmail.com'

# DISQUS_SITENAME = 'rvibekblog'  # rvibekghost
GOOGLE_ANALYTICS = "UA-177774-1"


TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll


# Social widget
SOCIAL = (
    ('email', 'mailto:contact@rvibek.com.np'),
    # ('flickr', 'https://flickr.com/rvibek'),
    ('github', 'https://github.com/rvibek'),
    ('instagram', 'https://instagram.com/rvibek'),
    ('linkedin', 'https://www.linkedin.com/in/rvibek/'),
    # ('Twitter', 'https://twitter.com/rvibek')

)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# PAGINATED_DIRECT_TEMPLATES = ['index', 'archives']
# PAGINATED_TEMPLATES = ['index', 'archives']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'articles': None}
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
# PLUGINS = ('pelican_extended_authors',)

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# BIO = "Hello world!"