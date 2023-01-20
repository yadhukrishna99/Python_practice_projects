import random


def play():
    user = input("What is your choice? 'r' for stone, 'p' for paper and 's' for scissor:\n ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if win(user, computer):
        return "You win!"

    return "You loose!  Computer won the game"


def win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True


while True:
    print(play())

