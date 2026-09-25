"""Functions for reading hardware product information from a text file."""
def read(file):
    """Read product information from the file and return it as a list of dictionaries."""

    products = []

    try:
        # Open the product file
        f = open(file, "r")

        for line in f.readlines():
            data = line.strip().split(",")

            # Store product details in a dictionary
            product = {
                "id": data[0],
                "name": data[1],
                "brand": data[2],
                "stock": int(data[3]),
                "unit": data[4],
                "rate": float(data[5])
            }

            products.append(product)

        f.close()

    except FileNotFoundError:
        print("File not found.")

    return products