import pygame

class Paddle(pygame.Rect):
    def __init__(self, velocity, left_key, right_key, *args, **kwargs):
        # set properties of paddle
        self.velocity = velocity
        self.left_key = left_key
        self.right_key = right_key
        # set properties of shape of paddle
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_width):
        keys_pressed = pygame.key.get_pressed()

        # move left if not on leftmost extremity
        if keys_pressed[self.left_key]:
            if self.x - self.velocity > 0:
                self.x -= self.velocity

        # move right if not on rightmost extremity
        if keys_pressed[self.right_key]:
            if self.x + self.velocity < board_width - self.width:
                self.x += self.velocity
    
