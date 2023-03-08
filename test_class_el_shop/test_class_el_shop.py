import pytest


from class_el_shop import Item

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100

def test_apply_discount(item1):
    assert item1.apply_discount() == 8.5


def test_instantiate_from_csv():
    p = Item.instantiate_from_csv()
    assert len(p) == 5

def test__str__(item1):
    assert str(item1) == "test"

def test_name(item1):
    assert item1.name == "test"


def test__repr__(item1):
    assert repr(item1) == "Имя: test, цена: 10"