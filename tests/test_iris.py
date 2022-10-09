import pytest

from iris import colored, cprint

TEST_STR = "test"
RED = "red"


def test_colored_non_enum_color_throws_error():
    with pytest.raises(TypeError):
        _ = colored(TEST_STR, color=RED)


def test_cprint_non_enum_color_throws_error():
    with pytest.raises(TypeError):
        _ = cprint(TEST_STR, color=RED)
