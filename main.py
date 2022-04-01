import pygame, sys
from paddle import Paddle
from ball import Ball
from collisionManager import CollisionManager
from scoreboard import PlayerScore
from constants import *

# SCREEN
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
screen.fill(BLUE)
pygame.draw.line (screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5 )
pygame.display.set_caption('PONG GAME')


def _draw_board():
    screen.fill( BLUE )
    pygame.draw.line( screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5 )

def _restart():
	_draw_board()
	score1.restart()
	score2.restart()
	ball._restart_pos()
	paddle1._restart_pos()
	paddle2._restart_pos()


# -------
# OBJECTS
# -------

paddle1 = Paddle( screen, RED, 15, HEIGHT//2 - 60, PADDLE_WIDTH, PADDLE_HEIGHT )
paddle2 = Paddle( screen, RED, WIDTH - 20 - 15, HEIGHT//2 - 60, PADDLE_WIDTH, PADDLE_HEIGHT )
ball = Ball( screen, WHITE, WIDTH//2, HEIGHT//2, 12 )
collision = CollisionManager()
score1 = PlayerScore( screen, '0', WIDTH//4, 15 )
score2 = PlayerScore( screen, '0', WIDTH - WIDTH//4, 15 )

# ---------
# VARIABLES
# ---------
playing = False
clock = pygame.time.Clock()

# --------
# MAINLOOP
# --------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and not playing:
				ball._start()
				playing = True

			if event.key == pygame.K_SPACE and playing:
				playing = False

			if event.key == pygame.K_SPACE and not playing:
				playing = True

			if event.key == pygame.K_r and playing:
				_restart()
				playing = False

			if event.key == pygame.K_w:
				paddle1.state = 'up'

			if event.key == pygame.K_s:
				paddle1.state = 'down'

			if event.key == pygame.K_UP:
				paddle2.state = 'up'

			if event.key == pygame.K_DOWN:
				paddle2.state = 'down'

		if event.type == pygame.KEYUP:
			paddle1.state = 'stopped'
			paddle2.state = 'stopped'

	if playing:
		_draw_board()

		# ball
		ball._move()
		ball._draw()

		# paddle 1
		paddle1._move()
		paddle1._clamp()
		paddle1._draw()

		# paddle 2
		paddle2._move()
		paddle2._clamp()
		paddle2._draw()

		# wall collision
		if collision._between_ball_and_walls(ball):
			print('WALL COLLISION')
			ball._wall_collision()

		# paddle1 collision
		if collision._between_ball_and_paddle1(ball, paddle1):
			print('COLLISION WITH PADDLE 1')
			ball._paddle_collision()

		# paddle2 collision
		if collision._between_ball_and_paddle2(ball, paddle2):
			print('COLLISION WITH PADDLE 2')
			ball._paddle_collision()

		# GOAL OF PLAYER 1 !
		if collision._between_ball_and_goal2(ball):
			_draw_board()
			score1.increase()
			ball._restart_pos()
			paddle1._restart_pos()
			paddle2._restart_pos()
			playing = False

		# GOAL OF PLAYER 2!
		if collision._between_ball_and_goal1(ball):
			_draw_board()
			score2.increase()
			ball._restart_pos()
			paddle1._restart_pos()
			paddle2._restart_pos()
			playing = False

	score1.show()
	score2.show()
	if score1.points == 3:
		score1.points == "You won!"
		score1.show()
		score2.show()
		playing = False

	clock.tick(40)
	pygame.display.update()

