import mymodule

#print("Welcome to an epic quest!")

#mymodule.human_features()

print("Welcome to the epic quest! You're in the middle of the Wild Forest? You need to find the Magic Mushroom. Where would you like to go?")
print("I'll give you time to think")
print("*", "**", "***", "**", "*", sep = "\n")

def lose_all_hp():
    if race_input == "human":
            minus_hp(human[hp], human)
    elif race_input == "elf":
        minus_hp(elf[hp], elf)
    else:
        minus_hp(dwarf[hp], dwarf)


def fight():
    choice = input(str("Swamper is waving with his sword. What do you want to do? 1 - throw him swampaccino in the eyes, 2 - kick the sword out of his hands, 3 - give up the quest"))
    if choice == "1":
        if race_input == "human":
            add_hp(3, human)
        elif race_input == "elf":
            add_hp(2, elf)
        else:
            add_hp(1, dwarf)
        print("The Swamper tries to lick the rest of swampaccino, you have a chance to run for your life. You're in the middle of the forest now")
    elif choice == "2":
        lose_all_hp()
        choice2 = input("You miss the target. The Swamper chops your head off. You lost all your hp. Do you want to risk and continue the game without it? y/n")
        if choice2 == "y":
            print("Brave choice, noble warrior! You're in the middle of the forest")
            mymodule.choosing_dir()
        elif choice2 == "n":
            print("Thank you for playing")
    
    elif choice == "3":
        print("You gave up the quest. You're back to the middle of the forest.")
        mymodule.choosing_dir()

def waiting():
    print("There's nothig better than a good story to accompany your best of the day time. THink about your life. When did it go wrong? Why are you in the middle of the forest at night? Alone with a beautiful swamper. Btw, watch out, he is approaching you with a knife")
    choice = input("What do you want to do? fight or run?")
    if choice == "run":
        print("Guess that swampaccino gave you extra energy? You're back in the middle of the forest")
        mymodule.choosing_dir()
    elif choice == "fight":
        fight()
    
choice_list = []

def go_east_forest():
    choice = input(("You moved to the east. You see a swamp. Want a swim or a sip? y/n"))
    if choice == "y":
        print("A beautiful Swamper rises from water and offers you a cup of hot swampaccino. You drink it and feel the urge to meditate in the bushes. You're gonna have to take a break")
        waiting()
    elif choice == "n":
        print("The Swamper gets bigger and bigger. You should run for your life.")
        choice2 = input("Do you wanna run? y/n")
        if choice2 == "y":
            print("You're in the middle of the forest now")
            mymodule.choosing_dir()
            
        elif choice2 == "n":
            print("It was a bad decision. The Swamper kills you. You lost all your hp. Do you want to risk and continue the game without it? y/n")
        if choice2 == "y":
            print("Brave choice, noble warrior! You're in the middle of the forest")
            mymodule.choosing_dir()
        elif choice2 == "n":
            print("Thank you for playing")


mymodule.choosing_dir()
#else:
    #print("There are only four winds")
