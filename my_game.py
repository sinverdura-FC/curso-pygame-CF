#Añado comentario para el curso de Git, branch Test

import pygame, sys
from pygame.locals import *
from random import randint

ancho = 900
alto = 480
listaEnemigo = []

class naveEspacial(pygame.sprite.Sprite):
	#Clase para las naves

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load('images/nave.jpg')
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto-30
		self.listaDisparo = []
		self.Vida = True
		self.velocidad = 20

		self.sonidoDisparo = pygame.mixer.Sound('sonidos/disparo.wav')

	def movimientoDerecha(self):
		self.rect.right += self.velocidad
		self._movimiento()

	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad
		self._movimiento()

	def _movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right > 900:
				self.rect.right = 900

	def disparar(self,x,y):
		# print('Disparo')
		miProyectil = Proyectil(x,y, "images/disparoa.jpg", True)
		self.listaDisparo.append(miProyectil)
		self.sonidoDisparo.play()
		

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)

class Proyectil(pygame.sprite.Sprite):
	def __init__(self, posx, posy, ruta, personaje):
		pygame.sprite.Sprite.__init__(self)

		self.ImageProyectil = pygame.image.load(ruta)
		self.rect= self.ImageProyectil.get_rect()
		self.velocidadDisparo = 5
		self.rect.top = posy
		self.rect.left= posx

		self.disparoPersonaje = personaje

	def trayectoria(self):
		if self.disparoPersonaje == True:
			self.rect.top = self.rect.top - self.velocidadDisparo
		else:
			self.rect.top = self.rect.top + self.velocidadDisparo

	def dibujar(self, superficie):
		superficie.blit(self.ImageProyectil, self.rect)

class Invasor(pygame.sprite.Sprite):
	def __init__(self, posx, posy,): # me quede aquí 15/06/21 curso video 23
		pygame.sprite.Sprite.__init__(self)

		self.ImageA = pygame.image.load('images/MarcianoA.jpg')
		self.ImageB = pygame.image.load('images/MarcianoB.jpg')

		self.listaImages = [self.ImageA, self.ImageB]
		self.posImage = 1

		self.imageInvasor = self.listaImages[self.posImage]
		self.rect= self.imageInvasor.get_rect()

		self.listaDisparo = []
		self.velocidad = 20
		self.rect.top = posy
		self.rect.left= posx

		self.rangoDisparo = 5
		self.tiempoCambio = 1

		self.derecha = True
		self.contador = 0
		self.Maxdescenso = self.rect.top + 40

	def dibujar(self, superficie):
		self.imageInvasor = self.listaImages[self.posImage]
		superficie.blit(self.imageInvasor, self.rect)

	def comportamiento(self, tiempo):
		self._movimientos()
		self._ataque()
		if self.tiempoCambio == tiempo:
			self.posImage += 1
			self.tiempoCambio += 1

			if self.posImage > len(self.listaImages)-1:
				self.posImage = 0

	def _movimientos(self):
		if self.contador < 3:
			self._movimientoLateral()
		else:
			self._descenso()

	def _descenso(self):
		if self.Maxdescenso == self.rect.top:
			self.contador = 0
			self.Maxdescenso = self.rect.top + 40
		else:
			self.rect.top += 1

	def _movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > 900:
				self.derecha = False
				# self.contador += 1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < 0:
				self.derecha = True	
				# self.contador += 1

	def _ataque(self):
		if (randint(0,100)<self.rangoDisparo):
			self._disparo()

	def _disparo(self):
		x,y = self.rect.center
		miProyectil = Proyectil(x,y, "images/disparob.jpg", False)
		self.listaDisparo.append(miProyectil)
	
def SpaceInvader():
	pygame.init()
	ventana = pygame.display.set_mode((ancho,alto))
	pygame.display.set_caption("Space Invader")
	ImagenFondo = pygame.image.load('images/Fondo.jpg')

	pygame.mixer.music.load('sonidos/Intro.mp3')
	pygame.mixer.music.play(5)

	jugador = naveEspacial()
	enemigo = Invasor (100,100)
	enJuego = True

	reloj = pygame.time.Clock()

	while True:
		# jugador.movimiento()
		reloj.tick(30)
		# DemoProyectil.trayectoria()
		tiempo = int(pygame.time.get_ticks()/1000)	

		for evento in pygame.event.get():
			if evento.type ==QUIT:
				pygame.quit()
				sys.exit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT:
						jugador.movimientoIzquierda()

					elif evento.key == K_RIGHT:
						jugador.movimientoDerecha()

					elif evento.key == K_s:
						x,y = jugador.rect.center
						jugador.disparar(x,y)

		ventana.blit(ImagenFondo,(0,0))
		# DemoProyectil.dibujar(ventana)
		enemigo.comportamiento(tiempo)

		jugador.dibujar(ventana)
		enemigo.dibujar(ventana)
		if len(jugador.listaDisparo)>0:
			for x in jugador.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()

				if x.rect.top < 50:
					jugador.listaDisparo.remove(x)

		if len(enemigo.listaDisparo)>0:
			for x in enemigo.listaDisparo:
				x.dibujar(ventana)
				x.trayectoria()

				if x.rect.top > 900:
					enemigo.listaDisparo.remove(x)

		pygame.display.update()

SpaceInvader()