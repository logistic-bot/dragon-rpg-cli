#!/usr/bin/env python3

"""This file contains the Item class."""

from utils import slowprint


def none_function(self):
    pass


class Item:
    """This class is used to represent an item in the world.

    Arguments:
    name: The name of the item. Should be pretty short. Will be used
          in the inventory.
    description: The long and detailed description of the item.
                 Should be long and detailed. Will be used when the
                 player look at the item and in room descriptions
    pocketable: default True. Determines if the player can carry the
                item in its main inventory.
    """

    def __init__(self, name, description, pocketable=True, take_message=None, after_take_function=None):
        self.name = name
        self.description = description
        self.pocketable = pocketable
        self.take_message = take_message

        if after_take_function is None:
            self.after_take_function = none_function
        else:
            self.after_take_function = after_take_function

    def describe(self, fast=False):
        """Describes the item using slowprint.

        if fast is True, print the description instantly.
        """
        #        slowprint(self.name, fast=fast)
        slowprint(self.description, fast=fast)

    def after_take(self):
        self.after_take_function(self)
