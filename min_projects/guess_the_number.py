import random as r

num = r.randint(1,20)
print(f"{num}")
print("Guess the number between 1 - 20 in 5 chances  :")

for i in range (1,6):
    guess=int(input("Enter number : "))
    if guess == num:
        print("You guessed it right ")
        break
    else :
        print(f"{5-i} chances left ")
else:
    print(f"Number was {num}")