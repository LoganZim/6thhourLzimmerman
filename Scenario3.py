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
print('Hello World!')
def r(msg):
    while True:
        try:

            return input(msg)


        except ValueError:

            print('nuh uh')
import random

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
enemyDict={
    "Megatron":{
        "HP":17,
        "Attack mod":7,
        "Damage roll":random.randint(1,6),
        "AC":16,
    },
    "Giant":{
        "HP":25,
        "Attack mod":5,
        "Damage roll":random.randint(1,6),
        "AC":13,
    },
    "Orc":{
        "HP":12,
        "Attack mod":6,
        "Damage roll":random.randint(1,6),
        "AC":11,
    },
    "Grog":{
        "HP":10,
        "Attack mod":4,
        "Damage roll":random.randint(1,6),
        "AC":10,
    },

}
print(enemyDict)


#Combat Code Goes Here
partyChoice=r("enter a party member you want to have battle: ")
enemyChoice=r("enter an enemy member you want to battle: ")
if partyChoice == "Lae'Zel" and enemyChoice == "Megatron":
    print("Lae'Zel attacks megatron")
    w=random.randint(1,20)
    if w+partyDict["Lae'Zel"]["Attack mod"] < enemyDict["Megatron"]["AC"]:
        input("Lae'Zel missed")
        print("Megatron is now going to attack Lae'Zel")
        e = random.randint(1, 20)
        if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
            print('megatron missed')
        else:
            y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
            input()
            if y <= 0:
                print("Lae'Zel has been killed")
            if y > 0:
                print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')
    else:
        x=enemyDict["Megatron"]["HP"]-(partyDict["Lae'Zel"]["Attack mod"]+partyDict["Lae'Zel"]["Damage roll"])
        if x <= 0:
            print('Megatron has been killed')
        if x > 0:
            print('Megatron now has', enemyDict["Megatron"]["HP"] - x, 'HP')
            input()
            print("Megatron is now going to attack Lae'Zel")
            e=random.randint(1,20)
            if e+enemyDict["Megatron"]["Attack mod"]<partyDict["Lae'Zel"]["AC"]:
                print('megatron missed')
            else:
                y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
                input()
                if y <= 0:
                    print("Lae'Zel has been killed")
                if y > 0:
                    print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')


