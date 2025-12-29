import random

# 1. Small list of predefined words
words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Create hidden word display
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# 2. While loop for the game
while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
    
    # 3. If-else logic
    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)
        
        # Update display
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        wrong_guesses += 1

# Game result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n❌ Game Over! The word was:", word)
