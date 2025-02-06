import random

num=random.randint(1,100)
while True:
    try:
        guess=int(input('guess num:'))
        if guess>num:
            print('High')
        elif guess<num:
            print('small')
        else:
            print('Congrats')
            break
            
    except ValueError:
         print('ENter valid int')
