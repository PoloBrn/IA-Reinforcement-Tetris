import numpy as np
import random
from copy import deepcopy
import os
import time
import keyboard

GRID_WIDTH = 10
GRID_HEIGHT = 15

TETROMINOES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
}

def rotate(piece):
    return [list(row)[::-1] for row in zip(*piece)]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Tetris:
    def __init__(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
        self.score = 0
        self.game_over = False
        self.reset_piece()
        self.drop_speed = 0.5  # normal drop speed (seconds)
        self.last_drop_time = time.time()

    def reset_piece(self):
        self.piece_type = random.choice(list(TETROMINOES.keys()))
        self.piece = TETROMINOES[self.piece_type]
        self.piece_x = GRID_WIDTH // 2 - len(self.piece[0]) // 2
        self.piece_y = 0

        if not self.can_move(0, 0):
            self.game_over = True

    def can_move(self, dx, dy, rotated_piece=None):
        shape = rotated_piece if rotated_piece else self.piece
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    nx = self.piece_x + x + dx
                    ny = self.piece_y + y + dy
                    if nx < 0 or nx >= GRID_WIDTH or ny < 0 or ny >= GRID_HEIGHT:
                        return False
                    if self.grid[ny][nx]:
                        return False
        return True

    def place_piece(self):
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + y][self.piece_x + x] = 1
        self.clear_lines()
        self.reset_piece()

    def clear_lines(self):
        new_grid = [row for row in self.grid if not all(row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        self.score += lines_cleared
        while len(new_grid) < GRID_HEIGHT:
            new_grid.insert(0, np.zeros(GRID_WIDTH, dtype=int))
        self.grid = np.array(new_grid)

    def step(self):
        if self.game_over:
            return

        current_time = time.time()
        # Drop faster if spacebar pressed (soft drop)
        speed = 0.05 if keyboard.is_pressed('space') else self.drop_speed
        
        if current_time - self.last_drop_time >= speed:
            if self.can_move(0, 1):
                self.piece_y += 1
            else:
                self.place_piece()
            self.last_drop_time = current_time

    def move_left(self):
        if self.can_move(-1, 0):
            self.piece_x -= 1

    def move_right(self):
        if self.can_move(1, 0):
            self.piece_x += 1

    def rotate_piece(self):
        rotated = rotate(self.piece)
        if self.can_move(0, 0, rotated):
            self.piece = rotated

    def render(self):
        clear_console()
        display = deepcopy(self.grid)
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    ny, nx = self.piece_y + y, self.piece_x + x
                    if 0 <= ny < GRID_HEIGHT and 0 <= nx < GRID_WIDTH:
                        display[ny][nx] = 2
        for row in display:
            print(''.join(['█' if x == 1 else '▓' if x == 2 else '.' for x in row]))
        print(f"Score: {self.score}")
        if self.game_over:
            print("GAME OVER")

# Game loop with user input handling
game = Tetris()

print("Controls: Left/Right arrows to move, Up arrow to rotate, Spacebar to drop faster, Ctrl+C to quit.")
try:
    while not game.game_over:
        game.render()
        # Check keypresses:
        if keyboard.is_pressed('left'):
            game.move_left()
            time.sleep(0.1)  # debounce for smooth movement
        if keyboard.is_pressed('right'):
            game.move_right()
            time.sleep(0.1)
        if keyboard.is_pressed('up'):
            game.rotate_piece()
            time.sleep(0.2)  # prevent too fast rotation
        game.step()
        time.sleep(0.02)  # small delay to reduce CPU usage
except KeyboardInterrupt:
    print("\nGame interrupted by user.")
    
game.render()
print("Final Score:", game.score)
