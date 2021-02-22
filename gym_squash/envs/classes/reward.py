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
