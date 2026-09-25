"""Functions for displaying, selling and restocking hardware products."""

from write import save, invoice, restock_invoice


def display(products):
    """Display all available hardware products in a readable table."""

    print("\n" + "BuiltMart Hardware Store".center(80))
    print("-" * 80)
    print(f"{'ID':<6}{'Product':<20}{'Brand':<20}{'Stock':<10}{'Unit':<12}{'Rate'}")

    for p in products:
        print(f"{p['id']:<6}{p['name']:<20}{p['brand']:<20}{p['stock']:<10}{p['unit']:<12}{p['rate']:>7}")

def get_discount(product, qty):
    """Calculate a 5% discount when the required quantity is reached."""

    if product["unit"] == "kg" and qty >= 50:
        return 0.05

    elif product["unit"] == "quantity" and qty >= 100:
        return 0.05

    return 0


def sell(products, file):
    """Sell one or more products and create one bill for the same transaction cycle."""

    customer = input("Customer name: ")

    # Store all products for the same bill
    items = []
    grand_total = 0

    while True:
        pid = input("Product ID: ")
        found = False

        try:
            qty = int(input("Quantity: "))

            if qty <= 0:
                print("Invalid quantity!")
                continue

        except ValueError:
            print("Invalid number!")
            continue

        # Search for the product ID
        for p in products:
            if p["id"] == pid:
                found = True

                if qty <= p["stock"]:
                    amount = qty * p["rate"]

                    discount_rate = get_discount(p, qty)
                    discount = amount * discount_rate

                    total = amount - discount

                    # Reduce stock
                    p["stock"] -= qty

                    # Add product to the same bill
                    items.append({
                        "product": p,
                        "qty": qty,
                        "amount": amount,
                        "discount": discount,
                        "total": total
                    })

                    grand_total += total

                    print("Product added to bill.")

                else:
                    print("Not enough stock.")

                break

        if not found:
            print("ID not found.")

        # Ask if another product should be added
        while True:
            more = input("Add another product? (yes/no): ").lower()

            if more == "yes":
                break

            elif more == "no":
                break

            else:
                print("Please enter yes or no.")

        if more == "no":
            break

    # Save updated stock and create one invoice
    if items:
        save(products, file)
        invoice(customer, items, grand_total)
        print("Sale done!")


def restock(products, file):
    """Add stock to an existing product and create a separate restock bill."""

    pid = input("Product ID to restock: ")

    for p in products:
        if p["id"] == pid:

            try:
                qty = int(input(f"Add qty for {p['name']}: "))

                if qty <= 0:
                    print("Invalid quantity!")
                    return

            except ValueError:
                print("Invalid number!")
                return

            # Increase product stock
            p["stock"] += qty

            # Save updated product information
            save(products, file)

            # Create separate restock bill
            restock_invoice(p, qty)

            print(f"New stock: {p['stock']}")
            return

    print("ID not found.")