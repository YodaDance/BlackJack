from BlackJack.modules import Test
deck = Test.Deck()
dealer = Test.Player()
player = Test.Player()
game_on = True

# while game_on:
#     deck.deck_creation()
#     a = 0
deck.deck_creation()
while True:
    for i in range(2):
        card = Test.Card(deck.take_card())
        player.get_card(card)
        card = Test.Card(deck.take_card())
        dealer.get_card(card)
    player.stand_or_hit(deck)
    Test.win_bust_check(player, dealer)
    break



print(player.hand)
print(dealer.hand)






