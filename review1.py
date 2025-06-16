# Python review exercise: guess the random number between 0-100
import random # we need a way to make random numbers

target = random.randint(0,100) # up to 100 inclusive
primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
guess_counter = 0

while True: # keep going!!
    guess_counter += 1
    guess = int(float(input('guess:'))) # make sure it's an int
    # conditionally act on the guess
    if guess == -2: # do they want a clue
        # odd or even
        if target//2 == target /2:
             print('Even')
        else:
             print('Odd')
        # square number
        if (target**0.5) == int(target**0.5):
             print('Square')
        # prime number
        if target in primes_t:
             print('Prime')
    elif guess == -1: # do they want to quit
        print (f'it was {target}' )
        break
    elif guess > target: # is the guess too high
        print('too high')
    elif guess < target: # is the guess too low (could be an else clause)
        print('too low')
    else:
        print(f'correct it was {target} you took {guess_counter} tries' )
        break