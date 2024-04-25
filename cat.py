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
    
    cat_states = ["alive", "dead"]
    num_cats = random.randint(2, 4)  # Randomly choose between 2 to 4 cats
    actual_cat_states = [random.choice(cat_states) for _ in range(num_cats)]
    
    # Display the number of cats
    print("There are", num_cats, "cats in the box.")
    
    guess = input("Do you think all the cats are alive or dead? ").lower()
    
    # Check if time is up
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time's up! You didn't make a guess in time.")
        print("The actual states of the cats were:", actual_cat_states)
        return
    
    # Check if the guess is correct
    if guess == "alive" or guess == "dead":
        if all(cat_state == guess for cat_state in actual_cat_states):
            print("Congratulations! You guessed correctly. All the cats are indeed", guess + ".")
        else:
            print("Sorry, you guessed wrong. The actual states of the cats were:", actual_cat_states)
    else:
        print("Invalid input. Please enter 'alive' or 'dead'.")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        schrodingers_cat_game()
    else:
        print("Thank you for playing Schrödinger's Cat Game!")

schrodingers_cat_game()
