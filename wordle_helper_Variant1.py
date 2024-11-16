#! /usr/bin/env python3
#! SCOTTY's WORDLE ASSISTANT
from wordle_words import wordList
from time import sleep
import random

def grab_guess():
    while True:
        try:
            guess = str(input("What is your guess: ")).lower()
            if len(guess) == 5:
                return guess
                break
            else:
                print("must be a 5 letter word, please try again")
        except ValueError:
            print("please enter a word...")


def ask_for_hints(guess):
    guess_with_colors = []
    for letter in guess:
        color = input(f"what color is the letter {letter.upper()}?\n(grey, yellow, or green): ")
        x = [letter,  color]
        guess_with_colors.append(x)
    return guess_with_colors

# updates the list based on your guess
def update_list(guess_with_colors, possibleWordList):
    removedWords = []
    possibleWords = []

    # Check for "grey" letters (letters that should not appear in the word)
    for letter in guess_with_colors:
        if letter[1] == "grey":
            # Add words containing the grey letter to the removed list
            removedWords.extend([word for word in possibleWordList if letter[0] in word])

    # Filter out words with grey letters
    possibleWordList = [word for word in possibleWordList if word not in removedWords]

    # Check for "green" letters (letters that should be in the correct position)
    for letter in guess_with_colors:
        if letter[1] == "green":
            letterIndex = guess_with_colors.index(letter)
            possibleWordList = [word for word in possibleWordList if word[letterIndex] == letter[0]]

    # Check for "yellow" letters (letters that should appear in the word but not in the same position)
    for letter in guess_with_colors:
        if letter[1] == "yellow":
            letterIndex = guess_with_colors.index(letter)
                                                #{-------------------logic for (wordle_simulator.py) here-------------------}
            possibleWordList = [word for word in possibleWordList if letter[0] in word and word[letterIndex] != letter[0]]

    return possibleWordList

def display_list_with_title(list,title="BLANK LIST TITLE: "):
    print(title)
    for i in list:
        print(i)



def main():

    print("SCOTTY'S WORDLE ASSISTANT")
    global wordList

    # the following line is test code to test if the program narrows it down to the proper word
    #print(f"TEST WORD FROM LIST: {random.choice(wordList)}")


    
    guessCounter = 1
    while len(wordList) > 1:
        print(f"\nGUESS {guessCounter}")
        guess = grab_guess()
        guess_with_colors = ask_for_hints(guess)
        wordList = update_list(guess_with_colors, wordList)
        display_list_with_title(wordList, title=f"POSSIBLE WORDS: {len(wordList)}")
        guessCounter += 1
    print(f"Correct word: {wordList}")





if __name__ == "__main__":
    main()