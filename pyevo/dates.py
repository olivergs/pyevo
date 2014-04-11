# -*- coding: utf-8 -*-
"""
PyEVO date tool utilities
===============================================

.. module:: pyevo.dates
    :platform: Unix, Windows
    :synopsis: PyEVO date tool functions
.. moduleauthor:: (C) 2012 Oliver Gutiérrez
"""

# Python imports
import calendar
from datetime import datetime,timedelta,time

def date_range(start,end):
    """
    Returns a range of dates
    """
    if start > end:
        # Swap values
        start,end=end,start
    
    days=(end-start).days
    if days==0:
        return [start]
    return [start + timedelta(days=x) for x in range(0,days)]

def date_day_bounds(start=None,end=None):
    """
    Return date range with time information
    """
    if start is None:
        start=datetime.now()
    if end is None:
        end=start
    start=datetime.combine(start, time.min)
    end=datetime.combine(end, time.max)
    return (start,end)

def month_bounds(date=None):
    """
    Return month start and end datetimes
    """
    if date is None:
        date=datetime.now()
    firstday,lastday=calendar.monthrange(date.year,date.month)
    start=datetime(date.year,date.month,firstday,0,0,0)
    end=datetime(date.year,date.month,lastday,23,59,59)
    return (start,end)

def day_bounds(date=None):
    """
    Return day bounds from a date
    """
    return date_day_bounds(date)

def days_ago(past,future):
    """
    Returns days passed from past date to future date
    """
    return (future-past).days

def days_ago_date(days,date=datetime.now()):
    """
    Returns the date corresponding to the specified days ago specified date 
    """
    delta=timedelta(days)
    return date-delta

def days_ago_range(days,date=datetime.now()):
    """
    Returns a date range between a date and the date specified days ago
    """
    start=days_ago_date(days,date)
    return date_range(start,date)

def date_from_text(udate):
    """
    Returns a datetime object from an string in format YYYYMMDD or YYYYMMDDhhmmss
    """
    if len(udate) in [8,12] and udate.isdigit():
        year=int(udate[:4])
        month=int(udate[4:6])
        day=int(udate[6:8])
        hours=0
        mins=0
        if len(udate)==12:
            hours=int(udate[8:10])
            mins=int(udate[10:12])
        try:
            return datetime(year,month,day,hours,mins)
        except:
            pass                     
    raise Exception(_('Invalid date specified. Must be in format: YYYYMMDD or YYYYMMDDhhmmss'))