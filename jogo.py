import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

FPS = 60
LARGURA = 800
ALTURA = 600

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Capivara Chase: Escape from Ibama')

cenario = pygame.image.load('fundo.png')

imagesdireita = [pygame.image.load("direitaum.png"), pygame.image.load("direitadois.png")]
imagesesquerda = [pygame.image.load("esquerdaum.png"), pygame.image.load("esquerdadois.png")]

class Pedro(pygame.sprite.Sprite):

    def pular(self):
        self.pulo = True

    def update(self):
        if self.pular:
            if self.rect.y <= self.pos_y_inicial - 50:
                self.pular = False
            self.rect.y -= 15
        else:
            if self.rect.y >= self.pos_y_inicial:
                self.rect.y = self.pos_y_inicial
            else:
                self.rect.y += 15

        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_pedro[int(self.index_lista)]

pedro = Pedro()
clock = pygame.time.Clock()

xpos = 0
ypos = 359
deltaX = 0
deltaY = 0
pressionado = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                deltaX = 0
            if event.key == pygame.K_SPACE:
                deltaY = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deltaX = -5
                pressionado = 1
            if event.key == pygame.K_RIGHT:
                deltaX = 5
                pressionado = 2
            if event.key == pygame.K_SPACE:
                deltaY = -5
                pressionado = 3 

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    xpos += deltaX
    ypos += deltaY

    if xpos < -25:
        xpos = LARGURA - 1
    if xpos > LARGURA:
        xpos = 0
    if ypos < -25:
        ypos = ALTURA - 1
    if ypos > ALTURA:
        ypos = 0

    tela.blit(cenario, (0, 0))
    indexImg = int(pygame.time.get_ticks() // 125) % 2  # Troca de imagem a cada 125 ms
    if deltaX > 0:
        tela.blit(imagesdireita[indexImg], (xpos, ypos))
    elif deltaX < 0:
        tela.blit(imagesesquerda[indexImg], (xpos, ypos))
    elif deltaX == 0 and pressionado == 1:
        tela.blit(imagesesquerda[0], (xpos, ypos))
    elif deltaX == 0 and pressionado == 2:
        tela.blit(imagesdireita[0], (xpos, ypos))
    elif deltaY == 0 and pressionado == 3:
        tela.blit(imagesdireita[0], (xpos, ypos))

    pygame.display.flip()
    clock.tick(FPS)