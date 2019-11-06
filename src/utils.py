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
    print(_print_legal_stuff())
