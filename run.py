import gspread
from google.oauth2.service_account import Credentials
import time
from descriptions import descriptions
from predictions import horoscope_predictions
from compatibility import zodiac_compatibility
from colorama import Fore
import random


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
888888888  ,adPPYba,   ,adPPYb,88 88 ,adPPYYba,  ,adPPYba
     a8P" a8"     "8a a8"    `Y88 88 ""     `Y8 a8"     ""
  ,d8P'   8b       d8 8b       88 88 ,adPPPPP88 8b          
,d8"      "8a,   ,a8" "8a,   ,d88 88 88,    ,88 "8a,   ,aa  
888888888  `"YbbdP"'   `"8bbdP"Y8 88 `"8bbdP"Y8  `"Ybbd8"'  
"""
)


def show_compatability(user_sign, match_sign):
    """
    Prints compatibility between two zodiac signs.
    Checks if the match sign is in the first 3 or last compatible signs.
    Prints out a compatibility percentage and statement.
    """
    user_compat = zodiac_compatibility[user_sign]

    if match_sign in user_compat[:3]:
        compatability_rate_one = random.randint(70, 100)
        print(Fore.BLUE + f"{user_sign} is very compatible with {match_sign}!")
        print(Fore.BLUE + f"Your compatibility rate:{compatability_rate_one}%")
    elif match_sign in user_compat[3:]:
        compatability_rate_two = random.randint(50, 69)
        print(Fore.BLUE + f"{user_sign} is compatible with {match_sign}!")
        print(Fore.BLUE + f"Your compatibility rate:{compatability_rate_two}%")
    else:
        print(Fore.BLUE + f"{match_sign} is not compatible with {user_sign}.")

