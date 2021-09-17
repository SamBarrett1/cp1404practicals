"""Practical 07 - Samuel Barrett - 13038579"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Samuel Barrett'


class ConvertMtoKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        # Window.size = (400, 200)
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_up_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value + 1
        self.root.ids.input_number.text = str(result)

    def handle_dn_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value - 1
        self.root.ids.input_number.text = str(result)

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = float(self.root.ids.input_number.text)
        result = value * 1.609344
        self.root.ids.output_label.text = float(f"{result:.2f}")


ConvertMtoKmApp().run()

