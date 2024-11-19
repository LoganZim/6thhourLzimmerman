#Name:Logan
#Class: 6th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.
import random
#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the rating
dressColor=['red','yellow', 'blue', 'green', 'brown', 'purple', 'pink']
hair=['ponytail', 'wavy', 'curly', 'bangs', 'straight']
eyes=['blue', 'green', 'brown', 'hazel', 'grey']

while True:
    print('hello player, you have been chosen to rate some models')
    x=int(input('first we need to know how many models there are(max 10): '))
    if x >10:
        print('Max 10')
    else:
        pass
    for i in x

