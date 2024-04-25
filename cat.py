import random

def schrodingers_cat_game():
    print("Welcome to Schrödinger's Cat Game!")
    print("You are in a room with a sealed box. Inside the box, there may be a cat, and it may be alive or dead.")
    print("Your task is to guess the state of the cat without opening the box.")
    print("Let's begin!")
    
    cat_states = ["alive", "dead"]
    actual_cat_state = random.choice(cat_states)
    
    guess = input("Do you think the cat is alive or dead? ").lower()
    
    if guess == actual_cat_state:
        print("Congratulations! You guessed correctly. The cat is indeed", actual_cat_state + ".")
    else:
        print("Sorry, you guessed wrong. The cat is actually", actual_cat_state + ".")
    
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        schrodingers_cat_game()
    else:
        print("Thank you for playing Schrödinger's Cat Game!")

schrodingers_cat_game()
