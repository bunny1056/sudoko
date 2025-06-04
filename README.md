# sudoko
# 🔢 Sudoku Solver in Python 🧩

A Python program that solves any valid 9×9 Sudoku puzzle using **recursion** and **backtracking**. This project is built from scratch and requires no external libraries.

---

## 📌 Features

- Input: 9×9 Sudoku grid (use `0` for empty cells)
- Solves using **Backtracking Algorithm**
- Checks for valid placement in:
  - Row
  - Column
  - 3×3 Subgrid
- Clean and readable board output in the console
- No dependencies required – works with pure Python

---

## 🧠 Core Concepts Used

| Concept           | Description                                  |
|-------------------|----------------------------------------------|
| **Backtracking**  | Tries all possible numbers recursively       |
| **Constraint Check** | Ensures Sudoku rules are not violated      |
| **2D Matrix Traversal** | Navigates through empty cells             |
| **Recursion**     | Solves board step-by-step with backtracking |

---

## 🚀 How to Run

1. Clone/download the script:
    ```
    git clone https://github.com/your-username/sudoku-solver.git
    cd sudoku-solver
    ```

2. Run the script with Python:
    ```
    python sudoku_solver.py
    ```

---

## 🧩 Sample Input

```python
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
