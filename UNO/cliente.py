import pygame
from rede import Rede

largura = 500
altura = 500

janela = pygame.display.set_mode(( largura, altura ))

pygame.display.set_caption( "Cliente" )

clientNum = 0


class Jogador():
    def __init__(self, x, y, largura, altura, cor): #pos x, y; largura e altura da jan; cor
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.rect = (x, y, largura, altura)
        self.velocidade = 2
           
    def desenha(self, janela):
        pygame.draw.rect(janela, self.cor, self.rect)

    def mover(self, ):
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            
        if teclas[pygame.K_UP]:
            self.y -= self.velocidade
            
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidade

        self.atualiza() #atualiza tds os jogadores por um lugar só
    def atualiza(self):
        self.rect = (self.x, self.y, self.largura, self.altura) #atualiz pos
        
def redrawJan(jogador, janela, jogador2):
    janela.fill((255, 255, 255))
    jogador.desenha(janela)
    jogador2.desenha(janela)
    pygame.display.update()
    
#Para cada cleinte, o cliente abre conexão com o serv, recebe a posição ini no mapa de acordo com q nr de cliente é,
# User muda pos do cliente e cliente manda newPos para serv.
# Serv interpreta tupla e manda pro outro cliente pra ele atualizar na tela

def lePos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def criaPos(tupla):
    return str(tupla[0]) + "," + str(tupla[1])
def main():
    rodando = True
    #importando minha rede
    mrede = Rede() #conecta ao servidor
    posIni = lePos(mrede.pegaPos())

    #-----------------------

    p1 = Jogador(posIni[0], posIni[1], 100, 100, (0, 0, 255))
    p2 = Jogador(0, 0, 100, 100, (0, 255, 0))

    tempo = pygame.time.Clock()
    
    while rodando:
        tempo.tick(60)

        p2Pos = lePos(mrede.send(criaPos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.atualiza()

        for event in pygame.event.get(): #sair jogo
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        p1.mover()       
        redrawJan(p1, janela, p2)
        
        
main()