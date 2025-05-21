import pytest
from solution import sum_two

def test_correct_types():
    assert sum_two(2, 3) == 5

def test_incorrect_type():
    with pytest.raises(TypeError):
        sum_two(2, "3")
