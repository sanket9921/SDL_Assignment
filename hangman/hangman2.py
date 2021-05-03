import time
import random

name = input("What is your name ?")
print("Hello " + name, "Time to play")

time.sleep(1)

print("Start guessing....")
time.sleep(0.5)

words = ["apple", "king", "sparrow", "mango", "door", "monkey", "peacock", "elephant", "house", "happy", "dog", "ball",
         "ground", "rose", "table", "mouse", "wood", "book", ]
n = random.randint(0, 17)
word = words[n]
guesses = ""

turns = 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("you won")
        break
    guess = input("guess the word :")
    guesses += guess[0]
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", +turns, "more guesses")

    if turns == 0:
        print("you loss")

print("The word is : ", word)
