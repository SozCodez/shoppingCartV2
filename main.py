import time
import datetime

#productIdx = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. "]
menuCnt = 0
start = True

products = {
    "Chips": 2.0,
    "Soda": 2.5,
    "Candy": 1.5,
    "Cookies": 3.0,
    "Water": 1.0,
    "Sandwich": 5.0
}

shoppingCart = {}

def viewProducts():
    choice1 = True
    while choice1:
        print("\n\n\n\n\n")
        for product, price in products.items():
            print(f"{product} - {price}")
        print()
        choice1Ret = input("Type 'close' to return: ")
        if choice1Ret == "close":
            break

def addProducts():
    menuCnt = 0
    choice2 = True
    print("\n\n\n\n\n")
    print("Which product would you like to add?")
    print()
    for product, price in products.items():
        menuCnt += 1
        print(f"{menuCnt}. {product} - ${price:,.2f}")
    print()
    menuCnt = 0
    addProd = int(input("Enter product number: "))
    if addProd == 1:
        if "Chips" not in shoppingCart:
            shoppingCart["Chips"] = 1
        else:
            shoppingCart["Chips"] += 1
    elif addProd == 2:
        if "Soda" not in shoppingCart:
            shoppingCart["Soda"] = 1
        else:
            shoppingCart["Soda"] += 1
    elif addProd == 3:
        if "Candy" not in shoppingCart:
            shoppingCart["Candy"] = 1
        else:
            shoppingCart["Candy"] += 1
    elif addProd == 4:
        if "Cookies" not in shoppingCart:
            shoppingCart["Cookies"] = 1
        else:
            shoppingCart["Cookies"] += 1
    elif addProd == 5:
        if "Water" not in shoppingCart:
            shoppingCart["Water"] = 1
        else:
            shoppingCart["Water"] += 1
    elif addProd == 6:
        if "Sandwich" not in shoppingCart:
            shoppingCart["Sandwich"] = 1
        else:
            shoppingCart["Sandwich"] += 1
    else:
        print()
        print("Please enter valid product number..")

def removeItem():
    choice3 = True
    menuCnt = 0
    while choice3:
        print("\n\n\n\n\n")
        print("~~~~~ YOUR SHOPPING CART ~~~~~")
        print()
        if len(shoppingCart) != 0:
            for product, count in shoppingCart:
                menuCnt += 1
                print(f"{menuCnt}.", product, "x" + count)
            print()
            menuCnt = 0
            removeProd = (input("Enter product name capitalized to remove: "))
            for product in shoppingCart:
                if removeProd == product:
                    if shoppingCart[product] >= 2:
                        shoppingCart[product] -= 1
                    else:
                        shoppingCart.pop(product)
                else:
                    print("Not a valid product")
        else:
            print("Cart is empty. Returning in 3 sec.")
            time.sleep(3)
            choice3 = False
            break

def viewCart():
    choice4 = True
    menuCnt = 0
    while choice4:
        print("\n\n\n\n\n")
        print("~~~~~ YOUR SHOPPING CART ~~~~~")
        print()
        totalItemsInCart = 0
        for product in shoppingCart:
            totalItemsInCart += shoppingCart[product]
            menuCnt += 1
            print(f"{menuCnt}. {product} {products[product]} x{shoppingCart[product]}")
        print("Items:", totalItemsInCart)
        menuCnt = 0
        choice4Ret = input("Type 'close' to return: ")
        if choice4Ret != "close":
            choice4Ret = input("Please type 'close' to return: ")
        else:
            choice4 = False
            break

def viewTotal():
    choice5 = True
    menuCnt = 0
    while choice5:
        print("\n\n\n\n\n")
        print("~~~~~ YOUR SHOPPING CART ~~~~~")
        print()
        subtotal = 0
        for product in shoppingCart:
            menuCnt += 1
            subtotal += shoppingCart[product] * products[product]
            print(f"{menuCnt}. {product} x{shoppingCart[product]}")
        print()
        print(f"Subtotal: ${subtotal:,.2f}")
        choice5Ret = input("Type 'close' to return: ")
        if choice5Ret != "close":
            choice5Ret = input("Please type 'close' to return: ")
        else:
            choice5 = False
            break

def checkoutCart():
    choice6 = True
    date = datetime.datetime.now()
    formattedDate = date.strftime("%Y-%m-%d")
    while choice6:
        subtotal = 0
        if len(shoppingCart) != 0:
            for product in shoppingCart:
                subtotal += shoppingCart[product] * products[product]
        else:
            print("\n\n\n\n\n")
            print("Cart is empty! returning in 2 sec.")
            time.sleep(2)
            break
        
        print("\n\n\n\n\n")
        print("~~~~~ CHECKOUT ~~~~~")
        print("Date:", formattedDate)
        print()
        print(f"Subtotal: ${subtotal:,.2f}")
        if subtotal >= 10:
            discount = 0.05
        elif subtotal >= 20:
            discount = 0.1
        elif subtotal >= 40:
            discount = 0.15
        else:
            discount = 0
        print(f"Discount: ${discount:,.2f}")
        amountSaved = subtotal * discount
        print(f"Saved: ${amountSaved:,.2f}")
        print()
        totalPrice = subtotal - amountSaved
        print(f"Total: ${totalPrice:,.2f}")
        choice6Ret = input("Type 'checkout' to complete order, 'close' to return: ")
        if choice6Ret == "close":
            choice6 = False
            break
        elif choice6Ret == "checkout":
            print()
            print("Thanks for shopping!")
            time.sleep(1)
            start = False
        break

while start:
    print("\n\n\n\n\n")
    print("~~~~~~~~~~ SMART SHOPPING CART ~~~~~~~~~~")
    print()
    print("1. View available products")
    print("2. Add product to cart")
    print("3. Remove product from cart")
    print("4. View shopping cart")
    print("5. View current total")
    print("6. Checkout")
    print()
    choice = input("Enter your choice #: ")
    if int(choice) == 1:
        viewProducts()
    elif int(choice) == 2:
        addProducts()
    elif int(choice) == 3:
        removeItem()
    elif int(choice) == 4:
        viewCart()
    elif int(choice) == 5:
        viewTotal()
    elif int(choice) == 6:
        checkoutCart()
        start = False
    else:
        print("Invalid option")
        time.sleep(2)