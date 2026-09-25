while True:
    print("\nWelcome To BuiltMart Hardware Store")
    print("1. Display Products")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display(products)

    elif choice == "2":
        sell(products, file)

    elif choice == "3":
        restock(products, file)

    elif choice == "4":
        print("Thank you for using our BuiltMart Hardware Store.")
        break

    else:
        print("Invalid choice.")