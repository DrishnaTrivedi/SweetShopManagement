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
    