# Find the grater number of two numbers 

num1,num2=int(input("Enter first number ")),int(input("Enter second number "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"Numbers are equal")
    