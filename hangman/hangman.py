import random

n = random.randint(1, 99)
guess = int(input("Guess the integer form 1 to 99 :"))
while n != "guess":
    if guess < n:
        print("Guess is low")
        guess = int(input("Enter the integer form 1 to 99"))
    elif guess > n:
        print("Guess is high")
        guess = int(input("Enter the integer form 1 to 99"))
    else:
        print("you Guessed it")
        break
