from app.errors import SweetNotFoundError, OutOfStockError
from app.cart import Cart   
from app.shoppingCart import ShoppingCart

class SweetShop:
    def __init__(self):
        self.sweets = []
        # Initializing an empty list to hold sweets in the shop     

    def add_sweet(self, sweet):
        if any(s.sweet_id == sweet.sweet_id for s in self.sweets):
            raise ValueError(f"Sweet with ID {sweet.sweet_id} already exists.")
        self.sweets.append(sweet)


    
    def get_all_sweets(self):
        return self.sweets

    def get_sweet_by_id(self, sweet_id):
        for sweet in self.sweets:
            if sweet.sweet_id == sweet_id:
                return sweet
        raise SweetNotFoundError("Sweet not found.")
    

    def get_sweet_by_name(self, name):
        for sweet in self.sweets:
            if sweet.name == name:
                return sweet
        raise SweetNotFoundError("Sweet not found.")

    
    def delete_sweet_by_id(self, sweet_id):
        for sweet in self.sweets:
            if sweet.sweet_id == sweet_id:
                self.sweets.remove(sweet)
                return
        raise SweetNotFoundError("Sweet not found.")
    

    def delete_sweet_by_name(self, name):
        for sweet in self.sweets:
            if sweet.name == name:
                self.sweets.remove(sweet)
                return
        raise SweetNotFoundError("Sweet not found.")
    

    #SEARCH SWEETS 
    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        results = self.sweets
        if name:
            results = [s for s in results if name.lower() in s.name.lower()]
        if category:
            results = [s for s in results if category.lower() == s.category.lower()]
        if min_price is not None:
            results = [s for s in results if s.price >= min_price]
        if max_price is not None:
            results = [s for s in results if s.price <= max_price]
        return results
    

    # SORT SWEETS
    def sort_sweets(self, by="name"):
        if by == "name":
            return sorted(self.sweets, key=lambda s: s.name)
        elif by == "price":
            return sorted(self.sweets, key=lambda s: s.price)
        else:
            return self.sweets
        


    # purchase sweet
    def purchase_sweet(self, sweet_id, quantity):
        sweet = self.get_sweet_by_id(sweet_id)
        if sweet.quantity >= quantity:
            sweet.quantity -= quantity
        else:
            raise OutOfStockError("Not enough stock.")
        
    
    def restock_sweet(self, sweet_id, quantity):
        sweet = self.get_sweet_by_id(sweet_id)
        sweet.quantity += quantity


    #update sweet
    def update_sweet_by_id(self,id, by , value):
        for sweet in self.sweets:
            if sweet.sweet_id == id:
                if by == 'name':
                    sweet.name = value
                elif by == 'category':
                    sweet.category = value
                elif by == 'price':
                    sweet.price = value
                elif by == 'quantity':
                    sweet.quantity = value
                return
        raise SweetNotFoundError("Sweet not found.")
    
    def low_stocks(self, threshold):
        low_stocks = []
        for sweet in self.sweets:
            if(sweet.quantity < threshold):
                low_stocks.append(sweet)
        return low_stocks
    
    def calc_inventory_value(self):
        value  = 0
        for sweet in self.sweets:
            value = value + (sweet.price * sweet.quantity)
        return value


    def clear_shop(self):
        self.sweets = []

    # FIND MAX PRICE SWEET
    def find_max_price_sweet(self):
        if not self.sweets:
            return None
        return max(self.sweets, key=lambda s: s.price)  
    

    #REMOVE EXPIRY DATE SWEET
    #SUPPOSE KAJU KATLI IS EXPIRED. SO REMIVE THAT 
    def remove_kaju_katli_as_Expired(self):
        sweet = self.get_sweet_by_name("Kaju Katli")
        if sweet:   
            self.sweets.remove(sweet)
    
    # FOR PROCESSING CART   - change in our shop
    def process_cart(self, cart):
        for item in cart.items:
            sweet = self.get_sweet_by_id(item.sweet_id)
            if sweet.quantity < item.quantity: 
                raise OutOfStockError("Not enough stock ")
            sweet.quantity -= item.quantity
        return True 
