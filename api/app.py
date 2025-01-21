from flask import Flask, jsonify, request, make_response
from datetime import datetime
import uuid
import tictactoe.board as board
import tictactoe.player as player

app = Flask(__name__)

# Store game states with session tokens as keys
# TODO: Move this to MongoDB, probably
game_states = {}

@app.route('/move', methods=['POST'])
def move():
    # Get session token from cookie
    session_token = request.cookies.get('session_token')
    if not session_token or session_token not in game_states:
        return jsonify({
            "error": "No active game session found",
            "status": "error"
        }), 401

    # Get move data from request JSON
    data = request.get_json()
    if not data:
        return jsonify({
            "error": "No data provided",
            "status": "error"
        }), 400
        
    # Validate required fields
    required_fields = ['player_name', 'x', 'y']
    if not all(field in data for field in required_fields):
        return jsonify({
            "error": "Missing required fields",
            "status": "error",
            "required_fields": required_fields
        }), 400
    
    #TODO: verify player so they can't cheat :)

    # Validate coordinate types
    try:
        x = int(data['x'])
        y = int(data['y'])
    except ValueError:
        return jsonify({
            "error": "Coordinates must be integers",
            "status": "error"
        }), 400
    
    # Record the move in game state
    try:
        game_states[session_token]["board"].move(x,y,game_states[session_token]["players"][data('player_name')])
    except board.IllegalMoveException as ime:
        return jsonify({
            "error": str(ime),
            "status": "error"
        }), 422

    
    return jsonify({
        "message": "Move recorded",
        "status": "success",
        "move": move_data,
        "game_state": game_states[session_token].board_state_string()
    })

@app.route('/check', methods=['GET'])
def check():
    # Get session token from cookie
    session_token = request.cookies.get('session_token')
    
    if not session_token or session_token not in game_states:
        return jsonify({
            "error": "No active game session found",
            "status": "error"
        }), 401
    
    result = game_states[session_token]["board"].winner()

    return jsonify({
        "message": "Game state checked",
        "status": ("Winner " + repr(result)) if result is not None else "No Winner",
    })

@app.route('/new_game', methods=['POST'])
def new_game():
    # Generate a new session token
    session_token = str(uuid.uuid4())

    # Get move data from request JSON
    data = request.get_json()
    if not data:
        return jsonify({
            "error": "No data provided",
            "status": "error"
        }), 400
        
    # Validate required fields
    required_fields = ['player1_name', 'player2_name']
    if not all(field in data for field in required_fields):
        return jsonify({
            "error": "Missing required fields",
            "status": "error",
            "required_fields": required_fields
        }), 400
   
    # Create new game state, start out just supporting 3x3
    game_states[session_token] = {
        "board": board.Board(),
        "players": {
            data['player1_name']: player.Player(data['player1_name']),
            data['player2_name']: player.Player(data['player2_name'])
        }
    }
    
    # Create response with game state
    response = make_response(jsonify({
        "message": "New game started",
        "status": "success",
        "game_state": game_states[session_token]
    }))
    
    # Set session token as cookie
    response.set_cookie('session_token', session_token, httponly=True)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)