class Rental(object):

    def __init__(self, movie, days_rented, pricing_system):
        self.movie = movie
        self.days_rented = days_rented
        self.pricing_system = pricing_system

    @property
    def dept(self):
        return self.pricing_system.score(self.movie, self.days_rented)

class RentalWithBonuses(Rental):

    def __init__(self, movie, days_rented, pricing_system, bonuses_list):
        super(RentalWithBonuses, self).__init__(
            movie, days_rented, pricing_system)
        self.bonuses_list = bonuses_list
        
    @property
    def bonus(self):
        rent_bonus = 0.0
        
        for bonus in self.bonuses_list:
            rent_bonus += bonus.score(self.movie, self.days_rented)

        return rent_bonus
