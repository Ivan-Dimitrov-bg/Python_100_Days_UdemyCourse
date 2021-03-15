
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter: row.code for (index, row) in data.iterrows()}
# for (index, row) in data.iterrows():
#     dict_data[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input("Enter a name:").upper()
    try:
        list_words = {letter: dict_data[letter] for letter in user_input}
    except KeyError:
        print("Please enter a valid word:")
        generate_phonetic()
    # list_words = {letter: value for (letter, value) in dict_data.items() if letter in user_input}
    else:
        print(list_words)


generate_phonetic()