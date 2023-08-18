# Aplicação Cliente-Servidor do Jogo UNO

Este é um sistema de jogo UNO implementado com uma arquitetura cliente-servidor. O jogo UNO é um jogo de cartas popular que envolve estratégia e diversão para 2 a 4 jogadores. Neste sistema, temos dois componentes principais: o servidor e o cliente.

## Instruções de Uso

### Passo 1: Executando o Servidor

1. Abra um terminal no computador que será o servidor.
2. Navegue até o diretório onde os arquivos `servidor.py` e `cliente.py` estão localizados.
3. Execute o seguinte comando para iniciar o servidor:

```bash
python3 servidor.py
```

### Passo 2: Executando Clientes (Jogadores)
Lembre-se de jogar com 2 a 4 jogadores!

1. Abra terminais separados para cada jogador. Eles podem ser testados na mesma máquina ou em várias conectadas à internet ou em uma conexão hamachi.
3. Navegue até o mesmo diretório onde os arquivos `servidor.py` e `cliente.py` estão localizados.
4. Execute o seguinte comando para iniciar um cliente para cada jogador:

```bash
python3 cliente.py
```

Repita o Passo 2 para cada jogador, de modo que cada jogador tenha um cliente em execução.

Lembre-se de que cada vez que você executa `cliente.py`, um novo cliente é criado, representando um jogador no jogo UNO.

## Regras do Jogo UNO

O UNO é um jogo de cartas com o objetivo de se livrar de todas as cartas da mão. Aqui estão algumas regras básicas:

1. **Objetivo:** O objetivo do jogo é ser o primeiro jogador a se livrar de todas as cartas na mão.

2. **Setup:** Cada jogador recebe uma mão de cartas. Uma carta éescolhida aleatoriamente pelo servidor para começar a pilha de descarte. Os jogadores combinam as cartas em suas mãos com a carta de topo na pilha de descarte por cor ou número.

3. **Regras de Combinação de Cartas:**
   - As cartas podem ser jogadas se combinarem por cor ou número com a carta no topo da pilha de descarte.
   - As cartas especiais têm ações associadas: pular o próximo jogador, obrigar o próximo jogador a comprar cartas, mudança de cor.
   - O jogador pode escolher uma cor ao jogar uma carta de mudança de cor.

4. **Compra de Cartas:** Se um jogador não puder jogar uma carta válida, ele deve comprar uma carta do baralho. Se a carta comprada for jogável, o jogador pode jogá-la imediatamente.

5. **Desafio de Cor:** Quando um jogador joga uma carta de mudança de cor (por exemplo, carta "Mudar Cor" ou "Mais 4"), os jogadores subsequentes podem desafiar a escolha de cor do jogador anterior. O jogador desafiado deve mostrar suas cartas. Se tiver pelo menos uma carta da cor escolhida, o desafiante deve comprar quatro cartas. Caso contrário, o jogador desafiado compra seis cartas.

6. **Vitória:** O jogador que ficar sem cartas na mão primeiro vence a rodada e acumula pontos com base nas cartas restantes nas mãos dos outros jogadores. O jogo geralmente é jogado em várias rodadas, e o jogador com menos pontos no final das rodadas é o vencedor geral.


Divirta-se jogando o UNO com o sistema cliente-servidor implementado!
