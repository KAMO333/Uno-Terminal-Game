import random
# Create a deck of cards
def createDeck():
    deck = []
    # Define the structure of the cards
    cards = {
        'Red': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Draw Two', 'Reverse'],
        'Blue': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Draw Two', 'Reverse'],
        'Green': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Draw Two', 'Reverse'],
        'Yellow': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Draw Two', 'Reverse']
    }
    
    # Add Wild cards
    wilds = ['Wild', 'Wild Draw Four'] * 4
    deck.extend(wilds)

    # Add colored cards
    for color, values in cards.items():
        for value in values:
            card = f"{color} {value}"
            # Add card (for 0, only one copy, for others, two copies)
            deck.append(card)
            if value != 0:
                deck.append(card)

    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# 3. Draw a card from the top of the deck
def draw_cards(num_cards):
    cardsDraw = [uno_game.pop(0) or x for x in range(num_cards)]
    return cardsDraw

# Print players hand
def show_players_hand(player, player_hand):
    print(f"Turn for Player {player + 1}")
    print("Cards in Hand")
    print("------------------")
    for i, card in enumerate(player_hand, 1):
        print(f"{i}) {card}")    
    print("")  


# Check whather a player can play a card or not
def can_play(colour, value, player_hand):
    # Find any element that returns True
    return any('Wild' in card or colour in card or value in card for card in player_hand)








uno_game = createDeck()
uno_game = shuffle_deck(uno_game)

