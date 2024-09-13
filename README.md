
# The Hangman Game


**The Hangman Game** is a fun and challenging Python-based game, running in a mock terminal environment on Heroku.

Players try to guess a hidden word by suggesting letters, with each incorrect guess lowering their amount of remaining turns. The game ends if they run out of turns or guess the word correctly.

[Link to The Hangman Game on Heroku](https://hangman-game-1-383bcb76f027.herokuapp.com/)

![Screenshot 2024-09-13 142632](https://github.com/user-attachments/assets/d09a8669-7a5c-496f-b542-85698c779749)
## Features

**Current Features**
- Starting the game asks the user to guess a letter

![start](https://github.com/user-attachments/assets/df974131-67ba-409a-bc5c-24074aa3a031)
- User input validation 

    - Checking if only one letter is provided 

    ![multipleletters](https://github.com/user-attachments/assets/540f7444-8c86-41a8-bea8-46b9d805026a)
    - Checking if only letters are provided, no symbols or numbers

    ![numberssymbols](https://github.com/user-attachments/assets/6baab224-7015-423c-a477-106bae4715ff)
    - Checking if the player already tried guessing that letter.

    ![sameletter](https://github.com/user-attachments/assets/a2294934-59ac-4366-8411-21264e321287)
    - Using 'exit' command to terminate the game early

    ![exit](https://github.com/user-attachments/assets/7fbd608f-8bd6-4a4e-a84b-e601c67f46f9)
- Victory message displaying the hidden word

![win](https://github.com/user-attachments/assets/76ec4fec-30df-4c50-8346-1bafdfba1ee1)

**Future Features**

- Adding topics and more challenging words to choose from.
- Adding a 'hint' command to show a hint about the word.
- Styling the console interface to include a "hangman figure"

## Data Model

To create this game, I used a "class" as my model for storing all the game settings and logic, I've also used methods to retrieve and modify the current game state such as:

```def print_current_game_state(self):```

```def players_guess(self, guess):```

```def check_for_victory(self):```

```def check_for_defeat(self):```

 "list" to store the words and a "random" module to randomly select a word from that list. 

```self.words = ["python", "learning", "hangman", "coding", "computer", "development", "programming", "software"]```

```import random```
 



## Testing

I used **Code Institute Python Linter** to test my python project and after the development process, it no longer found any issues.

![Screenshot 2024-09-13 135053](https://github.com/user-attachments/assets/7a7d0c31-f967-42c5-9076-85f49fcb4c8c)

I've also tried manually breaking the code by inputing numbers, multiple letters, symbols and letters that have been tried before. The code behaved as it should without any errors.


## Bugs

**Fixed Bugs**

During the development of this game, I've encountered a few bugs:
- Grammatical Errors
    - Missing colon kept on resulting in the game not being able to run after inputing a letter.
- Accidental Infinite Loop
    - Failing to enter a "break" command into some functions resulted in the game infinitely prompting me with underscores.
- Underscores on a new line
    - Initially, every letter of the hidden word was provided on a new line in the terminal, but after some research I fixed this by adding an empty print() method and adding empty "end=' '" parameters in the function that displays the current hidden word.

**Current Bugs**

After fixing the bugs above, I tried manually breaking the code to result in a bug but were unable to do so, therefore to my knowledge, there are currently no bugs on this project and everything works as it should.

To see my development process and bug fixes, please follow [this](https://github.com/1nsomn1aa/Hangman/commits/main/) link to my GitHub repository.

## Deployment

This project has been deployed to Heroku. The steps I took to do this are outlined below. 

- [x]   Create or fork a repository on GitHub
- [x]   Navigate to Heroku Dashboard and press "Create a New App"
- [x]   Select your required buildbacks (Pyhon and NodeJS)
- [x]   Connect your GitHub repository to Heroku in the Settings tab
- [x]   Click on Manual or Automated deployment


## Credits

- Code Institute python project template
- Code Institute LMS, Love-Sandwiches demo project
- [W3Schools](https://www.w3schools.com/python/) for syntax, functions and other python information reminders

