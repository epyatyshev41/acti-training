class Customer(object):
    """
    Class for customers in movies rent store
    """

    def __init__(self, name):
        self.name = name
        self.rentals_info = []

        self.total_dept = 0.0
        self.total_bonus = 0.0

    def add_rental(self, rental):

        rental_dept = rental.movie.get_price(
            rental.days_rented)
        self.total_dept += rental_dept
        self.rentals.append(
            {"title" : rental.movie.title, "dept": rental_dept})
