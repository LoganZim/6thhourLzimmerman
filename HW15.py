#Name:Logan
#Class: 6th Hour
#Assignment: HW15



#1. Create a def function that prints out "Hello World!"
def hello_world():
    print('hello world')

hello_world()
#2. Create a def function that calculates the average of three numbers.
def avr():
    n1=int(input('enter number 1:'))
    n2=int(input('enter number 2:'))
    n3=int(input('enter number 3:'))
    average=(n1+n2+n3)/3
    print('the average is',average)
avr()
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal(*a):
    print(a[2])
animal('monkey', 'bird', 'dog','cat','owl')
#4. Create a def function that loops from 1 to the number put in the argument.
def loop(*l):
    x=1
    for i in range(*l):
        print(x)
        x+=1

loop(5)
#5. Call all of the functions created in 1 - 4 with relevant arguments.

