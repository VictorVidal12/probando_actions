import random
import os

while True:
    print("----------------Welcome To Russian Roulette-------------")
    number = random.randint(0, 5) + 1                                        
    if number == random.randint(0, 5) + 1:
        print("You lose.")
        break
    else:
        print("You win.")
        break
