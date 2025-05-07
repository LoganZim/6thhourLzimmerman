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

        balance = 1000
        pot = 0
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        face_values = {face: i for i, face in enumerate(faces, start=2)}
        suits = ["♠", "♡", "♢", "♣"]
        deck = []
        table = []
        hand = []


        def create_deck():
            global deck
            deck = [(face, suit) for face in faces for suit in suits]
            random.shuffle(deck)


        def draw():
            global hand
            hand = [deck.pop(0), deck.pop(0)]
            print(f"You drew: {hand[0]} and {hand[1]}")
            time.sleep(1)


        def bet_input():
            global balance, pot
            while True:
                try:
                    print(f"Your balance: {balance}")
                    amount = int(input("Enter your bet: "))
                    if amount < 0 or amount > balance:
                        print("Invalid bet.")
                    else:
                        balance -= amount
                        pot += amount
                        print(f"Pot is now {pot}\n")
                        return
                except ValueError:
                    print("Please enter a valid number.")


        def flop():
            global table
            print("\nDealing the flop...")
            time.sleep(1)
            table.extend([deck.pop(0) for _ in range(3)])
            print(f"Flop: {table}\n")
            time.sleep(1)


        def turn():
            print("Dealing the turn...")
            time.sleep(1)
            table.append(deck.pop(0))
            print(f"Turn: {table[-1]}")
            print(f"Table: {table}\n")
            time.sleep(1)


        def river():
            print("Dealing the river...")
            time.sleep(1)
            table.append(deck.pop(0))
            print(f"River: {table[-1]}")
            print(f"Table: {table}\n")
            time.sleep(1)


        def evaluate_hand():
            global balance, pot
            all_cards = hand + table
            ranks = [card[0] for card in all_cards]
            suits_ = [card[1] for card in all_cards]
            rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
            suit_counts = {suit: suits_.count(suit) for suit in set(suits_)}
            values = sorted([face_values[r] for r in ranks], reverse=True)
            unique_vals = sorted(set(values), reverse=True)

            # Helper functions
            def is_flush():
                for suit in suits_:
                    if suits_.count(suit) >= 5:
                        return suit
                return None

            def is_straight(vals):
                vals = sorted(set(vals), reverse=True)
                for i in range(len(vals) - 4):
                    if vals[i] - vals[i + 4] == 4:
                        return vals[i]
                if set([14, 2, 3, 4, 5]).issubset(set(vals)):
                    return 5  # Wheel straight (A-2-3-4-5)
                return None

            def is_straight_flush():
                flush_suit = is_flush()
                if not flush_suit:
                    return None
                suited_cards = [card for card in all_cards if card[1] == flush_suit]
                suited_vals = sorted([face_values[card[0]] for card in suited_cards], reverse=True)
                high = is_straight(suited_vals)
                if high:
                    return high
                return None

            # Evaluation
            straight_flush_high = is_straight_flush()
            four_kind = 4 in rank_counts.values()
            three_kind = 3 in rank_counts.values()
            pairs = list(rank_counts.values()).count(2)
            flush = is_flush()
            straight = is_straight(values)

            # Determine hand type
            if straight_flush_high == 14:  # A-high straight flush
                hand_type, rank_value = "Royal Flush", 10
            elif straight_flush_high:
                hand_type, rank_value = "Straight Flush", 9
            elif four_kind:
                hand_type, rank_value = "Four of a Kind", 8
            elif three_kind and pairs >= 1:
                hand_type, rank_value = "Full House", 7
            elif flush:
                hand_type, rank_value = "Flush", 6
            elif straight:
                hand_type, rank_value = "Straight", 5
            elif three_kind:
                hand_type, rank_value = "Three of a Kind", 4
            elif pairs >= 2:
                hand_type, rank_value = "Two Pair", 3
            elif pairs == 1:
                hand_type, rank_value = "Pair", 2
            else:
                hand_type, rank_value = "High Card", 1

            # Payout multiplier per hand
            payout_multiplier = {
                10: 10,  # Royal Flush
                9: 8,  # Straight Flush
                8: 7,  # Four of a Kind
                7: 6,  # Full House
                6: 5,  # Flush
                5: 4,  # Straight
                4: 3,  # Three of a Kind
                3: 2,  # Two Pair
                2: 1.5,  # Pair
                1: 0  # High Card
            }[rank_value]

            winnings = pot * payout_multiplier
            balance += winnings
            print(f"\n==> You got a **{hand_type}**!")
            print(f"==> You won ${winnings:.2f}!")
            print(f"Your new balance: ${balance:.2f}\n")

    create_deck()
    draw()
    bet_input()
    flop()
    turn()
    river()
    evaluate_hand()