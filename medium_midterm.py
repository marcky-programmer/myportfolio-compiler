for i in range(1,7,1):
    for j in range(7,i,-1):
        print(" ",end="")
    for k in range(0,i,1):
        print("*",end=" ")
    print()

number = eval(input("Enter a number--> "))

for i in range(1,11,1):
    for j in range(1,number+1,1):
        
        print(f"{i} x {j} = {i*j}",end="\t")
    print()
    
