import pygame

WIDTH, HEIGHT = 900, 500 # add constants newn files


class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.draw()

    def draw(self):
        pygame.draw.rect( self.screen, self.color, (self.posX, self.posY, self.width, self.height) )


    def move(self):
		# moving up
        if self.state == 'up':
            self.posY -= 10

		# moving down
        elif self.state == 'down':
             self.posY += 10

    def clamp(self):
        if self.posY <= 0:
           self.posY = 0

        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height

    def restart_pos(self):
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self.draw()
