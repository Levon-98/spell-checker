import linecache
import re
from spell_checker import *


def dict_all() -> dict:
    dic_data = {}
    count = 26
    count_2 = 1000
    letter = "A"
    for j in range(count):
        for i in range(count_2):
            k = "".join([letter, str(i).zfill(3)])
            dic_data[k] = []

        letter = chr(ord(letter) + 1)
    return dic_data


def dict_final(dic_data: dict) -> dict:
    with open("dictionary.txt", "r") as rf:
        for i in range(194433):
            word = rf.readline()
            word = word[:-1]
            key = soundex(word)
            if not bool(dic_data):
                dic_data[key] = [word]
            elif bool(dic_data):
                if key in dic_data.keys():
                    dic_data[key].append(word)
                else:
                    dic_data.update({key: [word]})
    return dic_data


def open_file_dict():
    with open("dict_data.txt", "w") as new:
        for k, v in dict_final(dict_all()).items():
            new.write(str(k) + "-" +  str(v) + "\n")


def choose_le_levenshtein(misspelled_word: str, word_list: list) -> list:
    dict_lev_count = {}
    for i in word_list:

        count_key = levenshtein(misspelled_word, i)
        if not bool(dict_lev_count):
            dict_lev_count[count_key] = [i]
        elif bool(dict_lev_count):
            if count_key in dict_lev_count.keys():
                dict_lev_count[count_key].append(i)
            else:
                dict_lev_count.update({count_key: [i]})

    choose_list_word = min(dict_lev_count.keys())
    return dict_lev_count[choose_list_word]


def spell_correction(misspelled_word: str) -> list:
    misspelled_word_soundex = soundex(misspelled_word)

    letter, number = misspelled_word_soundex[:1], misspelled_word_soundex[1:]

    with open("dict_data.txt", "r"):
        word_list_str = linecache.getline(
            "dict_data.txt",
            (ord(letter) - ord("A")) * 1000 + int(number)  + 1,
        )
        word_list = re.sub("[^\w]", " ", word_list_str).split()
        return choose_le_levenshtein(misspelled_word, word_list[1:])


if __name__ == "__main__":

    # open_file_dict() # call to create the data file
    print(",".join(spell_correction("name")))
