import random

random_number = random.randint(1,10)
guess = None
    
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_number :
        print("Too low! try again")
    elif guess > random_number :
        print("Too high! try again")
    else:
        print("You won")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")
            break        

    
     
