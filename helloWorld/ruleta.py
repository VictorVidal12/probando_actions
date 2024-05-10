import random
import os

while True:
    print("----------------Welcome To Russian Roulette-------------")
    acc = str(input("Deseas jugar? (Y/N): "))
    if acc == "Y":
        number = random.randint(0, 5) + 1                                        
        if number == random.randint(0, 5) + 1:
            print("You lose.")
        else:
            print("You win.")
    else:
        print("Vuelva pronto.")
