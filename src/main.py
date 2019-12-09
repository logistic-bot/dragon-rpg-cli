#!/usr/bin/env python3

"""
The main file of the Dragon RPG.

E V E R Y T H I N G is happening from this file
"""

from sys import argv

from chapters.chapter1 import chapter1
from dragon import Dragon
from utils import slowprint, slowinput
from utils import wait

import utils

if __name__ == "__main__":
    if "fast" in argv:
        FASTPRINT = True
    else:
        FASTPRINT = False

    utils.print_legal_stuff(FASTPRINT)

    wait(3, FASTPRINT)

    slowprint("Please choose a name for your character.", end_interval=0, fast=FASTPRINT)
    slowprint('It will be used like this: "Hello `<name>`, how are you?"', fast=FASTPRINT)
    slowprint("You can use your real name, or invent one!", fast=FASTPRINT)
    slowprint("Note: At the time, your name is not stored anywhere.", end_interval=0, fast=FASTPRINT)
    slowprint("A warning message will be added when this is the case.", end_interval=0, fast=FASTPRINT)
    NAME = slowinput("name> ", fast=FASTPRINT)
    print()

    slowprint("Please chose a title for you character.", end_interval=0, fast=FASTPRINT)
    slowprint("It will be used in letters.", fast=FASTPRINT)
    slowprint('It could be something like "{} The Great"'.format(NAME), fast=FASTPRINT)
    slowprint("Note: You need to include your name, it is not added automaticaly.", end_interval=0, fast=FASTPRINT)
    TITLE = slowinput("title> ", fast=FASTPRINT)
    print()
    print()
    slowprint("----------------------------------------", fast=FASTPRINT)
    print()
    print()

    PLAYER = Dragon(name=NAME, title=TITLE)

    PLAYER.greet(fast=FASTPRINT)

    chapter1(PLAYER, fastprint=FASTPRINT)
