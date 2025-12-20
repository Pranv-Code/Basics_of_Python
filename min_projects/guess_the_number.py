import random as r

num = r.randint(1,20)
print(f"{num}")
guess = int(input("Guess the number between 1 - 20 :"))

if guess == num:
    print("You guessed it right ")
else :
    print(f"Number was {num}")