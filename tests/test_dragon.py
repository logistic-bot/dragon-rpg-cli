import pytest
from hypothesis import given, assume, note
from hypothesis.strategies import integers
from hypothesis.strategies import text

import src.dragon


@pytest.fixture()
def dragon():
    return src.dragon.Dragon(
        name="Test Dragon",
        title="The Greatest Testing Dragon in town",
        max_health_max=100,
        max_health_min=1,
    )


@given(
    sample_name=text(),
    sample_title=text(),
    sample_health_max=integers(2, 10000000),
    sample_health_min=integers(1, 10000000),
)
def test_attributes_are_correct(sample_name, sample_title,
                                sample_health_max, sample_health_min):
    # assume
    assume(sample_health_max >= sample_health_min)

    # setup
    sample_dragon = src.dragon.Dragon(sample_name, sample_title,
                                      sample_health_min,
                                      sample_health_max)

    # act

    # assert
    assert sample_dragon.name == sample_name
    assert sample_dragon.title == sample_title
    assert sample_dragon.max_health <= sample_health_max
    assert sample_dragon.max_health >= sample_health_min


def test_greet(dragon, capsys):
    dragon.greet()
    greeting = capsys.readouterr().out
    assert greeting in [
        "I bow down to you, Test Dragon.\n",
        "I bid you welcome, Test Dragon, to my game.\n",
        "Hello again, Test Dragon.\n",
        "Hello Test Dragon!\n",
        "Hello, Test Dragon.\n",
        "Hello and, again, welcome to my game Test Dragon\n",
        "I bow down to you, The Greatest Testing Dragon in town.\n",
        "I bid you welcome, The Greatest Testing Dragon in town, to my game.\n",
        "Hello again, The Greatest Testing Dragon in town.\n",
        "Hello The Greatest Testing Dragon in town!\n",
        "Hello, The Greatest Testing Dragon in town.\n",
        "Hello and, again, welcome to my game The Greatest Testing Dragon in town\n",
    ]


@given(sample_message=text())
def test_advance_story(dragon, sample_message, capsys):
    templates = ["", "tutorial", "separator", "chapter", "description"]
    templates_result = [
        "{}",
        "[tutorial] {}",
        "{}\n----------------------------------------\n",
        "\n\n---------=========[######]=========---------\nChapter {}"
        "\n---------=========[######]=========---------\n\n",
        "{}\n+++++++\n",
    ]

    index = 0
    for template in templates:
        dragon.advance_story(sample_message, template)

        story_message = capsys.readouterr().out
        assert (
            story_message == templates_result[index].format(sample_message) + "\n"
        ), template

        index += 1


@given(
    sample_name=text(),
    sample_title=text(),
    sample_max_health_min=integers(-10000, 0),
    sample_max_health_max=integers(0, 10000000),
)
def test_raise_max_health_min_big_enough(
    sample_name, sample_title, sample_max_health_min, sample_max_health_max
):
    # setup
    with pytest.raises(ValueError):
        src.dragon.Dragon(
            sample_name, sample_title, sample_max_health_min, sample_max_health_max
        )


@given(sample_name=text(), sample_title=text(), sample_max_health_number=integers())
def test_raises_health_difference_not_big_enought(
    sample_name, sample_title, sample_max_health_number
):
    # setup
    with pytest.raises(ValueError):
        src.dragon.Dragon(
            sample_name,
            sample_title,
            sample_max_health_number,
            sample_max_health_number - 1,
        )
