import pygame

class Ball(pygame.Rect):
    
    def __init__(self, velocity, *args, **kwargs):
        # properties of the ball
        self.velocity = velocity
        self.angle = 0
        # properties of the shape of the ball
        super().__init__(*args, **kwargs)

    def move_ball(self):
        """The ball continuously updates its position on the screen based on the parameters
        """
        self.x += self.velocity
        self.y += self.angle
