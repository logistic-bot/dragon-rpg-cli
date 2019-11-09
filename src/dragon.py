"""
This module provides the 'Dragon' class.

It is used thorough the game to represent the player.
"""

import random


class Dragon:
    """This class is used to store player data and utility functions."""

    # noinspection PyShadowingNames
    def __init__(self, name, title, max_health_min=5000, max_health_max=10000):
        """
        Initialises a Dragon Object.

        name: The name of the dragon. Expected to be in the form `Megamind`

        title: The title of the dragon. Expected to be in the form `Megamind:
        Extremely handsome criminal genius and master of all villainy`

        max_health_min: The max health is a random number between max_health_min
        and max_health_max.

        max_health_max: The max health is a random number between max_health_min
        and max_health_max.

        """
        if max_health_min < 1:
            raise Exception("Health must be at least 1")

        if max_health_max < max_health_min:
            raise Exception("max_health_max needs at least to be equal to max_health_min")

        self.max_health = random.randint(max_health_min, max_health_max)
        self.health = self.max_health
        self.name = name
        self.title = title

    def greet(self):
        """Greet the Dragon with a random message using either his name or title.
        The actual work is being done by the helper function self._greet()"""
        print(self._greet())

    # noinspection PyShadowingNames
    def _greet(self):
        """return a greeting for the Dragon with a random message using his name or title.
        This helper function is used by self.greet()"""
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

        return greeting.format(name)

    @staticmethod
    def _advance_story(message, template=None):
        format_str = ""

        if template is None:
            format_str = "{}"

        elif template == "tutorial":
            format_str = "[tutorial] {}"

        elif template == "separator":
            format_str = "{}\n----------------------------------------\n"

        elif template == "chapter":
            format_str = (
                "\n\n---------=========[######]=========---------\nChapter {"
                "}\n---------=========[######]=========---------\n\n"
            )

        elif template == "description":
            format_str = "{}\n+++++++\n"

        else:
            raise NotImplementedError(
                "Template {} was not found. Contact the programmer or choose "
                "another template.".format(template)
            )

        return format_str.format(message)

    def advance_story(self, message, template=None):
        """
        Prints a user provided message to stdout, adding some formatting using the
        helper function self._advance_story()
        The template for the formatting is provided using the "template" parameter.
        A list and a description of the availible templates can be found in the
        helper method self._advance_story()

        If you want to understand what the function does, I would advise you to
        read the self._advance_story()'s method documentation (and code, if you are
        a programmer)

        :param message: Message to be formatted and shown to the player
        :param template: Template by which the message should be formatted
        :return: None
        """
        print(self._advance_story(message, template))
