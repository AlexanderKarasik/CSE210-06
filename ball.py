import pygame
from constants import *

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.dx = 0
        self.dy = 0
        self.radius = radius
        self._draw()
	
		
    def _draw(self):
        pygame.draw.circle( self.screen, self.color, (self.posX, self.posY), self.radius )

    def _start(self):
		# this will be random
        self.dx = 15
        self.dy = 5

    def _move(self):
        self.posX += self.dx
        self.posY += self.dy

    def _wall_collision(self):
        self.dy = -self.dy

    def _paddle_collision(self):
        self.dx = -self.dx

    def _restart_pos(self):
        self.posX = WIDTH//2
        self.posY = HEIGHT//2
        self.dx = 0
        self.dy = 0
        self._draw()
