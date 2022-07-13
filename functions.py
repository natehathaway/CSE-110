

from types import new_class


def display_regular(string): 
    print(string)

def display_uppercase(string):
    print(string.upper())

def display_lowercase(string):
    print(string.lower())

new_string = input("Type your message here: ")
display_regular(new_string)
display_uppercase(new_string)
display_lowercase(new_string)