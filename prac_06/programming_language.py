"""Practical 06 - Samuel Barrett - 13038579"""


class ProgrammingLanguage:

    def __init__(self, language="", typing="", reflection="", year=""):
        """Initialise the language comparison class object"""

        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    # def is_dynamic(self):
    #     """Boolean if the language is dynamic or static"""
    #
    #     if self.typing:
    #         return "Dynamic"
    #     else:
    #         return "Static"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """print the class object with __string__"""

        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                           self.year)
