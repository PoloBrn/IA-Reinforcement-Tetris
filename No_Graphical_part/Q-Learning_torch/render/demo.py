import time

def run_demo(agent, env, episodes=10):
    agent.epsilon = 0.0  # No exploration during demo (greedy policy)

    for ep in range(episodes):
        done = False
        state = env.reset()
        total_reward = 0

        print(f"\n--- DEMO EPISODE {ep + 1} ---")
        time.sleep(1)

        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            state = next_state
            total_reward += reward

            env.render()
            time.sleep(0.1)

        print(f"Episode {ep + 1} finished with score: {env.score}, total reward: {total_reward}")
        time.sleep(2)  # Pause between episodes

    print("\nDemo session finished.")
