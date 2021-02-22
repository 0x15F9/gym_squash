import gym
from gym import error, spaces, utils
from gym.utils import seeding

import pygame
import random
import sys
from enum import Enum

from gym_squash.envs.classes.ball import Ball
from gym_squash.envs.classes.paddle import Paddle
from gym_squash.envs.classes.reward import RewardMode
from gym_squash.envs.classes.config import dimensions, ACTION_MEANING

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
        self.ball.move_ball()
        reward = 0
        done = False
        
        # check for collision
        if self.ball.y <= 0:  # vertical extremes
            self.ball.velocity = -self.ball.velocity  # mirror motion vertically
            self.ball.angle = random.randint(-self.BALL_V, self.BALL_V) # randomize angle of reflection
        elif self.ball.colliderect(self.paddle): # collision with paddle
            self.ball.velocity = -self.ball.velocity  # mirror motion vertically
            self.ball.angle = random.randint(-self.BALL_V, self.BALL_V) # randomize angle of reflection
            if self.reward_mode == RewardMode.COLLIDE:
                reward = 1
        elif self.ball.x <= 0 or self.ball.x + self.BALL_SIZE >= self.SCREEN_W: # side walls
            self.ball.angle = -self.ball.angle # mirror motion horizontally
        elif self.ball.y + self.BALL_SIZE > self.paddle.y: # move beyond paddle
            sys.exit()
            done = True
            
        self.score += reward
        return self.state, reward, done, ""
    
    def reset(self):
        self.score = 0
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
        
        self.ball = Ball(
            self.BALL_V, self.SCREEN_W, 
            self.SCREEN_H - self.PADDLE_H - self.PADDING,
            self.SCREEN_W / 2 - self.BALL_SIZE / 2,
            self.SCREEN_H / 2 - self.BALL_SIZE / 2,
            self.BALL_SIZE,
            self.BALL_SIZE
        )

    
    def render(self, mode="human", close=False):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, self.COLOUR, self.paddle)
        pygame.draw.rect(self.screen, self.COLOUR, self.ball)

        pygame.display.flip()
        self.clock.tick(60)
