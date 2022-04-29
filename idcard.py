
from ctypes import addressof
from turtle import title

#initial input
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input ("What is your email?")
phone = input ("What is your phone number?")
job_title = input ("What is your job title?")
ID = input("What is your ID number?")

#additional input
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

#printed format
print("The ID Card is:")
print("----------------------------------------------")
print("{0}, {1}".format(last_name.upper(), first_name.capitalize()))
print(job_title.title())
print(ID)
print(" ")
print(email.lower())
print(phone)
print()
print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------------")