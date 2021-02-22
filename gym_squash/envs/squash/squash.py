import pygame
import random
import sys
from enum import Enum

from ball import Ball
from paddle import Paddle

# Reward Mode
# Collide   +1 on collision with wall
# Tick      +1 per time tick
# NONE      No score
class Mode(Enum):
    COLLIDE = 1
    TICK = 2
    NONE = 3

class Squash:
    HEIGHT = 300
    WIDTH = 240

    PADDLE_WIDTH = 50
    PADDLE_HEIGHT = 10
    PADDING = 10 # some extra space

    BALL_WIDTH = 5
    BALL_VELOCITY = 5
    BALL_ANGLE = 0
    
    PADDLE_VELOCITY = 5

    COLOUR = (255, 255, 255)
    
    SCORE = 0

    def __init__(self, mode=Mode.COLLIDE):
        pygame.init()  # Start the pygame instance.
        self.mode = mode # reward mode

        # Setup the screen
        self.display = pygame.display
        self.screen = self.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        # Create the player objects.
        self.paddles = []
        self.balls = []
        
        top_wall = Paddle(
            0,
            pygame.K_w,
            pygame.K_s,
            True,
            0,
            self.PADDING,
            self.WIDTH,
            10
        )
        
        player_paddle = Paddle(
            self.PADDLE_VELOCITY,
            pygame.K_LEFT,
            pygame.K_RIGHT,
            False,
            (self.WIDTH - self.PADDLE_WIDTH) / 2,
            self.HEIGHT - self.PADDLE_HEIGHT - self.PADDING,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        )
        
        ball = Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        )
        
        self.paddles.append(top_wall)
        self.paddles.append(player_paddle)
        self.balls.append(ball)


    def check_ball_hits_wall(self):
        for ball in self.balls:
            # end condition: ball went past player
            if ball.y > self.HEIGHT - self.PADDLE_HEIGHT - self.PADDING:
                sys.exit(0)

            # on collision with side walls, adjust angle
            if ball.x >= self.WIDTH - self.BALL_WIDTH or ball.x <= 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-self.BALL_VELOCITY, self.BALL_VELOCITY)
                    if paddle.is_wall and self.mode == Mode.COLLIDE:
                        self.SCORE += 1
                        print(self.SCORE)
                    break

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                # Add some extra ways to exit the game.
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.check_ball_hits_paddle()
            self.check_ball_hits_wall()

            # Redraw the screen.
            self.screen.fill((0, 0, 0))

            for paddle in self.paddles:
                paddle.move_paddle(self.WIDTH)
                pygame.draw.rect(self.screen, self.COLOUR, paddle)

            # We know we're not ending the game so lets move the ball here.
            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            pygame.display.flip()
            self.clock.tick(60)
            if self.mode == Mode.TICK:
                self.SCORE += 1
                print(self.SCORE)


if __name__ == '__main__':
    game = Squash()
    game.game_loop()
