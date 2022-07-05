#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Functions used by the blog app
"""

from datetime import date
from random import randrange
from about import aboutme



def getRandNum(range):
    return randrange(0, range)

def weeks_past(iso_date):
    start = date.fromisoformat(aboutme.about['start_date'])
    tdy = date.today()
    week_progress = int((tdy-start).days/7)+1
    return week_progress
