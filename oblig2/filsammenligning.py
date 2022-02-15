def main():
    while True:
        try:
            file_1 = get_file("fil 1")
            file_2 = get_file("fil 2")
        except FileNotFoundError:
            print("Fil ikke funnet")
        else:
            break

    words_in_file_1 = get_words_in_file(file_1)
    words_in_file_2 = get_words_in_file(file_2)

    print(f"Antall unike ord i fil 1: {len(words_in_file_1)}")
    print(f"Antall unike ord i fil 2: {len(words_in_file_2)}")
    print(f"Unike ord i fil 1: {words_in_file_1}")
    print(f"Unike ord i fil 2: {words_in_file_2}")
    print(f"Forekommer i fil 1 OG fil 2: {words_in_file_1 & words_in_file_2}")
    print(
        "Forekommer i fil 1, men ikke fil 2: " 
        f"{words_in_file_1 - words_in_file_2}"
        )
    print(
        "Forekommer i fil 2, men ikke i fil 1: " 
        f"{words_in_file_2 - words_in_file_1}"
        )
    print(
        "Forekommer i fil 1 ELLER fil 2, men ikke i begge: "
         f"{words_in_file_1 ^ words_in_file_2}"
        )


def get_file(file_name="file"):
    file = input(f"Enter {file_name}: ")
    file = open(r"{}".format(file), "r") 
    return file


def get_words_in_file(file):
    words_in_file = set()
    for line in file:
        line = line.lower() #Ikke unikt ord ved ulik bokstavstørrelse
        words_in_line = set(line.split())
        for word in words_in_line:
            words_in_file.add(word)
    return words_in_file


main()