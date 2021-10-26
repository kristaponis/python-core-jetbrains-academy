# Hangman is a popular yet grim intellectual game.
# A cruel computer hides a word from you. Letter by letter you try to guess it.
# If you fail, you'll be hanged, if you win, you'll survive.
from string import ascii_lowercase
import random

print("H A N G M A N")
while True:
    play_exit = input('Type "play" to play the game, "exit" to quit: ')
    if play_exit == "play":
        break
    elif play_exit == "exit":
        quit()
    else:
        continue

builtin_words = ('python', 'kotlin', 'java', 'javascript')
random_word = random.choice(builtin_words)

count_letters = len(random_word)
secret_word = f"{count_letters * '-'}"
used_letters = set()
count_guesses = 0
while count_guesses < 8 and count_letters > 0:
    print()
    print(secret_word)
    index = -1
    user_letter = input("Input a letter: ")
    if len(user_letter) != 1:
        print("You should input a single letter")
        continue
    if user_letter not in ascii_lowercase:
        print("Please enter a lowercase English letter")
        continue
    if count_letters > 0:
        if user_letter in random_word:
            if user_letter not in used_letters:
                for letter in random_word:
                    if letter == user_letter:
                        index += 1
                        count_letters -= 1
                        index = random_word.find(user_letter, index)
                        secret_word = secret_word[:index] + user_letter + secret_word[index+1:]
            else:
                print("You've already guessed this letter")
        else:
            if user_letter in used_letters:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                count_guesses += 1
    else:
        break
    used_letters.add(user_letter)

if count_guesses > 7:
    print("You lost!")
elif count_letters > 0:
    print("You lost!")
else:
    print("You guessed the word!")
    print("You survived!")
