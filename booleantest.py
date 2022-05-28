

go_to_the_doctor = False

age = int(input("Input your age: "))
year_since_been_to_the_doctor = int(input("How many years since you've been to the doctor? "))

if year_since_been_to_the_doctor > 20:
    go_to_the_doctor = True

if go_to_the_doctor:
    print("You need to go to the doctor!!!!!!!")

else:
    print("You do not need a doctor visit.")