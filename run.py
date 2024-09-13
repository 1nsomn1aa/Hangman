import random

class Hangman:
    def __init__(self):
        """
        Create a class for the basic game settings and set the random word choice.
        """
        self.words = ["python", "learning", "hangman", "coding", "computer", "development", "programming", "software"]
        self.word = random.choice(self.words)
        self.guesses = ""
        self.turns = 10

    def print_current_game_state(self):
        """
        Iterate through the random word
        Display underscores for incorrect guesses
        Replace underscores with letters for correct guesses
        """
        for letter in self.word:
            if letter in self.guesses:
                print(letter, end=" ")
            else:
                print('_', end=" ")
        print()

    def players_guess(self, guess):
        """
        Update the guess string 
        Lower the remaining turns count if guess is incorrect
        """
        self.guesses += guess
        if guess not in self.word:
            self.turns -= 1
            print(f"Incorrect. You have, {self.turns} guesses left")

    def check_for_victory(self):
        """
        Check if all letters have been guessed correctly
        """
        return all(letter in self.guesses for letter in self.word)

    def check_for_defeat(self):
        """
        Check if player ran out of attempts
        """
        return self.turns == 0

def play_game():
    """
    Main game function
    """
    game = Hangman()

    while True:
        failed = game.print_current_game_state()

        if failed == 0:
            print("You win!")
            break
        
        if game.check_for_defeat():
            print(f"You lost! The word was {game.word}")
            break

        guess = input("Guess a letter (or type 'exit' to terminate the game): \n")

        # Check if player wants to quit
        if guess.lower() == "exit":
            print("Game terminated. The word was:", game.word)
            break

        # Check if the input is a single character
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        # Check if the input is a letter
        if guess.isalpha() == False:
            print("Please enter a letter, symbols and numbers are not allowed.")
            continue

        # Check if the user already tried guessing the letter
        if guess in game.guesses:
            print("You have already guessed that letter. Try again.")
            continue

        game.players_guess(guess)

        if game.check_for_victory():
            print("You win!")
            break

play_game()