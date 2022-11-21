"""Build a guess game where a users tries to guess the number that the computer will select from a given random number.

If the user gets the number correctly, he gets 2 points and an added trial.

If he misses it, he loses a trial.

The user has 3 trials at the beginning of the game.
"""

import random


numbers = [random.choice(range(100)) for _ in range(6)]



print("Guess the number that was selected from", numbers)
trials = 3
score = 0

while trials > 0:
    com_choice = random.choice(numbers)
    user_choice = int(input("> "))
    
    if user_choice in numbers:
        if user_choice == com_choice:
            score += 2
            
            print(f"You win\nYou have an extra trial and your current score is {score}")
        else:
            print(f"Computer selected {com_choice}")
            trials-=1
            print(f"You lose\n{trials} trial(s) left")
    else:
        trials-=1
        print(f"Invalid Input\n{trials} trial(s) left")
        
print("Game Over!")
print(f"Your total score is {score}")