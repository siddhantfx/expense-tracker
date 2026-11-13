# Command-Line Expense Tracker

A lightweight, terminal-based Python application for tracking daily spending. This project was built to practice core programming fundamentals, including interactive loops, dictionary data structures, modular design, and persistent file handling.

## Features
* **Add Expenses:** Log the amount, category, and a brief description of daily purchases.
* **View Summary:** Display a formatted list of all past transactions and calculate the total amount spent.
* **Filter by Category:** Instantly pull up records for specific spending categories (e.g., Food, Transport).
* **Data Persistence:** Automatically saves all entries to a local `.txt` file using pipe-delimited formatting, ensuring data is never lost between sessions.
* **Clear Records:** Securely wipe all past data to start fresh.

## Project Structure
* `main.py`: The entry point of the application. Contains the infinite `while` loop that powers the interactive command-line interface.
* `tracker.py`: The logic module. Houses the functions for writing to the text file, reading data, and calculating totals.
* `expense.txt`: The local database file generated automatically when the first expense is added (ignored by Git to keep personal data private).

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/siddhantfx/expense-tracker.git](https://github.com/siddhantfx/expense-tracker.git)