"""
filename: hello-world.py
description: The file contains basic string methods python supports
license: MIT
author: Thribhuvan Kumar DSVB <thribhuvan.d@mannkey.com>
scope: python-tutorial
created: 01/01/2023
"""

# printing string directly to std out with print method
print("hello world!")

#creating variable and passing the variable to print method

first_name = "Thribhuvan"
middle_name = "Kumar"
last_name = "DSVB"

# names above are initlized to a list for a looping exercise

names = [first_name, middle_name, last_name]

# for loop to print the names with space in between

"""
	from python  we can print a loop in same line dynamically by passing additional flags to the print method
	as follow 
	print(item, end=" ") in python 3
	print(item, sep=" ", end="", flush=True)
	ref: https://stackoverflow.com/a/3249539
"""
print("My name is ", end="")
for name in names:
	print(name, end=" ")
print("\n")

""" multiline string example """
# similar to the above comments, multiple string can be quoted between `"""` and `"""`

intro_text_in_tech = """
I am technology enthusiat. Always, I strive to enhance my skills and sharpen them 
by eluding with newer technical stack introductions. My favourite passtime is walking along with 
`Bruce lee`.
"""
print(intro_text_in_tech)
print('\n')

#get the length of the string in one line 

print("My fullname has ", end="")
print(len(first_name) + len(middle_name) + len(last_name), end=" ")
print("characters", end="\n")

""" string methods 
# string as list of chars
for char in first_name+middle_name+last_name:
    print(char, end=" ")

print('\n')
#check if substring exists in string
print("Like most people ask, my name has Kumar but not Kumari")
print("Kumar " , "kumar" in middle_name.lower())
print("Kumari " , "kumari" in middle_name.lower())

# string slicing
print("slice string methods")
print(first_name[2:5])
print(first_name[:6])
print(first_name[2:])
print(first_name[-1:4])
print(first_name.encode())
print((first_name+middle_name+last_name).istitle())

#formatting strings
"""
name_with_args = "My name is {} and I am {} years old."
age = 26
print(name_with_args.format(first_name,age))
