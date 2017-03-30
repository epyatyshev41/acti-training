class Rental(object):

    def __init__(movie, days_rented, pricing_system):
        self.movie = movie
        self.days_rented = days_rented
        self.pricing_system = pricing_system
        self.dept = 0

    def score_total_dept(self):

        self.dept += self.pricing_system.score(self.movie)

class RentalWithBonuses(Rental):

    def __init__(movie, days_rented, pricing_system, bonuses_list):
        super(RentalWithBonus, self).__init__(
            movie, days_rented, pricing_system)
        self.bonuses_list = bonuses_list

    def score_total_dept(self):

        self.dept += self.pricing_system.score(self.movie)
        for bonus in self.bonuses_list:
            self.dept += bonus.score(self.movie)
