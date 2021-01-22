from random import random
from time import perf_counter

randVal = random()

print(randVal)

upper = 1.0
lower = 0.0

guess = 0.5

startTime = perf_counter()
while(True):
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess
    
    guess = (upper+lower)/2
finishTime = perf_counter()

duration = (finishTime-startTime)

print(guess)
print(duration)