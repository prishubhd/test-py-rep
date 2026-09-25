"""Functions for saving product data and creating invoices."""


from datetime import datetime


def save(products, file):
    """Save the updated product information back to the text file."""

    f = open(file, "w")

    for p in products:
        f.write(
            p["id"] + "," +
            p["name"] + "," +
            p["brand"] + "," +
            str(p["stock"]) + "," +
            p["unit"] + "," +
            str(p["rate"]) + "\n"
        )

    f.close()


def invoice(customer, items, grand_total):
    """Create a unique invoice containing all products bought in one sale cycle."""

    # Create a unique filename for every sale
    filename = "Invoice_" + str(datetime.now().timestamp()) + ".txt"

    f = open(filename, "w")

    f.write("-------BuiltMart Invoice--------\n")
    f.write("Date and Time: " + str(datetime.now()) + "\n")
    f.write("Customer: " + customer + "\n")
    f.write("-" * 40 + "\n")

    # Write every product in the same bill
    for item in items:
        product = item["product"]

        f.write("Product: " + product["name"] + "\n")
        f.write("Brand: " + product["brand"] + "\n")
        f.write("Quantity: " + str(item["qty"]) + "\n")
        f.write("Type: " + product["unit"] + "\n")
        f.write("Price: Rs " + str(item["amount"]) + "\n")
        f.write("Discount: Rs " + str(item["discount"]) + "\n")
        f.write("Final Cost: Rs " + str(item["total"]) + "\n")
        f.write("-" * 40 + "\n")

    f.write("Grand Total: Rs " + str(grand_total) + "\n")

    f.close()

    print("Invoice saved to " + filename)


def restock_invoice(product, qty):
    """Create a unique bill containing details of a product restock."""

    # Create a unique filename for every restock
    filename = "Restock_" + str(datetime.now().timestamp()) + ".txt"

    f = open(filename, "w")

    f.write("-------BuiltMart Restock--------\n")
    f.write("Date and Time: " + str(datetime.now()) + "\n")
    f.write("-" * 40 + "\n")
    f.write("Product: " + product["name"] + "\n")
    f.write("Brand: " + product["brand"] + "\n")
    f.write("Quantity Added: " + str(qty) + "\n")
    f.write("Unit: " + product["unit"] + "\n")
    f.write("New Stock: " + str(product["stock"]) + "\n")
    f.write("-" * 40 + "\n")

    f.close()

    print("Restock bill saved to " + filename)