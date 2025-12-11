import tkinter as tk

from tkinter import messagebox
from game_engine import FifteenPuzzle

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("15 Puzzle Game")

        # 1. Initialize the backend
        self.game = FifteenPuzzle()

        # 2. Define the view buttons
        self.buttons = []
        self.create_widgets()

        # 3. Initial update to show the board
        self.update_ui()

    def create_widgets(self):
        # Create a 4x4 (NxN) grid of buttons
        for i in range(self.game.BOARD_SIZE ** 2):
            btn = tk.Button(self.root, text=str(i), font=("Arial", 20), width=5, height=2,
                            command=lambda idx=i: self.on_button_click(idx))
        
            # Grid layout
            row = i // 4
            col = i % 4
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

    def on_button_click(self, index):
        # 1. Call Backend
        success, updated_board = self.game.turn(index)

        # 2. Update view if move was valid
        if success:
            self.update_ui()
            if self.game.is_over:
                messagebox.showinfo("Victory", "You solved the puzzle!")

    def update_ui(self):
        current_board = self.game.board
        for i in range(self.game.BOARD_SIZE ** 2):
            tile_value = current_board[i]
            if tile_value == 0:
                self.buttons[i].config(text="", bg="lightgray", state="disabled", relief="sunken")
            elif tile_value == self.game.GOAL_STATE[i]:
                self.buttons[i].config(text=str(tile_value), bg="lightgreen", state="normal", relief="raised")
            else:
                self.buttons[i].config(text=str(tile_value), bg="white", state="normal", relief="raised")
