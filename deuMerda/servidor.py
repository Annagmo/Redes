import socket 
from _thread import *
import sys

servidor = "127.0.0.1"
porta = 5555 # é uma porta aberta pra aplicações desse tipo

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET é pra ipv4 e Sock_STREAM é se o fluxo de dados é bidirecional ou n ou q tipo

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
    return int(str[0], int(str[1]))

def criaPos(tupla):
    return str(tupla[0]) + "," + str(tupla[1])


def threadDeCliente(conexao, jogadorAtual):
    #mandamos a posição inicial p/ cada jogador no inicio das reespectivas conexões.
    #pegando o vec de posições e quebrando as tuplas com a criaPos
    conexao.send(criaPos(posicoes[jogadorAtual]))
    reply = ""
    while True:
        try:
            dados = lePos(conexao.recv(2048).decode()) # até 2048 bits q vao ser recebidos, nd mt grande pra rápido. decodifica p/ palavras.
            #pega a string e vira tupla
            posicoes[jogadorAtual] = dados #atualiza o vec de pos

            if not dados:
                print("Disconectado.") #disconectado por falta de transmissão de dados ou erros na decodificação.
                break
            else:
                if(jogadorAtual ==1):
                    resposta = posicoes[0] #se for o p1 envia onde é q tá o p2 e vice-versa
                else:
                    resposta = posicoes[1]
                print("Dados recebidos: {}", dados)
                print("Enviando: {}", resposta) #envia a respost
                
            conexao.sendall(str.encode(criaPos(resposta)) ) #coloca resposta string em tupla e codifica a resposta do servidor (é pra segurança).
        except:
            break
        
    print("Conexão Perdida.")
    conexao.close()

jogadorAtual = 0

while True:
    conexao, endIP = serv.accept()
    print("conectado ao cliente de endereço IP: {}", endIP)
    
    start_new_thread(threadDeCliente,(conexao,jogadorAtual))
    jogadorAtual += 1 # a cada inicio de conexão é mais 1 jogador, novo jogador é +1 doq anterior
    
