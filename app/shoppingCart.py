from app.cart import Cart


class ShoppingCart:
    def __init__(self):
        self.items = []     #initializing an empty list to hold cart items

    def add_items(self, sweet_id, quantity):
        for i in self.items:
            if i.sweet_id == sweet_id:
                i.quantity += quantity
                return
        self.items.append(Cart(sweet_id, quantity))

    def remove_items(self, sweet_id):
        for i in self.items:
            if i.sweet_id == sweet_id:
                self.items.remove(i)
                return
        raise ValueError("Sweet not found in cart.")
    
    def clear(self):
        self.items = []

    def reduce_qty(self, sweet_id):
        for s in self.items:
            if s.sweet_id == sweet_id:
                s.quantity -= 1

        return
