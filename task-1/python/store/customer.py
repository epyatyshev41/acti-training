class Customer(object):
    """
    Class for customers in movies rent store
    """

    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)
