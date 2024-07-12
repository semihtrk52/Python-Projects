import random
from words import word_list
import string

def hangman(word_list):
    
    word = random.choice(word_list).upper() 
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        hang_list = []
        for letter in word:
            if letter in used_letters:
                hang_list.append(letter)
            else:
                hang_list.append('-')

        print("Current word: ",' '.join(hang_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter not in word. You have {lives} lives left.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"You died. The word was {word}")
    else:
        print(f"Congratulations! You guessed the word {word}")

hangman(word_list)
