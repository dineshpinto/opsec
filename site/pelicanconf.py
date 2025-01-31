#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mikko Ohtamaa'
SITENAME = 'OPSEC - Operations Security'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ['categories', 'authors', 'archives', 'index']

PAGINATED_DIRECT_TEMPLATES = ['index']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://github.com/getpelican/pelican/issues/735
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
DEFAULT_PAGINATION = 10

INDEX_SAVE_AS = 'blog.html'

DISQUS_SITENAME = "opsec"


# TEMPLATE_PAGES = {"index.html", "blog.html"}

# DIRECT_TEMPLATES = ['blog']
# PAGINATED_DIRECT_TEMPLATES = ['blog']