# ✂️ Rock-Paper-Scissors Game (Python)

A modular, command-line implementation of the classic **Rock-Paper-Scissors** game written in Python.

---

## 📌 Project Overview

This project splits game logic into distinct Python modules for clean architecture and maintainability:

- **`ComputerChoice.py`**: Handles random computer selection from a pre-defined list using index-based random generation.
- **`UserChoice.py`**: Manages user input collection, case normalization, and input validation with interactive prompts.
- **`main.py`**: Executes the game flow, evaluates win/draw/loss conditions, and renders visual ASCII art representations of each choice.

---

## 📁 File Structure

```text
├── ComputerChoice.py   # Module for computer move generation
├── UserChoice.py       # Module for user input handling & validation
└── main.py             # Core game engine and ASCII art display
