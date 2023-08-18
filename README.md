# Aplicação Cliente-Servidor do Jogo UNO

Este é um sistema de jogo UNO implementado com uma arquitetura cliente-servidor. O jogo UNO é um jogo de cartas popular que envolve estratégia e diversão para 2 a 4 jogadores. Neste sistema, temos dois componentes principais: o servidor e o cliente.

## Instruções de Uso

### Passo 1: Executando o Servidor

1. Abra um terminal.
2. Navegue até o diretório onde os arquivos `servidor.py` e `cliente.py` estão localizados.
3. Execute o seguinte comando para iniciar o servidor:

```bash
python servidor.py
```

### Passo 2: Executando Clientes (Jogadores)

1. Abra terminais separados para cada jogador.
2. Navegue até o mesmo diretório onde os arquivos `servidor.py` e `cliente.py` estão localizados.
3. Execute o seguinte comando para iniciar um cliente para cada jogador:

```bash
python cliente.py
```

Repita o Passo 2 para cada jogador, de modo que cada jogador tenha um cliente em execução.

Lembre-se de que cada vez que você executa `cliente.py`, um novo cliente é criado, representando um jogador no jogo UNO.

## Regras do Jogo UNO

O UNO é um jogo de cartas com o objetivo de se livrar de todas as cartas da mão. Aqui estão algumas regras básicas:

1. **Objetivo:** O objetivo do jogo é ser o primeiro jogador a se livrar de todas as cartas na mão.

2. **Setup:** Cada jogador recebe uma mão de cartas. Uma carta é virada para cima para começar a pilha de descarte. Os jogadores combinam as cartas em suas mãos com a carta de topo na pilha de descarte por cor ou número.

3. **Regras de Combinação de Cartas:**
   - As cartas podem ser jogadas se combinarem por cor ou número com a carta no topo da pilha de descarte.
   - As cartas especiais têm ações associadas: pular o próximo jogador, inverter a direção do jogo, obrigar o próximo jogador a comprar cartas, mudança de cor.
   - O jogador pode escolher uma cor ao jogar uma carta de mudança de cor.

4. **Compra de Cartas:** Se um jogador não puder jogar uma carta válida, ele deve comprar uma carta do baralho. Se a carta comprada for jogável, o jogador pode jogá-la imediatamente.

5. **UNO:** Quando um jogador fica com uma carta em sua mão, ele deve dizer "UNO". Se outro jogador perceber e chamar "UNO" antes que o jogador o faça, o jogador que não disse "UNO" deve comprar cartas adicionais.

6. **Vitória:** O jogador que ficar sem cartas na mão primeiro vence a rodada e acumula pontos com base nas cartas restantes nas mãos dos outros jogadores. O jogo geralmente é jogado em várias rodadas, e o jogador com menos pontos no final das rodadas é o vencedor geral.

Lembrando que essas são regras básicas e podem haver variações regionais ou personalizadas do jogo.

Divirta-se jogando o UNO com o sistema cliente-servidor implementado!
