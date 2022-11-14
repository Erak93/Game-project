"""
scores = 0
scores = {"points": 0}
def add_score(score, dict):
    dict["points"] = dict["points"] + score
    print("points: ", dict["points"])



#def minus_score():

def test_score():
    choice = input("Do you want to kill a smuggler? y/n")
    if choice == "y":
        add_score(2, scores)
    else:
        add_score(4, scores)
"""

"""
one dict for hp, attack and armor, points
after killing monster:
call three functions:
add-points/substract-point
substract-hp/add-hp
add-armor/substract-armor
"""




"""

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

go_west_forest()

test_score()
"""
human = {"race": "human", "hp": 50, "attack": 20, "money": 30}
elf = {"race": "elf", "hp": 20, "attack": 50, "money": 30}
dwarf = {"race": "dwarf", "hp": 30, "attack": 20, "money": 50}   



"""
def human_features():
    print("race: "+human["race"], "hp: "+str(human["hp"]), "attack: "+str(human["attack"]), "money: "+str(human["money"]), sep="\n")

def elf_features():
     print("race: "+elf["race"], "hp: "+str(elf["hp"]), "attack: "+str(elf["attack"]), "money: "+str(elf["money"]), sep="\n")

def dwarf_features():
     print("race: "+dwarf["race"], "hp: "+str(dwarf["hp"]), "attack: "+str(dwarf["attack"]), "money: "+str(dwarf["money"]), sep="\n")



human_features()
elf_features()
dwarf_features()
"""

race_input=input("Come closer. I can not really see you well. Who are you?   ")

"""

def add_hp(score, race_input):
    if race_input == "human":
        human["hp"] = human["hp"] + score
        print("hp: ", human["hp"])
    elif race_input == "elf":
        elf["hp"] = elf["hp"] + score
        print("hp: ", elf["hp"])

add_hp(2, race_input)
"""

