import pygame
import sys
import cores

pygame.init()

# Tela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Botões com Classe")

# Fonte
fonte = pygame.font.SysFont("arial", 28)

class Botao:
    def __init__(self, rect, texto, cor):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.cor = cor
        self.pressed = False

    def desenhar(self, tela, fonte, hover=False):
        cor_atual = self.cor
        if self.pressed:
            cor_atual = cores.AZUL_ESCURO
        elif hover:
            cor_atual = cores.AZUL_CLARO

        # Sombra simples atrás do botão
        sombra_rect = self.rect.copy()
        sombra_rect.move_ip(3, 3)
        pygame.draw.rect(tela, cores.CINZA_CLARO, sombra_rect, border_radius=12)

        # Botão arredondado
        pygame.draw.rect(tela, cor_atual, self.rect, border_radius=12)

        # Texto com sombra
        texto_renderizado = fonte.render(self.texto, True, cores.PRETO)
        sombra_texto = fonte.render(self.texto, True, cores.CINZA_CLARO)

        ret_texto = texto_renderizado.get_rect(center=self.rect.center)
        ret_sombra = sombra_texto.get_rect(center=(self.rect.centerx + 2, self.rect.centery + 2))

        tela.blit(sombra_texto, ret_sombra)  # sombra texto
        tela.blit(texto_renderizado, ret_texto)  # texto normal

    def checar_click(self, pos):
        return self.rect.collidepoint(pos)

# Cria instâncias de Botao
botoes = [
    Botao((300, 150, 200, 50), "Jogar", cores.AZUL),
    Botao((300, 220, 200, 50), "Opções", cores.AZUL),
    Botao((300, 290, 200, 50), "Sair", cores.AZUL),
]

rodando = True
while rodando:
    pos_mouse = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for botao in botoes:
                if botao.checar_click(evento.pos):
                    print(f"Clicou no botão: {botao.texto}")
                    botao.pressed = True
                    if botao.texto == "Sair":
                        pygame.quit()
                        sys.exit()
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            for botao in botoes:
                botao.pressed = False

    tela.fill(cores.BRANCO)

    for botao in botoes:
        hover = botao.rect.collidepoint(pos_mouse)
        botao.desenhar(tela, fonte, hover)

    pygame.display.flip()

pygame.quit()
sys.exit()
