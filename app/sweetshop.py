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

    
    