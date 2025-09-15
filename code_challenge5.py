print("THE FACTORIAL program")

total = 1
factorial = eval(input("Enter a number --> "))
for i in range( factorial, 0,-1):
    total *= i
print("The factorial of", factorial , "is", total)