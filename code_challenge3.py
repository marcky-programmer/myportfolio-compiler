name = input("Whats your name ---> ")
print("from Lucena to Sariaya is 20 pero merong student discount".upper())
isStudent = input("Are you a student? (yes or no) ---> ")

if isStudent.lower() == "yes":
    print("Your eligible for student discount", name)
    fare = 20 * .2
    new_fare = 20 - fare
    print("Dahil ikaw ay student ang babayaran mo nalang ay", new_fare)
    bayad = eval(input("Enter your bayad ---> "))
else:
    print("Sorry, your not eligible for student discount", name, ":<")
