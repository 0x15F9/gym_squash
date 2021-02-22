import pygame

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