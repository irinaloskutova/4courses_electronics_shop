import pytest
from class_el_shop import Item


@pytest.fixture
def item1():
    return Item("test", 10, 10)

