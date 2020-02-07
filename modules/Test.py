import random


class Player():

    def __init__(self, name='Dealer', bank=1000, hand=list(), bet=1):
        self.name = str(name)
        self.bank = int(bank)
        self.hand = list(hand)
        self.bet = int(bet)

    def ask_name(self):
        self.name = input('What is your name?')
        return self.name

    def hand_score(self):
        sumhand = 0
        for card in self.hand:
            card = Card(card)
            card = card.card_nominal()
            sumhand += card
        return sumhand

    def betting(self):
        self.bet = int(input('Choose the bet, please: '))
        while True:
            if self.bank > self.bet:
                self.bank -= self.bet
            else:
                print('Your bet is out of bank')
            return self.bank

    def print_card(self, card):
        print(f"{self.name} have got {card}")

    def get_card(self, card):
        return self.hand.append(card)

    def stand_or_hit(self, deck):
        while True:
            try:
                choice = input('Would you like to stand or hit (answer "stand" or "hit"): ')
                if choice.lower() == 'hit':
                    card_turn = Card(deck.take_card())
                    self.print_card(card_turn)
                    card_turn = card_turn.card_nominal()
                    self.get_card(card_turn)
                    print(self.hand_score())
                    if self.hand_score() > 21:
                        return self.hand
                    else:
                        continue
                elif choice.lower() == 'stand':
                    print(self.hand_score())
                    return self.hand
                else:
                    print('Error!')
                    continue
            except TypeError:
                print('Ace is on the table')
                self.

class Card():
    nominal = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'quenn': 10,
               'king': 10, 'ace': (1, 11)}

    def __init__(self, card):
        self.card = card

    def __str__(self):
        self.card = str(self.card)
        return self.card

    def card_nominal(self):
        nominal = int(Card.nominal[self.__str__().split()[0].lower()])
        return nominal


class Deck():
    values = [str(i) for i in range(2, 11)] + ['Jack', 'Quenn', 'King', 'Ace']
    suits = ['clubs', 'diamonds', 'hearts', 'spaces']

    def __init__(self, card='0', deck=[]):
        self.deck = deck
        self.card = card

    def deck_creation(self):
        for val in Deck.values:
            for suit in Deck.suits:
                self.deck.append(val + ' ' + suit)
        random.shuffle(self.deck)
        return self.deck

    def take_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card


def win_bust_check(player, dealer):
    if player.hand_score() > 21:
        print('Busted!')
    elif 21 > player.hand_score() > dealer.hand_score():
        print('You have won!')
        player.bank += player.bet * 2
        return player.bank
    else:
        print('You have lost!')


def replay():
    return input('You wanna play again? Yes or No: ').lower().startswith('y')
