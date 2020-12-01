import time

import retro

env = retro.make(game='SuperMarioBros-Nes', record=True)
print(env.action_space)
env.reset()

done = False

while not done:
    env.render()

    #action = env.action_space.sample()
    #print(action)
    action = [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

    ob, rew, done, info = env.step(action)
    print("ob",ob,"Action ", action, "Reward ", rew, "done ", done, "info", info)
    time.sleep(1)

    if done:
        obs = env.reset()

env.close()