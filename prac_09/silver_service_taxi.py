from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, )
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall"""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the trip"""
        return self.price_per_km * self.current_fare_distance + self.flagfall

