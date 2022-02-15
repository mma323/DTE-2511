capitals_file = open(r"USCapitals.txt", "r") 
capitals = {}

for line in capitals_file:
    line = line.split(",")
    state = line[0]
    capital = line[1]
    capital = capital.strip("\n")   #Ønsker ikke få med linjeskifte
    capitals[state] = capital

capitals_file.close()

while True:
    try:
        user_keyword = input("Oppgi en stat: ")
        print(f"{capitals[user_keyword]}")
    except KeyError:
        print("Oppgi en gyldig stat ")
    else:
        break