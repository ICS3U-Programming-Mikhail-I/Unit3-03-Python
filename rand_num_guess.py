#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 23, 2025
# Description: A simple number guessing game using random numbers.

import random  # Import random module

# Generate a random number between 0 and 9
correct_answer = random.randint(0, 9)

# Ask the user for their guess
user_guess = int(input("Guess a number between 0 and 9: "))

# Check if the guess is correct
if user_guess == correct_answer:
    print("Answer is correct, congratulations!")  # Correct guess message
else:
    print(
        f"Are you sure? Try it again! The correct answer was: {correct_answer}"
    )  # Incorrect guess message with answer
