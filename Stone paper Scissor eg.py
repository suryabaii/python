import random
Rock='r'
Paper='P'
Scissors='s'
emojis={Rock:'🪨',Paper:'📰',Scissors:'✂️'}
choices=tuple(emojis.keys())

def get_user():
    user_choice =input('Guess the option?(r/p/s)').lower()
    if user_choice  in choices:
              return user_choice
    else:
        print('Invalid Input')
def display(user_choice,computer_choice):
       print (f'Youre Choice:{emojis[user_choice]}')
       print (f'Computer Choice:{emojis[computer_choice]}')    
def determine_winner(user_choice,computer_choice):
       if user_choice==computer_choice:
              print('Tie')
       elif (user_choice==Rock and computer_choice==Scissors) or (user_choice==Paper and computer_choice==Rock) or (user_choice==Scissors and computer_choice==Paper):
              print("Congrats you Won")
       else:
              print('You Lose')    
       
def play():
            
    while True:
       
       user_choice=get_user() 
       computer_choice=random.choice(choices)
       display(user_choice,computer_choice)
       determine_winner(user_choice,computer_choice)       
       want_to=input('continue?(y/n)') .lower()
       if want_to=='n':
               break
play()                    