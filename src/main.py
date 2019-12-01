#!/usr/bin/env python3

"""
The main file of the Dragon RPG.

E V E R Y T H I N G is happening from this file
"""
from chapters.chapter1 import chapter1
from dragon import Dragon
from utils import slowprint, slowinput
from time import sleep
import utils


if __name__ == "__main__":
    utils.print_legal_stuff()

    sleep(3)

    slowprint("Please choose a name for your character.", end_interval=0)
    slowprint('It will be used like this: "Hello `<name>`, how are you?"')
    slowprint("You can use your real name, or invent one!")
    slowprint("Note: At the time, your name is not stored anywhere.", end_interval=0)
    slowprint("A warning message will be added when this is the case.", end_interval=0)
    NAME = slowinput("name> ")
    print()

    slowprint("Please chose a title for you character.", end_interval=0)
    slowprint("It will be used in letters.")
    slowprint('It could be something like "{} The Great"'.format(NAME))
    slowprint(
        "Note: You need to include your name, it is not added automaticaly.",
        end_interval=0,
    )
    TITLE = slowinput("title> ")
    print()
    print()
    slowprint("----------------------------------------")
    print()
    print()

    PLAYER = Dragon(name=NAME, title=TITLE)

    PLAYER.greet()

    chapter1(PLAYER)
