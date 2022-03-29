import hashlib
import sys
from re import search
import time
import math
import os
import tqdm

print("Current directory: " + os.getcwd())



CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

animation = ["[□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■□□□□□□□]", "[■■■■■■■■■■■■■■□□□□□□]", "[■■■■■■■■■■■■■■■□□□□□]", "[■■■■■■■■■■■■■■■■□□□□]", "[■■■■■■■■■■■■■■■■■□□□]", "[■■■■■■■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■■■■■■■□]", "[■■■■■■■■■■■■■■■■■■■■]"]
animation2 = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    
def find_password(word):
    if hash_type == "md5":
        result = hashlib.md5(word.encode()).hexdigest()
    elif hash_type == "sha256":
        result = hashlib.sha256(word.encode()).hexdigest()

    if result == hash_to_crack: 
        print("\nFound password: " + word)
        if search(word, passwordsR.read()):
            pass
        else:
            with open(hash_type + "/" + hash_type + "_passwords.txt", "a") as passwords:
                passwords.write("\n" + word + " = " + result)
            print("New password detected and added to database")
        
        input("Press any button to exit... ")
        exit()
        
def numbers(word, num):
    for i in range(0, 10 ** num):
        
        find_password(word + str(i))
        #print(number_word)
        
def check_dictionary():
    lines = passwordsR.read().split("\n")
    for i in range(len(lines)):
        if hash_to_crack in lines[i]:
            word = lines[i].split(" ")
            print("Found password: " + word[0])
            print("Password is already in dictionary")
            
            input("Press any button to exit... ")
            exit()

def set_hash_type(hash_type):
    hash_to_crack = open(hash_type + "/" + hash_type + "_hash_to_crack.txt", "r").read()
    passwords = open(hash_type + "/" + hash_type + "_passwords.txt", "a")
    passwordsR = open(hash_type + "/" + hash_type + "_passwords.txt", "r")
    return hash_to_crack, passwords, passwordsR

def change_hash_to_crack():
    with open(hash_type + "/" + hash_type + "_hash_to_crack.txt", "w") as hash_to_crackR:
        hash_to_crackR.write(input("New Hash: "))
    

hash_type = input("Hash type: ")
lang = input("Language? (en/no)")
if lang == "en":
    wordlist = open("english.txt").readlines()
elif lang == "no":
    wordlist = open("norwegian.txt").readlines()

hash_to_crack, passwords, passwordsR = set_hash_type(hash_type)

what_to_do = input("What do you want to do? (crack, change) ")

if what_to_do == "change":
    change_hash_to_crack()
elif what_to_do == "crack":    
    print(hash_to_crack)    
    check_dictionary()    

    min_len = int(input("Minimum length: "))
    for word in tqdm.tqdm(wordlist):
        
        if len(word) >= min_len:
            word = word.strip()
            #print(word)
            find_password(word.lower())

           
            find_password(word.capitalize())

        for i in range(0, 3):
            if len(word) >= min_len - i:
                numbers(word.capitalize(), i)
                numbers(word.lower(), i)
        

    print("\nSearched through " + str(len(wordlist)) + " words and did not find the password")