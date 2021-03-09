import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")
name_dict = {row.letter: row.code for (index, row) in file.iterrows()}


def generate_phonetic():
    word = input("Enter your name : ").upper()
    try:
        output_list = [name_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
