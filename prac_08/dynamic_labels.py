from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabel(App):
    """Dynamic Label App"""

    def __init__(self, **kwargs):
        """Construct data"""
        super().__init__(**kwargs)
        self.names = ["Peter", "Joe", "Lois", "Meg"]

    def build(self):
        """build GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_label()
        return self.root

    def create_label(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabel().run()
