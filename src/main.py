#!/usr/bin/env python3

"""
The main file of the Dragon RPG.

E V E R Y T H I N G is happening from this file
"""

import random


class Dragon:
    """This class is used to store player data and utility functions."""

    def __init__(self, name, title, max_health_min=5000, max_health_max=10000):
        """
        Initalise a Dragon Object.

        name: The name of the dragon. Expected to be in the form `Megamind`

        title: The title of the dragon. Expected to be in the form `Megamind:
        Extremely handsome criminal genius and master of all villany`

        max_health_min: The max health is a random number between max_health_min
        and max_health_max.

        max_health_max: The max health is a random number between max_health_min
        and max_health_max.

        """
        self.max_health = random.randint(max_health_min, max_health_max)
        self.health = self.max_health
        self.name = name
        self.title = title

    def greet(self):
        """Greet the Dragon with a random message using his name or title."""
        greetings = [
            "I bow down to you, {}.",
            "I bid you welcome, {}, to my game.",
            "Hello again, {}.",
            "Hello {}!",
            "Hello, {}.",
            "Hello and, again, welcome to my game {}",
        ]

        greeting = random.choice(greetings)
        name = random.choice([self.title, self.name])

        print(greeting.format(name))


def print_legal_stuff():
    """Print legal copyright notice and license information."""
    print("Copyright 2019 Khaïs COLIN")
    print(
        """
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
"""
    )
    print("----------------------------------------")


def chapter1(player):
    """
    Take the player as an argument and make it play trought the first chapter.

    This chapter will contain:
     - Girl with a coin encounter
    """
    print("")


if __name__ == "__main__":
    print_legal_stuff()

    print("Please chosse a name for your character.")
    print('It will be used like this: "Hello `<name>`, how are you?"')
    name = input("name> ")
    print("")  # newline

    print("Please chose a title for you character.")
    print("It will be used in letters.")
    title = input("title> ")
    print("----------------------------------------")

    player = Dragon(name=name, title=title)

    player.greet()

    chapter1(player)
