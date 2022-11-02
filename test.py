#import quest1 
print("Hello, traveler! Welcome to the Stinging Forest. Watch out! You're standing too close to poisonous flowers. One bite - and you're dead.")
decision = input("Do you want to continue? y/n ")
if decision == "y":
    print("Good choice, brave warrior! A lot of treacherous adventures are awaiting for you")
elif decision == "n":
    print("Farewell, traveler!")
else:
    print("Please enter only 'y' or 'n'")
print("Choose your race: ")
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

print("It is time to pick your race. Here is an overview")
print()
print("HUMANS")
human_features()
print()
print("ELVES")
elf_features()
print("DWARF")
dwarf_features()
print()

chosen_race=str.lower(input(("Which race will you choose? ")))
if chosen_race =="human":
    human_features()
elif chosen_race=="elf":
    elf_features()
elif chosen_race=="dwarf":
    dwarf_features()
else:
    print("potato")

print("What quest would you like to choose? ")
print("1. Wild Forest Adventure", "2. Wicked Witch Confrontation", "3. Greedy Leprechaun Bargain", sep = "\n")


quest_choice = input("Which quest will you choose? 1, 2 or 3 ")

#script_type = ""

#def choosing_quest(script_type):
 #   return script_type

if quest_choice == "1":
    import quest1
    
    #execfile("\Admin\Desktop\Python\VScode\Exercises-from-Window\Game-project\quest1.py")
       











