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


uno_game = createDeck()
uno_game = shuffle_deck(uno_game)
print(uno_game)
