import os
from random import choice

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = choice([
    "apple", "banana", "orange", "grape", "cherry", "strawberry", "pineapple", "blueberry", "mango", "lemon",
    "elephant", "giraffe", "dolphin", "kangaroo", "penguin", "octopus", "butterfly", "hamster", "rabbit", "turtle",
    "computer", "keyboard", "monitor", "internet", "software", "database", "network", "algorithm", "python", "display",
    "mountain", "ocean", "forest", "desert", "island", "valley", "volcano", "river", "garden", "bridge",
    "adventure", "journey", "mystery", "fantasy", "treasure", "victory", "champion", "freedom", "imagine", "explore",
    "apartment", "building", "kitchen", "bedroom", "library", "stadium", "hospital", "museum", "factory", "theater",
    "sunlight", "rainbow", "thunder", "weather", "shadow", "planet", "galaxy", "universe", "science", "history",
    "guitar", "trumpet", "violin", "melody", "rhythm", "concert", "singer", "dancer", "painting", "artist",
    "bicycle", "airplane", "rocket", "helicopter", "subway", "scooter", "traffic", "captain", "driver", "travel",
    "morning", "evening", "calendar", "birthday", "holiday", "weekend", "diamond", "jewelry", "silence", "whisper"
])

user_guesses = ['_'] * len(word)
wrong_guesses = []

while "_" in user_guesses and len(wrong_guesses) < len(HANGMANPICS) - 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HANGMANPICS[len(wrong_guesses)])
    print("\nGuessing: " + ' '.join(user_guesses))
    print("\nWrong guesses: " + ', '.join(wrong_guesses))
    print("Remaining attempts: " + str(len(HANGMANPICS) - 1 - len(wrong_guesses)))
    
    guess = input("\nGuess a letter: ").lower()
    
    if guess in user_guesses or guess in wrong_guesses:
        continue
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                user_guesses[i] = guess

    else:
        wrong_guesses.append(guess)

os.system('cls' if os.name == 'nt' else 'clear')
print(HANGMANPICS[len(wrong_guesses)])
print("\nGuessing: " + ' '.join(user_guesses))
print("\nWrong guesses: " + ', '.join(wrong_guesses))
print("Remaining attempts: " + str(len(HANGMANPICS) - 1 - len(wrong_guesses)))
    
if "_" not in user_guesses:
    print("\nCongratulations! You've guessed the word: " + word)
    print("You win!")

else:
    print("\nSorry, you've been hanged! The word was: " + word)
    print("Game over!")
