class Person:
    #TODO for Alberto
    # people, wake up, go to work or look for garage, have vehicles
    def __init__(self, name, vehicles=None, ):
        self.name = name

    def wake_up(self):
        raise NotImplementedError('implement in the child class')


class Client(Person):
    #TODO for Franco
    def wake_up(self):
        pass
    # check if broken vehicles
    # if broken vehicles, look for garage
    # else drive your car

    def drive_vehicle(self):
        pass


class Mechanic(Person):
    #TODO for Rachel
    # has skills, repairs vehicle, name

    def __init__(self, skills):
        self.skills = skills

    def wake_up(self):
        pass
