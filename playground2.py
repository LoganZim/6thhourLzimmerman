
import random
import time


balance = 1000
pot = 0

print('This poker game isnt multiplayer but the better hand you get gets you more \n '
      'money and your goal is to make the most money you can and whatever you bet you get more back depending on the strength of your hand\n'
      'but if your hand isnt good you lose money\n')

while True:
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["\u2664", "\u2661", "\u2662", "\u2667"]
    deck = []
    table = []
    hand = []
    break1 = 0
    for i in range(0, len(faces)):
        for j in range(0, len(suits)):
            card = (faces[i], suits[j])
            deck.append(card)
    random.shuffle(deck)

    if balance <= 0:
        time.sleep(1)
        print('\nyou ran out of money')
        exit()

    def draw():
        global hand
        draw1 = deck[0]
        deck.remove(draw1)
        hand.append(draw1)

        draw2 = deck[0]
        deck.remove(draw2)
        hand.append(draw2)

        time.sleep(6)
        print('you drew a(n)', draw1, 'and a(n)', draw2)

        print(hand)
        print()
        time.sleep(2)


    def bet_1():
        global pot
        global balance

        print('Your balance is', balance)
        bet1 = int(input('How much do you want to bet: '))
        if bet1 > balance:
            print('Cant bet more than what you have')
            bet_1()
        elif bet1 < 0:
            print('Cant bet less that 0')
            bet_1()
        else:
            pot += bet1
            balance -= bet1
            print(' The pot is now', pot)
            print()
            time.sleep(2)

    def flop():
        global hand
        global table

        print('"hand reminder"', hand)
        print()
        time.sleep(2)

        flop1 = deck[0]
        deck.remove(flop1)
        table.append(flop1)

        flop2 = deck[0]
        deck.remove(flop2)
        table.append(flop2)

        flop3 = deck[0]
        deck.remove(flop3)
        table.append(flop3)

        print('The flop begins\n')
        time.sleep(2)
        print('The flop contains a(n)', flop1, 'a(n)', flop2, 'and a(n)', flop3)
        time.sleep(2)
        print('The table contains', table)
        time.sleep(3)

    def turn():
        global hand
        global table

        print('"hand reminder"', hand)
        print()
        time.sleep(2)

        turn1 = deck[0]
        deck.remove(turn1)
        table.append(turn1)

        print('The turn begins\n')
        time.sleep(2)
        print('The turn contains a(n)', turn1)
        time.sleep(3)
        print('the table contains', table)
        time.sleep(3)

    def river():
        global hand
        global table

        print('"Hand reminder"', hand)
        print()
        time.sleep(2)

        river1 = deck[0]
        deck.remove(river1)
        table.append(river1)

        print('The river begins\n')
        time.sleep(2)
        print('The river contains a(n)', river1)
        time.sleep(3)
        print('the table contains', table)

    def royal_flush():
        print()

    def straight_flush():
        print()

    def four_of_a_kind():
        print()

    def full_house():
        print()

    def flush():
        print()

    def straight():
        print()

    def three_of_a_kind():
        global hand, table, pot, balance, break1

        all_cards = hand + table
        break1 = 0

        for i in range(len(all_cards)):
            count = 0
            for j in range(len(all_cards)):
                if all_cards[i][0] == all_cards[j][0]:
                    count += 1
            if count == 3:
                print(f"You got three of a kind in {all_cards[i][0]}'s! You win the full pot!")
                balance += pot
                break1 = 1
                break

        if break1 == 0:
            two_pair()

    def two_pair():
        print()

    def pair():
        global hand, table, pot, balance, break1

        for l in range(5):
            if hand[0][0] == table[l][0]:
                print(f"You get 50% back with a pair of {hand[0][0]}'s")
                balance += pot/2
                break
            elif hand[1][0] == table[l][0]:
                print(f"You get 50% back with a pair of {hand[1][0]}'s")
                balance += pot/2
                break
            elif hand[0][0] == hand[1][0]:
                print(f"You get 50% back with a pair of {hand[0][0]}'s")
                balance += pot/2
                break
            for k in range(5):
                for o in range(k + 1, 5):
                    if table[k][0] == table[o][0]:
                        print(f"You get 50% back with a pair of {table[k][0]}'s")
                        break1 += 1
                        break
            if break1 == 1:
                break
            if break1==2:
                print('you had nothing and lose all of your bets')

        time.sleep(2)
        print('Next round')








    draw()
    flop()
    bet_1()
    turn()
    river()

    three_of_a_kind()

