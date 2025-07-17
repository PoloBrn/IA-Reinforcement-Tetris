import numpy as np
from env.tetris_env import TetrisEnv
from agents.dqn_agent import DQNAgent
from train.trainer import train

def main():
    env = TetrisEnv()
    state_dim = env.height * env.width
    action_dim = 4  # left, right, rotate, drop
    agent = DQNAgent(state_dim, action_dim)

    # Step 1: Always train first
    train(agent, env, episodes=30)

    # Step 2: Ask for demo
    choice = input("Do you want to see the AI play after training? (y/n): ").strip().lower()
    if choice in ['y', 'yes']:
        from render.demo import run_demo
        try:
            count = int(input("How many demo games to run? (default: 5): ").strip() or 5)
        except ValueError:
            count = 5
        run_demo(agent, env, episodes=count)
    else:
        print("Training complete. Exiting.")

if __name__ == "__main__":
    main()
