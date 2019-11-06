import src.dragon
import pytest


@pytest.fixture()
def dragon():
    return src.dragon.Dragon(name="Test Dragon", title="The Greatest Testing Dragon in town", max_health_max=100, max_health_min=1)


def test_atirbutes_are_correct(dragon):
    assert dragon.name == "Test Dragon"
    assert dragon.title == "The Greatest Testing Dragon in town"
    assert dragon.max_health <= 100
    assert dragon.max_health >= 1


def test_greet(dragon):
    assert dragon._greet() in [
            "I bow down to you, Test Dragon.",
            "I bid you welcome, Test Dragon, to my game.",
            "Hello again, Test Dragon.",
            "Hello Test Dragon!",
            "Hello, Test Dragon.",
            "Hello and, again, welcome to my game Test Dragon",
            "I bow down to you, The Greatest Testing Dragon in town.",
            "I bid you welcome, The Greatest Testing Dragon in town, to my game.",
            "Hello again, The Greatest Testing Dragon in town.",
            "Hello The Greatest Testing Dragon in town!",
            "Hello, The Greatest Testing Dragon in town.",
            "Hello and, again, welcome to my game The Greatest Testing Dragon in town",
        ]


def test_advance_story(dragon):
    assert dragon._advance_story("Test") == "Test"
