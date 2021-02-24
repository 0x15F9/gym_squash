import gym
import gym_squash

import sys

import cv2

def random_agent(episodes=1):
    env = gym.make("squash-v0", enable_render=False)
    env.reset()
    env.render()
    for e in range(episodes):
        action = env.action_space.sample()
        state, reward, done, _ = env.step(action)
        # print(reward, end=", ")
        print(state.shape)
        # env.render()
        if done:
            break
        
    cv2.imshow("image", state)
    cv2.waitKey()

if __name__ == '__main__':
    random_agent()
