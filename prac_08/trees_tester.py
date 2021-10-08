"""
CP1404/CP5632 Practical
Testing/example client code for trees classes
When you complete all the subclasses, you'll see that they behave differently.

"""
import prac_08.trees as trees
from prac_08.trees import Tree


def main():
    """Program to demonstrate trees of different types."""
    # Let's make some trees of different classes (subclasses)
    width = 10
    tree_list = [trees.Tree(), trees.EvenTree(), trees.UpsideDownTree(),
                 trees.WideTree(), trees.QuickTree(), trees.FruitTree(),
                 trees.PineTree()]

    # tree_list = [trees.WideTree()]

    # display all the trees
    for tree in tree_list:
        print(tree.__class__)
        print(tree)

    print("Time to grow!")
    # grow them several times
    for _ in range(5):
        for tree in tree_list:
            tree.grow(5, 2)

    # display all the trees again
    for tree in tree_list:
        print(tree.__class__)
        print(tree)

    print('My test')
    wide_tree = trees.WideTree()
    wide_tree.grow(10, 3)
    print(wide_tree)

    print('My test')
    pine_tree = trees.PineTree()
    pine_tree.grow(10, 3)
    print(pine_tree)


main()
