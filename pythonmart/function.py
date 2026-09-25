# Read data from text file
def read_data(file):
    products = []

    with open(file, "r") as f:
        for line in f:
            data = line.strip().split(",")
        
            #merging the extra pieces back into the brand.
            if len(data) > 6:
                # Join everything from index 2 up to (length - 3) back into one brand string
                brand_parts = data[2:-3] 
                brand = ",".join(brand_parts)
                
                # Rebuild the clean list: ID, Name, Brand, Stock, Unit, Rate
                data = [data[0], data[1], brand, data[-3], data[-2], data[-1]]

            product = {"id": data[0], "name": data[1],"brand": data[2],"stock": int(data[3]),"unit": data[4],"rate": int(data[5])}
            products.append(product)

    return products

# Display all products
def display_products(products):
    print("\nAvailable Hardware Products")
    print("-" * 80)
    print(f"{'ID':<6}{'Product':<20}{'Brand':<20}{'Stock':<10}{'Unit':<12}{'Rate'}")
    print("-" * 80)
    for p in products:
        print(f"{p['id']:<6}{p['name']:<20}{p['brand']:<20}{p['stock']:<10}{p['unit']:<12}{p['rate']}")


# Save updated inventory back to file
def save_data(products, file):
    with open(file, "w") as f:
        for p in products:
            # We write the brand back exactly as it is (even with commas)
            f.write(
                f"{p['id']},{p['name']},{p['brand']},{p['stock']},{p['unit']},{p['rate']}\n"
            )

# Sell product
def sell_product(products, file):
    customer = input("Enter customer name: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter quantity to buy: "))

    for p in products:
        if p["id"] == product_id:
            if quantity <= p["stock"]:
                total = quantity * p["rate"]
                discount = 0

                # Discount calculation
                if p["unit"] == "kg" and quantity >= 50:
                    discount = total * 0.05

                elif p["unit"] == "quantity" and quantity >= 100:
                    discount = total * 0.05
                final_amount = total - discount
                p["stock"] -= quantity
                save_data(products, file)

                generate_invoice( customer,p,quantity, discount, final_amount )
                print("\nSale completed successfully!")
                return


            else:
                print("Not enough stock available.")
                return


    print("Product ID not found.")



# Generate invoice
def generate_invoice(customer, product, quantity, discount, final_amount):

    filename = customer + "_invoice.txt"

    with open(filename, "w") as f:
        f.write("PythonMart Hardware Store\n")
        f.write("-----------------------------\n")
        f.write("Customer Name: " + customer + "\n")
        f.write("Product Name: " + product["name"] + "\n")
        f.write("Brand: " + product["brand"] + "\n")
        f.write("Unit: " + product["unit"] + "\n")
        f.write("Quantity: " + str(quantity) + "\n")
        f.write("Rate: Rs." + str(product["rate"]) + "\n")
        f.write("Discount: Rs." + str(discount) + "\n")
        f.write("Total Amount: Rs." + str(final_amount) + "\n")

    print("Invoice generated:", filename)