from gym.envs.registration import register

register(
    id='asteroids-v01',
    entry_point='gym_asteroids.envs.asteroids_env:AsteroidsEnv',
)
