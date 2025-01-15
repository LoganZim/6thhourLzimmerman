#Name:logan
#Class: 6th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps():
    x=int(input('enter rock(1) paper(2) or scissors(3): '))
    y=random.randint(1,3)
    if x==y:
        print('draw')
    elif x==1 and y==2:
        print('they picked paper, you lost')
    elif x == 1 and y == 3:
        print('they picked scissors, you won')
    elif x == 2 and y == 1:
        print('they picked rock, you won')
    elif x == 2 and y == 3:
        print('they picked scissors, you lost')
    elif x == 3 and y == 1:
        print('they picked rock, you lost')
    elif x == 3 and y == 2:
        print('they picked paper, you won')
rps()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
z=input('do you want to play again: ')
if z != 'yes':
    exit()
else:
    rps()