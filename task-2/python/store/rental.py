class Rental(object):
    """
    Rental class is aggregation of Movie class `store.movies.Movie`
    and Pricing System class `store.pricing.PricingSystem`.

    For each customers's movie rent user must specify current pricing system.
    For each rent user can set only one pricing system
    """
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

class RentalWithBonuses(Rental):

    """
    Subclass of `Rental` with specified bonus system list.
    For each rent user can apply several bonus systems.
    """

    def __init__(self, movie, days_rented, bonuses_list):
        super(RentalWithBonuses, self).__init__(
            movie, days_rented)
        self.bonuses_list = bonuses_list

    @property
    def bonus(self):
        rent_bonus = 0.0

        for bonus in self.bonuses_list:
            rent_bonus += bonus.score(self.movie, self.days_rented)

        return rent_bonus
