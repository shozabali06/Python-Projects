import random
import re
from collections import Counter
from termcolor import colored

attempts = 6

def is_word_in_file(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
        return word in content

def get_feedback(actual_word, guessed_word):
    feedback = ['*'] * len(actual_word)  # Initialize feedback with 'grey'
    actual_word_count = Counter(actual_word)  # Count occurrences of each letter in the actual word#

    
    # First pass: check for 'green'
    for i in range(len(actual_word)):
        if guessed_word[i] == actual_word[i]:
            feedback[i] = colored(guessed_word[i].upper(), 'green')
            actual_word_count[guessed_word[i]] -= 1

    # Second pass: check for 'yellow' and 'grey'
    for i in range(len(actual_word)):
        if feedback[i] == '*':  # Only consider letters not already marked 'green'
            if guessed_word[i] in actual_word and actual_word_count[guessed_word[i]] > 0:
                feedback[i] = colored(guessed_word[i].upper(), 'yellow')
                actual_word_count[guessed_word[i]] -= 1
            else:
                feedback[i] = colored(guessed_word[i].upper(), 'grey')
    return feedback            

def get_random_word():
    with open ("answerlist.txt") as file:
        word_list = file.read().splitlines()

    random_word = random.choice(word_list)
    return random_word

random_word = get_random_word()

def play():
    global attempts
    guessed_word = ""
    while guessed_word != random_word and attempts > 0:
        guessed_word = input("Enter your guess: ")
        if re.match("^[a-zA-Z]{5}$", guessed_word):
            if is_word_in_file("word_list.txt", guessed_word):
                feedback = get_feedback(random_word, guessed_word)
                print(" ".join(guessed_word).upper())
                print(" ".join(feedback))  # Display the feedback to the user
                attempts -= 1
            else:
                print("Not a word. Try Again.")
        else:
            print("Invalid input. Please enter a 5-letter word.")

    if guessed_word == random_word:
        print(f"You've guessed the word {random_word.upper()}")

play()
print(f"The word was {random_word.upper()}")

