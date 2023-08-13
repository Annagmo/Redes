import socket

class Rede:
    def __init__(self):
       self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #mesmo do serv
       self.servidor = "127.0.0.1"
       self.porta = 5555
       self.endIP = (self.servidor, self.porta)
       self.posicao = self.conectar()

    def pegaPos(self):
        return self.posicao
    def conectar(self):
        try:
            self.cliente.connect(self.endIP) #quando conecta recebe o "conexão estabelecida" e decodifica
            return self.cliente.recv(2048).decode()
        except:
            pass

    def send(self, dado):
        try:
            self.cliente.send(str.encode(dado))
            return self.cliente.recv(2048).decode()
        except socket.error as err:
            print(err)
