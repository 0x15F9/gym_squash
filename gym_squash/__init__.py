from gym.envs.registration import register

register(
    id='squash-v0',
    entry_point='gym_squash.envs:SquashEnv',
)