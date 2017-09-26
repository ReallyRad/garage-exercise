class Vehicle:
    #TODO for Ye
    def __init__(self):
        self.working = True

    def crash(self):
        self.working = False

    def sayFixed(self):
        raise NotImplementedError('implement in the child class!')

    def repair(self):
        self.working = True
        self.sayFixed()

    def drive(self):
        raise NotImplementedError('implement in the child class!')

class Car(Vehicle):

    def drive(self):
        print("Vrooom")

    def sayFixed(self):
        print("car fixed")

class Motorbike(Vehicle):
    def drive(self):
        print("Meeee")

    def sayFixed(self):
        print("Motorbike fixed")


class Bicycles(Vehicle):
    def drive(self):
        print("dring")

    def sayFixed(self):
        print("bicycle fixed")
