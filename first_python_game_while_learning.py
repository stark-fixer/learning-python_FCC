import random #importing module random

def get_choise(): #making of our function
    player_choise=input('enter a choice,rock,paper or scissors:') #taking input
    options=['rock','paper','scissors'] #creating a list
    computer_choise=random.choice(options) #using random.choice() in options for the computer_choise to choose randomly.
    choices={'player':player_choise, 'computer':computer_choise}
    return choices

def check_win(player,computer):
    print(f"You chose {player},computer chose {computer}") #using fstring
    #using NESTED IFs:-
    if player==computer:                                     
        return"It's a tie!"
    if player=='rock':
        if computer=='scissors':
          return('Rock smashes scissors! You win!')
        else:
          return('Paper covers the rock! You lose')  
    if player=='paper':
        if computer=='rock':
          return('Paper covers rock! You win!')
        else:
          return('scissors cut papers! You lose')  
    if player=="scissors":
        if computer=='paper':
          return('Scissors cut paper! You win!')
        else:
          return('Rock smashes scissors! You lose')        

#KNOWING THE RESULTS
choises=get_choise()
result=check_win(choises['player'],choises['computer'])#it will get the user's and the computer choise and will check the results based on our nested if commands[also learn how to acess disctionary values]
print(result)#printing the final result.   


