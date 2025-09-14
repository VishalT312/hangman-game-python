
# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.

import random

class Hangman:
    def Greeting(self):
        name = input("Enter your name: ")
        print(f"Hey {name}!,Welcome to Hangman game!")
    
    def random_word_select(self,lst):
        random_word = random.choice(lst)
        print(random_word)
        length_random_word = len(random_word)
        print("This is the length of your word:- ",length_random_word * " _ ")
        print(" ")
        track_ch2 = 0
        update_ch = ""
        while True:
            character = input("Guess a single character: ")
            update_ch += character
            if character in random_word:
                print("Ahh You are getting it...")
                if len(random_word) == len(update_ch) and random_word == update_ch:
                    print("Booom! You got it.......")
                    print(f"The correct word is:- {random_word}")
                    break
                
                if track_ch2 > length_random_word:
                    print("Limit Exceed")
                    return
            else:
                print("Incorrect Guess Try another character!")
                track_ch2 += 1
                if track_ch2 > length_random_word:
                    print("Limit Exceed")
                    break

h = Hangman()
h.Greeting()
words = ["apple", "banana", "python", "hangman"]
h.random_word_select(words)
