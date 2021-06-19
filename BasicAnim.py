import pygame, sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Basic_Animation")

my_image = pygame.image.load("images/moon.png")
pos_x = 200
pos_y = 100

vel = 2
Blanco = (255,255,255)
derecha = True

while True:
	ventana.fill(Blanco)
	ventana.blit(my_image, (pos_x, pos_y))
	for event in pygame.event.get():
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()

	if derecha == True:
		if pos_x < 400:
			pos_x += vel
		else:
			derecha = False
	else:
		if pos_x > 1:
			pos_x -= vel
		else:
			derecha = True


	pygame.display.update()