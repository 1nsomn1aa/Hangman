import random

class Hangman:
    def __init__(self):
        """
        Create a class for the basic game settings and set the random word choice.
        """
        self.words = ["python", "learning", "hangman", "coding", "computer", "development"]
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
                print(letter)
            else:
                print('_')

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
        
        if game.check_for_defeat():
            print(f"You lost! The word was {game.word}")

play_game()