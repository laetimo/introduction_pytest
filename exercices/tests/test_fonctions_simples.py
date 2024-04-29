from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform
import pytest

def test_add_with_int():
    assert add(3,4) == 7
    assert add(5, -1) == 4
    assert add(0, -5) == -5

def test_add_with_float():
    assert add(3.2, 4.2) == 7.4

def test_add_with_string():
    assert add("a", "b") == "ab"
    assert add("", "") == ""

def test_add_with_mixed_types():
    with pytest.raises(TypeError):
        add(1, "a")
        add(2, [1,2])
        add("2", ["1","2"])

def test_divide_integer():
    assert divide(10, 2) == 5

def test_divide_string():
    with pytest.raises(TypeError):
        divide("pm", 2)

def test_fail_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)

def test_add_integer_with_int():
    assert add_integer(3,4) == 7

def test_add_integer_with_float():
    with pytest.raises(TypeError):
        add_integer(3.2,4.5)

def test_uniform_with_integer():
    assert alea_uniform(1, 2) == 1 or 2

def test_uniform_with_other_type():
    with pytest.raises(TypeError):
        alea_uniform("a", "b")
        alea_uniform("a", 2)

   