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
    def __init__(self, velocity, board_width, is_wall, *args, **kwargs):
        self.velocity = velocity
        self.is_wall = is_wall
        self.board_width = board_width
        super().__init__(*args, **kwargs)

    def move_paddle(self, dir):
        if dir == 1:
            if self.x > 0:
                self.x -= self.velocity
        elif dir == 2:
            if self.x + self.width < self.board_width:
                self.x += self.velocity

class SquashEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    COLOUR = (255, 255, 255)
    
    # map to ACTION_MEANING for compatibility with ALE
    actions = [0, 3, 4]
    
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
        
        # gym attributes
        self.state = self.screen
        self.action_space = spaces.Discrete(len(self.actions))

        self.reset()
        pass
    
    def step(self, action):
        self.paddle.move_paddle(action)
            
        return self.state, 0, False, ""
    
    def reset(self):
        self.BALL_V = dimensions['ball_velocity']
        self.PADDLE_V = dimensions['paddle_velocity']
        
        self.paddle = Paddle(
            self.PADDLE_V,
            self.SCREEN_W,
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


ACTION_MEANING = {
    0: "NOOP",
    1: "FIRE",
    2: "UP",
    3: "RIGHT",
    4: "LEFT",
    5: "DOWN",
    6: "UPRIGHT",
    7: "UPLEFT",
    8: "DOWNRIGHT",
    9: "DOWNLEFT",
    10: "UPFIRE",
    11: "RIGHTFIRE",
    12: "LEFTFIRE",
    13: "DOWNFIRE",
    14: "UPRIGHTFIRE",
    15: "UPLEFTFIRE",
    16: "DOWNRIGHTFIRE",
    17: "DOWNLEFTFIRE",
}
