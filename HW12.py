#Name:Logan
#Class: 6th Hour
#Assignment: HW12
import time
#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
rang = [5,3,1,2,4]
rang.sort()
for i in rang:
    print(i)
    time.sleep(0.2)
else:
    print('hello world')
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for h in range(31):
    if h % 2 == 0:
        print(h)
#3. Create a for loop that prints 5 different animals from a list.
animal=['cat', 'dog', 'bird', 'snake', 'lion']
for a in animal:
    print(a)
#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for e in input('enter your name: ')[::-1]:
    print(e)