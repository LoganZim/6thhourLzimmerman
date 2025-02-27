#logan zimmerman
#6 hour
#playground
import random

s=1
def highOrLow():
    global s
    x = random.randint(1, 100)
    y=0
    print('\nYou will be playing a lottery number game.\n\nIf you pick the right number you will get',s,'M in cash.\n\nIf wrong you go home.\n')
    print('Ok, i am thinking of a number in my head and you will have 5 attempts to guess that number out of 100 and i will help you by telling you higher or lower.\n')
    while y < 4:
        z=int(input('enter a number: '))
        if z < x:
            print('higher')
        elif z > x:
            print('lower')
        else:
            print('you guessed it, you won',s,'M')
            t = input('\ndo you want to double or nothing: ')
            if t == 'yes':
                s*=2
                highOrLow()
            if t == 'no':
                print('have fun with your money then')
                exit()
            exit()
        y += 1
    w=int(input('Ok, you are on to your last guess, what will it be: '))
    if w < x:
        print('ooo! the number was',x,)
        p = input('do you want to try again(yes or no): ')
        if p == 'yes':
            highOrLow()
        if p == 'no':
            print('ok')
            exit()
    elif w > x:
        print('ooo! the number was', x)
        p=input('do you want to try again(yes or no): ')
        if p == 'yes':
            highOrLow()
        if p == 'no':
            print('ok')
            exit()
    else:
        print('you guessed it, you won',s,'M')
        t=input('\ndo you want to double or nothing: ')
        if t == 'yes':
            s*=2
            highOrLow()
        if t == 'no':
            print('have fun with your money then')
            exit()
highOrLow()