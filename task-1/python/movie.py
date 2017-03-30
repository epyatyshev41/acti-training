
class Movie(object):
    """
    Abstract class for Movies
    """
    def __init__(title):
        self.title = title

    @property
    def price_code():
        raise NotImplementedError

class RegularMovie(Movie):

    def __init__(title, price_code):
        super(RegularMovie, self).__init__(title)

    @property
    def price_code():
        return 0


class NewReleaseMovie(Movie):

    def __init__(title):
        super(NewReleaseMovie, self).__init__(title)

    @property
    def price_code():
        return 1

class ChildrensMovie(Movie):

    def __init__(title, price_code):
        super(ChildrensMovie, self).__init__(title)

    @property
    def price_code():
        return 2
