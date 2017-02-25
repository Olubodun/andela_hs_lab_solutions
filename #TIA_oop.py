# A shopping cart program modelled with OOP
class ShoppingCart:
    def __init__(self):
        total=0
        items={}
        self.total = total
        self.items=items
        
    def add_item(self, item_name, quantity, price):
        self.item_name=item_name
        self.quantity=quantity
        self.price=price
        self.total += (self.price*self.quantity)
        self.items[self.item_name]=self.quantity

    def remove_item(self, item_name, quantity, price):
        self.item_name=item_name
        self.quantity=quantity
        self.price=price
        currentqty = self.items[self.item_name]
        if self.quantity>=currentqty:
            self.items.pop(self.item_name)
            self.total -= (self.price * currentqty)
        else:
            currentqty -= self.quantity
            self.items[self.item_name]=currentqty
            self.total -= (self.price * self.quantity)

    def checkout(self, cash_paid):
        self.cash_paid = cash_paid
        if self.cash_paid < self.total:
            return "Cash paid not enough"
        else:
            return self.cash_paid - self.total

class Shop(ShoppingCart):
    def __init__(self):
        quantity = 100
        self.quantity=quantity

    def remove_item(self):
        self.quantity-=1