from movies import RegularMovie, NewReleaseMovie, ChildrensMovie

class PricingSystem(object):
    """
    Abstract Class for movies rent pricing rules.

    We assume that changes in Movies prices should be made without
    changes of subclasses of `store.movies.Movie`.
    """
    def score(self, movie):
        """
        If user not specify price of current Movie type
        PricingSystem returns default price of Movie
        """
        return movie.default_price

class SimplePricingSystem(PricingSystem):
    """
    Pricing system from task code
    """
    def score(self, movie, days_rented):

        if isinstance(movie, RegularMovie):
            dept_value = 2
            if days_rented > 2:
                dept_value += (days_rented - 2) * 1.5
            return dept_value

        if isinstance(movie, NewReleaseMovie):
            return days_rented * 3

        if isinstance(movie, ChildrensMovie):
            dept_value = 1.5
            if days_rented > 3:
                dept_value += (days_rented - 3) * 1.5
            return dept_value

        return super(SimplePricingSystem, self).score(movie)
