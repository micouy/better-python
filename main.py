import pygame
import lib
import game
import sys


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    game.okno.fill(lib.czarny)

    for instrukcja_warunkowa in lib.instrukcje_warunkowe:
        instrukcja_warunkowa.sprobuj_wykonac()

    game.w_kazdej_klatce()

    pygame.display.flip()
    clock.tick(lib.fps)
