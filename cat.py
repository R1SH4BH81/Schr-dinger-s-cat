import random
import time

def schrodingers_cat_game():
    print("Welcome to Schrödinger's Cat Game!")
    print("You are in a room with a sealed box. Inside the box, there may be multiple cats, and they may be alive or dead.")
    print("Your task is to guess the states of all the cats without opening the box.")
    print("But be careful, you only have a limited time to make your guess!")
    print("Let's begin!")
    
    # Add a time limit for making the guess
    time_limit = 30  # 30 seconds
    start_time = time.time()
    
    num_cats = random.randint(2, 4)  # Randomly choose between 2 to 4 cats
    actual_cat_states = [random.randint(0, 1) for _ in range(num_cats)]  # 0 for dead, 1 for alive
    
    # Display the number of cats
    print("There are", num_cats, "cats in the box.")
    
    guess = input("Enter your guess (1 for alive, 0 for dead, e.g., 101 for three cats): ")
    
    # Check if time is up
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time's up! You didn't make a guess in time.")
        print("The actual states of the cats were:", actual_cat_states)
        return
    
    # Check if the guess is valid
    if len(guess) != num_cats or not guess.isdigit():
        print("Invalid input. Please enter a sequence of 0s and 1s with the same length as the number of cats.")
        return
    
    # Convert the guess to a list of integers
    guess_list = [int(digit) for digit in guess]
    
    # Check if the guess is correct
    if guess_list == actual_cat_states:
        print("Congratulations! You guessed correctly. All the cats are indeed in the states:", actual_cat_states)
    else:
        print("Sorry, you guessed wrong. The actual states of the cats were:", actual_cat_states)

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        schrodingers_cat_game()
    else:
        print("Thank you for playing Schrödinger's Cat Game!")

schrodingers_cat_game()
