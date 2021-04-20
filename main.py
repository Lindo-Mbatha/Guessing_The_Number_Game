import random
from logo import Logo
from logo import number

print(Logo)
print("I'm thinking of a number between 1 and 100, can you guess it?")
computer_answer = random.choice(number)
player_answer = input("Please choose a difficulty level. Type 'easy' or 'hard': ").lower()

player_score = 10
player_score2 = 5

x = " "

if player_answer == "easy":
    print("You have 10 guesses to guess the right number")
    while computer_answer is not True:
        print(x)
        player_answer2 = int(input("What's your guess: "))
        player_score = player_score - 1
        if player_answer2 == computer_answer:
            print(f"You Win! The answer was {computer_answer}")
            break
        elif player_score == 0:
            print("Sorry, you lose")
            print(f"The right number was {computer_answer}")
            break
        elif player_answer2 > computer_answer:
            print("Your answer is too high")
            print(f"You have {player_score} guesses left")
        elif player_answer2 < computer_answer:
            print("Your answer is too low")
            print(f"You have {player_score} guesses left")
elif player_answer == "hard":
    print("You have 5 guesses to guess the right number")
    while computer_answer is not True:
        print(x)
        player_answer2 = int(input("What's your guess: "))
        player_score2 = player_score2 - 1
        if player_answer2 == computer_answer:
            print(f"You Win! The answer was {computer_answer}")
            break
        elif player_score2 == 0:
            print("Sorry, you lose")
            print(f"The right number was {computer_answer}")
            break
        elif player_answer2 > computer_answer:
            print("Your answer is too high")
            print(f"You have {player_score2} guesses left")
        elif player_answer2 < computer_answer:
            print("Your answer is too low")
            print(f"You have {player_score2} guesses left")
else:
    print("Invalid input, please try again")
