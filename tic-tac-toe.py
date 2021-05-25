board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "       1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "       4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "       7 | 8 | 9")

# The game is going on
game_is_going = True

# The constant winner is None that's because winner is never confirmed before the game.
winner = None

current_player = "X"

# -------------------- THe skeletal model ------------------
def play_game():
    global winner

    # Displays the initial board
    display_board()

    while game_is_going:
        handle_turns(current_player)
        check_for_game_over()
        flip_players()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")

# -------------------- Handling Turns of single arbitrary player ------------------
def handle_turns(player):
    global winner

    print(f"{player}'s turn")
    position = input("Enter the position between 1-9: ")

    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8",'9']:
            position = input("Invalid Input. Enter a position between 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go in there")

        board[position] = player

        # Displays the updated board after every single move by the player
        display_board()


# -------------------- Checks the status, whether it is a win or a tie ----------------
def check_for_game_over():
    check_for_winner()
    check_for_tie()

def flip_players():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

# --------------------- Checking for rows -----------------
def check_rows():
    global winner
    global game_is_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

# ------------------ Checking for columns -------------------
def check_columns():
    global winner
    global game_is_going

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_is_going = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None

# ------------------- Checking for diagonals ---------------------
def check_diagonals():
    global winner
    global game_is_going

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_is_going = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[3]
    else:
        return None

# -------------------- Checking for winner --------------------
def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# ------------------- Checking whether it's a tie or not -----------------
def check_for_tie():
    global game_is_going

    if "-" not in board:
        game_is_going = False
        return True
    else:
        return False

play_game()