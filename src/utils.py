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


def print_legal_stuff(fast=False):
    """
    Print legal copyright notice and license information.
    :return: None
    """
    slowprint(text=_print_legal_stuff(), fast=fast)


def slowprint(text, interval=0.02, end="\n", end_interval=0.5, fast=False, charcount_interval=1):
    """Print the given text slowly.

    Does not wait if a char is ` `

    Argument description:
    interval: time (in second) to wait between each letter
    end: string to append to the end of the text, default `\n` to mimic print() behavior
    end_interval: time (in second) to wait when the text has finished printing
    fast: default False. when True, will skip all waiting and print the text instantly

    This is used to print text more slowly, so users will not be confused by rapidly scrolling text.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != " " and not fast:
            sleep(interval)
    sys.stdout.write(end)
    if not fast:
        sleep(end_interval)


def slowinput(text, interval=0.03, end="", end_interval=0, fast=False):
    """Print the given text using utils.slowprint, using all the other arguments.
    Then asks the user for input, and return that input

    See the documentation for utils.slowprint for more information about the other arguments
    """
    slowprint(text, interval, end, end_interval, fast=fast)
    return input()


def wait(time, fast=False):
    """Sleep for the specified time. If fast is True, do nothing.

    This is used to add dramatic pauses, which can be disabled by the user
    """
    if not fast:
        sleep(time)


def ask_y_n(fast):
    action = "DUMMY ACTION"  # needed to avert an index out of range error
    while not action.strip().lower()[0] in ["y", "n"]:  # ensure that a valid input is given
        action = slowinput("[y/n]> ", fast=fast)
        if action == "":
            action = "DUMMY ACTION"

    if cleanup_string(action)[0] == "y":
        return True
    else:
        return False


def cleanup_string(action):
    action = action.lower()
    action = action.strip()
    action = action.strip(".")
    action = action.strip("!")
    action = action.strip("?")
    action = action.strip()
    return action
