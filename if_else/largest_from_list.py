# Find largest from list
l=[]
print("Enter 5 numbers :")
for i in range(5):
    l.append(int(input(f"Enter {i+1} number : ")))
print(f"Your list : {l}")

largest = 0
for i in l:
    if i > largest:
        largest=i

print(f"Largest : {largest}")