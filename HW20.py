#Name:logan
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print('hello world')

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    z=int(input('ender a number to be divided by 100: '))
    print(100/z)
except:
    print('divide by 0 error')

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    q=int(input('enter a number: '))
    print(q)
except:
    print('only integers')

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
a = 5

while a >= 0:
    try:
        print(a)
        a -= 1

        if a < 0:
            raise ValueError("Counter has gone below zero!")
    except ValueError as e:
        print(f"Exception: {e}")
        break
