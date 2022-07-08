import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess > x or guess < 1:
            print('Invalid number. Try again')
        elif guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high!')
    
    print(f'congratulations. You have correctly guess the random number {random_number}')

def start():
    starting_number = int(input('Enter a number to start the game : '))
    guess(starting_number)

start()

