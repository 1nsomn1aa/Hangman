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
        Display underscores for letters
        Replace underscores with correctly guessed letters
        """
        for letter in self.word:
            if letter in self.guesses:
                print(letter)
            else:
                print('_')


