import pytest
from class_el_shop import Item, Phone


@pytest.fixture
def item1():
    return Item("test", 10, 10)

@pytest.fixture
def item2():
    return Phone("test2", 10, 10, 10)