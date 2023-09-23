import gspread
from google.oauth2.service_account import Credentials
import time


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('zodiac_sign_app')

# Start the program
print("Your name should start with a capital letter, contain only letters.")
print("No numbers, symbols or spaces, and be no more than 20 characters long.")

while True:
    try:
        username = input("Enter your name: ")

        if not username:
            raise ValueError("Name cannot be empty")

        if " " in username:
            raise ValueError("Name cannot contain spaces")

        if not username.isalpha():
            raise ValueError("Name can only contain letters")

        if len(username) > 20:
            raise ValueError("Name must be 20 characters or less")

        if not username[0].isupper():
            raise ValueError("Name must start with a capital letter")

        break

    except ValueError as e:
        print(e)

print("Welcome to the Zodiac Sign App, " + username + "!")


def style(text, delay=0.008):
    """
    Prints out the given text with a delay between each character.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


style(
    """                                                        
                               88 88                        
                               88 ""                        
                               88                           
888888888  ,adPPYba,   ,adPPYb,88 88 ,adPPYYba,  ,adPPYba,  
     a8P" a8"     "8a a8"    `Y88 88 ""     `Y8 a8"     ""  
  ,d8P'   8b       d8 8b       88 88 ,adPPPPP88 8b          
,d8"      "8a,   ,a8" "8a,   ,d88 88 88,    ,88 "8a,   ,aa  
888888888  `"YbbdP"'   `"8bbdP"Y8 88 `"8bbdP"Y8  `"Ybbd8"'  """
)
