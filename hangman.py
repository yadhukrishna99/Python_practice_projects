from words import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    # while '-' in word or ' ' in word:
    #     word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_set = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = len(word)

    while len(word_set) != 0 and lives > 0:
        print("You have", lives, "left.....You have used these letters: ", ' '.join(used_letters))
        words_found = []
        for letter in word:
            if letter in used_letters:
                words_found.append(letter)
            else:
                words_found.append('-')
        print("Current word: ", ' '.join(words_found))

        user_letter = input("Enter an alphabet: ").upper()

        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_set:
                word_set.remove(user_letter)
            else:
                lives -= 1

        elif user_letter in used_letters:
            print("You have already used this letter.Try different letter")

        else:
            print("Invalid Letter...Use a valid alphabet")

    # if, while statement executes false then this code will be executed
    if lives == 0:
        print(f"Sorry,Your life is over...The correct word is {word}")
    else:
        print(f"You found the word {word}")


hangman()

