import random
import sys


def start_game():
    
    print("""
---------------------------------------
Welcome to the number guessing game!
---------------------------------------
    """)
    
    highscore = 1000
    replay = "yes"
    
    while replay == "yes":
        
        RANDOM_NUMBER = random.randint(1,10)
        attempts = 1
        user_number = 0
        
        while user_number != RANDOM_NUMBER: 
            print(RANDOM_NUMBER)
            try:
                user_number = int(input("Pick a number between 1 and 10: "))
                if user_number > 10 or user_number < 1:
                    raise ValueError("It needs to be a number between 1 and 10")
                elif user_number > RANDOM_NUMBER:
                    print("It is a lower!")
                    attempts += 1
                elif user_number < RANDOM_NUMBER:
                    print("It is a higher!")
                    attempts += 1
            
            except ValueError as err:
                print("Oh no! That's not a valid value.")
                print("({})".format(err))
                sys.exit(1)
        
        if attempts < highscore:
            highscore = attempts
        
        print("You got it! It took you {} tries".format(attempts))
        print("The highscore is {}".format(highscore))
        
        replay = (input("Do you want to play this game again?(yes/no) ")).lower()
        
    print("Goodbye, Hope you enjoyed the game")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()