"""Practical 07 - Samuel Barrett - 13038579"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

__author__ = 'Samuel Barrett'


class DynamicLabels(App):
    """Main program - Kivy dynamic labels application."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names_list = ["Tony", "Therese", "Steve", "Jess", "Abraham", "Lauren"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Labels Application"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names_list:
            temp_label = Label(text=name)
            # add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)

    # def clear_all(self):
    #     """Clear all of the widgets that are children of the "entries_box" layout widget."""
    #     self.root.ids.main.clear_widgets()


DynamicLabels().run()
