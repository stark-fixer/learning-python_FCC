import random #importing module random

def get_choise(): #making of our function
    player_choise=input('enter a choice,rock,paper or scissors:') #taking input
    options=['rock','paper','scissors'] #creating a list
    computer_choise=random.choice(options) #using random.choice() in options for the computer_choise to choose randomly.
    choices={'player':player_choise, 'computer':computer_choise}
    return choices




