import pygame, sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("load_blit")

my_image = pygame.image.load("images/moon.png")
pos_x = randint(10, 700)
pos_y = randint(10, 500)

ventana.blit(my_image, (pos_x, pos_y))
print(pos_x, pos_y)

while True:
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()