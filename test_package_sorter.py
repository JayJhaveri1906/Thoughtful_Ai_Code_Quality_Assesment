import pytest
from package_sorter import PackageSorter

@pytest.fixture
def my_package_sorter():
    return PackageSorter()

def test_sorter_output(my_package_sorter):
    ref_output = {"STANDARD", "SPECIAL", "REJECTED"}

    assert my_package_sorter.sort(1,2,3,4) in ref_output


# Test cases for STANDARD packages
## USED GPT to quickly generate some test cases
@pytest.mark.parametrize("width, height, length, mass", [
    (1, 2, 3, "4"),
    (50, 50, 50, 5),      
    (49, 49, "49", 19.9),   
    ("1", 1, 1, 0.1)
])
def test_sorter_output_standard(my_package_sorter, width, height, length, mass):
    assert my_package_sorter.sort(width, height, length, mass) == "STANDARD"


# Test cases for SPECIAL packages (either bulky or heavy)
## USED GPT to quickly generate some test cases
@pytest.mark.parametrize("width, height, length, mass", [
    (100, 100, 100, 5),       # Bulky due to volume only
    (200, "50", 50, 10),        # Bulky due to width dimension only
    (150.0, "50", 50, 10),      # Bulky due to exactly 150 cm dimension
    (50, 50.0, 160, 10),      # Bulky due to length dimension only
    (500, "10.0", 200, 15),       # Bulky due to volume with non-cubic dimensions
    (200, 200, 200, 10.0),    # Large dimensions but not heavy
    (50, 50, "50", 25.0),       # Heavy due to mass only
    (10, 10, 10.0, 30),       # Heavy package with small dimensions
    (50, 50, 50, 20)          # Edge case - heavy due to exactly 20 kg mass
])
def test_sorter_output_special(my_package_sorter, width, height, length, mass):
    assert my_package_sorter.sort(width, height, length, mass) == "SPECIAL"


# Test cases for REJECTED packages (both bulky and heavy)
## USED GPT to quickly generate some test cases
@pytest.mark.parametrize("width, height, length, mass", [
    (200, "200", 200, 25),
    (150, 150, 150, 20)
])
def test_sorter_output_rejected(my_package_sorter, width, height, length, mass):
    assert my_package_sorter.sort(width, height, length, mass) == "REJECTED"


# Testing, when input type is not what we expected
def test_sorter_input_type(my_package_sorter):
    assert my_package_sorter.sort("1",2,3,4) == "STANDARD"


# Testing, when input type is not what we expected
@pytest.mark.parametrize("width, height, length, mass", [
    ("a", 2, 3, 4),
    (1, "B", 3, 4),
    (1, 2, "c", 4),
    (1, 2, 3, "wrg"),
    (1, "Hello thoughtful ai!", "grwegreg", 4)
])
def test_sorter_wrong_input_type(my_package_sorter, width, height, length, mass):
    assert my_package_sorter.sort(width, height, length, mass) == "REJECTED"