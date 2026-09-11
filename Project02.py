print("=" * 35)
print("\tWELCOME TO CLOVER SHOP")
print("=" * 35)

print("\nAvailable product")

product = ["\n1. Rice    N50,000", "2. Chicken   N8,000", "3. Cooking oil  N12,000", "4. Sugar     N5,000", "5. Milk     N4,000"]
price = [50000, 8000, 12000, 5000, 4000]

for food in product:
    print(f"{food}")

print("\nChoose a product ")
choice = int(input(">> "))

def clover():

    if choice == 1:
        print("\nProvide quantity")
        quantity = int(input(">> "))

        cost = price[0] * quantity

        print(f"You bought {quantity} Rice")
        print(f"Cost: N{cost}")

        print("Buy another product?")

        R = input(">> ")

        if R == "yes":
            print("\nChoose a product")
            L = int(input(">> "))

            if L == 2:
                print("\nProvide quantity")
                quantitys = int(input(">> "))

                costs = price[1] * quantitys

                print(f"You bought {quantitys} Chicken")
                print(f"Cost: N{costs}")

                print("Buy another product?")
                R = input(">> ")

                if R == "no":
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nChicken * {quantitys}       N{costs}")
                    print(f"Rice * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")
                else:
                    print("SORRY WE OUT OF STOCK")
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nChicken * {quantitys}       N{costs}")
                    print(f"Rice * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")   

            elif L == 3:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[2] * quantitys

                    print(f"You bought {quantitys} Cooking oil")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}       N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}    N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

            elif L == 4:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[3] * quantitys

                    print(f"You bought {quantitys} Sugar")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                         
            elif L == 5:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[4] * quantitys

                    print(f"You bought {quantitys} Milk")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}       N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}       N{costs}")
                        print(f"Rice * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

        elif R == "no":
            print("=" * 25)
            print("\tRECIEPT")
            print("=" * 25)

            print(f"Rice * {quantity}          N{cost} ")

            print(f"\nTotal:            N{cost}")
            print("\nThank you for shopping!!")
        else:
            print("COMMAND ERROR")
       
    elif choice == 2:
        print("\nProvide quantity")
        quantity = int(input(">> "))

        cost = price[1] * quantity

        print(f"You bought {quantity} Chicken")
        print(f"Cost: N{cost}")

        print("Buy another product?")

        R = input(">> ")

        if R == "yes":
            print("\nChoose a product")
            L = int(input(">> "))

            if L == 1:
                print("\nProvide quantity")
                quantitys = int(input(">> "))

                costs = price[0] * quantitys

                print(f"You bought {quantitys} Rice")
                print(f"Cost: N{costs}")

                print("Buy another product?")
                R = input(">> ")

                if R == "no":
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Chicken * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")
                else:
                    print("SORRY WE OUT OF STOCK")
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Chicken * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")   

            elif L == 3:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[2] * quantitys

                    print(f"You bought {quantitys} Cooking oil")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}       N{costs}")
                        print(f"Chicken * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}    N{costs}")
                        print(f"Chicken * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

            elif L == 4:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[3] * quantitys

                    print(f"You bought {quantitys} Sugar")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Chicken * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Chicken * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                         
            elif L == 5:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[4] * quantitys

                    print(f"You bought {quantitys} Milk")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}           N{costs}")
                        print(f"Chicken * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}       N{costs}")
                        print(f"Chicken * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

        elif R == "no":
            print("=" * 25)
            print("\tRECIEPT")
            print("=" * 25)

            print(f"Chicken * {quantity}        N{cost} ")

            print(f"\nTotal:            N{cost}")
            print("\nThank you for shopping!!")
        else:
            print("COMMAND ERROR")

    elif choice == 3:
        print("\nProvide quantity")
        quantity = int(input(">> "))

        cost = price[2] * quantity

        print(f"You bought {quantity} Cooking oil")
        print(f"Cost: N{cost}")

        print("Buy another product?")

        R = input(">> ")

        if R == "yes":
            print("\nChoose a product")
            L = int(input(">> "))

            if L == 1:
                print("\nProvide quantity")
                quantitys = int(input(">> "))

                costs = price[0] * quantitys

                print(f"You bought {quantitys} Rice")
                print(f"Cost: N{costs}")

                print("Buy another product?")
                R = input(">> ")

                if R == "no":
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Cooking oil * {quantity}      N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")
                else:
                    print("SORRY WE OUT OF STOCK")
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Cooking oil * {quantity}       N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")   

            elif L == 2:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[1] * quantitys

                    print(f"You bought {quantitys} Chicken")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}       N{costs}")
                        print(f"Cooking oil * {quantity}         N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}    N{costs}")
                        print(f"Cooking oil * {quantity}       N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

            elif L == 4:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[3] * quantitys

                    print(f"You bought {quantitys} Sugar")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Cooking oil * {quantity}       N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}         N{costs}")
                        print(f"Cooking oil * {quantity}       N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                         
            elif L == 5:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[4] * quantitys

                    print(f"You bought {quantitys} Milk")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}           N{costs}")
                        print(f"Cooking oil * {quantity}      N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}       N{costs}")
                        print(f"Cooking oil * {quantity}    N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

        elif R == "no":
            print("=" * 25)
            print("\tRECIEPT")
            print("=" * 25)

            print(f"Cooking oil * {quantity}        N{cost} ")

            print(f"\nTotal:            N{cost}")
            print("\nThank you for shopping!!")
        else:
            print("COMMAND ERROR")


    elif choice == 4:
        print("\nProvide quantity")
        quantity = int(input(">> "))

        cost = price[3] * quantity

        print(f"You bought {quantity} Sugar")
        print(f"Cost: N{cost}")

        print("Buy another product?")

        R = input(">> ")

        if R == "yes":
            print("\nChoose a product")
            L = int(input(">> "))

            if L == 1:
                print("\nProvide quantity")
                quantitys = int(input(">> "))

                costs = price[0] * quantitys

                print(f"You bought {quantitys} Rice")
                print(f"Cost: N{costs}")

                print("Buy another product?")
                R = input(">> ")

                if R == "no":
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Sugar * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")
                else:
                    print("SORRY WE OUT OF STOCK")
                    print("=" * 25)
                    print("\tRECIEPT")
                    print("=" * 25)

                    print(f"\nRice * {quantitys}       N{costs}")
                    print(f"Sugar * {quantity}          N{cost} ")

                    print(f"\nTotal:            N{costs + cost}")
                    print("\nThank you for shopping!!")   

            elif L == 2:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[1] * quantitys

                    print(f"You bought {quantitys} Chicken")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}       N{costs}")
                        print(f"Sugar * {quantity}           N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}    N{costs}")
                        print(f"Sugar * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

            elif L == 3:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[2] * quantitys

                    print(f"You bought {quantitys} Cooking oil")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}         N{costs}")
                        print(f"Sugar * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}         N{costs}")
                        print(f"Sugar * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                         
            elif L == 5:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[4] * quantitys

                    print(f"You bought {quantitys} Milk")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}           N{costs}")
                        print(f"Sugar * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nMilk * {quantitys}       N{costs}")
                        print(f"Sugar * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

        elif R == "no":
            print("=" * 25)
            print("\tRECIEPT")
            print("=" * 25)

            print(f"Sugar * {quantity}        N{cost} ")

            print(f"\nTotal:            N{cost}")
            print("\nThank you for shopping!!")
        else:
            print("COMMAND ERROR")

    elif choice == 5:
            print("\nProvide quantity")
            quantity = int(input(">> "))

            cost = price[4] * quantity

            print(f"You bought {quantity} Milk")
            print(f"Cost: N{cost}")

            print("Buy another product?")

            R = input(">> ")

            if R == "yes":
                print("\nChoose a product")
                L = int(input(">> "))

                if L == 1:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[0] * quantitys

                    print(f"You bought {quantitys} Rice")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nRice * {quantitys}       N{costs}")
                        print(f"Milk * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nRice * {quantitys}       N{costs}")
                        print(f"Milk * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")   

                elif L == 2:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[1] * quantitys

                    print(f"You bought {quantitys} Chicken")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}       N{costs}")
                        print(f"Milk * {quantity}           N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nChicken * {quantitys}    N{costs}")
                        print(f"Milk * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

                elif L == 3:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[2] * quantitys

                    print(f"You bought {quantitys} Cooking oil")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}         N{costs}")
                        print(f"Milk * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nCooking oil * {quantitys}         N{costs}")
                        print(f"Milk * {quantity}          N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                         
                elif L == 4:
                    print("\nProvide quantity")
                    quantitys = int(input(">> "))

                    costs = price[3] * quantitys

                    print(f"You bought {quantitys} Sugar")
                    print(f"Cost: N{costs}")

                    print("Buy another product?")
                    R = input(">> ")

                    if R == "no":
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}           N{costs}")
                        print(f"Milk * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")
                    else:
                        print("SORRY WE OUT OF STOCK")
                        print("=" * 25)
                        print("\tRECIEPT")
                        print("=" * 25)

                        print(f"\nSugar * {quantitys}       N{costs}")
                        print(f"Milk * {quantity}        N{cost} ")

                        print(f"\nTotal:            N{costs + cost}")
                        print("\nThank you for shopping!!")

            elif R == "no":
                print("=" * 25)
                print("\tRECIEPT")
                print("=" * 25)

                print(f"Milk * {quantity}        N{cost} ")

                print(f"\nTotal:            N{cost}")
                print("\nThank you for shopping!!")
            else:
                print("COMMAND ERROR")   

clover()