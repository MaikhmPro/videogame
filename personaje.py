import pygame 
import contantes
class Personaje():
    def __init__(self,x,y):
        self.forma= pygame.Rect(0,0,contantes.ANCHO_PERSONAJE,contantes.ALTO_PERSONAJE)
        self.forma.center=(x,y)
    def dibujar(self,ventana):
         self.forma = pygame.Rect(0, 0, contantes.ANCHO_PERSONAJE, contantes.ALTO_PERSONAJE)
    def movimiento(self,delta_x,delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y






        

