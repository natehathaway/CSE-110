from cgi import print_arguments


first_name = input ("What is your first name?")
last_name = input ("What is your last name?")
agent = input ("What is your code number?")

print(" ")
#print("Your name is {}, {} {}.".format(last_name.capitalize(), first_name.capitalize(), last_name.capitalize()))
#print(f"Your name is {last_name.capitalize()}, {first_name.capitalize()}, {last_name.capitalize()}.")
print ("Your name is {1}, {0} {1}.".format(first_name.capitalize(), last_name.capitalize()))
#print ("Your name is " + last_name.capitalize() + ", " + first_name.capitalize() + " " + last_name.capitalize() + ".")
print (" ")
print ("Welcome, Agent " + agent + ".")