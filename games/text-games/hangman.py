import random

word_list = ["python", "hangman", "programming", "developer", "computer", "challenge"]
chosen_word = random.choice(word_list)
word_display = ["_"] * len(chosen_word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_display:
    print("Word:", " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

if "_" not in word_display:
    print("You won! The word was:", chosen_word)
else:
    print("You lost! The word was:", chosen_word)
