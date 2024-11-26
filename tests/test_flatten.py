import pytest
from otamas_playground.flatten_dictionary import flatten_dict


def test_base_case():
    nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}, "g": {"h": 5}}

    flattened = flatten_dict(nested_dict)
    assert flattened == {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 4, "g.h": 5}


def test_empty_dictionary_results_in_empty_dictionary():
    assert flatten_dict({}) == {}


@pytest.mark.parametrize("value", [5, "foo", pytest])
def test_non_dictionary_raises_value_error(value):
    with pytest.raises(ValueError):
        flatten_dict(value)
