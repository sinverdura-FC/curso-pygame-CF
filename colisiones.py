import pygame, sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Basic_Animation")

rectangulo2 = pygame.Rect(200,200,100,50)
pos_x = 200
pos_y = 100

vel = 2
Blanco = (255,255,255)
derecha = True

rectangulo = pygame.Rect(0,0,100,50)

while True:
	ventana.fill(Blanco)
	pygame.draw.rect(ventana, (0,255,0), rectangulo2)
	pygame.draw.rect(ventana, (255,0,0), rectangulo)
	rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

	if rectangulo.colliderect(rectangulo2):
		vel = 0
		print('Colision detectada')

	for event in pygame.event.get():
		if event.type ==QUIT:
			pygame.quit()
			sys.exit()

	if derecha == True:
		if pos_x < 500:
			pos_x += vel
			rectangulo2.left = pos_x
		else:
			derecha = False
	else:
		if pos_x > 1:
			pos_x -= vel
			rectangulo2.left = pos_x
		else:
			derecha = True


	pygame.display.update()