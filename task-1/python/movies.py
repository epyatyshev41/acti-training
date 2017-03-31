
class Movie(object):
    """
    Abstract class for Movies
    """
    def __init__(self, title):
        self.title = title

    @property
    def default_price(self):
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

    @property
    def default_price(self):
        return 0.5


class NewReleaseMovie(Movie):

    def __init__(self, title):
        super(NewReleaseMovie, self).__init__(title)

    @property
    def default_price(self):
        return 1

class ChildrensMovie(Movie):

    def __init__(self, title):
        super(ChildrensMovie, self).__init__(title)

    @property
    def default_price(self):
        return 2
