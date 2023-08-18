import socket 
from _thread import *
import random
import sys

# T = draw two  | R = reverse   | S = skip
# F = draw four | C = color
cardsC = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'R', 'S']
cardsW = ['F', 'C'] # these have no color

# r = red       | g = green     | b = blue      | y = yellow        | n = none
colors = ['r', 'g', 'b', 'y']

"""
function definitions
"""

# creates a deck
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

# shuffles deck
def Shuffle():
	for pos in range( len( gameDeck ) ):
		posRand = random.randint( 0, len( gameDeck ) - 1 )
		gameDeck[pos], gameDeck[posRand] = gameDeck[posRand], gameDeck[pos]

# draws card from deck
def Draw( amount ):
	cardsDrawn = []

	for x in range( amount ):
		cardsDrawn.append( gameDeck.pop( 0 ) )
		if len( gameDeck ) == 0: # checks if deck empty
			# shuffle all except latest from drawn pile into deck
			hold = drawn.pop( -1 )
			gameDeck.extend( drawn )
			Shuffle()
			drawn.clear()
			drawn.append( hold )

	return cardsDrawn

# checks if card is playable
def CanPlay( card, topColor, topValue ):
	if 'n' in card and challenge == 'N':
		return True
	
	elif ( topColor in card ) or ( topValue in card ):
		return True
	
	return False

# checks if has playable card in hand
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

"""
server stuff
"""

server = "127.0.0.1"
port = 5555 # é uma porta aberta pra aplicações desse tipo

serv = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
serv.settimeout( 5 )
#AF_INET é pra ipv4 e Sock_STREAM é ser TCP

try: # vai q o socket tá sendo usado
	serv.bind( ( server, port ) )
except socket.error as err:
	str( err )

serv.listen( 4 ) # jogos com no máximo 4
print( "esperando uma conexão, servidor inicializado" )

"""
message exchanging
"""

def EncryptHand( hand, top, current ):
	out = ""
	for i in range( len( hand ) ):
		if i == len( hand ) - 1:
			out = out + hand[i]
		else:
			out = out + hand[i] + ','

	return out + '|' + top + '|' + str( current )

"""
game setup
"""

playerHands = []
drawn = []

players = 4 # 2-4 players
direction = 1 # 1 or -1 for cw and ccw
resolved = True # whether or not the top card's effect has been resolved
challenge = 'N'

# setup playing deck
gameDeck = MakeADeck()
Shuffle()

# draw cards for each player
for player in range( players ):
	playerHands.append( Draw( 7 ) ) # 7 cards

# draw first card
while True:
	drawn.extend( Draw( 1 ) )

	if drawn[-1] == 'n F': # doesnt accept +4 as first card
		gameDeck.append( drawn.pop( 0 ) )
		Shuffle()

	else:
		break

# split first card as color and value
top = drawn[-1].split( ' ', 1 )
topC = top[0]
topV = top[1]

"""
connection
"""

def Send( msg, con ):
	reply = msg.encode( "utf-8" )
	con.send( reply )
	while True:
		try:
			ok = con.recv( 32 ).decode( "utf-8" )
			if ok == "ok":
				print( "ok" )
				break
		except:
			print( "resending" )
			con.send( reply )
			continue


def SendGlobal( msg ):
	for player in playersList:
		Send( msg, player )

def ClientThread( connection, id ):
	global playing
	global playersConnected
	
	while True:
		continue
	
	print( "conexão perdida" )
	playersConnected = playersConnected - 1
	connection.close()
				
playersConnected = 0
playersList = []
playing = False
waiting = False

while True:
	if playersConnected < 4:
		while True:
			try:
				connection, ipAddr = serv.accept()
				break
			except:
				print( "waiting" )
				continue

		playersConnected = playersConnected + 1
		playersList = playersList + [connection]
		print( "conectado ao cliente de endereço IP: {}" .format( ipAddr ) )
		print( "jogadores: {}" .format( playersConnected ) )
		
		start_new_thread( ClientThread,( connection, playersConnected ) )
		
		Send( "MSG/You are player " + str( playersConnected ), connection )
		Send( "MSG/Your hand: " + str( playerHands[playersConnected - 1] ) + 
       		  "\nCurrent card: " + str( drawn[-1] ) + 
			  " \n\nWaiting for players", connection )
		
		if not playing:
			if playersConnected == 4:
				SendGlobal( "MSG/Starting game" )
				playing = True
				break

			if playersConnected > 1:
				while True:
					Send( "YON/Would you like to start with " + str( playersConnected ) + " players?", playersList[0] )

					try:
						reply = playersList[0].recv( 32 ).decode( "utf-8" )
						print( "reply " + reply )
						break
					except:
						continue

				if reply == 'Y':
					SendGlobal( "MSG/Starting game" )
					playing = True
					break

	if playing:
		break


