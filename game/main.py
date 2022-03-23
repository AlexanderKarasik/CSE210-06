from paddle import Paddle
from ball import Ball
from collisioManager import CollisionManager
from scoreboard import PlayerScore

# ---------
# CONSTANTS
# ---------
WIDTH, HEIGHT = 900, 500 # add constants within of a new file
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# SCREEN
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('PONG')


def draw_board():
    screen.fill( BLACK )
    pygame.draw.line( screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5 )

def restart():
	draw_board()
	score1.restart()
	score2.restart()
	ball.restart_pos()
	paddle1.restart_pos()
	paddle2.restart_pos()


# -------
# OBJECTS
# -------

paddle1 = Paddle( screen, WHITE, 15, HEIGHT//2 - 60, 20, 120 )
paddle2 = Paddle( screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120 )
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
			if event.key == pygame.K_p and not playing:
				ball.start()
				playing = True

			if event.key == pygame.K_r and playing:
				restart()
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
		draw_board()

		# ball
		ball.move()
		ball.draw()

		# paddle 1
		paddle1.move()
		paddle1.clamp()
		paddle1.draw()

		# paddle 2
		paddle2.move()
		paddle2.clamp()
		paddle2.draw()

		# wall collision
		if collision.between_ball_and_walls(ball):
			print('WALL COLLISION')
			ball.wall_collision()

		# paddle1 collision
		if collision.between_ball_and_paddle1(ball, paddle1):
			print('COLLISION WITH PADDLE 1')
			ball.paddle_collision()

		# paddle2 collision
		if collision.between_ball_and_paddle2(ball, paddle2):
			print('COLLISION WITH PADDLE 2')
			ball.paddle_collision()

		# GOAL OF PLAYER 1 !
		if collision.between_ball_and_goal2(ball):
			draw_board()
			score1.increase()
			ball.restart_pos()
			paddle1.restart_pos()
			paddle2.restart_pos()
			playing = False

		# GOAL OF PLAYER 2!
		if collision.between_ball_and_goal1(ball):
			draw_board()
			score2.increase()
			ball.restart_pos()
			paddle1.restart_pos()
			paddle2.restart_pos()
			playing = False

	score1.show()
	score2.show()

	clock.tick(40)
	pygame.display.update()
