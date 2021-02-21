import pygame

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