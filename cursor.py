import pygame, sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Basic_Animation")

my_image = pygame.image.load("images/moon.png")
pos_x = 200
pos_y = 100

vel = 10
Blanco = (255,255,255)
derecha = True

while True:
	ventana.fill(Blanco)
	ventana.blit(my_image, (pos_x, pos_y))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				pos_x -= vel
			elif event.key == K_RIGHT:
				pos_x += vel
		elif event.type == pygame.KEYUP:
			if event.key == K_LEFT:
				print('izq liberada')
			elif event.key == K_RIGHT:
				print('der liberada')

	pos_x, pos_y = (pygame.mouse.get_pos())
	pos_x = pos_x-100
	pos_y = pos_y-50
	
	pygame.display.update()