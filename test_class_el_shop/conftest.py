import pytest
from class_el_shop import Item, Phone, KeyBoard


@pytest.fixture
def item1():
    return Item("test", 10, 10)

@pytest.fixture
def item2():
    return Phone("test2", 10, 10, 10)

@pytest.fixture
def item3():
    return KeyBoard('Dark Project KD87A', 9600, 5)


@pytest.fixture
def item4():
    return KeyBoard('Dark Project KD87A', 9600, 5, "RU")
