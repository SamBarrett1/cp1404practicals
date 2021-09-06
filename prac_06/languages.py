"""
Practical 06 - Samuel Barrett - 13038579
Simple languages program with a class
"""

from prac_06.programming_language import ProgrammingLanguage
from operator import attrgetter


def main():
    """Simple language class test"""
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(java)
    print(python)
    print(visual_basic)

    """
    My first attempt
    """
    # list_of_languages = ["Java", "Python", "Visual Basic"]
    # print("The dynamically typed languages are:")
    # data = [ProgrammingLanguage("Java", "Static", True, 1995), ProgrammingLanguage("Python", "Dynamic", True, 1991),
    #         ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
    # for language in data:
    #     if data.sort(key=attrgetter("typing")) == "Static":
    #         code_language = data.sort(key=attrgetter("language"))
    #         print(code_language)

    list_of_languages = [java, python, visual_basic]
    print("The dynamically typed languages are:")
    for coding_language in list_of_languages:
        if coding_language.is_dynamic():
            print(coding_language.language)


main()

