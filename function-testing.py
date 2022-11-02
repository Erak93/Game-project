print("Welcome to the epic quest! You're in the middle of the Wild Forest? You need to find the Magic Mushroom. Where would you like to go?")
print("I'll give you time to think")
print("*", "**", "***", "**", "*", sep = "\n")


def fight():
    choice = input(str("Swamper is waving with his sword. What do you want to do? 1 - throw him swampuccino in the eyes, 2 - kick the sword out of his hands, 3 - give up the quest"))
    if choice =="1":
        #hp_count()
        print("The Swamper tries to lick the rest of swampuccino, you have a chance to run for your life. You're in the middle of the forest now")
    elif choice =="2":
        #hp_count()
        print("You miss the target. The Swamper chops your head off. You're dead, loser")
    elif choice =="3":
        print("You gave up the quest, loser")


def waiting():
    print("There's nothig better than a good story to accompany your best of the day time. THink about your life. When did it go wrong? Why are you in the middle of the forest at night? Alone with a beautiful swamper. Btw, watch out, he is approaching you with a knife")
    choice = input("What do you want to do? fight or run?")
    if choice == "run":
        print("Guess that swampaccino gave you extra energy? You're back in the middle of the forest")
    elif choice == "fight":
        fight()
    elif choice == "run":
        print("You succeeded to run. You're in the middle of the forest now.")


def go_east_forest():
    choice =input ("You moved to the east. You see a swamp. Want a swim or a sip? y/n")
    if choice == "y":
        print("A beautiful Swamper rises from water and offers you a cup of hot swampaccino. You drink it and feel the urge to meditate in the bushes. You're gonna have to take a break")
        waiting()
    elif choice == "n":
        print("The Swamper gets bigger and bigger. You should run for your life.")
        choice2 = input("Do you wanna run? y/n")
        if choice2 == "y":
            print("You're in the middle of the forest now")
        elif choice2 == "n":
            print("It was a bad decision. The Swamper kills you, loser")

choice = input("Choose east, north, west or south: ")

if choice == "east":
    go_east_forest()
elif choice == "west":
    west_adv()
elif choice == "north":
    north_adv()
elif choice == "south":
    south_adv()
#else:
    #print("There are only four winds")