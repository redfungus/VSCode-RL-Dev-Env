"""
Simple example to check if the OpenAI Gym environments are working.
Taken from `https://gym.openai.com/docs/`
"""
import gym


def main():
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample()) # take a random action
    env.close()

if __name__ == '__main__':
    main()