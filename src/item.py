#!/usr/bin/env python3

"""This file contains the Item class."""


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

    def __init__(self, name, description, pocketable=True):
        self.name = name
        self.description = description
        self.pocketable = pocketable


#    def description
