import random
def user_input():
    choice=input('Roll The Dice ? (y/n)').lower()
    return choice
def roll():
 while True:
    try:
      choice=user_input()
      die1=random.randint(1,7)
      die2=random.randint(1,7)
      if choice=='y':
        print ({die1},{die2})
      elif choice=='n':
        print ('ThankYou')
        break
      else:
        'Invalid Input'
    except NameError:
      pass      
roll()