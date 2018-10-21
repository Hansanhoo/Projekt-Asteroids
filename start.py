import gym
import gym_asteroids

env  = gym.make('asteroids-v01')

env.seed(0)
env.reset()
env.step(0)
