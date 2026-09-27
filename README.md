# Library Management System

## Overview
A menu-driven Python Library Management System developed using lists, dictionaries, functions, modular programming, file storage, validation, and testing.

## Features
- Add, display, search, update, and remove books
- Add, display, and remove library members
- Issue and return books
- Maintain transaction history
- Generate library reports
- Save data permanently in JSON format
- Input validation and error handling
- Basic automated tests

## Technologies
- Python 3
- Lists
- Dictionaries
- Functions
- JSON file handling
- unittest
- Git/GitHub

## Project Structure
- `main.py` - main menu and program workflow
- `book_manager.py` - book operations
- `member_manager.py` - member operations
- `transaction_manager.py` - issue/return operations
- `storage.py` - JSON data storage
- `validators.py` - input validation and common search functions
- `reports.py` - library reports
- `tests/test_library.py` - validation tests
- `statement.md` - problem statement and scope
- `design.md` - architecture and design diagrams

## How to Run
1. Install Python 3.
2. Keep all project files in the same folder.
3. Run:
   `python main.py`

The program automatically creates `library_data.json` for data storage.

## Testing
Run:
`python -m unittest discover -s tests`

## Non-Functional Requirements
1. Usability: menu-driven and simple text interface.
2. Reliability: invalid input is handled and data is saved after changes.
3. Maintainability: functionality is separated into modules.
4. Resource efficiency: the system uses lightweight lists, dictionaries, and JSON storage.

## Version Control
The project should be uploaded to a GitHub repository with regular commits showing development progress.
