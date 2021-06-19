import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

pygame.draw.circle(ventana, (250,0,0), (80,90), 20)
pygame.draw.rect(ventana, (0,250,0), (0,0,100,50))
#creamos un hexagono, aunque podemos crear más formas uniendo lineas
pygame.draw.polygon(ventana, (0,0,250), ((140,0), (291,106), (237,277), (56,277), (0,106)))
while True:
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()