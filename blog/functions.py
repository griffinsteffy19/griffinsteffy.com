#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Functions used by the blog app
"""

from datetime import date
from random import randrange
from about import aboutme

import os, sys, re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def getRandNum(range):
    return randrange(0, range)

def weeks_past(iso_date):
    start = date.fromisoformat(aboutme.about['start_date'])
    tdy = date.today()
    week_progress = int((tdy-start).days/7)+1
    return week_progress

def savePage(url, pagepath='page'):
    def savenRename(soup, session, url, tag, inner):
        for res in soup.findAll(tag):   # images, css, etc..
            if res.has_attr(inner): # check inner tag (file object) MUST exists  
                try:
                    filename, ext = os.path.splitext(os.path.basename(res[inner])) # get name and extension
                    filename = re.sub('\W+', '', filename) + ext # clean special chars from name
                    fileurl = urljoin(url, res.get(inner))
                    # rename html ref so can move html and folder of files anywhere
                    if not os.path.isfile(filepath): # was not downloaded
                        with open(filepath, 'wb') as file:
                            filebin = session.get(fileurl)
                            file.write(filebin.content)
                except Exception as exc:
                    print(exc, file=sys.stderr)
    session = requests.Session()
    #... whatever other requests config you need here
    response = session.get(url)
    print(response.encoding)
    soup = BeautifulSoup(response.text.encode(response.encoding), "html.parser")
    path, _ = os.path.splitext(pagepath)
    tags_inner = {'img': 'src', 'link': 'href', 'script': 'src'} # tag&inner tags to grab
    for tag, inner in tags_inner.items(): # saves resource files and rename refs
        savenRename(soup, session, url, tag, inner)
    with open(path+'.html', 'wb') as file: # saves modified html doc
        file.write(soup.prettify(response.encoding))