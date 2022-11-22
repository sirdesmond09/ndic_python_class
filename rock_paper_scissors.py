import random


selection_list = ["r", "p", "s"]
print(f"Please use the first letter to Make a selection from the list:",selection_list)
com_choice = random.choice(selection_list)


trial = 1
score = 0

while trial > 0:
    user_choice = input("Choice:")
    if user_choice in selection_list:
        print(f"You chose: {user_choice}, Computer Chose: {com_choice}")
        if user_choice == com_choice:
            print("You made same selection, Try again")
        elif user_choice == "r":
            if com_choice == "s":
                print("Rock crushes Scissors, You win")
                score +=2
            else:
                print("Paper covers rock, You Loose!")
                trial-=1
        elif user_choice == "p":
            if com_choice == "r":
                print("Paper covers rock, You win!!")
                score +=2
            else:
                print("Scissors Cuts paper, You Loose!!")
                trial-=1
        elif user_choice == "s":
            if com_choice == "p":
                print("Scissors cuts Paper, you Win!!")
                score +=2
            else:
                print("Rock Smashes Paper, You Loose!!")
                trial-=1
    else:
        print("Invalid Input!!")
        
print(f"Your final score is {score}")