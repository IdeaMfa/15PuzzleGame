import tkinter as tk
from gui import PuzzleGUI

if __name__ == "__main__":
    root = tk.Tk()

    try: # Set window icon
        root.iconbitmap('game_icon.ico')
    except:
        pass

    app = PuzzleGUI(root)
    root.mainloop()