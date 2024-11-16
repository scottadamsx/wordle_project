#! /usr/bin/env python3
#! Scotty's WORDLE simulator

# import list of words
import wordle_words
import random


def check_guess(userGuess, todaysWordle, guessCounter, greyLetters, wordGrid):

    print(f"Guess-{guessCounter}: {userGuess.upper()}")
    for letter in userGuess: 
        if letter not in todaysWordle:
            letterHint = "grey"
            greyLetters.append(letter)
        elif letter in todaysWordle:
            if userGuess.index(letter) == todaysWordle.index(letter):
                # the following line is test code that outputs both indexes in the instance that it is green
                #####print("letter index",userGuess.index(letter),"wordle index:",todaysWordle.index(letter))
                letterHint = "green"
                greenLetterIndex = todaysWordle.index(letter)
                wordGrid[greenLetterIndex] = letter
            elif userGuess.index(letter) != todaysWordle.index(letter):
                #the following line is test code that outputs both indexes in the instance that it is yellow
                #####print("letter index",userGuess.index(letter),"wordle index:",todaysWordle.index(letter))
                letterHint = "yellow"
                
        print(f"{letter.upper()} is: {letterHint.upper()}")
    print("")



def main():


    wordList = wordle_words.wordList
    todaysWordle = random.choice(wordList)
    # the following line is test code to see the correct word upon running
    #print("TODAYS WORDLE: ",todaysWordle.upper())

    wordGrid = ["X","X","X","X","X"]
    greyLetters = []
    userGuess = ""
    guessCounter = 0

    while userGuess != todaysWordle:
        print(wordGrid)
        print(f"letters NOT in word: {greyLetters}")
        guessCounter += 1
        userGuess = input("Choose a word: ")
        check_guess(userGuess, todaysWordle, guessCounter, greyLetters, wordGrid)


    
    print(f"Congradulations!! You guessed it in {guessCounter} tries. The WORDLE of the day was {todaysWordle.upper()}")
    



if __name__ == "__main__":
    main()