#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Site Info
AUTHOR = 'SFPECVA'
SITENAME = 'SFPE Central VA'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Disable Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Rendering Info
PATH = 'content'
THEME = 'themes/sfpecva'
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['autopages']

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

SITE_LINKS = (
    ('Past Presenters', 'authors.html'),
    ('Topics', 'tags.html'),
    ('Archives', 'archives.html')
)

SFPE_LINKS = (
    ('National SFPE', 'http://www.sfpe.org'),
    ('SFPE Job Listings', 'https://jobs.sfpe.org')
)


def future_events(articles):
    return [
        a for a in articles
        if a.date > datetime.now(a.date.tzinfo)
        and a.category == "Meetings"
    ][::-1]


JINJA_FILTERS = {
    'future_events': future_events,
}
