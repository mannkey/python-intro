"""
filename: hello-list.py
description: lists and tuple methods 
author: Thribhuvan Kumar <Thribhuvan.d@mannkey.com>
license: MIT
scope: python_for_beginers
copyright: Thribhuvan Kumar DSVB
"""
# lets try to understand list, sublists 

from utils.date_utils import get_today_date_only, get_today_day 


car_makes = ["volkswagon", "mercedes", "audi", "toyota"]

#individual models of the above make
vw_cars = ["polo", "golf", "passat", "jetta", "vento"] 
merc_cars = ["s-class", "e-class", "g-class", "c-class"]
audi_cars = ["r8", "q7", "q5", "r7"]
toy_cars = ["land crusier", "fortuner", "innova"]

print("Total entries for car makers this year on {1} are {0}".format(len(car_makes), get_today_date_only()), end=".\n")

print("It is a beautiful {}".format(get_today_day()), end=".\n")

car_makes.append("volkswagon")

print("Post late entries, The updated car makers are {}".format(len(car_makes)))




