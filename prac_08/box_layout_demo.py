from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ BoxLayoutDemoApp is a Kivy App for box layout demo """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """ handle greet, show the format output """
        print("Test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """handle clear, clear the input and output"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
