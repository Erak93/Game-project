print("Intro about the world, background story and classes introduction")

race=input("Come closer. I can not really see you well. Who are you?   ")
race_class=input("What is your fighting style?" "Warrior,Archer or Wizard?   ")
hp="placeholder"
atk="placeholder"
armor="placeholder"

if race_class=="Warrior":
    hp=20
    atk=10
    armor=0
elif race_class=="Archer":
    hp=10
    atk=20
    armor=0
elif race_class=="Wizard":
    hp=30
    atk=0
    armor=0



def mycharacter(race,race_class):
  print("Your race is: ",race)
  print("Your class is:",race_class)
  print("Your hp is: ",hp)
  print("Your atk is:", atk)
  

mycharacter(race,race_class) 