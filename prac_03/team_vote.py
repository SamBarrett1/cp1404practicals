"""Conflict management tool by Sam"""
import random


def main():
    """
    Conflict Management Tool for CP1403 Design Thinking:
    A simple random voting program for the final decision of the team
    """
    team_member = ['Danielle', 'Brayden', 'Ethan', 'Adam', 'Jake', 'Sam']
    random_vote = get_vote()
    random_team_member = team_member[random_vote - 1]

    # Use this print line to determine an individual number
    # print("Our team will develop the {}{} idea".format(random_vote, number_end(random_vote)))

    # Use this print line to finalise the main idea
    print("Our team will develop {}'s idea".format(random_team_member))


def get_vote():
    """
    code to produce a random number inclusive of 1 and 5
    change this range accordingly, if the list length, or quantity changes
    """
    random_vote = random.randint(1, 5)
    return random_vote


def number_end(number):
    """decision tree to end numbers with 'st', 'nd', 'rd' or 'th'"""
    if number == 1:
        return 'st'
    elif number == 2:
        return 'nd'
    elif number == 3:
        return 'rd'
    else:
        return 'th'


def test():
    for i in range(0, 5):
        team_member = ['Danielle', 'Brayden', 'Adam', 'Jake', 'Ethan', 'Sam']
        random_vote = get_vote()
        random_team_member = team_member[random_vote - 1]
        print("We will develop the {}{} idea which is {}'s".format(random_vote, number_end(random_vote),
                                                                   random_team_member))


"""uncomment this and comment out main() to run tests"""
# test()


main()

