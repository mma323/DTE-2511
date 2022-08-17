#radars.py

from datetime import datetime

# # Fastgitte variabler
# # Distanse på 5 km
# distance = 5
# # Speed limit 60 kmt
# speed_limit = 60


# Funksjonen lagrer filename til en dictionary og returnerer den. En error melding blir printet hvis filename ikke finnes samt en tom dictionary returneres
def fileToDictionary(filename):
    try:
        inputfile = open(filename, "r")
        file_dictionary = {}
        for line in inputfile:
            # Verdiene splittes inn i en tuple før de setter inn i file_dictionary
            key, value = line.strip().split(",")
            file_dictionary[key] = value[1::]
        inputfile.close()
        return file_dictionary

    except FileNotFoundError:
        print(f"\nWARNING!!! The file {filename} does not exist in current working directory\n")
        return {}

# listSpeeders eller list_speeders ????
def list_speeders(filname_a, filname_b, speed_limit, distance):
    ticket_dictionary = {}

    # Går gjennom alle elementene i dictionary A, skjekker de opp mot coresponderende regnr i dictionary B. Konverterer tiden til sekunder og kalkulerer gjennomsnitshastighet.
    for key in filname_a:
        if key in filname_b:
            time_a = datetime.strptime(filname_a[key], "%Y-%m-%d %H:%M:%S")
            time_b = datetime.strptime(filname_b[key], "%Y-%m-%d %H:%M:%S")
            speed = distance / (abs(time_a.timestamp()-time_b.timestamp()) / 3600)
            
            # Tester gjennomsnitshastighet mot fartsgrense + 5%, skjekker så hvilken fotobox som tok bilde sist. Legger dette til en dictionary med regnr som key
            if speed > speed_limit * 1.05:
                if time_a > time_b:
                    ticket_dictionary[key] = (round(speed, 3), filname_a[key])
                if time_a < time_b:
                    ticket_dictionary[key] = (round(speed, 3), filname_b[key])
    return ticket_dictionary
