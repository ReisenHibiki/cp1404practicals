from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        """Build the kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def get_valid_input(self):
        """get valid input"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculate(self):
        """handle calculation"""
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        """handle increment"""
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


ConvertMilesKm().run()
