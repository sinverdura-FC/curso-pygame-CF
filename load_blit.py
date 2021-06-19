import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("load_blit")

my_image = pygame.image.load("images/moon.png")
pos_x, pos_y = 130, 70

ventana.blit(my_image, (pos_x, pos_y))

while True:
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()