print("Hello World!")
print("Welcome to Python 3 Basic Learning Session !")

print("------ ************ ----------------- ++++ ***********")
print("--------------------------------NEXT TOPIC - Data Types & Variables -----------------------------------")
product_name = "MacBook Pro Laptop"
price=17000.80
stock=10
RAM = 64
is_stock_available= stock>0 #True , if stock available

print(f"Product is :{product_name}, has Price of {price} and Quantity Available is : {stock}  which has RAM of {RAM}")

print("--------------------------------NEXT TOPIC - INPUT Types-----------------------------------")
RAM = int (input("How much RAM MAC Book Pro you want ?"))

print("--------------------------------NEXT TOPIC -- IF Else and elif Statements Conditional-----------------------------------")
if RAM < 64:
    print("Please Don't assign to Developer")
elif RAM>128:
    print("Assign to ML Engineers only for better Tasks")
else:
    print("Assign to Web Developer only")

print("--------------------------------NEXT TOPIC -- LOOP -----------------------------------")
Laptops =["Dell", "MACBook", "HP", "Lenovo"]
for laptop in Laptops :
    print(f"Available Laptops Brands are  {laptop} ")

laptopRequirement = input("Which Laptop You want: ")
usesType =["Gaming","Programming","Movie","ML/AI Learning"]
if laptopRequirement.upper() == "MAC":

    if RAM > 256:
        print(f"you choose {laptopRequirement} which is best for {usesType[3]}")
    elif RAM > 128:
        print(f"You choose {laptopRequirement} which is best for {usesType[1]} ")
    elif RAM >64:
        print(f"You choose {laptopRequirement} which is best for {usesType[0]} ")
    else:
        print(f"You choose {laptopRequirement} which is best for {usesType[2]} ")
if laptopRequirement.upper() == "HP":

    if RAM > 256:
        print(f"you choose {laptopRequirement} which is best for {usesType[3]}")
    elif RAM > 128:
        print(f"You choose {laptopRequirement} which is best for {usesType[1]} ")
    elif RAM >64:
        print(f"You choose {laptopRequirement} which is best for {usesType[0]} ")
    else:
        print(f"You choose {laptopRequirement} which is best for {usesType[2]} ")
if laptopRequirement.upper() == "DELL":

    if RAM > 256:
        print(f"you choose {laptopRequirement} which is best for {usesType[3]}")
    elif RAM > 128:
        print(f"You choose {laptopRequirement} which is best for {usesType[1]} ")
    elif RAM >64:
        print(f"You choose {laptopRequirement} which is best for {usesType[0]} ")
    else:
        print(f"You choose {laptopRequirement} which is best for {usesType[2]} ")
if laptopRequirement.upper() == "LENOVO":

    if RAM > 256:
        print(f"you choose {laptopRequirement} which is best for {usesType[3]}")
    elif RAM > 128:
        print(f"You choose {laptopRequirement} which is best for {usesType[1]} ")
    elif RAM >64:
        print(f"You choose {laptopRequirement} which is best for {usesType[0]} ")
    else:
        print(f"You choose {laptopRequirement} which is best for {usesType[2]} ")


# Price Calculator
import random

print("--------- FUNCTION EXAMPLE--------------")
def calculateLaptop_price(price,tax):
    total_price = price + (price * (tax/100))
    return total_price


Laptop_price = 12000
Tax = 10
Final_Price = calculateLaptop_price(Laptop_price, Tax)
print(f"The Final Price after Billing is : {Final_Price}")

# MATH MODULES
def lottery():
    return random.randint(1,100)

print("---------MATH MODULE EXAMPLE--------------")
lottery_number = lottery()
print(f"Your lottery Number is : {lottery_number}")

print(" -------- END---------       ")