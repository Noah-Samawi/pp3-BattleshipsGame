# Elements of this code were inspired by Knowledge Mavens on YouTube
# (https://www.youtube.com/watch?v=xz9GrOwQ_5E)
# Code elements were modified for additional functionality.

# imports the inbuilt python random module
import random
# imports google spreadsheet and google credentials APIs
import gspread
from google.oauth2.service_account import Credentials
import os


# Global variables assigned to allow access through Google APIs to gspread.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("user_data")


def main_screen():
    """
    A function to generate the main screen before the game starts.
    ASCII art dashboard and asks player to start game.
    """
    ascii_art = """
     _    _ _____ _     _____ ________  ___ _____   _____ _____
    | |  | |  ___| |   /  __ \\  _  |  \\/  ||  ___| |_   _|  _  |
    | |  | | |__ | |   | /  \\/ | | | .  . || |__     | | | | | |
    | |/\\| |  __|| |   | |   | | | | |\\/| ||  __|    | | | | | |
    \\  /\\  / |___| |___| \\__/\\ \\_/ / |  | || |___    | | \\ \\_/ /
     \\/  \\/\\____/\\_____/\\____/\\___/\\_|  |_|\\____/    \\_/  \\___/

    """
    # ANSI escape code for blue color
    blue_color_code = "\033[94m"
    # ANSI escape code to reset color
    reset_color_code = "\033[0m"
    print(blue_color_code + ascii_art + reset_color_code)

    ascii_art = """
 ___  __    _  _ ______    __ __   ___ _  __    __ _     __
 | |_||_    |_)|_| |  | |  |_ (_ |_| | |_)(_    /__|_||V||_
 | | ||__   |_)| | |  | |__|____)| |_|_|  __)   \\_| |||||__

    """
    # ANSI escape code for blue color
    blue_color_code = "\033[94m"
    # ANSI escape code to reset color
    reset_color_code = "\033[0m"
    print(blue_color_code + ascii_art + reset_color_code)

    ascii_art = """
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \\                                                             /
      \\_______________________________________________WWS_________/

   """
    # ANSI escape code for red color
    red_color_code = "\033[91m"
    # ANSI escape code to reset color
    reset_color_code = "\033[0m"
    print(red_color_code + ascii_art + reset_color_code)


