#Name:
#Class: 6th Hour
#Assignment: HW7
def w(msg):
    while True:
        try:

            return input(msg)


        except ValueError:

            print('nuh uh')

#1. Print Hello World!
print ('Hello World!')
#2. Create three different boolean variables named wifi, login, and admin.
wifi = w('enter if wifi = true or false')
login = w('enter if login = true or false')
admin = w('enter if admin = true or false')
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
Admin=0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == 'True':
    print()
    if login == 'True':
        print()
        if admin == 'True':
            print('welcome, there are', Admin + 1,'admins in here')
if wifi == 'False':
    print('you need wifi')
if login == 'False':
    print('you need to login')
if admin == 'False':
    print('you need an admin')