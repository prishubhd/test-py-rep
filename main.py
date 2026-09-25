"""Main program for the BuiltMart Hardware Store."""
from read import read
from rem import display, sell, restock

file = "data.txt"

# Load products from the text file
products = read(file)

# Main menu loop