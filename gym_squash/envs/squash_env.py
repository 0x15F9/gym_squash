import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np
import random
import sys
from enum import Enum

# disable welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from gym_squash.envs.classes.ball import Ball
from gym_squash.envs.classes.paddle import Paddle
from gym_squash.envs.classes.reward import RewardMode
from gym_squash.envs.classes.config import dimensions, ACTION_MEANING

class SquashEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array']
    }
    
    COLOUR = (255, 255, 255)
    
    atari_action_meaning = {
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
      
    action = [
        0, # NOOP
        2, # UP
        5  # DOWN
    ]
    
    # For compatibility with atari games
    def get_action_meanings(self):
        return [self.atari_action_meaning[i] for i in self.action]
    
    def __init__(self, enable_render=False):
        # constants
        self.PADDING = 15
        self.SCREEN_W = 160
        self.SCREEN_H = 210
        self.PADDLE_W = 5
        self.PADDLE_H = 15
        self.BALL_SIZE = 5
        self.TOP = 35
        self.BOTTOM = 195
        
        # pygame 
        self.enable_render = enable_render
        if enable_render:
            pygame.init()
            self.display = pygame.display
            self.screen = self.display.set_mode((self.SCREEN_W, self.SCREEN_H))
            self.clock = pygame.time.Clock()

        # gym attributes
        self.action_space = spaces.Discrete(len(self.action))
        self.observation_space = spaces.Box(
            low=0, high=1, 
            shape=(self.SCREEN_H, self.SCREEN_W, 3),
            dtype=np.uint8
        )
        self.reset()
        
    def reset(self):
        self.score = 0
        self.BALL_V = 5
        self.PADDLE_V = 3

        self.paddle = Paddle(
            self.PADDLE_V,
            self.TOP,
            self.BOTTOM,
            self.SCREEN_W - self.PADDLE_W - self.PADDING,
            (self.SCREEN_H - self.PADDLE_H) / 2,
            self.PADDLE_W,
            self.PADDLE_H
        )

        self.ball = Ball(
            self.BALL_V,
            (self.SCREEN_W - self.BALL_SIZE) / 2,
            (self.SCREEN_H - self.BALL_SIZE) / 2,
            self.BALL_SIZE,
            self.BALL_SIZE
        )

        return self.get_state()
    
    def step(self, action):
        self.paddle.move_paddle(action)
        self.ball.move_ball()
        reward = 0
        done = False
        
        # check for collision
        if self.ball.x <= 0:  # wall collision
            self.ball.velocity = -self.ball.velocity  # mirror motion vertically
            self.ball.angle = random.randint(-self.BALL_V, self.BALL_V) # randomize angle of reflection
        elif self.ball.colliderect(self.paddle): # collision with paddle
            self.ball.velocity = -self.ball.velocity  # mirror motion vertically
            self.ball.angle = random.randint(-self.BALL_V, self.BALL_V) # randomize angle of reflection
            reward = 1
        elif self.ball.y <= self.TOP or self.ball.y + self.BALL_SIZE >= self.BOTTOM: # vertical extremes
            self.ball.angle = -self.ball.angle # mirror motion horizontally
        elif self.ball.x + self.BALL_SIZE > self.paddle.x: # move beyond paddle
            # sys.exit()
            done = True
            
        self.score += reward
        if self.score == 20:
            done = True
        return self.get_state(), reward, done, {"score": self.score, "ball_y": self.ball.y, "paddle_y": self.paddle.y}
    
    def render(self, mode="human", close=False):
        if self.enable_render:
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, self.COLOUR, self.paddle)
            pygame.draw.rect(self.screen, self.COLOUR, self.ball)

            pygame.display.flip()
            self.clock.tick(60)
        else:
            print("Render not enabled")

    def get_state(self):
        surface = pygame.Surface((self.SCREEN_W, self.SCREEN_H))
        pygame.draw.rect(surface, self.COLOUR, self.paddle)
        pygame.draw.rect(surface, self.COLOUR, self.ball)
        # rotated = pygame.transform.rotate(surface, 90)
        return np.swapaxes(pygame.surfarray.array2d(surface), 0, 1)
