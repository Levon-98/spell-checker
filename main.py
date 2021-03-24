import sys
from spell_checker import *


user_choice_num = input(
    "1.Levenshtein\n" "2.Soundex\n" "3.Spell correction\n" "Type 1,2 or 3:\n"
)


def drive(user_choice_function: str):
    if user_choice_function == "1":
        str_1 = input("First string:")
        str_2 = input("Second string:")
        print(
            "Levenshtein distance for {} and {} is {}".format(
                str_1, str_2, levenshtein(str_1, str_2)
            )
        )
    elif user_choice_function == "2":
        str_1 = input("Input string:")
        if not str_1.isalpha():
            print("Invalid input format")
            sys.exit()

        print("Soundex code for {} is {}".format(str_1, soundex(str_1)))
    elif user_choice_function == "3":
        str_1 = input("Write misspelled word: ")
        if not str_1.isalpha():
            print("Invalid input format")
            sys.exit()

        print("Possible options:{}".format(",".join(spell_correction(str_1))))
    else:
        print("the function does not exist")


if __name__ == "__main__":
    drive(user_choice_num)
