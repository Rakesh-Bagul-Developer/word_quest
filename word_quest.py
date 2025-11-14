import random

def get_word():
    """Return a random word for the game."""
    words = ["python", "orange", "apple", "coding", "google", "banana", "laptop", "hangman", "school"]
    return random.choice(words).lower()


def display_progress(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_game():
    print("🎯 Welcome to WORD QUEST — Guess the Secret Word!\n")

    word = get_word()
    guessed_letters = []
    attempts = 6  # Lives

    while attempts > 0:
        print("\nWord:", display_progress(word, guessed_letters))
        guess = input("\nEnter a letter or guess the full word: ").lower().strip()

        # Full word guess
        if len(guess) > 1:
            if guess == word:
                print(f"\n🎉 Correct! You guessed the word: {word.upper()}")
                return
            else:
                attempts -= 1
                print(f"❌ Wrong guess! Attempts left: {attempts}")
                continue

        # Single letter guess
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a valid single alphabet.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✔️ Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 Congratulations! You guessed the word: {word.upper()}")
                return
        else:
            attempts -= 1
            print(f"❌ Wrong letter! Attempts left: {attempts}")

    print(f"\n💀 Game Over! The word was: {word.upper()}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("\nThanks for playing Word Quest! 👋")
            break


if __name__ == "__main__":
    main()
