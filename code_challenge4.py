print("Heyy you!!, Welcome to the Mangga Reader recommendation!!")
print("Answer a few question  to find your next read")
genre = input("What genre do you like ( School, Horror, Adventure) --> ")

if genre.lower() == "school":
    mangga_duration = input("How long should the mangga be? (short, medium, long)--> ")
    if mangga_duration.lower() == "short":
        decades = input("Which decades ? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend: \n\t\t\"A Moment in the Hallway\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Hotaru\"")
            print("ENJOY READING")
    elif mangga_duration.lower() == "medium":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"Ao Haru Ride\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"We Never Learn\"")
            print("ENJOY READING")
    elif mangga_duration.lower() == "long":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"Kimi ni Todoke\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"My Hero Academia\"")
            print("ENJOY READING")

elif genre.lower() == "horror":
     mangga_duration = input("How long should the mangga be? (short, medium, long)--> ")
     if mangga_duration.lower() == "short":
        decades = input("Which decades ? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend: \n\t\t\"Hideout\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Blood on the Tracks\"")
            print("ENJOY READING")
     elif mangga_duration.lower() == "medium":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"Happines\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Dandadan\"")
            print("ENJOY READING")
     elif mangga_duration.lower() == "long":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"Terra Formars\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Chainsaw Man\"")
            print("ENJOY READING")

elif genre.lower() == "adventure":
     mangga_duration = input("How long should the mangga be? (short, medium, long)--> ")
     if mangga_duration.lower() == "short":
        decades = input("Which decades ? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend: \n\t\t\"Alice in Borderland: Retry\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Time Paradox Ghostwriter\"")
            print("ENJOY READING")
     elif mangga_duration.lower() == "medium":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"Attack on Titan\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Fieren: Beyond Journey's End\"")
            print("ENJOY READING")
     elif mangga_duration.lower() == "long":
        decades = input("Which decades? (2010s, 2020s) --> ")
        if decades.lower() == "2010s":
            print("We recommend : \n\t\t\"One Piece\"")
            print("ENJOY READING")
        elif decades.lower() == "2020s":
            print("We recommend : \n\t\t\"Black Cover\"")
            print("ENJOY READING")
else :
    print("Ivalid Genre")



 