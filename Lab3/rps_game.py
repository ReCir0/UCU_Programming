answers = []
def playing(play):
    if play[0] == "S" and play[1] == "R":
        answers.insert(len(answers), "False")
    elif play[0] == "S" and play[1] == "P":
        answers.insert(len(answers), "True")
    elif play[0] == "R" and play[1] == "S":
        answers.insert(len(answers), "True")
    elif play[0] == "R" and play[1] == "P":
        answers.insert(len(answers), "False")
    elif play[0] == "P" and play[1] == "S":
        answers.insert(len(answers), "False")
    elif play[0] == "P" and play[1] == "R":
        answers.insert(len(answers), "True")
    else:
        answers.insert(len(answers), "False | False")
        
while True:
    play = input()
    if play == "":
        break
    playing(play)
    
for i in answers:
    print(i)