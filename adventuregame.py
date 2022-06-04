
choice1 = input("You find yourself floating in space! you look around and you see a spaceship leaving you. You have a flare gun in your hand. Do you shoot the FLARE, or PRAY that this is a dream?")

if choice1.lower() == "flare":
    flare_choice = input("You shoot your flare gun as a massive purple flare goes in the direction of the spaceship. Due to the force, you actually start to move backwards! Luckily, they see you and they start to turn around to get you. However, you realize that the spaceship is not a human one, but an alien one! They pick you up and put you in their hold. When they come and talk to you they say that they are on a scouting mission to invade earth and need info from you. Do you LIE to them or do you HELP them?")
    if flare_choice.lower() == "lie":
        lie_choice = input("You lie to them and tell them that the humans have advanced technology that they can use to destroy the aliens. That scares them and they begin to panic and turn around. You sigh in relief before you remember that you are still here! Do you STAY or do you LEAVE?")
        if lie_choice.lower() == "stay":
            print("You stay on the ship and they put you back in the hold. You wait a really long time before they show up and decide that because you are a human, and they are aliens, that you don't deserve to live anymore. They shoot you and you die. You lose!")
        elif lie_choice.lower() == "leave":
            print("You panic and ask them to send you back to earth. In their panic they don't even pay attention to you so you start to run around. You find an escape pod and shoot yourself towards earth. You land safely in a lake that just happens to be in your backyard. You walk inside and there is ice cream in the freezer. Score! You win!")
    if flare_choice.lower() == "help":
        help_choice = input("You decide to help them. You tell them that you hate humans and promise to help them take over. They believe you and decide to appoint you general of their armada. Do you INVADE or LEAVE with your fleet of alien invaders? ")
        if help_choice.lower() == "invade":
            print("You decide to invade earth and take over the Earth. You launch an offensive, and the humans, who don't have advanced enough tech for these invaders, fall easily. You are now the undisputed ruler of Earth, and in honor of your achievements, you are made emperor of Earth. You win!")
        elif help_choice.lower() == "leave":
            print("You leave with your fleet of alien invaders. They are not happy with your decision and decide to assassinate you in your sleep. You lose!")

elif choice1.lower() == "pray":
    pray_choice = input("As you begin to pray that this is just a dream and want to be anywhere else, you realize that you are sitting down somewhere. You look up and realize that you are no longer in space. You are in fact on a roller coaster as it starts to go! The ride is vicious, but as you finish and get off your friend next to you asks if you want to go again. Do you go AGAIN, or do you LEAVE?")
    if pray_choice.lower() == "again":
        again_choice = input("You go again, but this time you don't recognize the roller coaster you're on, nor your friend! As you go on the roller coaster that is definitely not the same, you look at your friend and they are not the same person! In fact, it is an alien in the seat next to you! Do you FIGHT it, RUN, or do NOTHING?")
        if again_choice.lower() == "fight":
            print("You punch the alien straight in the face! It stares at you, shocked, before it punches you back, but way harder. This alien beats the crap out of you on a moving roller coaster, and then kills you. You lose!")
        elif again_choice.lower() == "run":
            print("You run away from the alien, because somehow you can run away, and it starts to laugh at you and chase you. As you run, you realize you have no idea where you are. You get very very lost and all you hear is maniacal laughter from this alien you can't even see anymore. You are stuck. You lose!")
        elif again_choice.lower() == "nothing":
            print("You don't do anything and the alien starts laughing at you. You are so scared that you don't even know what to do. The alien gets off the ride, thanks you for a good time, and then gives you their number. You just got a second date with an alien! You win?")
    if pray_choice.lower() == "leave":
        leave_choice = input("You tell your friend that you don't want to go, and he goes again without you. You walk around and realize that you are actually at Disneyland! You decide to take the free vacation and go to wait for your friend to be done so you can have more adventures. Do you ride the SAME roller coaster, or go to a DIFFERENT one? ")
        if leave_choice.lower() == "same":
            print("You ride the roller coaster again, and this time it is less freaky and more exciting. You almost forget that you actually hate roller coasters. Almost. You get off of the ride and begin to vomit. You literally puke your guts out and die. You lose!")
        elif leave_choice.lower() == "different":
            print("You go to epcot because you want to eat some good food. You and your friend get some delicious food and have a great time there. You win!")


elif choice1.lower() == "fart":
    fart_choice = input("You fart and you create a green cloud that covers your vision. You are now in the middle of the spaceship! You look around and see a bunch of aliens. Do you FIGHT them, or do you RUN?")
    if fart_choice.lower() == "fight":
        print("You put up a fighting pose, but they all have guns and shoot you. You die, and you look ridiculous. You lose!")
    elif fart_choice.lower() == "run":
        print("You begin to run away from the aliens, but they don't even chase you. You're on a spaceship, where are you going to go? After 3 weeks of neglect you starve to death and they launch your body into space. You lose!")
    elif fart_choice.lower() == "fart":
        print("You are so startled that you fart again. This time, the aliens all cough and choke on your fart cloud and they all die. You now have a spaceship, and the entire galaxy at your fingertips. Go forth, Hero of Flatulence! You win!")


else :
    print("ERROR")


input("press ENTER to exit")