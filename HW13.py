#Name:Logan
#Class: 6th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
List1=[12,3,56,5,43,78,1,23,87,32]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers=0
oddNumbers=0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in List1:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
print(' there are', evenNumbers,'even numbers and',oddNumbers,'odd numbers' )
# Print the total count of even and odd numbers.