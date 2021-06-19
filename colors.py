#RGB, colores primarios. (0-255)

import pygame, sys
from pygame.locals import *

Color = (0,140,60)
Color2 =  pygame.Color(255,120,9)

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Colores")

while True:
	ventana.fill(Color2)
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()