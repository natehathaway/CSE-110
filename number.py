# Birthday Math
age_number = input("How old are you? ")
age_int = int(age_number)
birthday = age_int + 1
birthday_string = str(birthday)
print("On your next birthday, you will be " + birthday_string)

#Egg Cartons
carton = input("How many egg cartons do you have? ")
carton_int = int(carton)
eggs = carton_int * 12
egg_string = str(eggs)
print("You have " + egg_string + " eggs")

#Cookies
cookies = input("How many cookies do you have? ")
cookies_int = int(cookies)
people = input("How many people are there? ")
people_int = int(people)
cookies_people = cookies_int/people_int
cookies_people_str = str(cookies_people)
print("Each person may have " + cookies_people_str + " cookies")