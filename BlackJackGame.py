from modules import Test

deck = Test.Deck()
dealer = Test.Player()
player = Test.Player()
game_on = True


while game_on:
    player.ask_name()
    deck.deck_creation()
    while True:
        player.betting()
        for i in range(2):
            card = Test.Card(deck.take_card())
            player.print_card(card)
            card = card.card_nominal()
            player.get_card(card)
            card = Test.Card(deck.take_card())
            card = card.card_nominal()
            dealer.get_card(card)
        player.stand_or_hit(deck)
        Test.win_bust_check(player, dealer, deck)
        print(f"Dealer's hand is {dealer.hand}")
        player.hand = list()
        dealer.hand = list()
        print(f"{player.name}'s bank is {player.bank}")
        if not Test.replay():
            break
    print('Thanks for you time! See ya!')
    break

