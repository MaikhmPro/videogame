import pygame 
from personaje import Personaje
import contantes

player = Personaje(50,50)
pygame.init()

ancho = contantes.ANCHO_VENTANA
alto = contantes.ALTO_VENTANA
ventana = pygame.display.set_mode((ancho,alto))

pygame.display.set_caption("Mi first videogame")

"""Variables de mvimiento"""
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

run = True
"""Calcular movimiento"""
while run :

    delta_x = 0
    delta_y = 0
    if mover_derecha == True:
        delta_x= 5
    if mover_izquierda == True:
        delta_x= -5
    if mover_arriba == True:
        delta_y= -5 
    if mover_abajo == True:
        delta_Y= 5
    player.movimiento(delta_x, delta_y)
    player.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
                if event.key == pygame.K_d:
                    mover_derecha = True
                    if event.key == pygame.K_w:
                        mover_arriba = True
                        if event.key == pygame.K_s:
                            mover_abajo = True


pygame.display.update()
pygame.quit()