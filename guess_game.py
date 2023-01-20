import random
import time


# Computer guessing our number
def guess_num(num):
    low = 0
    high = num
    user = ''
    lives = 5
    while user != 'c' and lives > 0:
        guess = random.randint(low, high)
        user = input(f"Computer has {lives} lives left\nIs {guess} a correct guess..?\nIf this is High then enter(H), "
                     f"If this is low then enter(L), If this is correct then enter(C): ").lower()
        if user == 'h':
            high = guess - 1
            lives -= 1
        elif user == 'l':
            low = guess + 1
            lives -= 1

    if lives == 0:
        print("Hurray!...Computer Lost all its life....You won!!")
    else:
        print(f"Alas!...Computer found your number {guess} correctly!...")


# while True:
#     time.sleep(1.0)
#     guess_num(100)


# We guessing computers number
def guess_comp_num():
    low = 1
    high = 100
    comp_num = random.randint(low, high)
    user = 0
    lives = 5
    while user != comp_num and lives > 0:
        user = int(input(f"Enter a number between {low} and {high}: "))
        if user > comp_num:
            lives -= 1
            high = user
            print(f"Too High!... Guess Lower number\nYou have only {lives} lives left")

        elif user < comp_num:
            lives -= 1
            low = user
            print(f"Too Low!... Guess Higher number\nYou have only {lives} lives left")

    if lives == 0:
        print(f"Sorry...Your lives are over..The correct guess is {comp_num}")
    else:
        print(f"Hurray!...You guessed the computer's number {comp_num} correctly")


while True:
    guess_comp_num()





