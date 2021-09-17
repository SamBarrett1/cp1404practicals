"""Practical 07 - Samuel Barrett - 13038579"""

from kivy.app import App
from kivy.lang import Builder

MILES_CONVERSION = 1.609344

__author__ = 'Samuel Barrett'


class ConvertMtoKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        # Window.size = (400, 200)
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = self.get_validated_miles() + value
        self.root.ids.input_number.text = str(result)
        self.handle_calculate()

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        # result = value * 1.609344
        result = value * MILES_CONVERSION
        self.root.ids.output_label.text = str(f"{result:.3f}")

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMtoKmApp().run()

