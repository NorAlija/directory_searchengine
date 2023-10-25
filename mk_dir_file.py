import requests
import string
import os
from random import choices

API_URL = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(API_URL)
response.raise_for_status()
WORDS = response.content.decode("UTF-8").splitlines()

def get_words():
    """Generate 500 random words from the API"""
    num_of_words = 500
    rand_words = choices(WORDS, k=num_of_words)
    #Sampling again
    rand_words2 = choices(rand_words, k=num_of_words)
    return ' '.join(rand_words2)

def create_files():
    """Create files from 0-50"""
    num_file = [number for number in range(0,51)]
    return num_file
file_number = create_files()
    
def alphabet_letter():
    """Create folders from A-F"""
    alphabetLetter = string.ascii_uppercase[0:6]
    return list(alphabetLetter)
folder_letter = alphabet_letter()

def create_folders_files():
    """Append the words from API to the files"""
    for folder in folder_letter:
        os.mkdir(folder)
        for file in file_number:
            with open(f"{folder}/{file}.txt", "a") as data_file:
                data_file.writelines(get_words())
#create_folders_files()


