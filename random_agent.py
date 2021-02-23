import gym
import gym_squash

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

def random_agent(episodes=150):
    env = gym.make("squash-v0")
    env.reset()
    env.render()
    for e in range(episodes):
        action = env.action_space.sample()
        state, reward, done, _ = env.step(action)
        print(reward, end=", ")
        env.render()
        if done:
            break

if __name__ == '__main__':
    random_agent()
