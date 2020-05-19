"""
This package contains the code to make the player play through the first chapter.
This function is called chapter1
If you are reading this code for the first time, I (The author of this file)  would
advise you to start your reading in this function.

A (currently) short description of the events in the first chapter is included in
the corresponding function.
"""

from rooms.base_room import Room
from rooms.start_cave import StartCave # TODO
from item import Item


def after_take_big_rock(self):
    """TODO Temporary function"""
    self.description = self.description + " It is too heavy to carry."


SMALL_ROCK = Item(
    "Small rock",
    "A small, uninteresting, grey rock. It is simply lying on the ground.",
    take_message="You are not sure why you take these rocks, maybe they will be usefull later.",
)
BIG_ROCK = Item(
    "Big rock",
    "A pretty big rock, grey, lying in the corner of the cave.",
    pocketable=False,
    take_message="You try to take this rock, but it is too heavy to carry.",
    after_take_function=after_take_big_rock,
)

START_CAVE = Room(
    "Dark cave",
    "There is no light in this cave, but you have no problem seeing, thanks to your night vision.",
    [SMALL_ROCK, BIG_ROCK],
)


def chapter1(player, fastprint):
    """Take the player as an argument and make it play trough the first chapter.

    In this chapter, the player get familiarized with the controls of the game
    and learns how the combat system works. He will also learn that he is a
    dragon which does not remember much from his past life, and that he wakes up
    in a cave. Later in the story, he will learn that he is the last descendants
    of an ancient race that is now extinct, and that he only survived because #
    TODO: why did only this dragon survive?

    This chapter will contain:
     - going from the cave to the town.
     - learn the basic text-based controls
     - learn the combat system

    """
    player.advance_story("1", template="chapter", fast=fastprint)

    player.advance_story("You awake from a long, long sleep.", fast=fastprint)
    player.advance_story("As you open your eyes and look around, you see that you are in a cave.", fast=fastprint)
    player.advance_story(
        "The cave is dark, but thanks to your night vision, you have no problem seeing.", fast=fastprint
    )
    player.advance_story("You try to remember how you got there, but to no avail.", fast=fastprint)
    player.advance_story("Then, you start to look around.", template="separator", fast=fastprint)

    START_CAVE.describe(fast=fastprint)

    START_CAVE.run(player, fastprint)


# got_valid_input = False
# while not got_valid_input:
#     player.advance_story("You are in a cave.")
#     player.advance_story("There are a few rocks on the ground.")
#     player.advance_story("There is a corridor to the north.", template="description")
#
#     player.advance_story("When you see this `>` it means that the game is awaiting a command.",
#                          template="tutorial", )
#     player.advance_story("To input a command, simply type it, and press enter to validate it.",
#                          template="tutorial", )
#     player.advance_story("The game will tell you when you input an invalid command, and gives "
#                          "you some hints about what to try next.", template="tutorial", )
#     player.advance_story("Commands that you will often use include these: `go <direction>`, "
#                          "`take <object>`, `attack <object>`.", template="tutorial", )
#     player.advance_story("But other commands are also available, just try things out.",
#                          template="tutorial")
#
#    action = input(" > ")
