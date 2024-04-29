from basics.src.inverse import inverse, minus
import pytest

def test_long_list():
    assert inverse(["a", "b", "c", "d", "e"]) == "edcba"

def test_four_elements_list():
    assert inverse(["a", "b", "c", "d"]) == "dcba"

def test_fail_when_integer():
    with pytest.raises(ValueError): # equivalent de l'assertion d'un erreur
        inverse(87)

def test_lower_cases():
    assert inverse("hello") == "olleh"

def test_lower_cases_four_elements():
    assert inverse("hell") == "lleh"

def test_lower_cases_with_numbers():
    assert inverse("hello2") == "2olleh"

def test_minus():
    result = minus(8, 2)
    assert True