#Functions list


#Class function

class Race():
    def __init__(self, race, hp, attack, money):
        self.race = race
        self.hp = hp
        self.attack = attack
        self.money = money
    def hp_count (self, hp):
        hp = hp-2
    def attack_count(self):
        attack = attack-2
    def money_count(self):
        money = money+3
   
human = Race("human", 50, 20, 30)
elf=Race("elf", 20,50,30)
dwarf=Race("dwarf",30,20,50)

def human_features():
    print("race: "+human.race, "hp: "+str(human.hp), "attack: "+str(human.attack), "money: "+str(human.money), sep="\n")

def elf_features():
    print("race: "+elf.race, "hp: "+str(elf.hp), "attack: "+str(elf.attack), "money: "+str(elf.money), sep="\n")

def dwarf_features():
    print("race: "+dwarf.race, "hp: "+str(dwarf.hp), "attack: "+str(dwarf.attack), "money: "+str(dwarf.money), sep="\n")

scores = {"points": 0}
def add_score(score, dict):
    dict["points"] = dict["points"].value + score
    print(dict["points"])


def minus_score():


def go_west_forest():
    print("You are in the western corner of the forest. A misterious figure appear")
    first_choice=input("Do you want to investigate?  (y/n)")
    if first_choice=="y":
        print("A ghost appears. If it is knowledge you seek, step forward and answer my riddle  ")
        second_choice=input("Do you want to solve the riddle? y/n")
        if second_choice=="y":
            print("riddle riddle")
            riddle_answer=input("What is it?")
            if riddle_answer=="right answer":
                print("congratulations. Here is your hint")
                add_score(2, scores)
            else:
                print("Wrong answer. Leave")
        else:
            print("have it your way! You go back to the middle of the forest.")
    else:
        print("You go back to the middle of the forest")


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

