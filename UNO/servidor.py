import socket 
from _thread import *
from unoFuncs import *
import sys

servidor = "127.0.0.1"
porta = 5555 # é uma porta aberta pra aplicações desse tipo

direction = 1 #uno

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET é pra ipv4 e Sock_STREAM é ser TCP

try: #vai q o socket tá sendo usado
    serv.bind((servidor, porta))
except socket.error as err:
    str(err)

serv.listen(4) #jogos com no máximo 4p
print("Esperando uma conexão, servidor inicializado.")


#o serv tem q armazenar as pos dos jogadores, q n é mt coisa, entao vec.
posicoes = [(0, 0), (100, 100)]


def lePos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def criaPos(tupla):
    return str(tupla[0]) + "," + str(tupla[1])

def vecToStr(vector):
    string = ''
    for i in range(len(vector)-1):
        string += str(vector[i])
        string += ","
    string += str(vector[i+1])  #    'y 3', 'r 2', 'y 8', 'b 4'
    return string

def strToVec(string):
    vector = string.split(",")
    return vector


#uno:
#faz deck primeiro
gameDeck = MakeADeck()
gameDeck = Shuffle(gameDeck)
turnOne = True
drawn = []
def threadDeCliente(connection, players, gameDeck):
    if(turnOne == True): #uno
        #na entrada de cliente: servidor manda deck pra cada usr, usr tira carta e manda deck de volta, atualiza deck
        connection.send(str.encode(vecToStr(gameDeck))) #passa vect como str para o encode
        gameDeck = strToVec(connection.recv(2048).decode()) #decode volta em str e strToVect passa p/ vec


    # servidor inicializa, cria thread cliente 1, pega as cartas; cliente 2, 3, 4 tmb
    while True: # Draws first card (While true continues if special card)
        gameDeck = Shuffle(gameDeck)
        drawn.extend(Draw(1))
        if drawn[-1] == 'n F':  # doesnt accept +4 as first card
            gameDeck.append(drawn.pop(0))
        else:
            break
    connection.sendall(str.encode(gameDeck))
    reply = ""


    while True: #resto dos turnos
        try:
            dados = lePos(connection.recv(2048).decode()) # até 2048 bits q vao ser recebidos, nd mt grande pra rápido. decodifica p/ palavras.
            #pega a string e vira tupla
            posicoes[players] = dados #atualiza o vec de pos

            if not dados:
                print("Disconectado.") #disconectado por falta de transmissão de dados ou erros na decodificação.
                break
            else:
                if(players ==1):
                    resposta = posicoes[0] #se for o p1 envia onde é q tá o p2 e vice-versa
                else:
                    resposta = posicoes[1]
                print("Dados recebidos: {}", dados)
                print("Enviando: {}", resposta) #envia a respost
                
            connection.sendall(str.encode(criaPos(resposta)) ) #coloca resposta string em tupla e codifica a resposta do servidor (é pra segurança).
        except:
            break
        
    print("Conexão Perdida.")
    connection.close()
turnOne = False
players = 0

while True:
    connection, endIP = serv.accept()
    print("conectado ao cliente de endereço IP: {}", endIP)

    start_new_thread(threadDeCliente,(connection,players))
    
    """
    if not confirmation:
        while not playing:
            wait for confirmation
    """
    
    
    if(direction ==1):
        players += 1 # a cada inicio de conexão é mais 1 jogador, novo jogador é +1 doq anterior
    else: #uno falta wraparound
        players -=1
    
