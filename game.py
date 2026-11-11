import random

def play_game():
    lucky_number=random.randint(1,50)

    while True:
        guess_lucky_number=int(input("enter the number:"))
        if guess_lucky_number==lucky_number:
            print("finally you got the lucky number \n" 
            "game over")
            print("thank you for playing the game")
            break

        elif guess_lucky_number>lucky_number:
            print("your guess is too high")
        else:
            print("your guess is too low")

       

play_game()