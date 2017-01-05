#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Diego Becker'
SITEURL = 'http://localhost:8000'
SITENAME = "Diego Becker's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Sotfware Developer'
SITELOGO = '//s.gravatar.com/avatar/27e62c171c9f88dbb0d57e534d2e52a4?s=120'

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

THEME = '../tema-flex'
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'



# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
#MAIN_MENU = True

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)



# Social widget
SOCIAL = (('github', 'https://github.com/diegobecker'),
          ('linkedin', 'https://br.linkedin.com/in/diegoobecker'),
          ('facebook', 'https://www.facebook.com/diegobecker00'),
          ('twitter', 'https://twitter.com/_diegobecker_')
          #('rss', '//blog.alexandrevicenzi.com/feeds/all.atom.xml')
          )
DISQUS_SITENAME = 'diegobecker'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
