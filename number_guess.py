import random


def guess_num_game(winning_number):

    number = int(input("Guess a number: "))
    while 0 <= number <= 100:
        if number > winning_number:
            print("You have guessed too high")
        elif number < winning_number:
            print("You have guessed too low")
        else:
            print("You got it number was: ", winning_number)
            break
        number = int(input("Guess a number: "))
    else:
        print("You have exited too early winning number was, ", winning_number)


print("Winning number is between 0 to 100 inclusive")
guess_number = random.randint(0, 100)
guess_num_game(guess_number)