import requests
import string
import os
from random import sample

API_URL = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(API_URL)
response.raise_for_status()
WORDS = response.content.decode("UTF-8").splitlines()

def get_words():
    num_of_words = 500
    rand_words = sample(WORDS, num_of_words)
    return ' '.join(rand_words)


def create_files():
    num_file = [number for number in range(0,51)]
    return num_file
file_number = create_files()
    
    
def alphabet_letter():
    alphabetLetter = string.ascii_uppercase[0:6]
    return list(alphabetLetter)
folder_letter = alphabet_letter()

def create_folders_files():
    for folder in folder_letter:
        os.mkdir(folder)
        for file in file_number:
            with open(f"{folder}/{file}.txt", "a") as data_file:
                    data_file.writelines(get_words())