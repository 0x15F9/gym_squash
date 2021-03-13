import pygame

class Paddle(pygame.Rect):
    def __init__(self, velocity, screen_top, screen_bottom, *args, **kwargs):
        self.velocity = velocity
        self.screen_top = screen_top
        self.screen_bottom = screen_bottom
        super().__init__(*args, **kwargs)

    def move_paddle(self, dir):
        # 1 is up, 2 is down
        if dir == 1:
            if self.top > self.screen_top: # if rect top < screen_top
                self.y -= self.velocity
        elif dir == 2:
            if self.y + self.height < self.screen_bottom:
                self.y += self.velocity
