from app.errors import SweetNotFoundError, OutOfStockError

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
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