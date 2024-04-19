from shoppingCart import Item, ShoppingCart

if __name__ == "__main__":
    
    #create some items
    item1 = Item(name="Shirt", price= 25)
    item2 = Item(name="Jeans", price= 40)
    item3 = Item(name="Shoes", price= 60)
    
    #Create a Shopping cart
    cart = ShoppingCart()
    
    #add items to the cart
    cart.add(item1)
    cart.add(item2)
    cart.add(item3)
    
    # Calculate the total price 
    total_price = cart.total()
    print(f"Total price in the Shopping cart: ${total_price}")
    
    # Get the number of items in the cart 
    num_items = len(cart)
    print(f"Number of items in the cart: {num_items}")