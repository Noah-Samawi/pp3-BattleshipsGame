# imports the inbuilt python random module
import random

# imports google spreadhseet and google credentials APIs
 import gspread 
from google.oauth2.service_account import Credentials

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
# spreadsheet_ID = "1yxioI50CWpBggKnJvuZIBQLjkqSvaTdJQZ0VcVH4a0Y

def login() -> str:
    """
    Asks user if they're a new or existing user.
    Asks new users to create login details.
    Checks if existing users have correct information.
    """
    while True:
        print("===================================")
        print("Welcome to the Naval Defence System")
        print("===================================")
        new_old = input("Are you a new user? Y/N \n").lower()

        if str(new_old) == "y":
            new_user()
        elif str(new_old) == "n":
            old_user()

        if check_login(new_old):
            break
    return new_old


def check_login(new_old: str):
    """
    Checks user input is acceptable.
    Raises ValueError if not.
    @param new_old(str): user input from the login.
    """
    try:
        str(new_old)
        if new_old not in {"y", "n"}:
            raise ValueError("Invalid Input.")
    except ValueError as e:
        print(f"{e} Please type in Y or N.")
        return False

    return True