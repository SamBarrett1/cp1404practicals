"""Practical 10 - Samuel Barrett 13038579 """

import wikipedia


def user_defined_api_call():
    """user defined call for summary of wiki page with wikipedia API"""

    user_page = input("What page do you want: ")
    while user_page != '':
        try:
            summary = wikipedia.summary(user_page, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as a:
            print(a.options)
        else:
            print(summary)
        user_page = input("What page do you want: ")


user_defined_api_call()

