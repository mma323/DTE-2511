class Vehicle:
    def __init__(self, merke, aars_modell, kilometer_stand, pris):
        self.merke = merke
        self.aars_model = aars_modell
        self.kilometer_stand = kilometer_stand
        self.pris = pris

    def set_merke(self, merke):
        self.merke = merke   

    def get_merke(self):
        return self.merke
    
    def set_aars_modell(self, aars_modell):
        self.aars_model = aars_modell

    def get_aars_modell(self):
        return self.aars_model

    def set_kilometer_stand(self, kilometer_stand):
        self.kilometer_stand = kilometer_stand

    def get_kilometer_stand(self):
        return self.kilometer_stand

    def set_pris(self, pris):
        self.pris = pris

    def get_pris(self):
        return self.pris
    
    def __str__(self):
        return (
            f"Merke: {self.merke} \n" +
            f"Årsmodell: {self.aars_model} \n" +
            f"Kilometerstand: {self.kilometer_stand} km \n" +
            f"Pris: {self.pris} kr \n"
        )

    #For å sortere i car_truck_suv_demo.py
    def __lt__(self, other):
        return self.pris < other.pris


class Car(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, 
                 antall_dorer):
        super().__init__(merke, aars_modell, kilometer_stand, pris)
        self.antall_dorer = antall_dorer

    def set_antall_dorer(self, antall_dorer):
        self.antall_dorer = antall_dorer

    def get_antall_dorer(self):
        return self.antall_dorer

    def __str__(self):
        return super().__str__() + f"Antall dører: {self.antall_dorer} \n"
    
class Truck(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, hjuldrift):
        super().__init__(merke, aars_modell, kilometer_stand, pris)
        self.hjuldrift = hjuldrift
    
    def set_hjuldrift(self, hjuldrift):
        self.hjuldrift = hjuldrift

    def get_hjuldrift(self):
        return self.hjuldrift
    
    def __str__(self):
        return super().__str__() + f"Hjuldrift: {self.hjuldrift} \n"

class SUV(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, 
                 passasjer_kapasitet):
        super().__init__(merke, aars_modell, kilometer_stand, pris)
        self.passasjer_kapasitet = passasjer_kapasitet

    def set_passasjer_kapasitet(self, passasjer_kapasitet):
        self.passasjer_kapasitet = passasjer_kapasitet
    
    def get_passasjer_kapasitet(self):
        return self.passasjer_kapasitet
    
    def __str__(self):
        return (
            super().__str__() + 
            f"Passasjerkapasitet: {self.passasjer_kapasitet} \n"
        )

