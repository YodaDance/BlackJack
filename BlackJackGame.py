from modules import Test

deck = Test.Deck()
dealer = Test.Player()
player = Test.Player()
game_on = True

# while game_on:
#     deck.deck_creation()
#     a = 0
deck.deck_creation()
for i in range(2):
    card = Test.Card(deck.take_card())
    card = card.card_nominal()
    player.get_card(card)
    player.print_card(card)
    card = Test.Card(deck.take_card())
    card = card.card_nominal()
    dealer.get_card(card)
player.stand_or_hit(deck)
Test.win_bust_check(player, dealer)
print(player.hand)
print(player.bank)
