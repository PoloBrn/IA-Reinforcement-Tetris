# Project Steps

## Phase 1 — Minimalist Tetris (without AI) — **Completed**
- Created a basic Tetris game engine with:
  - Grid size: 10x15 (reduced height for faster simulation)
  - Standard Tetromino pieces (I, O, T, L, J, S, Z)
  - Left/right movement, rotation, and soft drop (quick fall)
  - Line clearing when a row is fully filled
  - Game over detection when pieces reach the top
  - Interactive terminal controls using arrow keys and spacebar for faster drop
- Objective achieved: a functional and playable Tetris game engine in the terminal

## Phase 2 — Q-Learning Agent Onboarding
- Define a simplified state space for the agent
- Define possible actions the agent can take
- Design a reward function to guide learning
- Implement the Q-Learning algorithm using a Q-table

## Phase 3 — Displaying the AI Playing Tetris
- Add lightweight visualization (e.g., using pygame or a terminal UI with curses)
- Visualize the AI’s gameplay during learning and execution

## Libraries Used
- `numpy`: for matrix and grid management
- `random`: for piece generation
- `keyboard`: for real-time user input in terminal
- (Optionally later) `pygame`: for graphical visualization of the game and AI
- (Optionally later) `matplotlib`: to plot scores and learning progress

---

**Note:**  
We will continue using the terminal interface for now, as it is simple and effective. A graphical interface can be added later if needed.
