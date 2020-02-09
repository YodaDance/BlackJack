import random


class Player:

    def __init__(self, name='Dealer', bank=1000, hand=list(), bet=1, nominal=list(), aces=0, sumhand=0):
        self.name = str(name)
        self.bank = int(bank)
        self.hand = list(hand)
        self.bet = int(bet)
        self.nominal = list(nominal)
        self.aces = int(aces)
        self.sumhand = int(sumhand)

    def ask_name(self):
        self.name = input('What is your name? ')
        return self.name

    def betting(self):
        while True:
            try:
                self.bet = int(input('Choose the bet, please: '))
                if self.bank >= self.bet:
                    self.bank -= self.bet
                    return self.bank
                else:
                    print('Your bet is out of bank')
                    continue
            except ValueError:
                print('You tapped not a number')

    def print_card(self, card):
        print(f"{self.name} have got {card}")

    def get_card(self, card, card_nominal):
        self.sumhand = 0
        self.hand.append(card)
        self.nominal.append(card_nominal)
        for numb in self.nominal:
            self.sumhand += numb
            if numb == 11:
                self.aces += 1
                self.adjust_for_ace()
        return self.hand

    def adjust_for_ace(self):
        while self.sumhand > 21 and self.aces:
            self.sumhand -= 10
            self.aces -= 1

    def stand_or_hit(self, deck):
        while True:
            choice = input('Would you like to stand or hit (answer "stand" or "hit"): ')
            if choice.lower() == 'hit':
                card = Card(deck.take_card())
                self.print_card(card)
                self.get_card(card, card.card_nominal())
                print(f"{self.name}'s hand value is {self.sumhand}")
                if self.sumhand >= 21:
                    return self.hand
                else:
                    continue
            elif choice.lower() == 'stand':
                print(f"{self.name}'s hand value is {self.sumhand}")
                return self.hand
            else:
                print('Error!')
                continue

    def hide_card(self):
        print(f"{self.name}'s hand is:")
        print('card hidden')
        print(f"{self.hand[1]}")


class Card:
    nominal = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'quenn': 10,
               'king': 10, 'ace': 11}

    def __init__(self, card):
        self.card = card

    def __str__(self):
        self.card = str(self.card)
        return self.card

    def card_nominal(self):
        card_nominal = Card.nominal[self.__str__().split()[0].lower()]
        card_nominal = int(card_nominal)
        return card_nominal


class Deck:
    values = [str(i) for i in range(2, 11)] + ['Jack', 'Quenn', 'King', 'Ace']
    suits = ['clubs', 'diamonds', 'hearts', 'spaces']

    def __init__(self, card='0', deck=[]):
        self.deck = deck
        self.card = card

    def deck_creation(self):
        for val in Deck.values:
            for suit in Deck.suits:
                self.deck.append(val + ' of ' + suit)
        random.shuffle(self.deck)
        return self.deck

    def take_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card


def win_bust_check(player, dealer, deck):
    while dealer.sumhand <= 16:
        card = Card(deck.take_card())
        dealer.get_card(card, card.card_nominal())
    if player.sumhand == 21:
        print('BlackJack!')
        player.bank += player.bet * 2
        return player.bank
    if player.sumhand > 21:
        print('Busted!')
    elif 21 > player.sumhand > dealer.sumhand or dealer.sumhand > 21:
        print('You have won!')
        player.bank += player.bet * 2
        return player.bank
    else:
        print('You have lost!')


def replay():
    return input('You wanna play again? Yes or No: ').lower().startswith('y')
