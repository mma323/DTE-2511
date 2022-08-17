class Vehicle:
    def __init__(self, 
        merke, aars_modell, kilometer_stand, pris, 
        bilnummer, tickets=set()
    ):
        self.merke           = merke
        self.aars_model      = aars_modell
        self.kilometer_stand = kilometer_stand
        self.pris            = pris
        self.bilnummer       = bilnummer
        self.tickets         = tickets

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

    def set_bilnummer(self, bilnummer):
        self.bilnummer = bilnummer

    def get_bilnummer(self):
        return self.bilnummer

    def add_ticket(self, ticket):
        self.tickets.add(ticket)

    def remove_ticket(self, ticket):
        self.tickets.remove(ticket)
    
    def get_tickets(self):
        return self.tickets
    
    def __str__(self):
        return (
            f"Merke: {self.merke} \n" +
            f"Årsmodell: {self.aars_model} \n" +
            f"Kilometerstand: {self.kilometer_stand} km \n" +
            f"Pris: {self.pris} kr \n"
            f"Registreringsnummer: {self.bilnummer} \n"
        )

    #For å sortere i car_truck_suv_demo.py
    def __lt__(self, other):
        return self.pris < other.pris


class Car(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, 
                 antall_dorer, bilnummer, tickets=set() ):
        super().__init__(
            merke, aars_modell, kilometer_stand, pris, bilnummer, tickets=set()
            )
        self.antall_dorer = antall_dorer

    def set_antall_dorer(self, antall_dorer):
        self.antall_dorer = antall_dorer

    def get_antall_dorer(self):
        return self.antall_dorer

    def __str__(self):
        return super().__str__() + f"Antall dører: {self.antall_dorer} \n"
    
class Truck(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, hjuldrift,
                bilnummer, tickets=set()
    ):
        super().__init__(
            merke, aars_modell, kilometer_stand, pris,
            bilnummer, tickets=set()
        )
        self.hjuldrift = hjuldrift
    
    def set_hjuldrift(self, hjuldrift):
        self.hjuldrift = hjuldrift

    def get_hjuldrift(self):
        return self.hjuldrift
    
    def __str__(self):
        return super().__str__() + f"Hjuldrift: {self.hjuldrift} \n"

class SUV(Vehicle):
    def __init__(self, merke, aars_modell, kilometer_stand, pris, 
                 passasjer_kapasitet, bilnummer, tickets=set()):
        super().__init__(
            merke, aars_modell, kilometer_stand, pris,
            bilnummer, tickets=set())
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

class SpeedTicket:
    def __init__(self, bilnummer, tidspunkt, hastighet, fartsgrense=60):
        self.bilnummer   = bilnummer
        self.tidspunkt   = tidspunkt
        self.hastighet   = hastighet
        self.fartsgrense = fartsgrense

    def set_bilnummer(self, bilnummer):
        self.bilnummer = bilnummer

    def get_bilnummer(self):
        return self.bilnummer

    def set_tidspunkt(self, tidspunkt):
        self.tidspunkt = tidspunkt
    
    def get_tidspunkt(self):
        return self.tidspunkt

    def set_hastighet(self, hastighet):
        self.hastighet = hastighet

    def get_hastighet(self):
        return self.hastighet
    
    def set_fartsgrense(self, fartsgrense):
        self.fartsgrense = fartsgrense
    
    def get_fartsgrense(self):
        return self.fartsgrense

    def __str__(self):
        return (
            f"Hastighet: {self.get_hastighet()} " +
            f"Fartsgrense: {self.get_fartsgrense()} " + 
            f"Tidspunkt: {self.get_tidspunkt()} "
        )

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
