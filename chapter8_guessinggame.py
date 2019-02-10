"""
Random Number Guessing Game
"""
import random
from textwrap import dedent

def main():

    print("So I'm thinking of a number between 1 and 50")

    # creates secret number
    secret_number = random.randrange(1, 50)

    # initalizes our attempt count
    user_attempt_count = 1

    # sets user guess to something the secret number can't be
    user_guess = 0

    # loops until user_guess == secret_number,
    # or user_attempt_count over allowed attempts

    while user_guess != secret_number and user_attempt_count < 10:
        print("This is your guess number ", user_attempt_count)
        
        try:
            user_input_text = input("Type any number between 1 and 50: ")
            user_guess = int(user_input_text)
                    # tells user if too high or low, or got it
            if user_guess > secret_number:
                print("That's too high.")
            elif user_guess < secret_number:
                print("That's too low.")
            else:
                print("Yay! That's it!")
        except ValueError:
            print("Type in an actual number")


        # Increment the attempt count
        user_attempt_count += 1

    if user_guess != secret_number:
        print(dedent(
            """
            Just so you're not wondering for the rest
            of your life what my number was, it was:
            """), secret_number)

if __name__ == "__main__":
    main()