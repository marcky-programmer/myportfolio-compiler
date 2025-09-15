print("ODD number summation")
sum = 0
for i in range(1,8,1):
    number = eval(input("Enter a number --> "))
    if number % 2 != 0:
         sum += number
print("The sum of all odd nnumbers is", sum)


