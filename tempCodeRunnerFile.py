
# 👋 Introduction
# "Hi everyone, today I’ll be walking you through a simple Python project — a Hangman game. This project is great for practicing concepts like loops, conditionals, and working with user input. Let’s go step by step."


# "We start by importing Python’s random module. This helps us select a random word from our list of words for the game."
import random


# "I created a class called Hangman to keep the code organized. Inside it, I’ve defined two methods: Greeting and random_word_select."
class Hangman:

    # "This function asks the player’s name and gives a friendly welcome message."
    def Greeting(self):
        name = input("Enter your name: ")
        print(f"Hey {name}!, Welcome to Hangman game!")

    # "This method picks a random word from the given list and calculates its length."
    def random_word_select(self, lst):
        random_word = random.choice(lst)
        length_random_word = len(random_word)

    # "To represent the hidden word, I create a list of underscores, one for each letter. For example, if the word is 'apple', it will start as _ _ _ _ _."
        blanks_list = ["_"] * length_random_word
        print(blanks_list)

    # "I use a set to store guessed letters, and two variables to track wrong guesses and the maximum allowed attempts — which is 6, just like in classic Hangman."
        # Track guesses
        guessed_letters = set()
        wrong_guesses = 0
        max_attempts = 6

        print("This is the length of your word:- ", " ".join(blanks_list))
        print(" ")

        # "This loop keeps running until the player either guesses the word or uses up all attempts."
        while True:
            character = input("Guess a single character: ").lower()

            # Validate input
            if len(character) != 1 or not character.isalpha():
                print("Please enter a single valid letter.")
                continue

            # Check duplicate guess
            if character in guessed_letters:
                print("You already guessed this letter!")
                continue

            guessed_letters.add(character)

            # "If the guessed letter is correct, I update the blank list to reveal all positions where that letter appears. This way, the word starts to form gradually."
            if character in random_word:
                print("Ahh You are getting it...")

                # Update blanks with correct letter(s)
                for i, ch in enumerate(random_word):
                    if ch == character:
                        blanks_list[i] = character

                print(" ".join(blanks_list))

                # "When there are no underscores left, it means the player has guessed the full word — and they win 🎉."
                # Win condition → no "_" left
                if "_" not in blanks_list:
                    print("Boom! You got it.......")
                    print(f"The correct word is: {random_word}")
                    break

            # "If the guess is wrong, I increase the counter and show how many attempts are left. After 6 wrong guesses, the game ends and the correct word is revealed."
            else:
                wrong_guesses += 1
                print("Incorrect Guess! Try another character!")
                print(f"Attempts left: {max_attempts - wrong_guesses}")
                
                # Lose condition
                if wrong_guesses == max_attempts:
                    print("Limit Exceeded! Game Over.")
                    print(f"The correct word was: {random_word}")
                    break


# ---------------- RUNNING THE GAME ----------------

# "Finally, I create an object of the Hangman class, greet the player, define a list of words, and start the game."
h = Hangman()
h.Greeting()
words = ["apple", "banana", "python", "hangman"]
h.random_word_select(words)
