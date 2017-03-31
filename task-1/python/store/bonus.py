from movies import NewReleaseMovie

class Bonus(object):
    """
    Abstract class for all Bonuse rules for movies rent
    """

    def score(self, movie, days_rented):
        """
        Abstract method for rental price score return
        """
        raise NotImplementedError

class SimpleBonus(Bonus):
    """
    Bonus system from task code
    """

    def score(self, movie, days_rented):

        #initial bonus for movie rent
        bonus_value = 1

        #bonus for two days rental
        if isinstance(movie, NewReleaseMovie) and days_rented > 1:
            bonus_value += 1

        return bonus_value
