import pygame

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = -velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self, isHorizontal=True):
        self.x += self.velocity if isHorizontal else self.angle
        self.y += self.angle if isHorizontal else self.velocity
