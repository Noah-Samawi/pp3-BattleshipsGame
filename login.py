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