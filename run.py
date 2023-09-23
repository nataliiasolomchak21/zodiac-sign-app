import gspread
from google.oauth2.service_account import Credentials
import time
from signs import get_zodiac_sign
from descriptions import descriptions
from predictions import horoscope_predictions
from compatibility import zodiac_compatibility
from colorama import Fore
import random
from datetime import date

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


def show_prediction(sign_predictions):
    """
    Prints horoscope predictions for the given zodiac sign.
    """
    for prediction in horoscope_predictions[sign_predictions]:
        print(Fore.BLUE + "- " + prediction)


# Main program loop
repeat = True
while repeat:
    # Print menu
    print(Fore.YELLOW + "1. Choose your zodiac sign")
    print("2. Choose a sign for compatibility")
    print("3. See predictions for your zodiac sign")
    print("4. See your lucky number for today")
    print("5. Exit program")

    # Get user choice
    choice = input(Fore.GREEN + "Enter your choice: ")
    if choice == "1":
        while True:
            try:
                birth_day = int(input("What day were you born? (1-31): "))

            except ValueError:
                print("Invalid input, please enter a number")

            else:
                if 1 <= birth_day <= 31:
                    break

                else:
                    print("Day must be between 1-31")

        while True:
            birth_month = input(Fore.GREEN +
                                "What month were you born? (1-12): ")

            if birth_month.isdigit():
                birth_month = int(birth_month)

                if 1 <= birth_month <= 12:
                    break

                else:
                    print(Fore.RED + "Month must be between 1 and 12")

            else:
                print(Fore.RED + "Invalid input. Please enter a number.")

        get_zodiac_sign(birth_day, birth_month)

    elif choice == "2":
        print(Fore.WHITE + ("Compatibility is based on the elements(fire, "
                            "earth, air, water)."))
        print("Zodiac signs should start with a capital letter.")

        valid_signs = zodiac_compatibility.keys()

        while True:
            try:
                user_sign = input(Fore.GREEN + "What is your zodiac sign? ")

                if user_sign not in valid_signs:
                    raise ValueError(
                        Fore.RED + "Invalid zodiac sign. Please try again."
                    )

                break

            except ValueError as e:
                print(e)

        while True:
            try:
                match_sign = input(
                    Fore.GREEN +
                    "What sign do you want to check compatibility with? "
                )

                if match_sign not in valid_signs:
                    raise ValueError(
                        Fore.RED + "Invalid zodiac sign. Please try again."
                    )

                break

            except ValueError as e:
                print(e)

        show_compatability(user_sign, match_sign)
