def levenshtein(a, b):

    n, m = len(a), len(b)
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = (
                previous_row[j] + 1,
                current_row[j - 1] + 1,
                previous_row[j - 1],
            )

            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def soundex(input_str):
    code = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 0,
        "F": 1,
        "G": 2,
        "H": 0,
        "I": 0,
        "J": 2,
        "K": 2,
        "L": 4,
        "M": 5,
        "N": 5,
        "O": 0,
        "P": 1,
        "Q": 2,
        "R": 6,
        "S": 2,
        "T": 3,
        "U": 0,
        "V": 1,
        "W": 0,
        "X": 2,
        "Y": 0,
        "Z": 2,
    }

    upper = input_str.upper()
    soundex_code = [upper[0]]


    for i in range(1, len(upper)):
        if len(soundex_code) < 4:
            if not upper[i].isalpha():
                continue
            if code.get(upper[i]) != 0 and code.get(upper[i - 1]) != code.get(upper[i]):
                soundex_code.append(str(code.get(upper[i])))
            else:
                continue
        else:
            break
    if len(soundex_code) < 4:
        soundex_code.append("0" * (4 - len(soundex_code)))
    return "".join(soundex_code)
