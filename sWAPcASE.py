# sWAP cASE
"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa."""

def swap_case(s):
    newLetter = ""
    for letter in s:
        if letter.islower():
            newLetter += letter.upper()
        elif letter.isupper():
            newLetter += letter.lower()
        else:
            newLetter += letter
    return newLetter

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)