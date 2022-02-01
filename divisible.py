import pytest


@pytest.fixture
def input_value():
    input = 39
    return input

def list_input_value():
    my_list = [12, 65, 54, 39, 102, 339, 221]
    return my_list

@pytest.mark.divisible
def test_divisible_by_2(input_value):
    assert input_value % 2 == 0
 
@pytest.mark.divisible
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


@pytest.mark.divisible
def test_divisible_by_13(input_value):
    assert input_value % 13 == 0


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11 * num == output