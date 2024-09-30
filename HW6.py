#Name:logan
#Class: 5th Hour
#Assignment: HW6


#Objectives

#1. Print Hello World!
print('Hello World!')
#2. Create a variable named num and assign it a variable.

while True:
    num=float(input('Enter a number:'))


#3. Create a nested if statement follows this structure:

#If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3
    if num%2==0:
        if num%3==0:
            print ('the result of num being divided by 2\n', num/2)
            print ('the result of num being divided by 3\n', num/3)
        else:
            print ('that it is not divisible by 3\n')
            print ('the result of num being divided by 2\n', num/2)
    else:
        if num%3==0:
            print ('that num is not divisible by 2\n')
            print ('the result of num being divided by 3\n', num/3)
        else:
            print ('that neither is divisible by 2 or 3')
