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

# listing the type of each item in the list using list comprehension


print("Updating the duplicate make\n")

def replace_list_items(itemList, item, replace_item_name):
    """ A simple item replacement function which replaces the desired item in the list with provided value 
        
        !Note: This method only works for string items 
        :param list itemList: The list desired to be modified
        :param str item: The item in the list to modify
        :param str replace_item_name; The new item name which should be updated
    """

    item_index = itemList.index(item)
    if(len(itemList) < 1): 
        return None;
    if (isinstance(item, str) and isinstance(replace_item_name, str)):
        if(item_index >= 0):
            itemList[item_index] = replace_item_name
            return itemList
        else:
            return None
    else:
        return None

car_makes = replace_list_items(car_makes, "volkswagon", "bently")

# list comprehension example
def title_case_list_elements(data_list: list[str]) -> list[str]: 
    return [element.capitalize() for element in data_list if len(data_list) > 0] 


###########################################################################
# Sorting function 
# - sorted
# > The return values for the below 3 method are `None`. This is so as to 
#   avoid confusion. The original list will be changed after the operation
#   is complete
# - Default sort
# - Reverse sort
# - Custom sort
##########################################################################

def return_sorted_list_of_strings(data_list: list[str]) -> list[str]:
    data_list.sort(key=str.lower)
    return data_list

def return_reverse_sorted_list_of_strings(data_list: list[str]) -> list[str]:
    data_list.sort(reverse=True, key=str.lower)
    return data_list

##########################################################################
# since, the sort method returns `None` after success, always create a copy
# always create a copy of original
##########################################################################

def return_string_length_sorted_list(data_list: list[str]) -> list[str]:
    dup_data_list = data_list.copy()
    dup_data_list.sort(key=len)
    return dup_data_list

##########################################################################
# printing methods
#########################################################################
print("Here's the final entries", end="\n")
print(title_case_list_elements(car_makes))
print("Car makes can be sorted in the following ways\n")

print("Default sort \t {0}".format(return_sorted_list_of_strings(car_makes)))
print("Reverse sort \t {0}".format(return_reverse_sorted_list_of_strings(car_makes)))
print("Custom sort on string length \t {0}".format(return_string_length_sorted_list(car_makes)))
