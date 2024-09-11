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