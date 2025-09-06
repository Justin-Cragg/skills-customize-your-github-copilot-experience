# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman word-guessing game in Python that reinforces string manipulation, control flow (loops and conditionals), and user input/output.

## 📝 Tasks

### 🛠️ Core Hangman Game

#### Description
Implement a command-line Hangman game where the program randomly selects a secret word and the player guesses letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (or a provided word file).
- Accept single-letter guesses (case-insensitive) and update the displayed progress (e.g., _ a _ _).
- Show letters already guessed and remaining incorrect attempts.
- End the game with a clear win or lose message and reveal the secret word when the player loses.
- Keep the core game logic in `starter-code.py` so it can be executed directly.


### 🛠️ Polishing & Optional Enhancements

#### Description
Add one or more optional features to improve gameplay, usability, or replayability.

#### Requirements
If you implement enhancements, ensure each is documented and the base game still works. Possible enhancements (pick any):

- Read words from `words.txt` or a CSV file instead of a hardcoded list.
- Add difficulty levels that adjust allowed attempts or word length.
- Provide a hint system (reveal one letter or give a category).

## Example Input / Output

Example run (user input shown after prompts):

> Welcome to Hangman!
> The word: _ _ _ _
> Guess a letter: a
> Correct! The word: _ a _ _
> Guess a letter: z
> Incorrect. Attempts remaining: 5

## Notes for Submission

- Ensure `starter-code.py` runs with `python3 starter-code.py` and contains the main game loop.
- If you add extra files (word lists, helper modules), list them and include short usage notes in this README.
