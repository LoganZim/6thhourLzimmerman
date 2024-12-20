#Name: logan
#Class: 6th Hour
#Assignment: Scenario 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4


import random

from scenario1 import enemyDict

#Party Dictionary Goes Here
partyDict={
    "Lae'Zel":{
        "HP":10,
        "Attack mod":5,
        "Damage roll":random.randint(1,6),
        "AC":16,
    },
    "Shadowheart":{
        "HP":10,
        "Attack mod":4,
        "Damage roll":random.randint(1,6),
        "AC":17,
    },
    "Gale":{
        "HP":25,
        "Attack mod":5,
        "Damage roll":random.randint(1,6),
        "AC":10,
    },
    "Astarion":{
        "HP":15,
        "Attack mod":7,
        "Damage roll":random.randint(1,6),
        "AC":15,
    },

}
print(partyDict)

#Enemy Dictionary Goes Here
partyDict={
    "megatron":{
        "HP":17,
        "Attack mod":7,
        "Damage roll":random.randint(1,6),
        "AC":16,
    },
    "giant":{
        "HP":25,
        "Attack mod":5,
        "Damage roll":random.randint(1,6),
        "AC":13,
    },
    "orc":{
        "HP":12,
        "Attack mod":6,
        "Damage roll":random.randint(1,6),
        "AC":11,
    },
    "grog":{
        "HP":10,
        "Attack mod":4,
        "Damage roll":random.randint(1,6),
        "AC":10,
    },

}



#Combat Code Goes Here
partyChoice=input("enter a party member you want to have battle: ")
enemyChoice=input("enter an enemy member you want to battle: ")
if partyChoice == "Lae'Zel" and enemyChoice == "megatron":
    print("Lae'Zel attacks megatron")
    w=random.randint(1,20)
    if w+partyDict["Lae'Zel"]["Attack mod"] < enemyDict["megatron"]["AC"]:
        input("Lae'Zel missed")
    else:
        x=enemyDict["megatron"]["HP"]-(partyDict["Lae'Zel"]["Attack mod"]+partyDict["Lae'Zel"]["Damage roll"])
        if x <= 0:
            print('megatron has been killed')
        if x > 0:
            print('megatron now has', enemyDict["megatron"]["HP"] - x, 'HP')
            input()
            print("megatron is now going to attack Lae'Zel")
            y = partyDict["Lae'Zel"]["HP"] - (enemyDict["megatron"]["Attack mod"] + enemyDict["megatron"]["Damage roll"])
            input()
            if y <= 0:
                print("Lae'Zel has been killed")
            if y > 0:
                print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')

'''
if partyChoice == "Lae'Zel" and enemyChoice == "giant":
if partyChoice == "Lae'Zel" and enemyChoice == "orc":
if partyChoice == "Lae'Zel" and enemyChoice == "grog":
if partyChoice == "Shadowheart" and enemyChoice == "megatron":
if partyChoice == "Shadowheart" and enemyChoice == "giant":
if partyChoice == "Shadowheart" and enemyChoice == "orc":
if partyChoice == "Shadowheart" and enemyChoice == "grog":
if partyChoice == "Gale" and enemyChoice == "megatron":
if partyChoice == "Gale" and enemyChoice == "giant":
if partyChoice == "Gale" and enemyChoice == "orc":
if partyChoice == "Gale" and enemyChoice == "grog":
if partyChoice == "Astarion" and enemyChoice == "megatron":
if partyChoice == "Astarion" and enemyChoice == "giant":
if partyChoice == "Astarion" and enemyChoice == "orc":
if partyChoice == "Astarion" and enemyChoice == "grog":
'''