import random


words = ["PUMPKIN", "COMPUTER", "ASTROLOGY", "BUBBLETEA", "NOTEBOOK"]
word = random.choice(words)

 
max_attempts = 6
attempts_left = max_attempts


guessed_word = ["-"] * len(word)
guessed_letters = []  

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_attempts, "incorrect guesses allowed.\n")

while attempts_left > 0:
    print("Word: " + "".join(guessed_word))
    print("Guessed letters so far:", ", ".join(guessed_letters))
    letter = input("Guess a letter: ").strip().upper()

    if not letter.isalpha() or len(letter) != 1:
        print(" Please enter a single alphabet letter.\n")
        continue

    if letter in guessed_letters:
        print(" You've already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(letter)

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word[index] = letter
        print(" Correct guess!\n")
        
        if "".join(guessed_word) == word:
            print(" CONGRATULATIONS! You've guessed the word correctly: " + word)
            break
    else:
        attempts_left -= 1
        print(" Incorrect guess.")
        print("Remaining attempts:", attempts_left, "\n")

else:
    print("Game Over! You've run out of moves.")
    print("The correct word was:", word)