if partyChoice == "Lae'Zel" and enemyChoice == "Giant":
    print("Lae'Zel attacks Giant")
    w = random.randint(1, 20)
    if w + partyDict["Lae'Zel"]["Attack mod"] < enemyDict["Giant"]["AC"]:
        input("Lae'Zel missed")
        print("Giant is now going to attack Lae'Zel")
        e = random.randint(1, 20)
        if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
            print('Giant missed')
        else:
            y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Lae'Zel has been killed")
            if y > 0:
                print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Giant"]["HP"] - (partyDict["Lae'Zel"]["Attack mod"] + partyDict["Lae'Zel"]["Damage roll"])
        if x <= 0:
            print('Giant has been killed')
        if x > 0:
            print('Giant now has', enemyDict["Giant"]["HP"] - x, 'HP')
            input()
            print("Giant is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Giant"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
                print('Giant missed')
            else:
                y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
                input()
                if y <= 0:
                    print("Lae'Zel has been killed")
                if y > 0:
                    print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')

if partyChoice == "Lae'Zel" and enemyChoice == "Orc":
    print("Lae'Zel attacks Orc")
    w = random.randint(1, 20)
    if w + partyDict["Lae'Zel"]["Attack mod"] < enemyDict["Orc"]["AC"]:
        input("Lae'Zel missed")
        print("Orc is now going to attack Lae'Zel")
        e = random.randint(1, 20)
        if e + enemyDict["Orc"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
            print('Orc missed')
        else:
            y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
            input()
            if y <= 0:
                print("Lae'Zel has been killed")
            if y > 0:
                print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Orc"]["HP"] - (partyDict["Lae'Zel"]["Attack mod"] + partyDict["Lae'Zel"]["Damage roll"])
        if x <= 0:
            print('Orc has been killed')
        if x > 0:
            print('Orc now has', enemyDict["Orc"]["HP"] - x, 'HP')
            input()
            print("Orc is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Orc"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
                print('megatron missed')
            else:
                y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
                input()
                if y <= 0:
                    print("Lae'Zel has been killed")
                if y > 0:
                    print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')

if partyChoice == "Lae'Zel" and enemyChoice == "Grog":
    print("Lae'Zel attacks Grog")
    w = random.randint(1, 20)
    if w + partyDict["Lae'Zel"]["Attack mod"] < enemyDict["Grog"]["AC"]:
        input("Lae'Zel missed")
        print("Grog is now going to attack Lae'Zel")
        e = random.randint(1, 20)
        if e + enemyDict["Grog"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
            print('Grog missed')
        else:
            y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
            input()
            if y <= 0:
                print("Lae'Zel has been killed")
            if y > 0:
                print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Grog"]["HP"] - (partyDict["Lae'Zel"]["Attack mod"] + partyDict["Lae'Zel"]["Damage roll"])
        if x <= 0:
            print('Grog has been killed')
        if x > 0:
            print('Grog now has', enemyDict["Grog"]["HP"] - x, 'HP')
            input()
            print("Grog is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Grog"]["Attack mod"] < partyDict["Lae'Zel"]["AC"]:
                print('Grog missed')
            else:
                y = partyDict["Lae'Zel"]["HP"] - (enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
                input()
                if y <= 0:
                    print("Lae'Zel has been killed")
                if y > 0:
                    print("Lae'Zel now has", partyDict["Lae'Zel"]["HP"] - y, 'HP')

if partyChoice == "Shadowheart" and enemyChoice == "Megatron":
    print("Shadowheart attacks megatron")
    w = random.randint(1, 20)
    if w + partyDict["Shadowheart"]["Attack mod"] < enemyDict["Megatron"]["AC"]:
        input("Shadowheart missed")
        print("Megatron is now going to attack Shadowheart")
        e = random.randint(1, 20)
        if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
            print('megatron missed')
        else:
            y = partyDict["Shadowheart"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
            input()
            if y <= 0:
                print("Shadowheart has been killed")
            if y > 0:
                print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Megatron"]["HP"] - (partyDict["Shadowheart"]["Attack mod"] + partyDict["Shadowheart"]["Damage roll"])
        if x <= 0:
            print('Megatron has been killed')
        if x > 0:
            print('Megatron now has', enemyDict["Megatron"]["HP"] - x, 'HP')
            input()
            print("Megatron is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
                print('megatron missed')
            else:
                y = partyDict["Shadowheart"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
                input()
                if y <= 0:
                    print("Shadowheart has been killed")
                if y > 0:
                    print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')

if partyChoice == "Shadowheart" and enemyChoice == "Giant":
    print("Shadowheart attacks Giant")
    w = random.randint(1, 20)
    if w + partyDict["Shadowheart"]["Attack mod"] < enemyDict["Giant"]["AC"]:
        input("Shadowheart missed")
        print("Giant is now going to attack Shadowheart")
        e = random.randint(1, 20)
        if e + enemyDict["Giant"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
            print('Giant missed')
        else:
            y = partyDict["Shadowheart"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Shadowheart has been killed")
            if y > 0:
                print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Giant"]["HP"] - (partyDict["Shadowheart"]["Attack mod"] + partyDict["Shadowheart"]["Damage roll"])
        if x <= 0:
            print('Giant has been killed')
        if x > 0:
            print('Giant now has', enemyDict["Giant"]["HP"] - x, 'HP')
            input()
            print("Giant is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Giant"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
                print('Giant missed')
            else:
                y = partyDict["Shadowheart"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
                input()
                if y <= 0:
                    print("Shadowheart has been killed")
                if y > 0:
                    print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')

if partyChoice == "Shadowheart" and enemyChoice == "Orc":
    print("Shadowheart attacks Orc")
    w = random.randint(1, 20)
    if w + partyDict["Shadowheart"]["Attack mod"] < enemyDict["Orc"]["AC"]:
        input("Shadowheart missed")
        print("Orc is now going to attack Shadowheart")
        e = random.randint(1, 20)
        if e + enemyDict["Orc"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
            print('Orc missed')
        else:
            y = partyDict["Shadowheart"]["HP"] - (enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
            input()
            if y <= 0:
                print("Shadowheart has been killed")
            if y > 0:
                print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Orc"]["HP"] - (partyDict["Shadowheart"]["Attack mod"] + partyDict["Shadowheart"]["Damage roll"])
        if x <= 0:
            print('Orc has been killed')
        if x > 0:
            print('Orc now has', enemyDict["Orc"]["HP"] - x, 'HP')
            input()
            print("Orc is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Orc"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
                print('Orc missed')
            else:
                y = partyDict["Shadowheart"]["HP"] - (enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
                input()
                if y <= 0:
                    print("Shadowheart has been killed")
                if y > 0:
                    print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')

if partyChoice == "Shadowheart" and enemyChoice == "Grog":
    print("Shadowheart attacks Grog")
    w = random.randint(1, 20)
    if w + partyDict["Shadowheart"]["Attack mod"] < enemyDict["Grog"]["AC"]:
        input("Shadowheart missed")
        print("Grog is now going to attack Shadowheart")
        e = random.randint(1, 20)
        if e + enemyDict["Grog"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
            print('Grog missed')
        else:
            y = partyDict["Shadowheart"]["HP"] - (enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
            input()
            if y <= 0:
                print("Shadowheart has been killed")
            if y > 0:
                print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Grog"]["HP"] - (partyDict["Shadowheart"]["Attack mod"] + partyDict["Shadowheart"]["Damage roll"])
        if x <= 0:
            print('Grog has been killed')
        if x > 0:
            print('Grog now has', enemyDict["Grog"]["HP"] - x, 'HP')
            input()
            print("Grog is now going to attack Lae'Zel")
            e = random.randint(1, 20)
            if e + enemyDict["Grog"]["Attack mod"] < partyDict["Shadowheart"]["AC"]:
                print('Grog missed')
            else:
                y = partyDict["Shadowheart"]["HP"] - (enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
                input()
                if y <= 0:
                    print("Shadowheart has been killed")
                if y > 0:
                    print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
                if y > 0:
                    print("Shadowheart now has", partyDict["Shadowheart"]["HP"] - y, 'HP')
if partyChoice == "Gale" and enemyChoice == "Megatron":
    print("Gale attacks megatron")
    w = random.randint(1, 20)
    if w + partyDict["Gale"]["Attack mod"] < enemyDict["Megatron"]["AC"]:
        input("Gale missed")
        print("Megatron is now going to attack Gale")
        e = random.randint(1, 20)
        if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Gale"]["AC"]:
            print('megatron missed')
        else:
            y = partyDict["Gale"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
            input()
            if y <= 0:
                print("Gale has been killed")
            if y > 0:
                print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Megatron"]["HP"] - (partyDict["Gale"]["Attack mod"] + partyDict["Gale"]["Damage roll"])
        if x <= 0:
            print('Megatron has been killed')
        if x > 0:
            print('Megatron now has', enemyDict["Megatron"]["HP"] - x, 'HP')
            input()
            print("Megatron is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Gale"]["AC"]:
                print('megatron missed')
            else:
                y = partyDict["Gale"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
                input()
                if y <= 0:
                    print("Gale has been killed")
                if y > 0:
                    print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')

if partyChoice == "Gale" and enemyChoice == "Giant":
    print("Gale attacks Giant")
    w = random.randint(1, 20)
    if w + partyDict["Gale"]["Attack mod"] < enemyDict["Giant"]["AC"]:
        input("Gale missed")
        print("Giant is now going to attack Gale")
        e = random.randint(1, 20)
        if e + enemyDict["Giant"]["Attack mod"] < partyDict["Gale"]["AC"]:
            print('Giant missed')
        else:
            y = partyDict["Gale"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Gale has been killed")
            if y > 0:
                print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Giant"]["HP"] - (partyDict["Gale"]["Attack mod"] + partyDict["Gale"]["Damage roll"])
        if x <= 0:
            print('Giant has been killed')
        if x > 0:
            print('Giant now has', enemyDict["Giant"]["HP"] - x, 'HP')
            input()
            print("Giant is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Giant"]["Attack mod"] < partyDict["Gale"]["AC"]:
                print('Giant missed')
            else:
                y = partyDict["Gale"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
                input()
                if y <= 0:
                    print("Gale has been killed")
                if y > 0:
                    print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')

if partyChoice == "Gale" and enemyChoice == "Orc":
    print("Gale attacks Orc")
    w = random.randint(1, 20)
    if w + partyDict["Gale"]["Attack mod"] < enemyDict["Orc"]["AC"]:
        input("Gale missed")
        print("Orc is now going to attack Gale")
        e = random.randint(1, 20)
        if e + enemyDict["Orc"]["Attack mod"] < partyDict["Gale"]["AC"]:
            print('Orc missed')
        else:
            y = partyDict["Gale"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Gale has been killed")
            if y > 0:
                print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Orc"]["HP"] - (partyDict["Gale"]["Attack mod"] + partyDict["Gale"]["Damage roll"])
        if x <= 0:
            print('Orc has been killed')
        if x > 0:
            print('Orc now has', enemyDict["Orc"]["HP"] - x, 'HP')
            input()
            print("Orc is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Orc"]["Attack mod"] < partyDict["Gale"]["AC"]:
                print('Orc missed')
            else:
                y = partyDict["Gale"]["HP"] - (
                        enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
                input()
                if y <= 0:
                    print("Gale has been killed")
                if y > 0:
                    print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')

if partyChoice == "Gale" and enemyChoice == "Grog":
    print("Gale attacks Grog")
    w = random.randint(1, 20)
    if w + partyDict["Gale"]["Attack mod"] < enemyDict["Grog"]["AC"]:
        input("Gale missed")
        print("Grog is now going to attack Gale")
        e = random.randint(1, 20)
        if e + enemyDict["Grog"]["Attack mod"] < partyDict["Gale"]["AC"]:
            print('Grog missed')
        else:
            y = partyDict["Gale"]["HP"] - (enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Gale has been killed")
            if y > 0:
                print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Grog"]["HP"] - (partyDict["Gale"]["Attack mod"] + partyDict["Gale"]["Damage roll"])
        if x <= 0:
            print('Grog has been killed')
        if x > 0:
            print('Grog now has', enemyDict["Orc"]["HP"] - x, 'HP')
            input()
            print("Grog is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Grog"]["Attack mod"] < partyDict["Gale"]["AC"]:
                print('Grog missed')
            else:
                y = partyDict["Gale"]["HP"] - (
                        enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
                input()
                if y <= 0:
                    print("Gale has been killed")
                if y > 0:
                    print("Gale now has", partyDict["Gale"]["HP"] - y, 'HP')

if partyChoice == "Astarion" and enemyChoice == "Megatron":
    print("Astarion attacks megatron")
    w = random.randint(1, 20)
    if w + partyDict["Astarion"]["Attack mod"] < enemyDict["Megatron"]["AC"]:
        input("Astarion missed")
        print("Megatron is now going to attack Astarion")
        e = random.randint(1, 20)
        if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Astarion"]["AC"]:
            print('megatron missed')
        else:
            y = partyDict["Astarion"]["HP"] - (enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
            input()
            if y <= 0:
                print("Astarion has been killed")
            if y > 0:
                print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Megatron"]["HP"] - (partyDict["Astarion"]["Attack mod"] + partyDict["Astarion"]["Damage roll"])
        if x <= 0:
            print('Megatron has been killed')
        if x > 0:
            print('Megatron now has', enemyDict["Megatron"]["HP"] - x, 'HP')
            input()
            print("Megatron is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Megatron"]["Attack mod"] < partyDict["Astarion"]["AC"]:
                print('megatron missed')
            else:
                y = partyDict["Astarion"]["HP"] - (
                            enemyDict["Megatron"]["Attack mod"] + enemyDict["Megatron"]["Damage roll"])
                input()
                if y <= 0:
                    print("Astarion has been killed")
                if y > 0:
                    print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
if partyChoice == "Astarion" and enemyChoice == "Giant":
    print("Astarion attacks Giant")
    w = random.randint(1, 20)
    if w + partyDict["Astarion"]["Attack mod"] < enemyDict["Giant"]["AC"]:
        input("Astarion missed")
        print("Giant is now going to attack Astarion")
        e = random.randint(1, 20)
        if e + enemyDict["Giant"]["Attack mod"] < partyDict["Astarion"]["AC"]:
            print('Giant missed')
        else:
            y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
            input()
            if y <= 0:
                print("Astarion has been killed")
            if y > 0:
                print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Giant"]["HP"] - (partyDict["Astarion"]["Attack mod"] + partyDict["Astarion"]["Damage roll"])
        if x <= 0:
            print('Giant has been killed')
        if x > 0:
            print('Giant now has', enemyDict["Giant"]["HP"] - x, 'HP')
            input()
            print("Giant is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Giant"]["Attack mod"] < partyDict["Astarion"]["AC"]:
                print('Giant missed')
            else:
                y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Giant"]["Attack mod"] + enemyDict["Giant"]["Damage roll"])
                input()
                if y <= 0:
                    print("Astarion has been killed")
                if y > 0:
                    print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
if partyChoice == "Astarion" and enemyChoice == "Orc":
    print("Astarion attacks Orc")
    w = random.randint(1, 20)
    if w + partyDict["Astarion"]["Attack mod"] < enemyDict["Orc"]["AC"]:
        input("Astarion missed")
        print("Orc is now going to attack Astarion")
        e = random.randint(1, 20)
        if e + enemyDict["Orc"]["Attack mod"] < partyDict["Astarion"]["AC"]:
            print('Orc missed')
        else:
            y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
            input()
            if y <= 0:
                print("Astarion has been killed")
            if y > 0:
                print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Orc"]["HP"] - (partyDict["Astarion"]["Attack mod"] + partyDict["Astarion"]["Damage roll"])
        if x <= 0:
            print('Orc has been killed')
        if x > 0:
            print('Orc now has', enemyDict["Orc"]["HP"] - x, 'HP')
            input()
            print("Orc is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Orc"]["Attack mod"] < partyDict["Astarion"]["AC"]:
                print('Orc missed')
            else:
                y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Orc"]["Attack mod"] + enemyDict["Orc"]["Damage roll"])
                input()
                if y <= 0:
                    print("Astarion has been killed")
                if y > 0:
                    print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
if partyChoice == "Astarion" and enemyChoice == "Grog":
    print("Astarion attacks Grog")
    w = random.randint(1, 20)
    if w + partyDict["Astarion"]["Attack mod"] < enemyDict["Grog"]["AC"]:
        input("Astarion missed")
        print("Grog is now going to attack Astarion")
        e = random.randint(1, 20)
        if e + enemyDict["Grog"]["Attack mod"] < partyDict["Astarion"]["AC"]:
            print('Grog missed')
        else:
            y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
            input()
            if y <= 0:
                print("Astarion has been killed")
            if y > 0:
                print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
    else:
        x = enemyDict["Grog"]["HP"] - (partyDict["Astarion"]["Attack mod"] + partyDict["Astarion"]["Damage roll"])
        if x <= 0:
            print('Grog has been killed')
        if x > 0:
            print('Grog now has', enemyDict["Grog"]["HP"] - x, 'HP')
            input()
            print("Grog is now going to attack Gale")
            e = random.randint(1, 20)
            if e + enemyDict["Grog"]["Attack mod"] < partyDict["Astarion"]["AC"]:
                print('Grog missed')
            else:
                y = partyDict["Astarion"]["HP"] - (
                        enemyDict["Grog"]["Attack mod"] + enemyDict["Grog"]["Damage roll"])
                input()
                if y <= 0:
                    print("Astarion has been killed")
                if y > 0:
                    print("Astarion now has", partyDict["Astarion"]["HP"] - y, 'HP')
else:
    print('you may have misspelled something')