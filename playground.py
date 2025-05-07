def w(msg):
    while True:
        try:

            return int(input(msg))

        except ValueError:

            print('nuh uh')


print('Enter 1 for pythagorean theorem\n')
print('Enter 2 for reverse pythagorean theorem\n')
print('Enter 3 for distance formula\n')
print('Enter 4 for midpoint formula\n')
print('Enter 5 for area of a circle\n')
print('Enter 6 for circumfrance of a circle\n')
print('Enter 7 for area of a sphere\n')
print('Enter 8 for surface area of a sphere\n')
print('Enter 9 for the slope of a line\n')
print('Enter 10 for the quadratic formula\n')
print('Enter 11 for energy formula\n')
print('Enter 12 for nuetons law of gravitation\n')
print('Enter 13 for formula for a circle\n')
print('Enter 14 for calculator\n')
print('Enter 15 for E=hv\n')
print('Enter 16 for blackjack\n')
choice = w('enter choice:')
while True:
    if choice == 1:
        print()
        a = (float(input("enter side a length:")))
        b = (float(input("enter side b length:")))
        c = a ** 2 + b ** 2
        import math

        print(math.sqrt(c))


    elif choice == 2:
        print()
        z = (float(input("enter side a/b:")))
        y = (float(input("enter side c:")))
        a = y ** 2 - z ** 2
        import math

        print(math.sqrt(a))

    elif choice == 3:
        print()
        a = (float(input("enter x one coordinate:")))
        b = (float(input("enter y one coordinate:")))
        c = (float(input("enter x two coordinate:")))
        d = (float(input("enter y two coordinate:")))
        e = (c - a) ** 2 + (d - b) ** 2
        import math

        print(math.sqrt(e))

    elif choice == 4:
        print()
        a = (float(input("enter x one coordinate:")))
        b = (float(input("enter y one coordinate:")))
        c = (float(input("enter x two coordinate:")))
        d = (float(input("enter y two coordinate:")))
        e = (c + a) / 2
        v = (d + b) / 2
        import math

        print(e)
        print(v)

    elif choice == 5:
        print()
        b = (float(input("enter the radius:")))
        pie = 3.1415926535897 * b ** 2
        print(pie)

    elif choice == 6:
        print()
        b = (float(input("enter the radius:")))
        pi = 2 * 3.1415926535897 * b
        print(pi)

    elif choice == 7:
        print()
        r = (float(input("enter the radius:")))
        pie = (4 / 3) * 3.1415926535897 * r ** 3
        print(pie)

    elif choice == 8:
        print()
        r = (float(input("enter the radius:")))
        pie = 4 * 3.1415926535897 * r ** 2
        print(pie)

    elif choice == 9:
        print()
        X_one = (float(input("enter x one coordinate: ")))
        Y_one = (float(input("enter y one coordinate: ")))
        X_two = (float(input("enter x two coordinate: ")))
        Y_two = (float(input("enter y two coordinate: ")))
        e = (Y_two - Y_one) / (X_two - Y_one)
        print(e)

    elif choice == 10:
        print()
        a = (float(input("enter value a:")))
        b = (float(input("enter value b:")))
        c = (float(input("enter value c:")))
        f = b ** 2 - 4 * a * c
        import math

        print('the iside of the square root is: ', f)
        x = (math.sqrt(f))

        e = -b + x
        print('-b + the square root is: ', round(e, 2))
        d = -b - x
        print('-b - the square root is: ', round(d, 2))
        l = d / (2 * a)

        z = e / (2 * a)
        print()
        print('the first coordinate is', round(z, 2))
        print()
        print('the second coordinate is', round(l, 2))

    elif choice == 11:
        print()
        mass = float(input("Enter mass in kg: "))
        speed_of_light = 299792458
        energy = mass * speed_of_light ** 2
        print("The energy equivalent of mass", mass, "is", energy)


    elif choice == 12:
        m1 = float(input("Enter mass 1: "))
        m2 = float(input("Enter mass 2: "))
        G = 6.67430e-11
        R = float(input("Enter the distance between the masses: "))
        force = G * (m1 * m2) / R ** 2
        print("The gravitational force between the two masses is", force)


    elif choice == 13:
        h = (float(input('Enter the x of the center of the circle : ')))
        k = (float(input('Enter the y of the center of the circle : ')))
        x = (float(input('Enter the x of the edge of the circle : ')))
        y = (float(input('Enter the y of the edge of the circle : ')))
        e = (x - h) ** 2 + (y - k) ** 2
        print(e ** 2)

    elif choice == 14:
        '''
        Calculator
        -------------------------------------------------------------
        '''

        import os


        def addition():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Addition')

            continue_calc = 'y'

            num_1 = float(input('Enter a number: '))
            num_2 = float(input('Enter another number: '))
            ans = num_1 + num_2
            values_entered = 2
            print(f'Current result: {ans}')

            while continue_calc.lower() == 'y':
                continue_calc = (input('Enter more (y/n): '))
                while continue_calc.lower() not in ['y', 'n']:
                    print('Please enter \'y\' or \'n\'')
                    continue_calc = (input('Enter more (y/n): '))

                if continue_calc.lower() == 'n':
                    break
                num = float(input('Enter another number: '))
                ans += num
                print(f'Current result: {ans}')
                values_entered += 1
            return [ans, values_entered]


        def subtraction():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Subtraction')

            continue_calc = 'y'

            num_1 = float(input('Enter a number: '))
            num_2 = float(input('Enter another number: '))
            ans = num_1 - num_2
            values_entered = 2
            print(f'Current result: {ans}')

            while continue_calc.lower() == 'y':
                continue_calc = (input('Enter more (y/n): '))
                while continue_calc.lower() not in ['y', 'n']:
                    print('Please enter \'y\' or \'n\'')
                    continue_calc = (input('Enter more (y/n): '))

                if continue_calc.lower() == 'n':
                    break
                num = float(input('Enter another number: '))
                ans -= num
                print(f'Current result: {ans}')
                values_entered += 1
            return [ans, values_entered]


        def multiplication():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Multiplication')

            continue_calc = 'y'

            num_1 = float(input('Enter a number: '))
            num_2 = float(input('Enter another number: '))
            ans = num_1 * num_2
            values_entered = 2
            print(f'Current result: {ans}')

            while continue_calc.lower() == 'y':
                continue_calc = (input('Enter more (y/n): '))
                while continue_calc.lower() not in ['y', 'n']:
                    print('Please enter \'y\' or \'n\'')
                    continue_calc = (input('Enter more (y/n): '))

                if continue_calc.lower() == 'n':
                    break
                num = float(input('Enter another number: '))
                ans *= num
                print(f'Current result: {ans}')
                values_entered += 1
            return [ans, values_entered]


        def division():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Division')

            continue_calc = 'y'

            num_1 = float(input('Enter a number: '))
            num_2 = float(input('Enter another number: '))
            while num_2 == 0.0:
                print('Please enter a second number > 0')
                num_2 = float(input('Enter another number: '))

            ans = num_1 / num_2
            values_entered = 2
            print(f'Current result: {ans}')

            while continue_calc.lower() == 'y':
                continue_calc = (input('Enter more (y/n): '))
                while continue_calc.lower() not in ['y', 'n']:
                    print('Please enter \'y\' or \'n\'')
                    continue_calc = (input('Enter more (y/n): '))

                if continue_calc.lower() == 'n':
                    break
                num = float(input('Enter another number: '))
                while num == 0.0:
                    print('Please enter a number > 0')
                    num = float(input('Enter another number: '))
                ans /= num
                print(f'Current result: {ans}')
                values_entered += 1
            return [ans, values_entered]


        def calculator():
            quit = False
            while not quit:
                results = []
                print('Simple Calculator in Python!')
                print('Enter \'a\' for addition')
                print('Enter \'s\' for substraction')
                print('Enter \'m\' for multiplication')
                print('Enter \'d\' for division')
                print('Enter \'q\' to quit')

                choice = input('Selection: ')

                if choice == 'q':
                    quit = True
                    continue

                if choice == 'a':
                    results = addition()
                    print('Ans = ', results[0], ' total inputs: ', results[1])
                elif choice == 's':
                    results = subtraction()
                    print('Ans = ', results[0], ' total inputs: ', results[1])
                elif choice == 'm':
                    results = multiplication()
                    print('Ans = ', results[0], ' total inputs: ', results[1])
                elif choice == 'd':
                    results = division()
                    print('Ans = ', results[0], ' total inputs: ', results[1])
                else:
                    print('Sorry, invalid character')


        if __name__ == '__main__':
            calculator()

    elif choice == 15:
        print()
        h = float(input("enter the value of Planck's constant (h):"))
        v = float(input("enter the frequency (v):"))
        energy = h * v
        print("Energy (E) = ", energy)
    elif choice == 16:
        '''
        Blackjack
        -------------------------------------------------------------
        '''

        import random
        import os


        class Card:

            def __init__(self, card_face, value, symbol):
                self.card_face = card_face
                self.value = value
                self.symbol = symbol


        def show_cards(cards, hidden):
            s = ''
            for card in cards:
                s = s + '\t ________________'
            if hidden:
                s += '\t ________________'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|                |'
            print(s)

            s = ''
            for card in cards:
                if card.card_face in ['J', 'Q', 'K', 'A']:
                    s = s + '\t|  {}             |'.format(card.card_face)
                elif card.value == 10:
                    s = s + '\t|  {}            |'.format(card.value)
                else:
                    s = s + '\t|  {}             |'.format(card.value)

            if hidden:
                s += '\t|                |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|      * *       |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|    *     *     |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|   *       *    |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|   *       *    |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|       {}        |'.format(card.symbol)
            if hidden:
                s += '\t|          *     |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|         *      |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|        *       |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|                |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|                |'
            if hidden:
                s += '\t|                |'
            print(s)

            s = ''
            for card in cards:
                if card.card_face in ['J', 'Q', 'K', 'A']:
                    s = s + '\t|            {}   |'.format(card.card_face)
                elif card.value == 10:
                    s = s + '\t|           {}   |'.format(card.value)
                else:
                    s = s + '\t|            {}   |'.format(card.value)
            if hidden:
                s += '\t|        *       |'
            print(s)

            s = ''
            for card in cards:
                s = s + '\t|________________|'
            if hidden:
                s += '\t|________________|'
            print(s)
            print()


        def deal_card(deck):
            card = random.choice(deck)
            deck.remove(card)
            return card, deck


        def play_blackjack(deck):
            player_cards = []
            dealer_cards = []
            player_score = 0
            dealer_score = 0
            os.system('clear')

            while len(player_cards) < 2:
                player_card, deck = deal_card(deck)
                player_cards.append(player_card)
                player_score += player_card.value

                # If dealt a second Ace, adjust player score
                if len(player_cards) == 2:
                    if player_cards[0].value == 11 and player_cards[1].value == 11:
                        player_cards[0].value = 1
                        player_score -= 10

                print('PLAYER CARDS: ')
                show_cards(player_cards, False)
                print('PLAYER SCORE = ', player_score)

                input('Continue...')

                dealer_card, deck = deal_card(deck)
                dealer_cards.append(dealer_card)
                dealer_score += dealer_card.value

                # If dealt a second Ace, adjust dealer score
                # Note: adjusts 2nd card to hide that the dealer has an Ace
                if len(dealer_cards) == 2:
                    if dealer_cards[0].value == 11 and dealer_cards[1].value == 11:
                        dealer_cards[1].value = 1
                        dealer_score -= 10

                print('DEALER CARDS: ')
                if len(dealer_cards) == 1:
                    show_cards(dealer_cards, False)
                    print('DEALER SCORE = ', dealer_score)
                else:
                    show_cards(dealer_cards[:-1], True)
                    print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)

                input('Continue...')

            if player_score == 21:
                print('PLAYER HAS A BLACKJACK!!!!')
                print('PLAYER WINS!!!!')
                quit()
            os.system('clear')

            print('DEALER CARDS: ')
            show_cards(dealer_cards[:-1], True)
            print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
            print()
            print('PLAYER CARDS: ')
            show_cards(player_cards, False)
            print('PLAYER SCORE = ', player_score)

            while player_score < 21:
                choice = input('Enter H to Hit or S to Stand: ').upper()
                if len(choice) != 1 or (choice not in ['H', 'S']):
                    os.system('clear')
                    print('Invalid choice!! Try Again...')
                    continue

                if choice.upper() == 'S':
                    break
                else:
                    player_card, deck = deal_card(deck)
                    player_cards.append(player_card)
                    player_score += player_card.value
                    card_pos = 0

                    # If dealt an Ace, adjust score for each existing Ace in hand
                    while player_score > 21 and card_pos < len(player_cards):
                        if player_cards[card_pos].value == 11:
                            player_cards[card_pos].value = 1
                            player_score -= 10
                            card_pos += 1
                        else:
                            card_pos += 1

                    if player_score > 21:
                        break

                    os.system('clear')
                    print('DEALER CARDS: ')
                    show_cards(dealer_cards[:-1], True)
                    print('DEALER SCORE = ', dealer_score - dealer_cards[-1].value)
                    print()
                    print('PLAYER CARDS: ')
                    show_cards(player_cards, False)
                    print('PLAYER SCORE = ', player_score)

            os.system('clear')
            print('PLAYER CARDS: ')
            show_cards(player_cards, False)
            print('PLAYER SCORE = ', player_score)
            print()
            print('DEALER IS REVEALING THEIR CARDS....')
            print('DEALER CARDS: ')
            show_cards(dealer_cards, False)
            print('DEALER SCORE = ', dealer_score)

            if player_score == 21:
                print('PLAYER HAS A BLACKJACK, PLAYER WINS!!!')
                quit()

            if player_score > 21:
                print('PLAYER BUSTED!!! GAME OVER!!!')
                quit()

            input('Continue...')
            while dealer_score < 17:
                os.system('clear')
                print('DEALER DECIDES TO HIT.....')
                dealer_card, deck = deal_card(deck)
                dealer_cards.append(dealer_card)
                dealer_score += dealer_card.value

                # If dealt an Ace, adjust score for each existing Ace in hand
                card_pos = 0
                while dealer_score > 21 and card_pos < len(dealer_cards):
                    if dealer_cards[card_pos].value == 11:
                        dealer_cards[card_pos].value = 1
                        dealer_score -= 10
                        card_pos += 1
                    else:
                        card_pos += 1

                print('PLAYER CARDS: ')
                show_cards(player_cards, False)
                print('PLAYER SCORE = ', player_score)
                print()
                print('DEALER CARDS: ')
                show_cards(dealer_cards, False)
                print('DEALER SCORE = ', dealer_score)
                if dealer_score > 21:
                    break
                input('Continue...')

            if dealer_score > 21:
                print('DEALER BUSTED!!! YOU WIN!!!')
                quit()
            elif dealer_score == 21:
                print('DEALER HAS A BLACKJACK!!! PLAYER LOSES!!!')
                quit()
            elif dealer_score == player_score:
                print('TIE GAME!!!!')
            elif player_score > dealer_score:
                print('PLAYER WINS!!!')
            else:
                print('DEALER WINS!!!')


        def init_deck():
            suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
            # UNICODE values for card symbol images
            suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                            'Spades': '\u2664', 'Clubs': '\u2667'}
            cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                     '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
            deck = []
            for suit in suits:
                for card, value in cards.items():
                    deck.append(Card(card, value, suit_symbols[suit]))
            return deck


        if __name__ == '__main__':
            deck = init_deck()
            play_blackjack(deck)
    elif choice == 17:

        import random
        import time

        balance=1000
        pot=0
        score = ""
        deck = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,
                'Jack', 'Queen', 'King', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'ace', 2, 3,
                4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        random.shuffle(deck)

        print('this poker game isnt multiplayer but the better hand you get gets you more \n '
              'points and your goal is to make a high score and whatever you bet you get more back depending on the strength of your hand\n'
              'but if your hand isnt good you lose money\n')
        time.sleep(4)


        def draw():
            global balance
            draw1 = deck[0]
            deck.remove(draw1)

            draw2 = deck[0]
            deck.remove(draw2)

            print('you drew a(n)', draw1,'and a(n)',draw2)
            hand = draw1 and draw2
            time.sleep(2)

        def bet_1():
            print('your balance is', balance)
            bet1 = int(input('how much do you want to bet: '))
            if bet1 > balance:
                print('cant bet more than what you have')
                bet_1()
            elif bet1 < 0:
                print('cant bet less that 0')
                bet_1()


    def flop():
            flop1=deck[0]
            deck.remove(flop1)

            flop2=deck[0]
            deck.remove(flop2)

            flop3=deck[0]
            deck.remove(flop3)

            print('the flop begins\n')
            time.sleep(1)
            print('the flop contains a(n)',flop1,'a(n)',flop2,'and a(n)',flop3)


        draw()
