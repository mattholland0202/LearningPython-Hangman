import random
import string
import re
import DrawHangman

global word
global current_guess
global letters_remaining
global letters_correct
global letters_incorrect

def print_current_status():
    print("Current guess: " + " ".join(current_guess))
    print("{0} guesses remaining".format(10 - len(letters_incorrect)))
    print("Potential letters remaining: " + ",".join(letters_remaining))
    print("Hangman: " + DrawHangman.print_hangman(len(letters_incorrect)))

def turn():
    print() # Print empty line to separate new turn
    if "".join(current_guess) != word:
        print_current_status()
        guess = input("Guess a letter: ").upper()

        if guess in letters_remaining:
            if guess in word:
                letters_remaining.remove(guess)
                print("CORRECT!")
                letter_locations = [m.start() for m in re.finditer(guess, word)]
                for location in letter_locations:
                    current_guess[location] = guess
                turn()
            else:
                letters_remaining.remove(guess)
                letters_incorrect.append(guess)
                if len(letters_incorrect) < 10:
                    print("INCORRECT!")
                    turn()
                else:
                    print("Hangman: " + DrawHangman.print_hangman(10))
                    print("GAME OVER! The word was '{0}'.".format(word.upper()))
        else:
            print("Invalid letter. Try again.")
            turn()

    else:
        print("Congratulations, you've won! The word was: " + word)

def play():
    global word
    global letters_remaining
    global letters_correct
    global letters_incorrect
    global current_guess
    letters_remaining = list(string.ascii_uppercase)
    letters_incorrect = list()
    letters_correct = list()
    current_guess = list("_" * len(word))
    turn()

def one_player():
    global word
    words = open("words.txt").readlines()
    word = random.choice(words).strip().upper()

    play()

def two_players():
    global word

    word = input("Player 1, enter your chosen word: ").upper()

    play()

def main():
    player_count = input("Enter the number of players (1 or 2): ")

    try:
        count = int(player_count)

        if count == 1:
            one_player()
        elif count == 2:
            two_players()
        else:
            main()
    except Exception as err:
        print("Invalid input, try again. Message: " + str(err))

main()
