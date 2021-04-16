# Number Guessing Game
import time, random, math
print('***Welcome to Number Guessing Game***')
time.sleep(1)
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
secret_number = random.randint(lower, upper)
total_guess_allowed = round(math.log2(upper - lower + 1))
guess_taken = 1
while guess_taken <= total_guess_allowed:
    print(f'You have {total_guess_allowed  + 1 - guess_taken} guesses left to guess the correct number.')
    try:
        guess = int(input('Enter your guess: '))
    except:
        print('Hint: Enter a number nothing else.')
        continue
    if guess == secret_number:
        break
    elif guess > secret_number:
        print('You Guessed too High.')
    else:
        print('You Guessed too Small.')
    guess_taken += 1

if guess == secret_number:
    print(f'\tCORRECT GUESS \n\tYou guessed the number in {guess_taken} guesses.')
else:
    print(f'\tThe number is {secret_number}')
    print('\tBetter Luck Next Time')
