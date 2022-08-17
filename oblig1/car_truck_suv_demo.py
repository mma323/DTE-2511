# This program creates a Car object, a Truck object,
# and an SUV object.
import pickle
import vehicles
import os.path

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():

    if not os.path.isfile("vehicles.dat"):
        vehicles_list = []
    else:
        try:
            vehicles_file = open("vehicles.dat", "rb")
            vehicles_list = pickle.load(vehicles_file)
            vehicles_file.close()
        except EOFError: 
            vehicles_list = []

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Only integers")

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            new_car = vehicles.Car("", 0, 0, 0, 0)
            new_vehicle(new_car)
            antall_dorer = input("Skriv inn antall dører: ")
            new_car.set_antall_dorer(antall_dorer)
            vehicles_list.append(new_car)

        elif choice == NEW_TRUCK_CHOICE:
            new_truck = vehicles.Truck("", 0, 0, 0, "2WD")
            new_vehicle(new_truck)
            hjuldrift_options = ["2WD", "4WD"]
            
            #Bygger string med alternativer for hjuldrift til brukeren
            hjuldrift_options_str = f""
            for hjuldrift_option in hjuldrift_options:
                hjuldrift_options_str += f"{hjuldrift_option}/"

                if hjuldrift_option == hjuldrift_options[-1]:
                    hjuldrift_options_str = (
                        hjuldrift_options_str.rstrip(hjuldrift_options_str[-1])
                    )

            while True:
                hjuldrift = input(
                    f"Skriv inn hjuldrift ({hjuldrift_options_str}): "
                    )
                if hjuldrift in hjuldrift_options:
                    break
                else:
                    print(
                        f"Aksepterte verdier: {hjuldrift_options_str} "
                    )

            new_truck.set_hjuldrift(hjuldrift)
            vehicles_list.append(new_truck)

        elif choice == NEW_SUV_CHOICE:
            new_SUV = vehicles.SUV("", 0, 0, 0, 0)
            new_vehicle(new_SUV)
            passasjer_kapasitet = input("Skriv inn passasjerkapasitet: ")
            new_SUV.set_passasjer_kapasitet(passasjer_kapasitet)
            vehicles_list.append(new_SUV)

        elif choice == FIND_VEHICLE_CHOICE:
            searched_vehicle = input("Søk etter bilmerke: ")
            vehicles_found = 0
            for vehicle in vehicles_list:
                if vehicle.get_merke() == searched_vehicle:
                    print(vehicle)
                    vehicles_found +=1
            if vehicles_found == 0:
                print("Ingen biler med dette bilmerket funnet")
                    
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)  
                
        elif choice == QUIT_CHOICE:
            vehicles_list = sorted(vehicles_list)
            add_vehicles_to_file(vehicles_list)
            print('Exiting the program...')   

        else:
            print('Enter a number between 1 and 6')

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     

def new_vehicle(vehicle):
    merke = input("Skriv inn merke: ")
    aars_modell = input("Skriv inn årsmodell: ")
    kilometer_stand = input("Skriv inn kilometerstand: ")
    pris = input("Skriv inn pris: ")

    vehicle.set_merke(merke)
    vehicle.set_aars_modell(aars_modell)
    vehicle.set_kilometer_stand(kilometer_stand)
    vehicle.set_pris(pris)

def add_vehicles_to_file(vehicles):
    vehicles_file = open("vehicles.dat", "wb")
    pickle.dump(vehicles, vehicles_file)
    vehicles_file.close()

# Call the main function.
if __name__ == '__main__':
      main()