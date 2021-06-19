import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

Fuente = pygame.font.SysFont('Consolas',30)

aux = 1
while True:
	ventana.fill((255,255,255))
	Tiempo = pygame.time.get_ticks()/1000
	if aux == Tiempo:
		aux += 1
		print(Tiempo)
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	contador = Fuente.render('Tiempo:' +  str(Tiempo),0,(0,255,0))
	ventana.blit(contador,(100,100))		
	pygame.display.update()

