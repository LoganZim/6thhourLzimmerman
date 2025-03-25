#Name:Logan
#Class: 6th Hour
#Assignment: Scenario8
import random
import time


#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
damage = 0
class stats:
    def __init__(self,health,atkroll,atkmod,ac,name):
        self.health = health
        self.atkroll = atkroll
        self.atkmod = atkmod
        self.ac = ac
        self.name = name
#party stats
LaeZel = stats(25,6,3,1,"LaeZel")
Shaddowheart = stats(18,6,2,1,"Shaddowheart")
Gale = stats(16,8,1,1,"Gale")
partylist = [LaeZel,Shaddowheart,Gale]
#enemy stats
Megatron = stats(19,4,2,1,"Megatron")
Grog = stats(15,6,1,1,"Grog")
Orc = stats(18,10,1,1,"Orc")
enemylist = [Megatron,Grog,Orc]
#damage roll def
def damageroll(attacker,target):
    global damage
    randomX = random.randint(1,20)
    if randomX > target.ac:
        damage = random.randint(1,attacker.atkroll)
        damage += attacker.atkmod
        target.health -= damage
    else:
        damage = 0
#enemy attack
def enemy_attack():
    try:
        enemyAttacker = random.choice(enemylist)
        try:
            partyTarget = random.choice(partylist)
            damageroll(enemyAttacker, partyTarget)
            if damage > 0:
                print(enemyAttacker.name, "has done", damage, "damage to", partyTarget.name)
            else:
                print(enemyAttacker.name, "missed the", partyTarget.name)
        except:
            enemy_attack()
    except:
        enemy_attack()
#party attack
def party_attack():
    partyAttacker = int(input("Which do you choose to attack the enemy 1(LaeZel) 2(Shaddowheart) 3(Gale): "))
    enemyTarget = int(input("Which do you attack 1(Grog) 2(Megatron) 3(Orc): "))
    try:
        if enemyTarget == 2:
            enemyTarget = Megatron
        if enemyTarget == 1:
            enemyTarget = Grog
        if enemyTarget == 3:
            enemyTarget = Orc
        try:
            if partyAttacker == 2:
                partyAttacker = Shaddowheart
            if partyAttacker == 1:
                partyAttacker = LaeZel
            if partyAttacker == 3:
                partyAttacker = Gale
            damageroll(partyAttacker, enemyTarget)
            if damage > 0:
                print(partyAttacker.name, "has done", damage, "damage to", enemyTarget.name)
            else:
                print(partyAttacker.name, "missed the", enemyTarget.name)
        except:
            print("That party member is dead")
    except:
        print("That enemy is dead")

#show healths
def show_healths():
    try:
        print("LaeZel health:",LaeZel.health)
    except:
        print("LaeZel is dead")
    try:
        print("Shaddowheart health:", Shaddowheart.health)
    except:
        print("Shaddowheart is dead")
    try:
        print("Gale health:", Gale.health)
    except:
        print("Gale is dead")
    try:
        print("Megatron health:", Megatron.health)
    except:
        print("Megatron is dead")
    try:
        print("Grog health:", Grog.health)
    except:
        print("Grog is dead")
    try:
        print("Orc health:", Orc.health)
    except:
        print("Orc is dead")
#check if dead

def check_death():
    global LaeZel
    global Shaddowheart
    global Gale
    global Megatron
    global Grog
    global Orc
    try:
        if LaeZel.health < 1:
            del LaeZel
            partylist.remove(LaeZel)
    except:
        print("")
    try:
        if Shaddowheart.health < 1:
            del Shaddowheart
            partylist.remove(Shaddowheart)
    except:
        print("")
    try:
        if Gale.health < 1:
            del Gale
            partylist.remove(Gale)
    except:
        print("")
    try:
        if Megatron.health < 1:
            del Megatron
            enemylist.remove(Megatron)
    except:
        print("")
    try:
        if Grog.health < 1:
            del Grog
            enemylist.remove(Grog)
    except:
        print("")
    try:
        if Orc.health < 1:
            del Orc
            enemylist.remove(Orc)
    except:
        print("")

while True:
    check_death()
    show_healths()
    time.sleep(1)
    party_attack()
    time.sleep(2)
    enemy_attack()
    time.sleep(2)