players = playersConnected
turn = random.randint( 0, players - 1 ) # determines current player index

for i in range( players, 4 ):
	gameDeck.extend( playerHands[i] )

Shuffle()

if topC == 'n': # colors first card if uncolored
	Send( "COL/Choose color: (r)ed, (g)reen, (b)lue, (y)ellow \n > ", playersList[turn] )
	colorChosen = playersList[turn].recv( 32 ).decode( "utf-8" )
	topC = colorChosen
	top[0] = colorChosen

SendGlobal( "MSG/Current card: " + topC + ' ' + topV + "\nCurrent player: " + str( turn + 1 ) )

while True: # gameplay loop
	SendGlobal( "MSG/" + str( turn + 1 ) + "'s turn" ) # playerHands[turn] is current client
	if not resolved: # check if card was effect activated yet
		if topV == 'S': # skip
			SendGlobal( "MSG/Skipped" )
			turn = WrapCheck( turn + direction, players )
			resolved = True
			continue

		elif topV == 'T': # +2
			SendGlobal( "MSG/+2 and skipped" )
			playerHands[turn].extend( Draw( 2 ) )
			turn = WrapCheck( turn + direction, players )
			resolved = True
			continue

		elif topV == 'F': # +4
			Send( "YON/Challenge? (Y/N)", playersList[turn] )
			challenge = playersList[turn].recv( 32 ).decode( "utf-8" )
			
			if challenge == 'Y':
				valid = HandCheck( playerHands[turn - direction], topC, '-' )
				if valid:
					SendGlobal( "MSG/+2 fail penalty" )
					playerHands[turn].extend( Draw( 2 ) )
					SendGlobal( "MSG/+4 and skipped" )
					playerHands[turn].extend( Draw( 4 ) )
					turn = WrapCheck( turn + direction, players )
					resolved = True
					challenge = 'N'
					continue
				else:
					SendGlobal( "MSG/+4 penalty for challenged" )
					playerHands[WrapCheck( turn - direction, players )].extend( Draw( 4 ) )
					resolved = True
					challenge = 'N'
			else:
				SendGlobal( "MSG/+4 and skipped" )
				playerHands[turn].extend( Draw( 4 ) )
				turn = WrapCheck( turn + direction, players )
				resolved = True
				challenge = 'N'
				continue
	
	if not HandCheck( playerHands[turn], topC, topV ):
		SendGlobal( "MSG/No playable cards, drawing" )

	while not HandCheck( playerHands[turn], topC, topV ):
		playerHands[turn].extend( Draw( 1 ) ) # draws until able to play
	
	Send( "MSG/Your hand: " + str( playerHands[turn] ), playersList[turn] )

	topM = topC + ' ' + topV
	Send( "CAR/" + EncryptHand( playerHands[turn], topM, turn ), playersList[turn] )
	cardChosen = playersList[turn].recv( 32 ).decode( "utf-8" )

	for i in range( len( playerHands[turn] ) ):
		if cardChosen == playerHands[turn][i]:
			cardChosen = i

	# removes card from current client's hand into drawn pile
	drawn.append( playerHands[turn].pop( cardChosen ) )
	top = drawn[-1].split( ' ', 1 ) # updates top card info
	topC = top[0]
	topV = top[1]

	if topC == 'n': # colors for the uncolored
		Send( "COL/Choose color: (r)ed, (g)reen, (b)lue, (y)ellow \n > ", playersList[turn] )
		colorChosen = playersList[turn].recv( 32 ).decode( "utf-8" )
		topC = colorChosen
		top[0] = colorChosen
	
	if topV == 'R': # reverse
		direction = direction * -1
	
	if topV == 'R' or 'S' or 'T' or 'F': # turns resolved flag off on effect cards
		resolved = False

	if len( playerHands[turn] ) == 1: # one card left
		SendGlobal( "MSG/UNO from player " + str( turn ) ) # button?

	elif len( playerHands[turn] ) == 0: # end game on empty hand
		break

	# current client goes to playerHands[turn + direction]
	turn = WrapCheck( turn + direction, players ) 

	SendGlobal( "MSG/Current card: " + topC + ' ' + topV )

Send( "MSG/You are winner :)", playersList )

SendGlobal( "END/end" )