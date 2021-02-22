import gym
from gym import error, spaces, utils
from gym.utils import seeding

import pygame
import random
import sys
from enum import Enum

class RewardMode(Enum):

    """Reward Mode
    
    - Collide   +1 on collision with wall
    - Tick      +1 per time tick
    - NONE      No score
    """
    COLLIDE = 1
    TICK = 2
    NONE = 3


dimensions = {
    # screen
    'screen_width': 300,
    'screen_height': 240,
    # paddle
    'paddle_width': 50,
    'paddle_height': 10,
    'paddle_velocity': 5,
    # ball
    'ball_size': 5,
    'ball_velocity': 5,
    # misc.
    'padding': 10
}


class Paddle(pygame.Rect):
    def __init__(self, velocity, left_key, right_key, is_wall, *args, **kwargs):
        self.velocity = velocity
        self.left_key = left_key
        self.right_key = right_key
        self.is_wall = is_wall
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_width):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.left_key]:
            if self.x > 0:
                self.x -= self.velocity

        if keys_pressed[self.right_key]:
            if self.x + self.width < board_width:
                self.x += self.velocity

class SquashEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    COLOUR = (255, 255, 255)
    
    def __init__(self, reward_mode=RewardMode.COLLIDE):
        # constants
        self.PADDING = dimensions['padding']
        self.SCREEN_W = dimensions['screen_width']
        self.SCREEN_H = dimensions['screen_height']
        self.PADDLE_W = dimensions['paddle_width']
        self.PADDLE_H = dimensions['paddle_height']
        self.BALL_SIZE = dimensions['ball_size']

        # 
        pygame.init()
        self.reward_mode = reward_mode
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.clock = pygame.time.Clock()

        self.reset()
        pass
    
    def step(self, action):
        pass
    
    
    def reset(self):
        self.BALL_V = dimensions['ball_velocity']
        self.PADDLE_V = dimensions['paddle_velocity']
        
        self.paddle = Paddle(
            self.PADDLE_V,
            pygame.K_LEFT,
            pygame.K_RIGHT,
            False,
            (self.SCREEN_W - self.PADDLE_W) / 2,
            self.SCREEN_H - self.PADDLE_H - self.PADDING,
            self.PADDLE_W,
            self.PADDLE_H
        )

    
    def render(self, mode="human", close=False):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, self.COLOUR, self.paddle)

        pygame.display.flip()
        self.clock.tick(60)
