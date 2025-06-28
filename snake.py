# Importando bibliotecas/módulos
import pygame
import time
import random

# --- Configurações Gerais ---
LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_BLOCO = 10
VELOCIDADE_INICIAL = 15

# --- Cores ---
PRETO = pygame.Color(0, 0, 0)
BRANCO = pygame.Color(255, 255, 255)
VERMELHO = pygame.Color(255, 0, 0)
VERDE = pygame.Color(0, 255, 0)
AZUL = pygame.Color(0, 0, 255)

class Cobra:
    """
    Classe para representar uma cobra, suas propriedades e ações.
    """
    def __init__(self, cor, pos_inicial, teclas_controle):
        self.cor = cor
        self.posicao = list(pos_inicial)
        self.corpo = [list(pos_inicial), 
                      [pos_inicial[0] - TAMANHO_BLOCO, pos_inicial[1]],
                      [pos_inicial[0] - (2 * TAMANHO_BLOCO), pos_inicial[1]]]
        self.direcao = 'RIGHT'
        self.muda_para = self.direcao
        self.pontos = 0
        self.teclas = teclas_controle

    def mover(self):
        # Validação para não permitir que a cobra se mova na direção oposta instantaneamente
        if self.muda_para == 'UP' and self.direcao != 'DOWN':
            self.direcao = 'UP'
        if self.muda_para == 'DOWN' and self.direcao != 'UP':
            self.direcao = 'DOWN'
        if self.muda_para == 'LEFT' and self.direcao != 'RIGHT':
            self.direcao = 'LEFT'
        if self.muda_para == 'RIGHT' and self.direcao != 'LEFT':
            self.direcao = 'RIGHT'

        # Atualiza a posição da cabeça da cobra
        if self.direcao == 'UP':
            self.posicao[1] -= TAMANHO_BLOCO
        if self.direcao == 'DOWN':
            self.posicao[1] += TAMANHO_BLOCO
        if self.direcao == 'LEFT':
            self.posicao[0] -= TAMANHO_BLOCO
        if self.direcao == 'RIGHT':
            self.posicao[0] += TAMANHO_BLOCO

    def crescer(self):
        self.corpo.insert(0, list(self.posicao))
        self.pontos += 10

    def encolher(self):
        self.corpo.insert(0, list(self.posicao))
        self.corpo.pop()

    def desenhar(self, tela):
        for pos in self.corpo:
            pygame.draw.rect(tela, self.cor, pygame.Rect(pos[0], pos[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

    def verificar_colisao_propria(self):
        # A cabeça colidiu com qualquer parte do corpo?
        for bloco in self.corpo[1:]:
            if self.posicao == bloco:
                return True
        return False
        
    def verificar_colisao_parede(self):
        if self.posicao[0] < 0 or self.posicao[0] > LARGURA_TELA - TAMANHO_BLOCO:
            return True
        if self.posicao[1] < 0 or self.posicao[1] > ALTURA_TELA - TAMANHO_BLOCO:
            return True
        return False


class Jogo:
    """
    Classe principal que gerencia o estado e o loop do jogo.
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Multiplayer Melhorado')
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.fps = pygame.time.Clock()
        self.fonte_placar = pygame.font.SysFont('consolas', 20)
        self.fonte_fim_jogo = pygame.font.SysFont('consolas', 50)
        self.iniciar_jogo()

    def iniciar_jogo(self):
        # Define as teclas de controle para cada jogador
        teclas_p1 = {'UP': pygame.K_w, 'DOWN': pygame.K_s, 'LEFT': pygame.K_a, 'RIGHT': pygame.K_d}
        teclas_p2 = {'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN, 'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT}
        
        self.cobra1 = Cobra(VERDE, [100, 50], teclas_p1)
        self.cobra2 = Cobra(AZUL, [100, 550], teclas_p2)
        
        self.fruta_pos = self.gerar_fruta()
        self.fruta_nasc = True
        
        self.game_over = False
        self.vencedor = None
        
        self.velocidade_cobra = VELOCIDADE_INICIAL

    def gerar_fruta(self):
        return [random.randrange(1, (LARGURA_TELA // TAMANHO_BLOCO)) * TAMANHO_BLOCO,
                random.randrange(1, (ALTURA_TELA // TAMANHO_BLOCO)) * TAMANHO_BLOCO]

    def mostrar_placar(self):
        placar1_superficie = self.fonte_placar.render(f'Verde: {self.cobra1.pontos}', True, BRANCO)
        placar2_superficie = self.fonte_placar.render(f'Azul: {self.cobra2.pontos}', True, BRANCO)
        
        placar1_ret = placar1_superficie.get_rect(topleft=(20, 10))
        placar2_ret = placar2_superficie.get_rect(topright=(LARGURA_TELA - 20, 10))
        
        self.tela.blit(placar1_superficie, placar1_ret)
        self.tela.blit(placar2_superficie, placar2_ret)

    def tela_fim_de_jogo(self):
        self.tela.fill(PRETO)
        
        # Define a mensagem do vencedor
        if self.vencedor == 'Empate':
            msg_vencedor = 'Empate!'
        else:
            msg_vencedor = f'O jogador {self.vencedor} venceu!'
            
        texto_fim = self.fonte_fim_jogo.render('FIM DE JOGO', True, VERMELHO)
        texto_vencedor = self.fonte_placar.render(msg_vencedor, True, BRANCO)
        texto_restart = self.fonte_placar.render('Pressione R para reiniciar ou Q para sair.', True, BRANCO)
        
        # Posiciona os textos na tela
        texto_fim_ret = texto_fim.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 - 50))
        texto_vencedor_ret = texto_vencedor.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2))
        texto_restart_ret = texto_restart.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + 50))
        
        self.tela.blit(texto_fim, texto_fim_ret)
        self.tela.blit(texto_vencedor, texto_vencedor_ret)
        self.tela.blit(texto_restart, texto_restart_ret)
        pygame.display.flip()

    def rodar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.iniciar_jogo()
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                    else:
                        # Controla a direção da cobra 1
                        for direcao, tecla in self.cobra1.teclas.items():
                            if event.key == tecla:
                                self.cobra1.muda_para = direcao
                        # Controla a direção da cobra 2
                        for direcao, tecla in self.cobra2.teclas.items():
                            if event.key == tecla:
                                self.cobra2.muda_para = direcao

            if not self.game_over:
                self.logica_do_jogo()
            else:
                self.tela_fim_de_jogo()
            
            self.fps.tick(self.velocidade_cobra)

    def logica_do_jogo(self):
        # Movimentação
        self.cobra1.mover()
        self.cobra2.mover()

        # Crescimento ao comer a fruta
        if self.cobra1.posicao == self.fruta_pos:
            self.cobra1.crescer()
            self.fruta_nasc = False
        else:
            self.cobra1.encolher()

        if self.cobra2.posicao == self.fruta_pos:
            self.cobra2.crescer()
            self.fruta_nasc = False
        else:
            self.cobra2.encolher()
        
        # Gerar nova fruta se a anterior foi comida
        if not self.fruta_nasc:
            self.fruta_pos = self.gerar_fruta()
        self.fruta_nasc = True
        
        # Aumentar velocidade com base na pontuação total
        self.velocidade_cobra = VELOCIDADE_INICIAL + (self.cobra1.pontos + self.cobra2.pontos) // 20

        # Desenhar elementos na tela
        self.tela.fill(PRETO)
        self.cobra1.desenhar(self.tela)
        self.cobra2.desenhar(self.tela)
        pygame.draw.rect(self.tela, BRANCO, pygame.Rect(self.fruta_pos[0], self.fruta_pos[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        
        # Verificação de Colisões e Fim de Jogo
        # 1. Colisão com a parede
        if self.cobra1.verificar_colisao_parede():
            self.game_over = True
            self.vencedor = 'Azul'
        if self.cobra2.verificar_colisao_parede():
            self.game_over = True
            self.vencedor = 'Verde'

        # 2. Colisão com o próprio corpo
        if self.cobra1.verificar_colisao_propria():
            self.game_over = True
            self.vencedor = 'Azul'
        if self.cobra2.verificar_colisao_propria():
            self.game_over = True
            self.vencedor = 'Verde'
            
        # 3. Colisão entre as cobras
        for bloco in self.cobra2.corpo:
            if self.cobra1.posicao == bloco:
                self.game_over = True
                self.definir_vencedor_colisao()
        for bloco in self.cobra1.corpo:
            if self.cobra2.posicao == bloco:
                self.game_over = True
                self.definir_vencedor_colisao()

        # Atualização do display
        self.mostrar_placar()
        pygame.display.update()

    def definir_vencedor_colisao(self):
        if self.cobra1.pontos > self.cobra2.pontos:
            self.vencedor = 'Verde'
        elif self.cobra2.pontos > self.cobra1.pontos:
            self.vencedor = 'Azul'
        else:
            self.vencedor = 'Empate'

if __name__ == '__main__':
    jogo = Jogo()
    jogo.rodar()
    