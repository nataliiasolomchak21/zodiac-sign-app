from descriptions import descriptions
from colorama import Fore


def get_zodiac_sign(birth_day, birth_month):
    """
    Determines and prints the zodiac sign based on a given birth day and month.
    Checks the birth day and month against the date ranges for each sign.
    Prints the sign, symbol, and traits if a match is found.
    """
    if (birth_month == 12 and birth_day >= 22) or (
        birth_month == 1 and birth_day <= 19
    ):
        sign = "Capricorn"
    elif (birth_month == 1 and birth_day >= 20) or (
        birth_month == 2 and birth_day <= 18
    ):
        sign = "Aquarius"
    elif (birth_month == 2 and birth_day >= 19) or (
        birth_month == 3 and birth_day <= 20
    ):
        sign = "Pisces"
    elif (birth_month == 3 and birth_day >= 21) or (
        birth_month == 4 and birth_day <= 19
    ):
        sign = "Aries"
    elif (birth_month == 4 and birth_day >= 20) or (
        birth_month == 5 and birth_day <= 20
    ):
        sign = "Taurus"
    elif (birth_month == 5 and birth_day >= 21) or (
        birth_month == 6 and birth_day <= 20
    ):
        sign = "Gemini"
    elif (birth_month == 6 and birth_day >= 21) or (
        birth_month == 7 and birth_day <= 22
    ):
        sign = "Cancer"
    elif (birth_month == 7 and birth_day >= 23) or (
        birth_month == 8 and birth_day <= 22
    ):
        sign = "Leo"
    elif (birth_month == 8 and birth_day >= 23) or (
        birth_month == 9 and birth_day <= 22
    ):
        sign = "Virgo"
    elif (birth_month == 9 and birth_day >= 23) or (
        birth_month == 10 and birth_day <= 22
    ):
        sign = "Libra"
    elif (birth_month == 10 and birth_day >= 23) or (
        birth_month == 11 and birth_day <= 21
    ):
        sign = "Scorpio"
    elif (birth_month == 11 and birth_day >= 22) or (
        birth_month == 12 and birth_day <= 21
    ):
        sign = "Sagittarius"

    print("Your zodiac sign is " + sign)
    print(f"You are: {' '.join(descriptions[sign])}")
