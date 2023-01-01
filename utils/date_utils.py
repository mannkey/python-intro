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
    """
       In the below function there are few intresting things are happening. Let's understand them one by one
       - we are spliting the date returned by get_today_date_only method
       - The returned list contains string elements
       - We want to construct a new date with list items using python datetime module
       - The datetime.datetime() method expects args as integers
       - We are using list comprehension to covert the string item to int
       - We are using `*` operator to expand the iterator and pass them as args
    """
    current_date = datetime.datetime(*[int(item) for item in current_date])
    return current_date.strftime("%A")

