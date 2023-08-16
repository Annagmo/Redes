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

# draw card from deck
def Draw( amount ):
	cardsDrawn = []
	for x in range( amount ):
		cardsDrawn.append( gameDeck.pop( 0 ) )
		# if deck empty
			# shuffle all except latest from drawn pile into deck
	return cardsDrawn

# is card playable
def CanPlay( card, topColor, topValue ):
	if 'n' in card:
		return True
	elif ( topColor in card ) or ( topValue in card ):
		return True
	
	return False

# has playable card in hand
def HandCheck( hand, topColor, topValue ):
	for card in hand:
		if CanPlay( card, topColor, topValue ):
			return True
	return False

# cycles through players
def WrapCheck( turn, players ):
	if turn > players - 1:
		return 0
	if turn < 0:
		return players - 1
	return turn


# gui pending

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

# draw cards for each player
for player in range( players ):
	playerHands.append( Draw( 7 ) ) # 7 cards

# draw first card
while True:
	gameDeck = Shuffle( gameDeck )
	drawn.extend( Draw( 1 ) )
	if drawn[-1] == 'n F': # doesnt accept +4 as first card
		gameDeck.append( drawn.pop( 0 ) )
	else:
		break

top = drawn[-1].split( ' ', 1 )
topC = top[0]
topV = top[1]

resolved = True

print( "deck", gameDeck )
print( "player hands", playerHands )
print( "drawn pile", drawn )
print( "current card {}" .format( topC + ' ' + topV ) )

if topC == 'n': # colors first card if uncolored
	colorChosen = input( "choose color" )
	# validity check pending
	topC = colorChosen

while True: # gameplay loop
	print( "{}'s turn" .format( turn + 1 ) )

	if not resolved:
		if topV == 'S': # skip
			print( "skipped" )
			turn = WrapCheck( turn + direction, players )
			resolved = True
			continue
		elif topV == 'T': # +2
			print( "+2 and skipped" )
			playerHands[turn].extend( Draw( 2 ) )
			turn = WrapCheck( turn + direction, players )
			resolved = True
			continue
		elif topV == 'F': # +4
			# challenge?
			# if not:
			print( "+4 and skipped" )
			playerHands[turn].extend( Draw( 4 ) )
			# if yes:
			# if win: playerHands[WrapCheck( turn - direction, players )].extend( Draw( 4 ) )
			# if lose: playerHands[turn].extend( Draw( 6 ) )
			turn = WrapCheck( turn + direction, players )
			resolved = True
			continue

	while not HandCheck( playerHands[turn], topC, topV ):
		print( "no playable cards, +1" )
		playerHands[turn].extend( Draw( 1 ) ) # draws until able to play

	while True:
		print( "hand", playerHands[turn] )
		cardChosen = int( input( "choose card index" ) )
		# validity check pending
		if CanPlay( playerHands[turn][cardChosen - 1], topC, topV ):
			print( "ye" )
			break
		print( "no ")

	drawn.append( playerHands[turn].pop( cardChosen - 1 ) )
	top = drawn[-1].split( ' ', 1 )
	topC = top[0]
	topV = top[1]

	if topC == 'n': # colors for the uncolored
		colorChosen = input( "choose color" )
		# validity check pending
		topC = colorChosen
	
	if topV == 'R': # reverse
		direction = direction * -1
	
	if topV == 'R' or 'S' or 'T' or 'F':
		resolved = False

	if len( playerHands[turn] ) == 1:
		print( "uno" ) # button?
	elif len( playerHands[turn] ) == 0:
		break

	turn = WrapCheck( turn + direction, players )

	print( "drawn pile", drawn )
	print( "current card {}" .format( topC + ' ' + topV ) )

print( "you are winner :)" )