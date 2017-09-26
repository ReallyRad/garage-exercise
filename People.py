class Person:
    #TODO for Alberto
    # people, wake up, go to work or look for garage, have vehicles
    def __init__(self, name, vehicles=None, ):
        self.name = name

    def wake_up(self):
        raise NotImplementedError('implement in the child class')


class Client(Person):
    global Vehicle
    def wake_up(self):
        if Vehicle.crash:
            return drive_vehicle
        else:
            return Vehicle.sayfixed

    def drive_vehicle(self):
        good_conditions = 6
        good_conditions =- 1
        if good_conditions == 0:
            return Vehicle.crash




class Mechanic(Person):
    #TODO for Rachel
    # has skills, repairs vehicle, name

    def __init__(self, skills):
        self.skills = skills

    def wake_up(self):
        pass
