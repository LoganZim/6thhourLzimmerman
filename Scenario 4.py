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
clothing=['dress','suit']
color=['red','yellow','green','black','grey','brown']
hair=['wavy', 'curly', 'straight']
eyes=['blue', 'green', 'brown', 'hazel', 'grey']
overall=[]
print('hello player, you have been chosen to rate some models')
x=int(input('first we need to know how many models there are(max 10): '))
if x >10:
    print('Max 10')
    exit()
else:   pass
for i in range(x):
    print('model number',i+1,'is wearing a',random.choice(color),random.choice(clothing),'and has',random.choice(hair),'hair and',random.choice(eyes),'eyes')
    rating=int(input('how would you rate this model (1-10): '))
    if rating > 10: rating=10
    if rating < 1: rating=1
    overall.insert(i,rating)
print("the overall average of all of your ratings is", sum(overall)/x)


