import gym
import gym_squash

import sys

import cv2
import matplotlib.pyplot as plt

def random_agent(episodes=1000):
    env = gym.make("squash-v0", enable_render=False)
    state = env.reset()
    env.render()
    
    bally, paddley = 0, 0
    for e in range(episodes):
        action = 1 if paddley>bally else 2
        state, reward, done, info = env.step(action)
        paddley = info["paddle_y"]
        bally = info["ball_y"]
        # print(e, reward, end=", ")
        # print(state.shape)
        # env.render()
        if done:
            print(e, done)
            break
    print(state.shape)
    plt.imshow(state)
    plt.show()
    # cv2.imshow("image", state)
    # cv2.waitKey()

if __name__ == '__main__':
    random_agent()
