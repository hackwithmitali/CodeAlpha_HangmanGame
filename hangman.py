import random

words = ["python", "engineer", "coding", "machine", "laptop"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    letter = input("Guess a letter: ").lower().strip()

    if not letter.isalpha() or len(letter) != 1:
        print("Enter only ONE alphabet letter.")
        continue

    if letter in guessed_letters:
        print("You already tried that!")
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("\n You won! The word was:", word)
else:
    print("\nGame Over! The word was:", word)
