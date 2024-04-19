from .item import Item

class ShoppingCart:
    def __init__(self):
        self.items = [] #List to store items in the cart
        
    def add(self, item: Item):
        self.items.append(item) #wiil include instance of the Item class
    
    def total(self) -> int: #sum all prices from the list 
        return sum(item.price for item in self.items)
    
    def __len__(self) -> int:
        return len(self.items)
    