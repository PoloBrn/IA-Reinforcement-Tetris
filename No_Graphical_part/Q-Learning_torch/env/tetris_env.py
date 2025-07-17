import os
import numpy as np
import random
from copy import deepcopy
from .tetrominoes import TETROMINOES

class TetrisEnv:
    def __init__(self, height=20, width=10):
        self.height = height
        self.width = width
        self.reset()

    def reset(self):
        self.grid = np.zeros((self.height, self.width), dtype=int)
        self.score = 0
        self.game_over = False
        self.new_piece()
        return self._get_observation()

    def new_piece(self):
        self.piece_type = random.choice(list(TETROMINOES.keys()))
        self.piece = TETROMINOES[self.piece_type]
        self.piece_x = self.width // 2 - len(self.piece[0]) // 2
        self.piece_y = 0
        if not self._can_place(self.piece_x, self.piece_y, self.piece):
            self.game_over = True

    def _can_place(self, x, y, shape):
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    nx, ny = x + j, y + i
                    if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                        return False
                    if self.grid[ny][nx] != 0:
                        return False
        return True

    def _lock_piece(self):
        for i, row in enumerate(self.piece):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + i][self.piece_x + j] = 1
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        new_grid = [row for row in self.grid if not all(row)]
        lines_cleared = self.height - len(new_grid)
        self.score += lines_cleared
        while len(new_grid) < self.height:
            new_grid.insert(0, np.zeros(self.width))
        self.grid = np.array(new_grid)

    def step(self, action):
        if self.game_over:
            return self._get_observation(), 0, True

        moved = False
        if action == 0:  # left
            if self._can_place(self.piece_x - 1, self.piece_y, self.piece):
                self.piece_x -= 1
                moved = True
        elif action == 1:  # right
            if self._can_place(self.piece_x + 1, self.piece_y, self.piece):
                self.piece_x += 1
                moved = True
        elif action == 2:  # rotate
            rotated = np.rot90(self.piece, -1)
            if self._can_place(self.piece_x, self.piece_y, rotated):
                self.piece = rotated
                moved = True
        elif action == 3:  # drop
            while self._can_place(self.piece_x, self.piece_y + 1, self.piece):
                self.piece_y += 1
            self._lock_piece()
            return self._get_observation(), 1, self.game_over

        if self._can_place(self.piece_x, self.piece_y + 1, self.piece):
            self.piece_y += 1
        else:
            self._lock_piece()

        return self._get_observation(), int(moved), self.game_over

    def _get_observation(self):
        grid_copy = deepcopy(self.grid)
        for i, row in enumerate(self.piece):
            for j, cell in enumerate(row):
                if cell:
                    y, x = self.piece_y + i, self.piece_x + j
                    if 0 <= y < self.height and 0 <= x < self.width:
                        grid_copy[y][x] = 2
        return grid_copy
    
    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid = deepcopy(self.grid)

        # Show the active piece in the grid
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    ny = self.piece_y + y
                    nx = self.piece_x + x
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        grid[ny][nx] = 2

        for row in grid:
            print("".join(['█' if cell == 1 else '▓' if cell == 2 else '.' for cell in row]))
        print(f"Score: {self.score}")
        if self.game_over:
            print("GAME OVER")
