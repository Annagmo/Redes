import random

# T = draw two  | R = reverse   | S = skip
# F = draw four | C = color
cardsC = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'R', 'S']
cardsW = ['F', 'C']  # these have no color

# r = red       | g = green     | b = blue      | y = yellow        | n = none
colors = ['r', 'g', 'b', 'y']

"""
function definitions
"""


# create deck
def MakeADeck():
    deck = []

    for color in colors:
        for card in cardsC:  # all colored
            value = "{} {}".format(color, card)
            deck.append(value)

            if card != '0':  # all except zero go twice
                deck.append(value)

        for card in cardsW:  # all non colored ( n = none )
            value = "{} {}".format("n", card)
            deck.append(value)

    return deck


# shuffle deck
def Shuffle(deck):
    for pos in range(len(deck)):
        posRand = random.randint(0, len(deck) - 1)
        deck[pos], deck[posRand] = deck[posRand], deck[pos]
    return deck


# draw card from deck
def Draw(amount):
    cardsDrawn = []
    for x in range(amount):
        cardsDrawn.append(gameDeck.pop(0))
    # if deck empty
    # shuffle all except latest from drawn pile into deck
    return cardsDrawn


# is card playable
def CanPlay(card, topColor, topValue):
    if 'n' in card:
        return True
    elif (topColor in card) or (topValue in card):
        return True

    return False


# has playable card in hand
def HandCheck(hand, topColor, topValue):
    for card in hand:
        if CanPlay(card, topColor, topValue):
            return True
    return False


# cycles through players
def WrapCheck(turn, players):
    if turn > players - 1:
        return 0
    if turn < 0:
        return players - 1
    return turn

# gui pending