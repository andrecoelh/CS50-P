import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

numero = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess <= 0:
            continue

        if guess < numero:
            print("Too small!")
        elif guess > numero:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass