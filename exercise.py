class Garage:
    #     has mechanics, has vehicles to repair, has clients, checks availability, accepts transaction, reject,
    #     saying "Thanks for trusting our garage! Come back next morning as if nothing had happened"
    def __init__(self, mechanics):
        self.mechanics = mechanics

    def accept_transaction(self):
        # TODO for Levan
        pass

    def check_availbaility(self, vehicle):
        for skills in self.mechanics.skills:
            if skills is vehicle:
                self.accept_transaction()
            else:
                self.reject()

    def reject(self):
        print("We are sorry we can't fix your vehicle, please try another garage")

    def say_thanks(self):
        # TODO for Levan
        pass

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

days_elapsed = 0
#bunch of initializiations for our simulation
#TODO For Alberto

while True: #loop for each day
    #TODO for Maria
    #people wake up
    #clients drive or go to garages
    #transactions get accepted or rejected
    #Vehicles get fixed

    days_elapsed += 1