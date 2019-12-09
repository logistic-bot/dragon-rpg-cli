from hypothesis import given
from hypothesis.strategies import text

from src.room import Room

import sys

sys.path.append("../src")


@given(sample_name=text(), sample_description=text())
def test_room_describe(sample_name, sample_description, capsys):
    # setup
    room_to_test = Room(sample_name, sample_description)

    # act
    room_to_test.describe(fast=True)
    provided_description = capsys.readouterr().out

    # assert
    assert provided_description == sample_description + "\n"  # when a string is printed,
    # it adds a `\n`


@given(sample_name=text(), sample_description=text())
def test_room_attributes(sample_name, sample_description):
    # setup
    room_to_test = Room(sample_name, sample_description)

    # act
    description = room_to_test.description
    name = room_to_test.name

    # assert
    assert description == sample_description
    assert name == sample_name
