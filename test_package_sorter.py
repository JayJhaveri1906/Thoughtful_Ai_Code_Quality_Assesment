import pytest
from package_sorter import PackageSorter

@pytest.fixture
def my_package_sorter():
    return PackageSorter()

def test_package_sorter_output(my_package_sorter):
    ref_output = {"STANDARD", "SPECIAL", "REJECTED"}

    assert my_package_sorter.sort(1,2,3,4) in ref_output