# Global variables assigned to allow access through Google APIs to gspread.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("user_data_sheet")

 """
    Main function.
    Generates board and ships.
    Incorporates a turn limit.
    Prompts user for input and provides feedback on turn results.
    """
    enemy_board = GameBoard([[" "] * 9 for i in range(9)])
    enemy_target_board = GameBoard([[" "] * 9 for i in range(9)])
    user_board = GameBoard([[" "] * 9 for i in range(9)])
    user_target_board = GameBoard([[" "] * 9 for i in range(9)])
    Warship.generate_fleet(enemy_board)
    Warship.generate_fleet(user_board)
    # turn counter
    missiles = 32
    enemy_missiles = 32
    while missiles > 0:
        GameBoard.generate_board(user_target_board)
        GameBoard.generate_board(enemy_target_board)
        # get user input
        user_x_row, user_y_col = Warship.user_fire_mission(object)
        # checks if input is valid
        while (
            user_target_board.board[user_x_row][user_y_col] == "-"
            or user_target_board.board[user_x_row][user_y_col] == "X"
        ):
            print("You have already fired on that location. Choose another.")
            user_x_row, user_y_col = Warship.user_fire_mission(object)
        # check for hit or miss
        if enemy_board.board[user_x_row][user_y_col] == "X":
            print("Direct hit! Enemy warship sunk!")
            user_target_board.board[user_x_row][user_y_col] = "X"
        else:
            print("Miss. No enemy warship at those co-ordinates.")
            user_target_board.board[user_x_row][user_y_col] = "-"
        # check victory condition
        if Warship.count_damaged_ships(user_target_board) == 8:
            print("Victory! The enemy fleet has been sunk!")
            break
        else:
            missiles -= 1
            print(f"You have {missiles} missiles remaining.")
            if missiles == 0:
                print("We are out of missiles. The enemy fleet has escaped.")
                GameBoard.generate_board(user_target_board)
        # get computer input
        enemy_x_row, enemy_y_col = Warship.enemy_fire_mission(object)
        while (
            enemy_target_board.board[enemy_x_row][enemy_y_col] == "-"
            or enemy_target_board.board[enemy_x_row][enemy_y_col] == "X"
        ):
            enemy_x_row, enemy_y_col = Warship.enemy_fire_mission(object)
        # check for computer hit or miss
        if user_board.board[enemy_x_row][enemy_y_col] == "X":
            print("Direct hit! The enemy have sunk one of our ships!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "X"
        else:
            print("The enemy have missed!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "-"
        # check victory condition
        if Warship.count_damaged_ships(enemy_target_board) == 8:
            print("Retreat! The enemy have sunk our fleet!")
            break
        else:
            enemy_missiles -= 1
            if missiles == 0:
                print("The enemy have run out of missiles.")
                GameBoard.generate_board(enemy_target_board)
    game_over()