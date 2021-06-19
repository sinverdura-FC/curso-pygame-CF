import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

my_font = pygame.font.Font(None, 30)
my_text = my_font.render('OFGC', 0, (0,0,255), (255,255,255))

my_font_system = pygame.font.SysFont('Consolas', 60)
my_text2 = my_font_system.render('Consolas',0, (255,0,0))

while True:
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	ventana.blit(my_text2,(0,0))		
	ventana.blit(my_text,(200,200))

	pygame.display.update()