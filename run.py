import gspread
from google.oauth2.service_account import Credentials
import time
import random
from pyfiglet import figlet_format
from signs import get_zodiac_sign
from descriptions import descriptions
from predictions import horoscope_predictions
from compatibility import zodiac_compatibility
from colorama import Fore
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


def show_compatibility(user_sign, match_sign):
    """
    Prints compatibility between two zodiac signs.
    Checks if the match sign is in the first 3 or last compatible signs.
    Prints out a compatibility percentage and statement.
    """
    user_compatibility = zodiac_compatibility[user_sign]

    if match_sign in user_compatibility[:3]:
        compatibility_rate_one = random.randint(70, 100)
        print(Fore.BLUE + f"{user_sign} is very compatible with {match_sign}!")
        print(Fore.BLUE +
              (f"Your compatibility rate is {compatibility_rate_one}%"))
    elif match_sign in user_compatibility[3:]:
        compatibility_rate_two = random.randint(50, 69)
        print(Fore.BLUE +
              (f"{user_sign} is slightly compatible with {match_sign}!"))
        print(Fore.BLUE +
              f"Your compatibility rate is {compatibility_rate_two}%")
    else:
        print(Fore.BLUE + f"{match_sign} is not compatible with {user_sign}.")


def show_prediction(sign_predictions):
    """
    Prints horoscope predictions for the given zodiac sign.
    """
    for prediction in horoscope_predictions[sign_predictions]:
        print(Fore.BLUE + "- " + prediction)


def update_zodiac_worksheet(data):
    """
    Updata zodiac worksheet, add new row with the data provided
    """
    zodiac_worksheet = SHEET.worksheet("zodiac")
    row = [username, sign_predictions]
    zodiac_worksheet.append_row(row)


def give_lucky_number(sign):
    """
    Generates and prints a random lucky number for the given zodiac sign today.
    """
    lucky_number = random.randint(1, 25)

    today = date.today()

    result = f"Today is {today}. {user_sign}'s lucky number is {lucky_number}"

    print(Fore.BLUE + result)


# Start the program
print(Fore.WHITE +
      ("Your name should start with a capital letter."))
print(Fore.WHITE +
      ("It should be no more than 20 characters long."))
print(Fore.WHITE +
      ("No numbers, symbols or spaces. Letters only."))

while True:
    try:
        username = input(Fore.GREEN + "Enter your name: ")

        if not username:
            raise ValueError(Fore.RED + "Name cannot be empty")

        if " " in username:
            raise ValueError(Fore.RED + "Name cannot contain spaces")

        if not username.isalpha():
            raise ValueError(Fore.RED + "Name can only contain letters")

        if len(username) > 20:
            raise ValueError(Fore.RED + "Name must be 20 characters or less")

        if not username[0].isupper():
            raise ValueError(Fore.RED +
                             ("Name must start with a capital letter"))

        break

    except ValueError as e:
        print(e)

print(Fore.BLUE + "Hi " + username + "!" + " Welcome to the")


def style(text="", delay=0.008, art=True):
    """
    Styles ASCII art to appear character by character
    """
    if art:
        with open("art.txt") as f:
            art = f.read()
        formatted = art
    else:
        formatted = text

    for char in formatted:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


style(art=True)


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
                birth_day = int(input(Fore.GREEN +
                                      ("What day were you born? (1-31): ")))

            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number")

            else:
                if 1 <= birth_day <= 31:
                    break

                else:
                    print(Fore.RED + "Day must be between 1-31")

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

        show_compatibility(user_sign, match_sign)

    elif choice == "3":
        valid_signs = zodiac_compatibility.keys()

        while True:
            try:
                sign_predictions = input(Fore.GREEN +
                                         ("Enter sign for prediction: "))

                if sign_predictions not in valid_signs:
                    raise ValueError(
                        Fore.RED + "Invalid zodiac sign. Please try again."
                    )

                break

            except ValueError as e:
                print(e)

        show_prediction(sign_predictions)
        data = username, show_prediction
        update_zodiac_worksheet(data)

    elif choice == "4":
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

        give_lucky_number(user_sign)

    elif choice == "5":
        repeat = False
        print(Fore.BLUE + ("Thank you for participating, " + username +
                           ". Goodbye ;)"))

    else:
        print(Fore.RED + "Invalid choice. Please try again")
