inventory={
    "apple":70.5,
    "banana":45.5,
    "milk":60.0,
    "bread":45.5,
    "eggs":5.5,
    "cheese":25.5
}

cart=["apple","banana","milk","eggs","orange"]

print("InventoryType:",type(inventory))
print("The price of apple:",inventory["apple"])
print("CartType:",type(cart))

total_bill=0
for item in cart:
    if item in inventory:
        price=inventory[item]
        total_bill+=price
    else:
        print(item,"not available in the inventory")    

print("Total_Price:",total_bill)

cart_set=set(cart)
print("Unique cart item:",cart_set)
Product_Categories=("fruits","dairy","bakery")
print("Product_Categories:",Product_Categories)
print("Type of product actegories:",type(Product_Categories))
inventory["watermelon"] = None
print("Type of the item:",type(inventory["watermelon"]))

is_discount_applied=False
if total_bill>100:
    is_discount_applied=True

