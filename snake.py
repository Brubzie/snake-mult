# Importando bibliotecas/módulos
import pygame
import time
import random

velCobra = 30

# Tamanho da janela
largura = 1280
altura = 1080

# Definindo as cores
preto = pygame.Color(0, 0, 0)
branco = pygame.Color(255, 255, 255)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)

# Inicializando o pygame
pygame.init()

# Inicializando a janela do jogo
pygame.display.set_caption('Snake Mult')
tela = pygame.display.set_mode((largura, altura))

# Controlador de FPS (Frames Per Second)
fps = pygame.time.Clock()

# Definindo as posições padrões das cobras
cobraPos = [100, 50] # [x, y]
cobraPos2 = [100, 150]

# Definindo os primeiros 4 blocos das cobras
# Corpo 1
corpoCobra = [
    [150, 100], # Posição [x, y] do 1° Bloco que compõe a primeira cobra
    [140, 100], # Posição [x, y] do 2° Bloco que compõe a primeira cobra
    [130, 100], # Posição [x, y] do 3° Bloco que compõe a primeira cobra
    [120, 100]  # Posição [x, y] do 4° Bloco que compõe a primeira cobra
]

# Corpo 2
corpoCobra2 = [
    [150, 150], # Posição [x, y] do 1° Bloco que compõe a segunda cobra
    [140, 150], # Posição [x, y] do 2° Bloco que compõe a segunda cobra
    [130, 150], # Posição [x, y] do 3° Bloco que compõe a segunda cobra
    [120, 150]  # Posição [x, y] do 4° Bloco que compõe a segunda cobra
]

