from modules import Test

deck = Test.Deck()
dealer = Test.Player()
player = Test.Player()

print('Welcome to the new world of BlackJack!')
player.ask_name()
while True:
    deck.deck_creation()
    player.betting()
    for i in range(2):
        card = Test.Card(deck.take_card())
        player.print_card(card)
        player.get_card(card, card.card_nominal())
        card = Test.Card(deck.take_card())
        dealer.get_card(card, card.card_nominal())
    dealer.hide_card()
    print(f"{player.name}'s hand value is {player.sumhand}")
    player.stand_or_hit(deck)
    Test.win_bust_check(player, dealer, deck)
    print("Dealer's hand is "+', '.join([str(card) for card in dealer.hand]))
    print(f"Dealer's value is {dealer.sumhand}")
    player.hand = list()
    dealer.hand = list()
    print(f"{player.name}'s bank is {player.bank}")
    if not Test.replay():
        print('Thanks for your time! See ya!')
        break


