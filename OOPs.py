from DataStructure import product

print("Welcome to OOPS Concepts using Python !")

#Scenario 1 : You are creating a system to manage products in an online store.
# Each product has attributes like name, price, and stock, and behaviorus like calculating total value.

# Define a Product Class
class Product:
# Special method __init__ to initialize attributes
    def __init__(self,name,price,stock):
        self.name = name    # Attribute: product name
        self.price = price  # Attribute: product price
        self.stock = stock  # Attribute: product stock

# Method to calculate total value of stock
    def calculateStockValue(self):
        return self.price * self.stock

# Creating an object of the Product class

productObj1 = Product("IPhone",12000,15)


# Accessing attributes and methods
print(f"Product is {productObj1.name}, Price is : ${productObj1.price} and Stocks are Available : {productObj1.stock}")
print(f"Total Value of Stocks in our Shop : ${productObj1.calculateStockValue()}")

# Inheritance Concepts
print("Working on ")
