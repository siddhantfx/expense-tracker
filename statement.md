# Problem Statement: Command-Line Expense Tracker

## Background
College students frequently make small, daily transactions for meals, transportation, stationery, and entertainment. However, tracking these expenses manually is tedious, and existing mobile applications are often bloated with ads, require online accounts, or have overly complex interfaces. 

## Objective
To design and develop a lightweight, terminal-based Expense Tracker using Python. The application provides a fast, offline, and distraction-free way to log daily spending, categorize expenses, and monitor financial habits directly from the command line.

## Functional Requirements
The system must support the following operations through an interactive menu:
1. **Add Expense:** Accept user input for expense category, amount, and an optional description, then store it.
2. **View Summary:** Retrieve and display a formatted list of all recorded expenses, alongside a calculated total of all money spent.
3. **Filter by Category:** Allow the user to search for and display only the expenses belonging to a specific category.
4. **Clear Records:** Provide a secure option to permanently wipe all stored data and reset the tracker.

## Technical Specifications
* **Language:** Python 3.x
* **Interface:** Command-Line Interface (CLI) utilizing `while` loops and conditional routing.
* **Data Storage:** Persistent local storage using text file handling (`.txt`).
* **Data Format:** Pipe-delimited string formatting for reliable parsing and data extraction.

## Learning Outcomes
This project serves as a practical application of first-semester programming fundamentals, specifically focusing on:
* Modular programming via custom functions and file imports.
* Persistent file operations (read, write, and append modes).
* Data manipulation using string splitting, type casting, and dictionary mapping.
