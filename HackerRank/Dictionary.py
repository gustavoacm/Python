# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:34:46 2024

@author: Usuario
"""

#dictionary
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
#morning invenrory
department_store = {} 
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores', sorted(department_store.items()))
print('-----------------')
#create an dempty shopping cart
cart = {}
purse = 1000
buy_items1 = ''
total_sum = float()
#loop through stores/dicts
for shop in (freelancers,antiques) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit the store) what do you want to buy: {shop}').lower()
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update string info
    buy_items1 += f'{buy_item}:{shop[buy_item]} Gp. '
    temp = shop.pop(buy_item)
    #update the cart
    cart.update({buy_item:temp}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
total_sum = sum(cart.values())
print(f'You Purchased {buy_items1}Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
#evening inventory
department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))