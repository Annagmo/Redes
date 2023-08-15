import random

# T = draw two  | R = reverse   | S = skip
# F = draw four | C = color
cardsC = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'R', 'S']
cardsW = ['F', 'C'] # these have no color

# r = red       | g = green     | b = blue      | y = yellow        | n = none
colors = ['r', 'g', 'b', 'y']

"""
function definitions
"""

# create deck
def MakeADeck():
	deck = []

	for color in colors:
		for card in cardsC: # all colored
			value = "{} {}" .format( color, card )
			deck.append( value )

			if card != '0': # all except zero go twice
				deck.append( value )

		for card in cardsW: # all non colored ( n = none )
			value = "{} {}" .format( "n", card )
			deck.append( value )
	
	return deck

# shuffle deck
def Shuffle( deck ):
	for pos in range( len( deck ) ):
		posRand = random.randint( 0, len( deck ) - 1 )
		deck[pos], deck[posRand] = deck[posRand], deck[pos]
	return deck

# draw card
def Draw( amount ):
	cardsDrawn = []
	for x in range( amount ):
		cardsDrawn.append( gameDeck.pop( 0 ) )
	return cardsDrawn

"""
# basic gameplay
def CanDraw():
def PlayCard():

# effects
def Skip():
def Reverse():
def Color():
def PlusTwo():
def PlusFour():

# gui pending
"""

"""
setup game
"""

playerHands = []
drawn = []

players = 4 # 2-4 players
direction = 1 # 1 or -1 for cw and ccw
turn = random.randint( 0, players - 1 ) # determines current player index

# setup playing deck
gameDeck = MakeADeck()
gameDeck = Shuffle( gameDeck )
print( "deck", gameDeck )

# draw cards for each player
for player in range( players ):
	playerHands.append( Draw( 5 ) )

# draw first card
drawn.append( Draw( 1 ) )

print( "player hands", playerHands )
print( "drawn pile", drawn )

"""
gameplay loop
"""

# player turn
	# check top of drawn for effect cards
		# if effect
			# execute its function
	# draw card if needed
	# play card
		# if legal move
			# remove from hand
			# add to drawn
			# if effect
				# execute its function
		# else
			# deny
			# repeat 'play card'
		# if current hand == 1
			# display uno shout button
		# if current hand == 0
			# end game
	# end turn
	# next player