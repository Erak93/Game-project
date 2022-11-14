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
