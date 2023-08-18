import socket
import time

server = "127.0.0.1"
port = 5555

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect( ( server, port ) )

def DecryptHand( str ):
	str = str.split( '|' )
	hand = str[0]
	hand = hand.split( ',' )
	top = str[1]
	current = int( str[2] )

	return hand, top, current

def CanPlay( card, topColor, topValue ):
	if 'n' in card:
		return True
	
	elif ( topColor in card ) or ( topValue in card ):
		return True
	
	return False

def Send( msg ):
	reply = msg.encode( "utf-8" )
	client.sendall( reply )

def Receive( msg ):
	msg = msg.split( '/' )
	header = msg[0]
	info = msg[1]
	match header:
		case "MSG":
			print( info )
			Send( "ok" )
			return info
		
		case "YON":
			print( info, end="" )
			while True:
				reply = input( " (Y/N): " )

				if reply == 'Y' or 'N':
					print( "oke" )
					break

				else:
					print( "invalid input" )
					continue
			
			Send( "ok" )
			time.sleep( 1 )
			Send( reply )
		
		
		case "COL":
			print( info, end="" )
			while True:
				reply = input()
				if reply == 'r' or 'g' or 'b' or 'y':
					break

				else:
					print( "invalid input" )
					continue
			
			Send( "ok" )
			time.sleep( 1 )
			Send( reply )
		
		
		case "CAR":
			hand, top, curr = DecryptHand( info )
			top = top.split( ' ', 1 )
			topC = top[0]
			topV = top[1]

			while True:
				while True:
					reply = input( "Choose a card to play: " )
					if len( reply ) != 3:
						print( "invalid input" )
						continue

					replyC, replyV = reply.split( ' ' )
					print( replyC + " " + replyV )
					if len( replyC ) == 1 and len( replyV ) == 1 and ( replyC == 'r' or 'g' or 'b' or 'y' ) and ( replyV.isdigit or replyV == 'T' or 'F' or 'C' or 'S' or 'R' ):
						break
					else:
						print( "invalid input" )
						continue

				if CanPlay( reply, topC, topV ):
					if reply in hand:
						break
				
				print( "invalid input" )
			
			Send( "ok" )
			time.sleep( 1 )
			Send( reply )
		
		case "END":
			Send( "ok" )
			client.close()

while True:
	info = client.recv( 2048 ).decode( "utf-8" )

	if info:
		info = Receive( info )

	