"""
filename: date_utils.py
description: exporting date utility functions
author: Thribhuvan Kumar <Thribhuvan.d@mannkey.com>
scope: python_for_beginers
license: MIT
copyright: Thribhuvan Kumar
"""

#import date module from python inbuilt
import datetime


def get_today_date_only():
    """ A simple function which returns date in format mm-dd-yy"""
    current_date =  datetime.datetime.now()
    # strftime is a method in datetime class to format date
    return current_date.strftime("%x").replace("/", "-")

def get_today_day():
    """ A simple function to return day """
    # convert the date string returned by the get_today_date_only to list
    current_date = get_today_date_only().split("-")
    #current date from python datetime constructor
    current_date = datetime.datetime(...current_date)
    return current_date.strftime("%A")

