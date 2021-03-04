import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")
name_dict = {row.letter: row.code for (index, row) in file.iterrows()}

name_data = input("Enter your name : ").upper()
name_list = [name for name in name_data]

output_list = [name_dict[letter] for letter in name_list]
print(output_list)
