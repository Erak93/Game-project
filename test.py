print("Hello, traveler! Welcome to the Stinging Forest. Watch out! You're standing too close to poisonous flowers. One bite - and you're dead.")
decision = input("Do you want to continue? y/n")
if decision == "y":
    print("Good choice, brave warrior! A lot of treacherous adventures are awaiting for you")
else:
    print("Farewell, traveler!")
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
    #print("race: ", race)
    #print("hp: ", hp)
    #print("attack: ", attack)
    #print("money", money)
human = Race("human", 50, 20, 30)
elf=Race("elf", 20,50,30)
dwarf=Race("dwarf",30,20,50)

def human_features():
    print("race: "+human.race, "hp: "+str(human.hp), "attack: "+str(human.attack), "money: "+str(human.money), sep="\n")

def elf_features():
    print("race: "+elf.race, "hp: "+str(elf.hp), "attack: "+str(elf.attack), "money: "+str(elf.money), sep="\n")

def dwarf_features():
    print("race: "+dwarf.race, "hp: "+str(dwarf.hp), "attack: "+str(dwarf.attack), "money: "+str(dwarf.money), sep="\n")


chosen_race=input("1. Human 2. Elf 3. Dwarf")
if chosen_race =="human":
    human_features()
elif chosen_race=="elf":
    elf_features()
elif chosen_race=="dwarf":
    dwarf_features()
else:
    print("potato")


#print("race: "+human.race, "hp: "+str(human.hp), "attack: "+str(human.attack), "money: "+str(human.money), sep="\n")








