print("🦜 PARROT SIMULATOR -  THE ECHO CHAMBER!")
phrase = input("What do you want your parrot to say ? Enter a phrase --> ")
repetition = eval(input("How many times should the parrot squawk it ? "))
print("\nListen to your parrot 🦜:")
for i in range(0 , repetition , 1):
    print("🦜 Squawk!", phrase) 