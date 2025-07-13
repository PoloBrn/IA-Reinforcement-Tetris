# Project steps
## Phase 1 — Minimalist Tetris (without AI)
- Create a basic version of Tetris:
- Grid 10x20.
- Standard parts (I, O, T, L, J, S, Z).
- Left/right movement, rotation, quick fall.
- Deletion of complete lines.
- Objective: a functional and simulable game engine.

## Phase 2—Q-Learning Agent Onboarding
- Definition of a simplified state space.
- Definition of possible actions.
- Reward function.
- Implementation of the Q-Learning algorithm (table Q).

## Phase 3 — Displaying the AI that is playing
- Added a lightweight graphical user interface (pygame) or console with curses.
- Visualization of the AI during its learning or during execution.

## Libraries used
- pygame: simple display (to visualize Tetris and the AI).
- numpy: matrix processing (states, grid).
- random: random management.

(optionally later: matplotlib to view scores)