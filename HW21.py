#Name:logan
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
dict={
    'sport1' : {
        'baseball': True,
        'players' : 9

    },
    'sport2' : {
        'football': True,
        'players' : 11
    },
    'sport3' : {
        'basketball': True,
        'players' : 5
    },
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def pull():
    print(dict['sport1']['players']+dict['sport2']['players']+dict['sport3']['players'])
#3. Call the function with arguments here
pull()