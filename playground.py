#logan zimmerman
#6 hour
#playground


print('hello world! ')






#intro
print('you are going to put in what simple equation you want to use then you can plug in the numbers you want to use')

#variables
s=(input('enter the kind of problem you want to do (addition,subtraction,multiplication, or division): '))

#addition
if s==('addition'):
    f=int(input('ok, what is the first number you want to add: '))
    d=int(input('now what is your second number: '))
    g=input('do you want to add a third number: ')


    list1 = [f,d]
    if g==('yes'):
        y=int(input('ok what is the 3rd number you want to add: '))
        list1.append(y)
        print('ok, your answer is: ', list1[0]+list1[1]+list1[2])
    else:
        print('ok')
        print('your answer is: ', list1[0] + list1[1])

#subtracton
if s==('subtraction'):
    f = int(input('ok, what is the first number you want to subtract: '))
    d = int(input('now what is your second number: '))
    g = input('do you want to subtract those two by a third number: ')

    list1 = [f, d]
    if g == ('yes'):
        y = int(input('ok what is the 3rd number you want to use: '))
        list1.append(y)
        print('ok, your answer is: ', list1[0] - list1[1] - list1[2])
    else:
        print('ok')
        print('your answer is: ', list1[0] - list1[1])

#multiplication
if s==('multiplication'):
    f = float(int(input('ok, what is the first number you want to multiply: ')))
    d = float(int(input('now what is your second number: ')))
    g = input('do you want to multiply those two by a third number: ')

    list1 = [f, d]
    if g == ('yes'):
        y = int(input('ok what is the 3rd number you want to use: '))
        list1.append(y)
        print('ok, your answer is: ', list1[0] * list1[1] * list1[2])
    else:
        print('ok')
        print('your answer is: ', list1[0] * list1[1])

#division
if s==('division'):
    f = float(int(input('ok, what is the first number you want to divide with: ')))
    d = float(int(input('now what is your second number: ')))
    g = input('do you want to divide those two by a third number: ')

    list1 = [f, d]
    if g == ('yes'):
        y = int(input('ok what is the 3rd number you want to use: '))
        list1.append(y)
        print('ok, your answer is: ', list1[0] / list1[1] / list1[2])
    else:
        print('ok')
        print('your answer is: ', list1[0] / list1[1])



