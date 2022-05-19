
choice1 = input("You find yourself floating in space! you look around and you see a spaceship leaving you. You have a flare gun in your hand. Do you shoot the FLARE, or PRAY that this is a dream?")

if choice1.lower() == "flare":
    flare_choice = input("You shoot your flare gun as a massive purple flare goes in the direction of the spaceship. Due to the force, you actually start to move backwards! Luckily, they see you and they start to turn around to get you. However, you realize that the spaceship is not a human one, but an alien one! They pick you up and put you in their hold. When they come and talk to you they say that they are on a scouting mission to invade earth and need info from you. Do you LIE to them or do you HELP them?")

elif choice1.lower() == "pray":
    pray_choice = input("As you begin to pray that this is just a dream and want to be anywhere else, you realize that you are sitting down somewhere. You look up and realize that you are no longer in space. You are in fact on a roller coaster as it starts to go! The ride is vicious, but as you finish and get off your friend next to you asks if you want to go again. Do you go AGAIN, or do you LEAVE?")

else :
    print("ERROR")


