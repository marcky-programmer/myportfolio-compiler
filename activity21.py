isCoughing = True
talk = 0

while isCoughing == True:
    confirm = input("Do you cough (yes / no): ").lower()
    if confirm == "yes":
        print("your coughing ")
        talk += 1
        continue
    else:
        print("ahh congrats you stop coughing")
        break
print(f" The total cough you did is {talk}")