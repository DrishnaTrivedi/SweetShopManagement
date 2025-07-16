import pytest
from app.sweet import Sweet
from app.sweetshop import SweetShop


def test_add_sweet():
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    assert len(shop.get_all_sweets()) == 1
    assert shop.get_all_sweets()[0].name == "Kaju Katli"