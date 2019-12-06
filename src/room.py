"""This file contains the `Room` class."""

from utils import slowprint


class Room:
    """This class is used to represent a place in the world.

    It includes a list of all the items in this place.

    It takes a name, a description, and a list of items.
    """

    def __init__(self, name, description="", items=None):
        if items is None:
            items = []

        self.name = name
        self.description = description
        self.items = items

    def _describe(self):
        return self.description

    def describe(self, fast=False):
        """Slowprints a description of the room, including all its items, to the user"""
        slowprint(self._describe(), fast=fast)

        for item in self.items:
            slowprint(item.description)
