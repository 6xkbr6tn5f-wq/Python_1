import random


def play_game():
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.\n")
            elif guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.\n")


if __name__ == "__main__":
    play_game()