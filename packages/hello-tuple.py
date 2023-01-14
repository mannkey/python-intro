'''
filename: hello-tuple.py
description: basic understanding of tuple data type and tuple methods
author: Thribhuvan Kumar DSVB <Thribhuvan.d@outlook.com>
license: MIT
copyright: mannkey developers
created_at: 14-01-2023
'''

home_groceries_category = ("staples", "fruits", "nuts", "dairy", "home_supplies", "personal_care");

print(type(home_groceries_category))

#########################################################################################
# To update a value in tuple, it has to be changed to list and then we can perform 
# required operations followed by a tuple coversion again
#########################################################################################

def update_tuple_entry(data_tuple: tuple[str], old_entry:str, new_entry:str)->tuple[str]:
    list_from_tuple = list(data_tuple)
    try:
        original_entry_index = list_from_tuple.index(old_entry)
        list_from_tuple[original_entry_index] = new_entry 
        return tuple(list_from_tuple)
    except ValueError: 
        print("Unable to find entry {0}".format(old_entry))

########################################################################################
# To remove an entry from tuple, the similar sequence of conversion to list and then to
# tuple is to be followed
########################################################################################

def remove_entry_from_tuple(data_tuple:tuple[str], entry:str) -> tuple[str]:
    list_from_tuple = list(data_tuple)
    try:
        original_entry_index = list_from_tuple.index(entry)
        list_from_tuple.pop(original_entry_index)
        return tuple(list_from_tuple)
    except ValueError: 
        print("Unable to find entry {0}".format(entry))

print(update_tuple_entry(home_groceries_category, "home_supplies", "home_suppliments"))
print("remove a tuple entry", end="\n")

print(remove_entry_from_tuple(home_groceries_category, "nuts"), end="\nUnpacking a tuple\n")

########################################################################################
# unpacking a tuple to a list, 
# starring the variable will unpack all the entries in the tuple to variable
########################################################################################
(*groceries,) = home_groceries_category
print(groceries)



