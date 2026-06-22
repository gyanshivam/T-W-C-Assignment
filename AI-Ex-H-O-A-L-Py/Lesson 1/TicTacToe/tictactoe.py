"""
Tic‑Tac‑Toe with a Basic AI Opponent
No external libraries required.
"""

import random

def print_board(board):
    """Display the current board."""
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_win(board, player):
    """Return True if player has three in a row."""
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def is_full(board):
    """Return True if board is full (no empty spaces)."""
    return all(cell in ['X', 'O'] for cell in board)

def get_empty_positions(board):
    """Return list of indices of empty cells (where cell is a digit)."""
    return [i for i, cell in enumerate(board) if cell not in ['X', 'O']]

def player_move(board):
    """Get valid move from human player."""
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Position out of range. Please enter 1-9.")
            elif board[move] in ['X', 'O']:
                print("That spot is already taken. Choose another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board, ai_symbol, human_symbol):
    """
    AI move with priority:
    1. Win if possible
    2. Block human win
    3. Take center (index 4)
    4. Take a corner (0,2,6,8)
    5. Take any empty edge
    """
    empty = get_empty_positions(board)
    
    # 1. Win
    for pos in empty:
        board_copy = board[:]
        board_copy[pos] = ai_symbol
        if check_win(board_copy, ai_symbol):
            return pos
    
    # 2. Block human win
    for pos in empty:
        board_copy = board[:]
        board_copy[pos] = human_symbol
        if check_win(board_copy, human_symbol):
            return pos
    
    # 3. Center
    if 4 in empty:
        return 4
    
    # 4. Corners
    corners = [0, 2, 6, 8]
    available_corners = [c for c in corners if c in empty]
    if available_corners:
        return random.choice(available_corners)
    
    # 5. Any edge (1,3,5,7)
    edges = [1, 3, 5, 7]
    available_edges = [e for e in edges if e in empty]
    if available_edges:
        return random.choice(available_edges)
    
    # Fallback (should never happen)
    return random.choice(empty)

def play_game():
    """Main game loop."""
    print("=" * 40)
    print("     TIC TAC TOE - Against Coding_Ultron")
    print("=" * 40)
    name = input("Enter your name: ").strip() or "Player"
    
    # Choose symbol
    while True:
        choice = input(f"{name}, do you want to be X or O? ").upper()
        if choice in ['X', 'O']:
            break
        print("Please enter X or O.")
    
    human_symbol = choice
    ai_symbol = 'O' if human_symbol == 'X' else 'X'
    print(f"\nYou are {human_symbol}. AI is {ai_symbol}.\n")
    
    # Randomise who goes first?
    first = random.choice(['human', 'ai'])
    print(f"{'You' if first == 'human' else 'AI'} will start first.\n")
    
    board = [str(i+1) for i in range(9)]  # initial positions 1-9
    game_over = False
    
    while not game_over:
        print_board(board)
        
        if first == 'human':
            # Human turn
            move = player_move(board)
            board[move] = human_symbol
            if check_win(board, human_symbol):
                print_board(board)
                print(f"🎉 Congratulations {name}! You won! 🎉")
                game_over = True
            elif is_full(board):
                print_board(board)
                print("It's a tie! 🤝")
                game_over = True
            else:
                first = 'ai'
        else:
            # AI turn
            print("AI is thinking...")
            move = ai_move(board, ai_symbol, human_symbol)
            board[move] = ai_symbol
            print(f"AI places {ai_symbol} at position {move+1}.")
            if check_win(board, ai_symbol):
                print_board(board)
                print("🤖 AI wins! Better luck next time. 🤖")
                game_over = True
            elif is_full(board):
                print_board(board)
                print("It's a tie! 🤝")
                game_over = True
            else:
                first = 'human'
    
    # Play again?
    again = input("\nPlay again? (yes/no): ").lower()
    if again in ['yes', 'y']:
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_game()