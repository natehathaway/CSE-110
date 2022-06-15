

#what it should look like
#Type the name of a friend: Peter
#Type the name of a friend: James
#Type the name of a friend: John
#Type the name of a friend: end

#Your friends are:
#Peter
#James
#John


friends = []

new_friend = input("Type the name of a friend (type end to quit): ")

while new_friend.lower() != "end":
    friends.append(new_friend)
    new_friend = input("Type the name of a friend (type end to quit): ")
    if new_friend.lower() == "nate":
        print("You are not a friend of mine.")

print()
print("Your friends are:")
for friend in friends:
    print(friend.capitalize())

input("press ENTER to exit")
print("\n")
