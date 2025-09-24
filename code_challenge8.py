print("MULTIPLICATION TABLE MAKER")
number = eval(input("Enter a number: "))
print("\nMultiplication table for:", number)
for i in range(1,11,1):
    answer = i * number
    print(number,"x", i,"=",answer)
 
   