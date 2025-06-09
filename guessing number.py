import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
sorandom = random.randint(1,100)
difficulty = int(input("Enter your choice : "))

def attempts(a):
    if a == 1:
        return "Easy difficulty level", 10
    elif a == 2:
        return "Medium difficulty level", 5
    elif a == 3:
        return "Hard difficulty level", 3
    else:
        return "Medium difficulty level by default", 5
level, soattemps = attempts(difficulty)
print(f"Great! You have selected the {level} and you have {soattemps} attempts\nLet's start the game!")




while soattemps > 0:
    guess = int(input(f"Attempts : {soattemps} Enter your guess : "))
    if guess == sorandom:
        print(f"Congratulations! You guessed the correct number in {soattemps}")
        break
    elif guess > sorandom:
        print(f"Incorrect! The number is less than {guess}.")
        soattemps -= 1
    elif guess < sorandom:
        print(f"Incorrect! The number is greater than {guess}.")
        soattemps -= 1
    if soattemps == 0:
        print("You have lost the game (out of attempts)")
