import pygame

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
        
        self.rect = (self.x, self.y, self.largura, self.altura) #atualiz pos
        
def redrawJan(jogador, janela):
    janela.fill((255, 255, 255))
    jogador.desenha(janela)
    pygame.display.update()
    
    
def main():
    running = True
    
    p1 = Jogador(50, 50, 100, 100, (0, 0, 255))
    tempo = pygame.time.Clock()
    
    while running: 
        tempo.tick(60)
        for event in pygame.event.get(): #sair jogo
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        p1.mover()       
        redrawJan(p1, janela)
        
        
main()