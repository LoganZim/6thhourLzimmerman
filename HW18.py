#Name:logan z
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag=['red','yellow','brown','green','grey']
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pull():
    x = random.choice(beanbag)
    print(x,'was the color pulled')
    beanbag.remove(x)
    again()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def again():
    y=input('do you want to pull another bean out of the bag: ')
    if y == 'yes':
        pull()
    if y == 'no':
        exit()

#5. Call the #3 function at the bottom.
pull()