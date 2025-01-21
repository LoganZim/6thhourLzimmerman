#Name: logan z
#Class: 6th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print('hello world')
#2. Create two empty integer variables named "heads" and "tails"
heads=0
tails=0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip(*c):
    for i in range(*c):
        x=random.randint(1,2)
        if x == 1:
            global heads
            heads+=1
        else:
            global tails
            tails+=1
#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
coin_flip(100)
#5. Print the final result of heads and tails here
print('there were',heads,'heads')
print('there were',tails,'tails')