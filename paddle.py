import pygame
from constants import *
from actor import Actor


class Paddle (Actor):
    """Solid thing to hit the ball"""
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'
        self._draw()

    def _draw(self):
        """Method to draw a paddle"""
        pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height) )


    def _move(self):
		# moving up
        if self.state == 'up':
            self.posY -= 10

		# moving down
        elif self.state == 'down':
             self.posY += 10

    def _clamp(self):
        if self.posY <= 0:
           self.posY = 0

        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height

    def _restart_pos(self):
	"""Restarts paddle to default position"""
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self._draw()

