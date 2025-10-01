import work5task1 as w
import pytest


@pytest.mark.parametrize("input_value,expected,description", [
        (3, 4, "add one with default"),
        (3, 5, "add two with parameter"),
        (3, 6, "add two with parameter"),
    ])

def test_add_function(input_value, expected, description):
    if "default" in description:
        assert w.add(input_value) == expected
    else:
        assert w.add(input_value, 2) == expected