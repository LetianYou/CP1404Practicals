from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

names = ["Alice", "Bob", "Charlie", "David"]


class DynamicLabelsApp(App):
    """Main application class."""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
