dimensions = {
    # screen
    'screen_width': 160,
    'screen_height': 210,
    # paddle
    'paddle_width': 5,
    'paddle_height': 15,
    'paddle_velocity': 5,
    'top': 34,
    'bottom': 194,
    # ball
    'ball_size': 5,
    'ball_velocity': 7, # set ball v > paddle v to allow losing
    # misc.
    'padding': 15
}

ACTION_MEANING = {
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
