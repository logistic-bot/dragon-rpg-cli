"""
This module provides utils functions for the game, such as copyright notice
"""

from os.path import abspath
from time import sleep
import sys


def _print_legal_stuff(full=False):
    """Returns legal copyright notice and license information."""
    if full:
        with open(abspath("../LICENSE"), "r") as file:
            return file.read()
    else:
        licence_str = """
        Dragon RPG  Copyright (C) 2019 Khaïs COLIN
    This program comes with ABSOLUTELY NO WARRANTY; for details type `license'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `license' for details.
"""
        return licence_str


def print_legal_stuff():
    """
    Print legal copyright notice and license information.
    :return: None
    """
    slowprint(text=_print_legal_stuff(), interval=0.005, end_interval=0)


def slowprint(text, interval=0.03, end="\n", end_interval=0.5):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c == " ":
            pass
        else:
            time.sleep(interval)
    sys.stdout.write(end)
    time.sleep(end_interval)


def slowinput(text, interval=0.03, end="", end_interval=0):
    slowprint(text, interval, end, end_interval)
    return input()
