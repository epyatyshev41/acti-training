
class Movie(object):
    """
    Abstract class for Movies
    """
    def __init__(self, title):
        self.title = title

    def get_price(self):
        """
        Abstract property for movie rent price.
        This property used when user doesn't specify
        price scoring rule for objects of this subclass
        PricingSystem (subclasses of `pricing.PricingSystem`)
        """
        raise NotImplementedError

class RegularMovie(Movie):

    def __init__(self, title):
        super(RegularMovie, self).__init__(title)

    @staticmethod
    def get_price(days_rented):
        dept_value = 2
        if days_rented > 2:
            dept_value += (days_rented - 2) * 1.5
        return dept_value

class NewReleaseMovie(Movie):

    def __init__(self, title):
        super(NewReleaseMovie, self).__init__(title)

    @staticmethod
    def get_price(days_rented):
        return days_rented * 3

class ChildrensMovie(Movie):

    def __init__(self, title):
        super(ChildrensMovie, self).__init__(title)

    @staticmethod
    def get_price(days_rented):
        dept_value = 1.5
        if days_rented > 3:
            dept_value += (days_rented - 3) * 1.5
        return dept_value
