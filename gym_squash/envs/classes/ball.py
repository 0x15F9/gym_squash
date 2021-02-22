import pygame

class Ball(pygame.Rect):
    def __init__(self, velocity, screen_width, screen_height, *args, **kwargs):
        self.velocity = velocity
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.angle
        self.y += self.velocity
