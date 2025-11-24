import random

words = ["apple", "banana", "orange", "grapes", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess:", " ".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")
        print("Word:", " ".join(guessed))

if "_" not in guessed:
    print(" You won! The word was:", word)
else:
    print(" You lost! The word was:", word)
