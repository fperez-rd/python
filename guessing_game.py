from random import randint

randVal = randint(0,100)

while(True):
    guess = int(input("Please enter your guess: "))
    if guess == randVal:
        break
    elif guess < randVal:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

print("Your guessed correctly with:",randVal)