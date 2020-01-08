#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Site Info
AUTHOR = ''
SITENAME = 'SFPE Central VA'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
PAYPAL_MEETING = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RL65DGSCD2MHQ'
PAYPAL_MEMBER = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=V6CYLBB5B7FB2'

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
AUTHOR_URL = AUTHOR_SAVE_AS = 'presenter/{slug}.html'
AUTHORS_SAVE_AS = 'presenters.html'
TAG_URL = TAG_SAVE_AS = 'topic/{slug}.html'
TAGS_SAVE_AS = 'topics.html'

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
    ('Presenters', AUTHORS_SAVE_AS),
    ('Topics', TAGS_SAVE_AS),
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


def str2time(timestr):
    return datetime.strptime(timestr, "%H:%M").strftime(' %I:%M %p').replace(' 0', ' ')


JINJA_FILTERS = {
    'future_events': future_events,
    'str2time': str2time,
}
