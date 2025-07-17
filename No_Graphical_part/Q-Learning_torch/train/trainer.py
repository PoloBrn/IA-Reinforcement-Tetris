import numpy as np

def train(agent, env, episodes=1000, update_target_every=10):
    rewards = []
    for ep in range(episodes):
        state = env.reset()
        state = state.astype(np.float32).flatten()
        done = False
        ep_reward = 0

        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            next_state = next_state.astype(np.float32).flatten()

            agent.remember(state, action, reward, next_state, done)
            agent.train_step()

            state = next_state
            ep_reward += reward

        agent.decay_epsilon()
        if ep % update_target_every == 0:
            agent.update_target_network()
        rewards.append(ep_reward)
        print(f"Episode {ep} - Reward: {ep_reward:.2f} - Epsilon: {agent.epsilon:.3f}")
    return rewards