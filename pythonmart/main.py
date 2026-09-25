from function import read_data, display_products, sell_product
file = "Data.txt"

products = read_data(file)

while True:
    print("\nWelcome To PythonMart Hardware Store")
    print("1. Display Products")
    print("2. Sell Product")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products(products)

    elif choice == "2":
        sell_product(products, file)

    elif choice == "3":
        print("Thank you for using PythonMart Hardware Store System.")
        break

    else:
        print("Invalid choice. Please try again.")