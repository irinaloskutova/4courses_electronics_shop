import pytest


from class_el_shop import Item

@pytest.fixture
def item1():
    return Item("test", 10, 10)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100

def test_apply_discount(item1):
    assert item1.apply_discount() == 8