cart_subtotal = 0.0

while True:
   
    choice = input("Welcome to your shopping cart! Choose what you would like to do today: Type 1 if you would like to add an item price to your cart. Type 2 if you would like to view your current subtotal. Type 3 if you would like to checkout and exit. ")
    choice = int(choice)
    if choice == 1:
        item_price = input("What is the price of your item? ")
        item_price = float(item_price)
        cart_subtotal += item_price
    elif choice == 2:
        print(f'Your current cart subtotal is {cart_subtotal}')
    elif choice == 3:
        calculate_tax = 0.13 * cart_subtotal
        calculate_grand_total = cart_subtotal + calculate_tax
        print(f'Here is your receipt: Subtotal: {cart_subtotal} Tax Amount: {calculate_tax} Final Grand Total: {calculate_grand_total}')
        break
    else:
        print("Invalid! Please pick a proper choice!")
