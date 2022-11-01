print("Hello, traveler! Welcome to the Stinging Forest. Watch out! You're standing too close to poisonous flowers. One bite - and you're dead.")
decision = input("Do you want to continue? y/n")

if decision == "y":
    print("Good choice, brave warrior! A lot of treacherous adventures are awaiting for you")
else: 
    print("Farewell, traveler!")

print("Choose your race: ")
print("1. Human", "2. Elf", "3. Dwarf", sep = "\n")


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
#attributes = dir(human)
#print(f"race: {human.race}, hp: {human.hp}, attack: {human.attack}, money: {human.money}", sep="\n")
print("race: "+human.race, "hp: "+str(human.hp), "attack: "+str(human.attack), "money: "+str(human.money), sep="\n")
#print(attributes)
"""   
    print("race: ", race)
    print("hp: ", hp)
    print("armour: ", armour)
    print("attack: ", attack)
    print("money", money)

"""
#human = Race("human", 50, "sword", 20, 30)
#print(human)
"""list = []

list.append(Race("human", 50, "sword", 20, 30))
list.append(Race("elf", 50, "bow and arrows", 20, 50))
list.append(Race("dwarf", 50, "hammer", 20, 100))



print(list)
#character = race("human")
#print(character)

race = input("Choose your race")

if race == "human":
    print(list[0])
elif race == "elf":
    print(list[1])
elif race == "dwarf":
    print(list[2])


x = input("Choose your movement")
hp = 50

if x == "hit":
    list.append(Race("human", 48, "sword", 20, 30))
    hp = Race.hp_count(50)
    print("hp: ", hp)
    #print("hp:", list[0].hp)
    #print(human.hp)




#def stats_count
"""