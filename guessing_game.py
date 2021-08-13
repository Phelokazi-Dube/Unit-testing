import random

def generate_number():
    n = random.randint(1, 100)
    return n

def user_guess():
    guess = int(input())
    return guess

def compare_numbers(guess, n):
    if guess > 100 or guess < 0:
        raise ValueError("Invalid input your number must be between 1 to 100")
    if type(guess) is not int:
        raise TypeError("Invalid input your number must be an integer")
    if guess > n:
        return "You have guessed incorrectly the number is too high "
    elif guess < n:
        return "You have guessed incorrectly the number is too low "
    else:
        return "You have guessed correctly!"

def menu():
    num_of_guesses = 0
    n = generate_number()
    while num_of_guesses < 5:
        print("Enter a number from 1 to 100 : ")
        guess = user_guess()
        num_of_guesses = num_of_guesses + 1
        message = compare_numbers(guess, n)
        print(message)
        if message=="You have guessed correctly!":
           break
    else:
        print('You did not guess the number and exceded your trials, The number was ' + str(n))
if __name__=='__main__':
  menu()
