import pytest
from app.sweet import Sweet
from app.sweetshop import SweetShop
from app.errors import SweetNotFoundError, OutOfStockError
from app.cart import Cart
from app.shoppingCart import ShoppingCart

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

def test_add_sweet_duplicate_raises():
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    with pytest.raises(ValueError):
        shop.add_sweet(sweet)  # duplicate




# DELETING SWEETS


def test_delete_sweet_by_id(sample_shop):
    sample_shop.delete_sweet_by_id(1001)
    with pytest.raises(SweetNotFoundError):
        sample_shop.get_sweet_by_id(1001)
    assert len(sample_shop.get_all_sweets()) == 2  # One sweet should be deleted

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
  
# SORT SWEETS TEST

def test_sort_by_name(sample_shop):
    sorted_sweets = sample_shop.sort_sweets(by="name")
    names = [s.name for s in sorted_sweets]
    assert names == sorted(names)

def test_sort_by_price(sample_shop):
    sorted_sweets = sample_shop.sort_sweets(by="price")
    prices = [s.price for s in sorted_sweets]
    assert prices == sorted(prices)

def test_sort_sweets_invalid_key_returns_unsorted():
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50)
    sample_shop = SweetShop()   
    sample_shop.add_sweet(sweet1)
    sample_shop.add_sweet(sweet2)
    result = sample_shop.sort_sweets(by="unknown")
    assert result == [sweet1, sweet2]


# PURCHASING SWEETS

def test_purchase_sweet(sample_shop):
    sample_shop.purchase_sweet(1002, 10)
    assert sample_shop.get_sweet_by_id(1002).quantity == 40

def test_purchase_insufficient_stock(sample_shop):
    with pytest.raises(OutOfStockError):
        sample_shop.purchase_sweet(1003, 100)
    # sweet 1003 had 15 qty only


#restock 

def test_restock_sweet(sample_shop):
    sample_shop.restock_sweet(1001, 10)
    assert sample_shop.get_sweet_by_id(1001).quantity == 30



# ----------------------------------


 #Update sweets
def test_update_sweet(sample_shop):
    sample_shop.update_sweet_by_id(id = 1001, by = "name"  , value = "kaju katli updated")
    assert sample_shop.get_sweet_by_id(1001).name == "kaju katli updated"
    with pytest.raises(SweetNotFoundError):
        sample_shop.update_sweet_by_id(id = 9999, by = "name", value = "non-existent sweet")

def test_low_stock_alert(sample_shop):
    low_stock_sweets = sample_shop.low_stocks(threshold = 30)
    assert len(low_stock_sweets) == 2
    assert low_stock_sweets[0].name == "Kaju Katli"
    assert low_stock_sweets[1].name == "Gajar Halwa"

#counting total price of the inventory
def test_total_inventory_value(sample_shop):
    value = sample_shop.calc_inventory_value()
    assert value == 1950 # (50*20) + (10*50) + (30*15) = 1000 + 500 + 450 = 1950        

# Edge case: inventory value after clearing shop
def test_total_inventory_value_after_clearing(sample_shop):
    sample_shop.clear_shop()
    value = sample_shop.calc_inventory_value()
    assert value == 0

# test for clearing the shop

def test_clear_Shop(sample_shop):
    sample_shop.clear_shop()
    assert len(sample_shop.get_all_sweets()) == 0

# Edge case: clearing an already empty shop
def test_clear_empty_shop(sample_shop):
    sample_shop.clear_shop()
    sample_shop.clear_shop()  # Should not raise error
    assert len(sample_shop.get_all_sweets()) == 0


def remove_kaju_katli_as_Expired(sample_shop):
    sample_shop.remove_kaju_katli_as_Expired()
    assert len(sample_shop.get_all_sweets()) == 2  # Kaju Katli should be removed
    with pytest.raises(SweetNotFoundError):
        sample_shop.get_sweet_by_name("Kaju Katli")
    
    with pytest.raises(SweetNotFoundError):
        sample_shop.get_sweet_by_name("Kaju Katli")




def test_cart_add_unique_items():
    cart = ShoppingCart()
    cart.add_items(1001, 2)  # Added 2 Kaju Katli
    cart.add_items(1002, 3)  # Add 3 Gulab Jamun

    assert len(cart.items) == 2
    assert cart.items[0].sweet_id == 1001
    assert cart.items[0].quantity == 2
    assert cart.items[1].sweet_id == 1002
    assert cart.items[1].quantity == 3


def test_add_duplicate_item():
    #arrange
    cart = ShoppingCart()
   
    cart.add_items(1001, 2) 
    #act
    cart.add_items(1001, 1)  # adding kaju katli again
    #assertion
    assert cart.items[0].quantity == 3


def test_remove_item():
    #arrange
    cart = ShoppingCart()
    cart.add_items(1002, 2)
    #act
    cart.remove_items(1002)

    #assert
    assert len(cart.items) == 0
    


def test_remove_item_not_found():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.remove_items(9999)  # Non-existent sweet ID


def test_process_cart(sample_shop):
    #arrange
    cart = ShoppingCart()
    cart.add_items(1001, 5)
    cart.add_items(1002, 4)
    #act
    # Process the cart
    sample_shop.process_cart(cart)

    #assert
    assert sample_shop.get_sweet_by_id(1001).quantity == 15  # 20 - 5
    assert sample_shop.get_sweet_by_id(1002).quantity == 46  #50 - 4

def test_cart_clear():
    #arrange
    cart = ShoppingCart()
    cart.add_items(1002, 4)

    #act
    cart.clear()  # Clear the cart after processing

    #assert
    assert len(cart.items) == 0  # Cart empty


def test_reduce_qty(sample_shop):
     cart = ShoppingCart()
     cart.add_items(1001, 7)
     

     cart.reduce_qty(1001)


     assert len(cart.items) == 1
     
     assert cart.items[0].quantity == 6