class GameBoard:
    """
    Stores the values needed to generate the game board.
    Dictionary stores letter/number values for co-ordinates.
    Stores values for a board outline for user visuals.
    """

    def __init__(self, board):
        self.board = board

    @staticmethod
    def co_ordinates():
        co_ordinates = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
        }
        return co_ordinates

    def generate_board(self, label):
        print(f"\n{label} Board:")
        print("  A B C D E F G H I ")
        print("  x-x-x-x-x-x-x-x-x ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Warship:
    """
    Class that stores the values needed to generate the ships.
    """

    def __init__(self, board):
        self.board = board

    @staticmethod
    def generate_fleet(board):
        """
        For statement loops through the board co-ordinate lists.
        Generates random integers and assigns 'X' as a ship to each.
        Integers translated into co-ordinates and a ship is placed.
        """

        for i in range(8):
            x_row, y_col = random.randint(0, 8), random.randint(0, 8)
            while board[x_row][y_col] == "X":
                x_row = random.randint(0, 8)
                y_col = random.randint(0, 8)
            board[x_row][y_col] = "X"
        return board

    @staticmethod
    def user_fire_mission():
        """
        Takes the user input and checks for validation.
        Assigns the shot to a co-ordinate and checks for hit/miss/sink.
        Feeds back to user.
        """
        try:
            y_col = input("Enter Co-Ordinate (A-I): ").upper()
            while y_col not in "ABCDEFGHI":
                print("Invalid co-ordinate. Enter a letter A-I.")
                y_col = input("Enter Co-Ordinate (A-I): ").upper()

            x_row = input("Enter Co-Ordinate (1-9): ")
            while x_row not in "123456789":
                print("Invalid co-ordinate. Enter a number 1-9.")
                x_row = input("Enter Co-Ordinate (1-9): ")

            return int(x_row) - 1, GameBoard.co_ordinates()[y_col]

        except ValueError or KeyError:
            print("Not a valid input. Enter a letter or a number.")
            return Warship.user_fire_mission()

    @staticmethod
    def enemy_fire_mission():
        """
        Generates computer shot.
        Takes co-ordinates from a random choice of letters and integers.
        """
        choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        y_col = random.choice(choices).upper()
        x_row = random.randint(0, 8)
        return int(x_row), GameBoard.co_ordinates()[y_col]

    @staticmethod
    def count_damaged_ships(board):
        damaged_ships = 0
        for row in board:
            for column in row:
                if column == "X":
                    damaged_ships += 1
        return damaged_ships


def run_game():
    """
    Main function.
    Generates board and ships.
    Incorporates a turn limit.
    Prompts user for input and provides feedback on turn results.
    """
    enemy_board = [[" "] * 9 for _ in range(9)]
    enemy_target_board = GameBoard([[" "] * 9 for _ in range(9)])
    user_board = [[" "] * 9 for _ in range(9)]
    user_target_board = GameBoard([[" "] * 9 for _ in range(9)])

    Warship.generate_fleet(enemy_board)
    Warship.generate_fleet(user_board)

    missiles = 32
    enemy_missiles = 32

    while missiles > 0:

        enemy_target_board.generate_board("Enemy Target")
        user_target_board.generate_board("User Target")

        user_x_row, user_y_col = Warship.user_fire_mission()
        while (
            user_target_board.board[user_x_row][user_y_col] == "-"
            or user_target_board.board[user_x_row][user_y_col] == "X"
        ):
            print("You have already fired on that location. Choose another.")
            user_x_row, user_y_col = Warship.user_fire_mission()

        if enemy_board[user_x_row][user_y_col] == "X":
            print("Direct hit! Enemy warship sunk!")
            user_target_board.board[user_x_row][user_y_col] = "X"
        else:
            print("Miss. No enemy warship at those co-ordinates.")
            user_target_board.board[user_x_row][user_y_col] = "-"

        if Warship.count_damaged_ships(user_target_board.board) == 8:
            print("Victory! The enemy fleet has been sunk!")
            break
        else:
            missiles -= 1
            print(f"You have {missiles} missiles remaining.")
            if missiles == 0:
                print("We are out of missiles. The enemy fleet has escaped.")

                user_target_board.generate_board("User Target")

        enemy_x_row, enemy_y_col = Warship.enemy_fire_mission()
        while (
            enemy_target_board.board[enemy_x_row][enemy_y_col] == "-"
            or enemy_target_board.board[enemy_x_row][enemy_y_col] == "X"
        ):
            enemy_x_row, enemy_y_col = Warship.enemy_fire_mission()

        if user_board[enemy_x_row][enemy_y_col] == "X":
            print("Direct hit! The enemy has sunk one of our ships!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "X"
        else:
            print("The enemy has missed!")
            enemy_target_board.board[enemy_x_row][enemy_y_col] = "-"

        if Warship.count_damaged_ships(enemy_target_board.board) == 8:
            print("Retreat! The enemy has sunk our fleet!")
            break
        else:
            enemy_missiles -= 1
            if enemy_missiles == 0:
                print("The enemy has run out of missiles.")

                enemy_target_board.generate_board("Enemy Target")

    game_over()


def game_over():
    """
    Runs when all ships sunk.
    Prompts user to restart or exit.
    """
    print("GAME OVER")
    retry = input("Would you like to play again? Y/N: \n").lower()

    if retry == 'y':
        run_game()
    elif retry == 'n':
        print("Thank you Admiral. You are relieved of your command.")
        quit()
    else:
        print("Invalid Input. Type in Y/N.")
        game_over()


def main():
    """
    main function"
    """
    main_screen()
    run_game()


if __name__ == "__main__":
    main()
