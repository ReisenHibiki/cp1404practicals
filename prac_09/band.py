class Band:
    """Represent a Band object"""

    def __init__(self, name=""):
        """Construct a Musician with a name and empty instrument collection."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a band"""
        return f"{self.members}"

    def add(self, musician):
        """add a musician to the band"""
        self.members.append(musician)

    def play(self):
        """display a string showing the band playing music"""
        for musician in self.members:
            print(musician.play())


if __name__ == '__main__':
    from musician import Musician

    test = Musician("Nuno Bettencourt")
    test.add("Washburn N4 (1990) : $2,499.95")
    test2 = Musician("Gary Cherone")
    band = Band("wolf")
    band.add(test)
    band.add(test2)
    print(band)
    band.play()
