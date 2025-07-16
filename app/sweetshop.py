from app.errors import SweetNotFoundError, OutOfStockError

class SweetShop:
    def __init__(self):
        self.sweets = []

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