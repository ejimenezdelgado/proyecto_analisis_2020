
import retro

env = retro.make(game='Airstriker-Genesis', record=True)

env.reset()

done = False

while not done:
    env.render()

    # action = env.action_space.sample()
    action = [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

    ob, rew, done, info = env.step(action)
    print("ob",ob,"Action ", action, "Reward ", rew, "done ", done, "info", info)

if done:
    obs = env.reset()

env.close()