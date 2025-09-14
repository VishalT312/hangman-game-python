
# Import random module to choose a random word
import random 

class Hangman:
    
    def Greeting(self):
        # Ask for player name and welcome them
        name = input("Enter your name: ")
        print(f"Hey {name}!, Welcome to Hangman game!")

    def random_word_select(self, lst):
        # Select a random word from the list
        random_word = random.choice(lst)
        length_random_word = len(random_word)

        # Create blanks for each letter in the word
        blanks_list = ["_"] * length_random_word
        print(blanks_list)

        # Track guessed letters and attempts
        guessed_letters = set()
        wrong_guesses = 0
        max_attempts = 6

        print("This is the length of your word:- ", " ".join(blanks_list))
        print(" ")

        # Main game loop
        while True:
            character = input("Guess a single character: ").lower()

            # Validate input
            if len(character) != 1 or not character.isalpha():
                print("Please enter a single valid letter.")
                continue

            # Check for duplicate guesses
            if character in guessed_letters:
                print("You already guessed this letter!")
                continue

            guessed_letters.add(character)

            # Case 1: Correct guess
            if character in random_word:
                print("Ahh You are getting it...")

                # Replace blanks with correct letter
                for i, ch in enumerate(random_word):
                    if ch == character:
                        blanks_list[i] = character

                print(" ".join(blanks_list))

                # Win condition → all letters guessed
                if "_" not in blanks_list:
                    print("Boom! You got it.......")
                    print(f"The correct word is: {random_word}")
                    break

            # Case 2: Incorrect guess
            else:
                wrong_guesses += 1
                print("Incorrect Guess! Try another character!")
                print(f"Attempts left: {max_attempts - wrong_guesses}")
                
                # Lose condition → too many wrong guesses
                if wrong_guesses == max_attempts:
                    print("Limit Exceeded! Game Over.")
                    print(f"The correct word was: {random_word}")
                    break


h = Hangman()
h.Greeting()
words = ["apple", "banana", "python", "hangman"]
h.random_word_select(words)

