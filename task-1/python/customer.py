class Customer(object):

    def __init__(name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)
