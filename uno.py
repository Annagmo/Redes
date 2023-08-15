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
		# if deck empty
			# shuffle all except latest from drawn pile into deck
	return cardsDrawn

"""
# basic gameplay
def CanDraw():
def PlayCard():

# effects
def Skip():
	next misses turn

def Reverse():
	turn = turn * -1

def Color():
	choose color

def PlusTwo():
	next draws 2, misses turn

def PlusFour():
	choose color
	if chosen color is in hand
		if true
			legal = false
		else
			legal = true

	if next challenges
		if illegal
			draw 4
		else
			next draws 6, misses turn
	else
		next draws 4, misses turn

# gui pending

# shout?
# catch uno?
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
	playerHands.append( Draw( 7 ) )

# draw first card
drawn.append( Draw( 1 ) )
# while first == +4
# 	return card to deck

print( "player hands", playerHands )
print( "drawn pile", drawn )

"""
gameplay loop
"""

# player[n] turn
	# if previous player can uno shout but didnt
		# catch
		# previous draws 4
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
	# player[n + turn] turn ( or n + ( turn * 2 ) if skip )