#Name:logan
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class market:
    def __init__(self,stock,cost,weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
banana=market(10,2,2)
apple=market(25,1,2)
pumpkin=market(8,3,8)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"the banana stock: {banana.stock}")
print(f"the apple stock: {apple.stock}")
print(f"the pumpkin stock: {pumpkin.stock}")
print(f'the apple costs: {apple.cost}')

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
apple.double()
print(f'the apple costs: {apple.cost}')
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
pumpkin.stock = 2
print(f'the new pumpkin stock is: {pumpkin.stock}')
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del banana
try:
    print(f'the bananas weight is: {banana.weight}')
except NameError:
    print('nuh uh')
