# Snake Multiplayer em Pygame

Um clone do clássico jogo Snake, desenvolvido em Python com a biblioteca Pygame, focado em uma experiência competitiva para dois jogadores locais.

## 📜 Sobre o Projeto

Este projeto é uma versão aprimorada do jogo da cobrinha, permitindo que dois jogadores compitam na mesma tela para ver quem consegue a maior pontuação. O jogo foi reestruturado usando Programação Orientada a Objetos para garantir um código mais limpo, organizado e fácil de estender.

## ✨ Funcionalidades

  - **Modo Multiplayer Local:** Desafie um amigo na mesma máquina.
  - **Controles Individuais:** Jogador 1 utiliza as teclas **WASD** e o Jogador 2 utiliza as **Setas Direcionais**.
  - **Placar em Tempo Real:** Acompanhe a pontuação de ambos os jogadores durante a partida.
  - **Dificuldade Progressiva:** A velocidade do jogo aumenta conforme os jogadores pontuam, tornando o desafio cada vez maior.
  - **Tela de "Fim de Jogo" Inteligente:** Ao final da partida, o jogo declara o vencedor e oferece opções.
  - **Reinício Rápido:** Pressione a tecla **'R'** na tela de fim de jogo para começar uma nova partida instantaneamente, sem precisar fechar o programa.

## 🛠️ Tecnologias Utilizadas

  - **Python 3**
  - **Biblioteca Pygame**

## 🚀 Como Jogar

Siga as instruções abaixo para executar o jogo em sua máquina local.

### Pré-requisitos

  - Você precisa ter o **Python 3** instalado em seu computador.
  - O `pip` (gerenciador de pacotes do Python) também é necessário para instalar o Pygame.

### Instalação e Execução

1.  **Clone o repositório ou baixe os arquivos**
    Se você tem o Git, pode clonar o repositório com o comando:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

    Caso contrário, apenas baixe o arquivo `.py` com o código do jogo.

2.  **Navegue até a pasta do projeto**
    Use o terminal para entrar na pasta onde você salvou os arquivos.

    ```bash
    cd caminho/para/a/pasta
    ```

3.  **Instale o Pygame**
    Execute o seguinte comando no seu terminal para instalar a biblioteca Pygame:

    ```bash
    pip install pygame
    ```

4.  **Execute o Jogo**
    Para iniciar o jogo, execute o script Python:

    ```bash
    python snake.py
    ```

### Controles

  - **Jogador 1 (Cobra Verde):**

      - `W` - Mover para Cima
      - `S` - Mover para Baixo
      - `A` - Mover para a Esquerda
      - `D` - Mover para a Direita

  - **Jogador 2 (Cobra Azul):**

      - `Seta para Cima` - Mover para Cima
      - `Seta para Baixo` - Mover para Baixo
      - `Seta para Esquerda` - Mover para a Esquerda
      - `Seta para Direita` - Mover para a Direita

  - **Tela de Fim de Jogo:**

      - `R` - Reiniciar a partida
      - `Q` - Sair do jogo

## 🏗️ Estrutura do Código

O projeto foi desenvolvido com uma abordagem de Programação Orientada a Objetos (POO) para garantir um código limpo, modular e de fácil manutenção.

  - **Classe `Jogo`**: Gerencia o estado principal do jogo, o loop de eventos, as telas (jogo, fim de jogo), a geração de frutas e as regras gerais de colisão entre jogadores.
  - **Classe `Cobra`**: Modela cada jogador, encapsulando suas propriedades (cor, corpo, posição, pontuação) e comportamentos (mover, crescer, desenhar, verificar colisões com a parede e com o próprio corpo).
