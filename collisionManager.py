from constants import *
class CollisionManager:
    #Regulates collision of the ball with paddle and wall
    def _between_ball_and_paddle1(self, ball, paddle):
        ballX = ball.posX
        ballY = ball.posY
        paddleX = paddle.posX
        paddleY = paddle.posY

		# y is in collision area?
        if ballY + ball.radius > paddleY and ballY - ball.radius < paddleY + paddle.height:
			# x is in collision area?
            if ballX - ball.radius <= paddleX + paddle.width:
				# collision
                return True

		# no collision
        return False

    def _between_ball_and_paddle2(self, ball, paddle):
        ballX = ball.posX
        ballY = ball.posY
        paddleX = paddle.posX
        paddleY = paddle.posY

		# y is in collision?
        if ballY + ball.radius > paddleY and ballY - ball.radius < paddleY + paddle.height:
			# x is in collision?
            if ballX + ball.radius >= paddleX:
				# collision
                return True

		# no collision
        return False

    def _between_ball_and_walls(self, ball):
        ballY = ball.posY

		# top collision
        if ballY - ball.radius <= 0:
            return True

		# bottom collision
        if ballY + ball.radius >= HEIGHT:
            return True

		# no collision
        return False

    def _between_ball_and_goal1(self, ball):
        return ball.posX + ball.radius <= 0

    def _between_ball_and_goal2(self, ball):

        return ball.posX - ball.radius >= WIDTH

    


        
        
