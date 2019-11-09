#!/usr/bin/env python3

"""
The main file of the Dragon RPG.

E V E R Y T H I N G is happening from this file
"""
from chapters.chapter1 import chapter1
from dragon import Dragon
import utils


if __name__ == "__main__":
    utils.print_legal_stuff()

    print("Please choose a name for your character.")
    print('It will be used like this: "Hello `<name>`, how are you?"')
    NAME = input("name> ")
    print("")  # newline

    print("Please chose a title for you character.")
    print("It will be used in letters.")
    TITLE = input("title> ")
    print()
    print()
    print("----------------------------------------")
    print()
    print()

    PLAYER = Dragon(name=NAME, title=TITLE)

    PLAYER.greet()

    chapter1(PLAYER)
