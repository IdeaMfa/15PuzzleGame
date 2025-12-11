# 15 Puzzle Game (MVP)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Status](https://img.shields.io/badge/status-MVP-orange) ![Python](https://img.shields.io/badge/python-3.x-yellow)

A classic 15-puzzle game built with Python and Tkinter.

**This project is currently in the MVP (Minimum Viable Product) stage.** It serves as the foundation for a larger project exploring Artificial Intelligence search algorithms (inspired by the CS50 AI curriculum).

## 🎯 Motivation
I built this application to bridge the gap between software engineering and AI theory. My primary goal is to create a visualization environment where I can implement and test various search algorithms (like **BFS, DFS, and A\***) to solve the puzzle automatically.

While the current version is a playable game for humans, the next phase of development will focus on the "Solver" engine.

## 🚀 Features
### Current (v1.0 - MVP)
- **Playable Interface:** Smooth tile movements using a Tkinter GUI.
- **Solvability Check:** Implements mathematical parity logic to ensure every generated board is solvable (invariant analysis).
- **Windows Installer:** Fully packaged `.exe` installer for easy distribution.

### 🗺️ Roadmap & Future Features
- [ ] **AI Solver:** Implementation of A* (A-Star) search to auto-solve the board.
- [ ] **Game Loop:** Main Menu, Restart Button, and Victory Screen.
- [ ] **Stats & History:** Tracking move counts and solution efficiency.
- [ ] **Heuristic Visualizer:** Visualizing how the AI "thinks" (Manhattan Distance vs. Misplaced Tiles).

## 📥 How to Download & Install
You don't need Python installed to play the game. I have packaged it as a standard Windows Installer.

1.  Go to the **[Releases Page](../../releases/latest)** of this repository.
2.  Download the file named **`15PuzzleInstaller.exe`**.
3.  Run the installer and follow the setup wizard.
4.  Launch the game from your Desktop shortcut!

## 🛠️ Technical Stack
- **Language:** Python 3
- **GUI:** Tkinter
- **Packaging:** PyInstaller (Binary generation) & Inno Setup (Windows Installer)
- **Version Control:** Git & GitHub

## 🧩 The Math Behind the Solvability
Not all 15-puzzle configurations are solvable. This engine includes a validation layer that calculates the **inversion count** and the **blank tile position**.
> If the grid width is even, and the blank is on an even row counting from the bottom, then the number of inversions must be odd.

This ensures users never face an impossible board.

---
*Developed by IdeaMfa (Fatih Aytar). Feedback is welcome!*