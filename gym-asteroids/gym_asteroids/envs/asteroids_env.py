import gym
from gym import error, spaces, utils
from gym.utils import seeding

class AsteroidsEnv(gym.Env):
  metadata = {'render.modes': ['human']}


  def __init__(self):
        self.__version__ = "0.1.0"


        # General variables defining the environment
        self.MAX_PRICE = 2.0
        self.TOTAL_TIME_STEPS = 2

        self.curr_step = -1
        self.alive = True;


        # Store what the agent tried
        self.curr_episode = -1
        self.action_episode_memory = []

  def step(self, action):
      self.curr_step += 1
      ob = self._get_state()
      reward = self._get_reward()
      episode_over = False
      return ob,reward,episode_over,{}
          #    Parameters
          #    ----------
          #    action :

          #    Returns
          #    -------
          #    ob, reward, episode_over, info : tuple
          #        ob (object) :
          #            an environment-specific object representing your observation of
          #            the environment.
          #        reward (float) :
          #            amount of reward achieved by the previous action. The scale
          #            varies between environments, but the goal is always to increase
          #            your total reward.
          #        episode_over (bool) :
          #            whether it's time to reset the environment again. Most (but not
          #            all) tasks are divided up into well-defined episodes, and done
          #            being True indicates the episode has terminated. (For example,
          #            perhaps the pole tipped too far, or you lost your last life.)
          #        info (dict) :
          #             diagnostic information useful for debugging. It can sometimes
          #             be useful for learning (for example, it might contain the raw
          #             probabilities behind the environment's last state change).
          #             However, official evaluations of your agent are not allowed to
          #             use this for learning.
      #
  def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        # Derive a random seed. This gets passed as a uint, but gets
        # checked as an int elsewhere, so we need to keep it below
        # 2**31.
        seed2 = seeding.hash_seed(seed1 + 1) % 2**31


        return [seed1, seed2]

  def _get_state(self):
      """Get the observation."""
      ob = [self.TOTAL_TIME_STEPS - self.curr_step]
      return ob

  def _get_reward(self):
      if(self.alive):
          return 1
      else:
          return 0

  def reset(self):
        self.curr_episode += 1
        self.action_episode_memory.append([])
        self.alive = True
            
        return self._get_state()
