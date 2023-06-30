import random

real = random.randint(1,100)
print("real:", real)

low = 1
high = 100

num_guesses = 0
while high >= low:
    guess = (high+low)//2
    num_guesses += 1
    if guess == real:
        print(guess)
        print(num_guesses)
        break
    elif real < guess:
        high = guess-1
    elif real > guess:
        low = guess+1

if high < low:
    print("Not in the range")
