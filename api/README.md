# Flask Tic-Tac-Toe and Friends Game Session Manager

A simple Flask application that manages game sessions using cookies.

## Prerequisites

- Python 3.x
- Make

## Project Setup

This project uses a Makefile to manage the Python virtual environment setup. Here's how to get started:

### Creating the Virtual Environment

To create a new virtual environment and install all required dependencies:

```bash
make venv
```

This command will:
1. Create a new virtual environment in the `venv` directory
2. Install all dependencies listed in `requirements.txt`

### Cleaning Up

To remove the virtual environment and start fresh:

```bash
make clean
```

## Running the Application

After setting up the virtual environment, you can run the Flask application:

```bash
# Activate the virtual environment
source venv/bin/activate  # On Unix/MacOS
# OR
.\venv\Scripts\activate   # On Windows

# Run the Flask application
python app.py
```

The server will start on `http://localhost:5000` by default.

## API Endpoints

The application provides three endpoints:

- `POST /new_game`: Starts a new game session and returns a session cookie
- `GET /check`: Checks the current game state using the session cookie
- `GET /move`: Makes a move in the current game using the session cookie

Each endpoint requires a valid session cookie to work (except `/new_game` which creates the session).

## TODO
- Implement MongoDB instead of inmemory state for the games, would require tictactoe to implement json serialization of players and the board, probably as a passthrough from the inmemory state, implementing some cache sharing so that the server can be pushed into an HA environment (decentralized).

## Project Structure

```
api/
  ├── app.py              # Flask application
  ├── requirements.txt    # Python dependencies
  ├── Makefile           # Build automation
  └── README.md          # This file
```
