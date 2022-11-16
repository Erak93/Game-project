#Functions list


#Class function
human = {"race": "human", "hp": 50, "attack": 20, "money": 30}
elf = {"race": "elf", "hp": 20, "attack": 50, "money": 30}
dwarf = {"race": "dwarf", "hp": 30, "attack": 20, "money": 50}   

#race_input=input("Come closer. I can not really see you well. Who are you?   ")
race_input="human"


def human_features():
    print("race: "+human["race"], "hp: "+str(human["hp"]), "attack: "+str(human["attack"]), "money: "+str(human["money"]), sep="\n")

def elf_features():
     print("race: "+elf["race"], "hp: "+str(elf["hp"]), "attack: "+str(elf["attack"]), "money: "+str(elf["money"]), sep="\n")

def dwarf_features():
     print("race: "+dwarf["race"], "hp: "+str(dwarf["hp"]), "attack: "+str(dwarf["attack"]), "money: "+str(dwarf["money"]), sep="\n")

"""
def add_hp(score, race_input):
    if race_input == "human":
        human["hp"] = human["hp"].value + score
        print("hp: ", human["hp"])
    elif race_input = "elf":
        human["hp"] = human["hp"].value + score
        print("hp: ", human["hp"])
"""
"""
def add_hp(score, race_input):
    race_input["hp"] = race_input["hp"] + score
    print("hp: "+race_input["hp"])
"""

def add_hp(score, dict):
    dict["hp"] = dict["hp"] + score
    print("hp: "+str(dict["hp"]))
   

def add_attack(score, dict):
    dict["attack"] = dict["attack"] + score
    print("attack: "+str(dict["attack"]))

def add_money(score, dict):
    dict["money"] = dict["money"] + score
    print("money: "+str(dict["money"]))



def minus_hp(score, dict):
    dict["hp"] = dict["hp"] - score
    print("hp: "+str(dict["hp"]))


def minus_attack(score, dict):
    dict["attack"] = dict["attack"] - score
    print("attack: "+str(dict["attack"]))



def minus_money(score, dict):
    dict["money"] = dict["money"] - score
    print("money: "+str(dict["money"]))

    


def go_west_forest():
    print("You are in the western corner of the forest. You see something lurking in the shadow")
    first_choice=input("Do you want to investigate?  (y/n)")
    if first_choice=="y":
        print("A ghost appears. If it is knowledge you seek, step forward and answer my riddle  ")
        second_choice=input("Do you want to solve the riddle? y/n")
        if second_choice=="y":
            print("What is not alive but grows, does not breaths but needs air.")
            print()
            print("You are allowed to only give one word ")
            riddle_answer=input("What is it?").capitalize()
            if riddle_answer=="Fire":
                print("You surprise me",race_input,"Here is some Gold")
                print()
                print("What you seek can be found where the sun shines less.")
                if race_input == "human":
                    add_money(5, human)
                elif race_input == "elf":
                    add_money(5, elf)
                else:
                    add_money(10, dwarf)
                    print("You gained more money thanks to your ability, Hard Bargain !")
                
            else:
                print("Wrong answer. Leave")
                if race_input == "human":
                    minus_hp(5, human)
                elif race_input == "elf":
                    minus_hp(5, elf)
                else:
                    minus_hp(2, dwarf)
        else:
            print("have it your way! You go back to the middle of the forest.")
    else:
        print("You go back to the middle of the forest")

#go_west_forest()


def go_south_forest():
    print("You are in the southern corner of the forest. You hear a whisper. The voice comes from a small hut in the distance")
    first_choice=input("Do you want to get closer? y/n")
    if first_choice=="y":
        print("You enter the hut. An old lady is sitting next to the fire. The light is dim and the hut smells of mixed herbs and berries")
        print("You who stands at my door, it's time to play a game.")
        print("You are pushed by some sort of magic and you find yourself sitting at a table. The old lady is sitting in front of you. She gives you a couple of dice.")
        second_choice=input("You lost all your money.You can decide to leave now or try your fortune.""What do you wanna do?" "Flee or Play?")
        if second_choice=="Play":
          
         import random
        min = 1
        max = 6

        roll_again = "yes"

        while roll_again == "yes" or roll_again == "y":
                print ("Rolling the dices...")
                print ("You got...")
                print (random.randint(min, max))
                

                roll_again = input("Roll the dices again?" )  
        else:
            print("potato")        
    else:
        print("potato")       



 
#Variables list

#Rolling the dice
"""
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")
"""