# Posição da fruta
frutaPos = [random.randrange(1, (largura // 10)) * 10,
            random.randrange(1, (altura // 10)) * 10]
frutaNasc = True

# Configurações padrões da direção da cobra
direcao = 'RIGHT'
mudaPara = direcao

direcao2 = 'RIGHT'
mudaPara2 = direcao2

# Inicializando a pontuação
pontos1 = 0
pontos2 = 0

def desenhaCobra(corpoCobra, cor):
    for pos in corpoCobra:
        pygame.draw.rect(tela, cor, pygame.Rect(pos[0], pos[1], 10, 10))
        
    for pos in corpoCobra2:
        pygame.draw.rect(tela, cor, pygame.Rect(pos[0], pos[1], 10, 10))


# Funcionamento dos pontos
def mostraPontos(pontos, escolha, cor, font, tam):
    
    # Criando a font do objeto fontPontos
    fontPontos = pygame.font.SysFont(font, tam)
    
    # Criando o display da interface do objeto
    # interfacePontos
    interfacePontos = fontPontos.render('Pontos: ' + str(pontos), True, cor)

    # Criando um objeto retangular para o objeto de
    # superfície de texto
    pontosRet = interfacePontos.get_rect()

    # Exibindo o texto
    tela.blit(interfacePontos, pontosRet)

# Função de fim de jogo
def fim():
    
    # Criando o objeto fonte minhaFont
    minhaFont = pygame.font.SysFont('times new roman', 50)
    
    # Criando uma superfície de texto na qual o texto
    # vai ser escrito
    fimInterface1 = minhaFont.render('Sua pontuação: ' + str(pontos1), True, verde)
    fimInterface2 = minhaFont.render('Sua pontuação: ' + str(pontos2), True, azul)

    # Criando um objeto retangular para o texto de
    # interface de objeto
    fimRet1 = fimInterface1.get_rect()
    fimRet2 = fimInterface2.get_rect()

    # Configurando a posição do texto
    fimRet1.midtop = (largura / 2, altura / 4)
    fimRet2.midbottom = (largura / 2, altura / 4)

    # Desenha o texto na tela
    tela.blit(fimInterface1, fimRet1)
    tela.blit(fimInterface2, fimRet2)
    pygame.display.flip()

    # Após 2 segundos nós saimos do programa
    time.sleep(2)

    # Desativando a biblioteca pygame
    pygame.quit()

    # Sai do programa
    quit()
    
# Função Principal (main)
while True:
    
    # Lidando com eventos chave
    for event in pygame.event.get():
        
        # Imprime no console todos os eventos
        # print(event)
        
        # Teclas da cobra 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mudaPara = 'UP'
            if event.key == pygame.K_s:
                mudaPara = 'DOWN'
            if event.key == pygame.K_a:
                mudaPara = 'LEFT'
            if event.key == pygame.K_d:
                mudaPara = 'RIGHT'
            
        # Teclas da cobra 2
            if event.key == pygame.K_UP:
                mudaPara2 = 'UP'
            if event.key == pygame.K_DOWN:
                mudaPara2 = 'DOWN'
            if event.key == pygame.K_LEFT:
                mudaPara2 = 'LEFT'
            if event.key == pygame.K_RIGHT:
                mudaPara2 = 'RIGHT'
                
    # Se duas teclas forem pressionadas simultaneamente ela não consegue ir para duas direções ao mesmo tempo
    # Cobra 1
    if mudaPara == 'UP' and direcao != 'DOWN':
        direcao = 'UP'
    if mudaPara == 'DOWN' and direcao != 'UP':
        direcao = 'DOWN'
    if mudaPara == 'LEFT' and direcao != 'RIGHT':
        direcao = 'LEFT'
    if mudaPara == 'RIGHT' and direcao != 'LEFT':
        direcao = 'RIGHT'
        
    # Cobra 2
    if mudaPara2 == 'UP' and direcao2 != 'DOWN':
        direcao2 = 'UP'
    if mudaPara2 == 'DOWN' and direcao2 != 'UP':
        direcao2 = 'DOWN'
    if mudaPara2 == 'LEFT' and direcao2 != 'RIGHT':
        direcao2 = 'LEFT'
    if mudaPara2 == 'RIGHT' and direcao2 != 'LEFT':
        direcao2 = 'RIGHT'
    
    # Movendo a cobra
    if direcao == 'UP':
        cobraPos[1] -= 10
    if direcao == 'DOWN':
        cobraPos[1] += 10
    if direcao == 'LEFT':
        cobraPos[0] -= 10
    if direcao == 'RIGHT':
        cobraPos[0] += 10
        
    # Movendo a cobra 2
    if direcao2 == 'UP':
        cobraPos2[1] -= 10
    if direcao2 == 'DOWN':
        cobraPos2[1] += 10
    if direcao2 == 'LEFT':
        cobraPos2[0] -= 10
    if direcao2 == 'RIGHT':
        cobraPos2[0] += 10

    
    # Mecânica de crescimento da cobra
    # Se a cobra e a fruta colidirem a pontuação
    # vai ser incrementada em 10
    corpoCobra.insert(0, list(cobraPos))
    corpoCobra2.insert(0, list(cobraPos2))
    
    if cobraPos[0] == frutaPos[0] and cobraPos[1] == frutaPos[1]:
        pontos1 += 10
        frutaNasc = False
    else:
        corpoCobra.pop()
        
    if cobraPos2[0] == frutaPos[0] and cobraPos2[1] == frutaPos[1]:
        pontos2 += 10
        frutaNasc = False
    else:
        corpoCobra2.pop()
        
    if not frutaNasc:
        frutaPos = [random.randrange(1, (largura // 10)) * 10,
        random.randrange(1, (altura // 10)) * 10]
        
    frutaNasc = True
    tela.fill(preto)
    
    desenhaCobra(corpoCobra, verde)
    desenhaCobra(corpoCobra2, azul)
        
    pygame.draw.rect(tela, branco, pygame.Rect(
    frutaPos[0], frutaPos[1], 10, 10))
    
    # Condições de fim de jogo
    if cobraPos[0] < 0 or cobraPos[0] > largura - 10:
        fim()
    if cobraPos[1] < 0 or cobraPos[1] > altura - 10:
        fim()

    if cobraPos2[0] < 0 or cobraPos2[0] > largura - 10:
        fim()
    if cobraPos2[1] < 0 or cobraPos2[1] > altura - 10:
        fim()
    
    # Tocando o corpo da cobra
    # Cobra 1
    for block in corpoCobra[1:]:
        if cobraPos[0] == block[0] and cobraPos[1] == block[1]:
            fim()

    # Cobra 2
    for block in corpoCobra2[1:]:
        if cobraPos2[0] == block[0] and cobraPos2[1] == block[1]:
            fim()
            
    # Tocando o corpo da outra cobra
    for block1 in corpoCobra:
        for block2 in corpoCobra2:
            if block1[0] == block2[0] and block1[1] == block2[1]:
                fim()
        
    # Mostrando a pontuação continuamente
    mostraPontos(pontos1, 1, branco, 'times new roman', 20)
    mostraPontos(pontos2, 2, azul, 'times new roman', 20)
    
    # Recarrega a tela do jogo
    pygame.display.update()
    
    # Frame Per Second
    fps.tick(velCobra)
