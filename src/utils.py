"""
This module provides utils functions for the game, such as copyright notice
"""


def _print_legal_stuff():
    """Returns legal copyright notice and license information."""
    return """Copyright 2019 Khaïs COLIN
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License , or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, write to

       The Free Software Foundation, Inc.
       51 Franklin Street, Fifth Floor
       Boston, MA 02110-1335  USA
----------------------------------------
    """


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
