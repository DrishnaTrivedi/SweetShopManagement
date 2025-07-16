import pytest
from app.sweet import Sweet
from app.sweetshop import SweetShop
from app.errors import SweetNotFoundError, OutOfStockError

# dummy sweets added to shop
@pytest.fixture
def sample_shop():
    shop = SweetShop()
    shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    shop.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50))
    shop.add_sweet(Sweet(1003, "Gajar Halwa", "Vegetable-Based", 30, 15))
    return shop


def test_add_sweet():
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    assert len(shop.get_all_sweets()) == 1
    assert shop.get_all_sweets()[0].name == "Kaju Katli"


# DELETING SWEETS


def test_delete_sweet_by_id(sample_shop):
    sample_shop.delete_sweet_by_id(1001)
    with pytest.raises(SweetNotFoundError):
        sample_shop.get_sweet_by_id(1001)

def test_delete_sweet_by_id(sample_shop):
    sample_shop.delete_sweet_by_name("Gajar Halwa")
    with pytest.raises(SweetNotFoundError):
        sample_shop.get_sweet_by_name("Gajar Halwa") 


#SEARCHING SWEETS TESTS
def test_search_by_name(sample_shop):
    results = sample_shop.search_sweets(name="Gulab Jamun")
    assert len(results) == 1
    assert results[0].name == "Gulab Jamun"

def test_search_by_category(sample_shop):
    results = sample_shop.search_sweets(category="Milk-Based")
    assert len(results) == 1

def test_search_by_price_range(sample_shop):
    results = sample_shop.search_sweets(min_price=20, max_price=50)
    assert len(results) == 2
  

