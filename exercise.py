class Garage:
    #     has mechanics, has vehicles to repair, has clients, checks availability, accepts transaction, reject,
    #     saying "Thanks for trusting our garage! Come back next morning as if nothing had happened"
    def __init__(self, mechanics):
        self.mechanics = mechanics

    def accept_transaction(self):
        # TODO for Levan
        pass

    def check_availbaility(self):
        #TODO for Roman
        pass

    def reject(self):
        #TODO for Roman
        pass

    def say_thanks(self):
        # TODO for Levan
        pass

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

days_elapsed = 0
#bunch of initializiations for our simulation

#TODO For Alberto
import People
import Vehicles
toni_mech = People.Mechanic(name='Toni', skills={'Car': 2, 'Motorbike': 1, 'Bicycles': 0.5})
george_mech = People.Mechanic(name='George', skills={'Car': 1, 'Motorbike': 1, 'Bicycles': 1})
toyota = Vehicles.Car()
ford = Vehicles.Car()
honda = Vehicles.Motorbike()
yamaha = Vehicles.Motorbike()
orbea = Vehicles.Bicycles()
bwin = Vehicles.Bicycles()
paul_client = People.Client(name='Paul', vehicles=[toyota, orbea])
peter_client = People.Client(name='Peter', vehicles=[honda, bwin, yamaha])
repair_everything_garage = Garage([toni_mech, george_mech])


while True: #loop for each day
    #TODO for Maria
    #people wake up
    #clients drive or go to garages
    #transactions get accepted or rejected
    #Vehicles get fixed

    days_elapsed += 1