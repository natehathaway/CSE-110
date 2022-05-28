


can_ride = False

#One Rider
first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider in inches? "))
golden_passport = int(input("Do you have a golden passport (yes/no)? "))

if golden_passport.lower() == "yes":
    first_rider_age = 18
if first_rider_age >= 18 and first_rider_height >= 62:
    can_ride = True


#Two Riders
is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider? "))
    golden_passport2 = int(input("Do you have a golden passport (yes/no)? "))
    if golden_passport2.lower() == "yes":
        second_rider_age = 18
    if first_rider_age >=18 or second_rider_age >= 18:
        can_ride = True
    if first_rider_height < 36 or second_rider_height < 36:
        can_ride = False
    if first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
        can_ride = True
    if first_rider_age >= 16 and second_rider_age >=14 or first_rider_age >=14 and second_rider_age >=16:
        can_ride = True

if can_ride:
    print("You may ride! I hope you don't die, that would be too much paperwork!")
else:
    print("Sorry, you may not ride. Go buy some ice cream for your tears.")

input("press ENTER to exit")



