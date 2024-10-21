from Hello import price

print("--------------- Learning Data Structures ----------------")

#LISTS - Un-Ordered Collections
print("--------LISTS EXAMPLE--------")

prod_cart =["IPhone","Samsung","Oppo","Vivo"]

# Adding New item to the Cart
prod_cart.append("One Plus")

print(f"Now the Products are : {prod_cart}")

# Removing New item to the Cart
prod_cart.remove("Samsung")
print(f"Now the Products are : {prod_cart}")

#Slicing Elements in Lists
print(f"Before Slicing the Products are in the Cart : {prod_cart}") #O/p = ['IPhone', 'Samsung', 'Oppo', 'Vivo', 'One Plus']
cart = prod_cart[:2] # list[start:stop:step]

print(f"After Slicing  the Products are : {cart}") # cart[:2] means slice from the beginning of the list (index 0) up to,
                                                        # but not including, index 2 but will include 0.
                                                            # O/p = ['IPhone', 'Samsung']

cart = prod_cart[2:4] # list[start:stop:step]
print(f"After Slicing  the Products  in 2nd time are : {cart}") #o/p = ['Oppo', 'Vivo']


#Sets - Un-Ordered Collections
print("--------SETS EXAMPLE--------")
unique_visitors ={"Abhishek","Namrata","Reyansh","Akshita"}
print(f"Before Adding the Visitors are : {unique_visitors}")
#Adding New Visitor
unique_visitors.add("Janaki")
print(f"After Adding the Visitors are : {unique_visitors}")

# Trying to add Duplicate Visitors
unique_visitors.add("Abhishek")
print(f"After Adding the Duplicate Visitors are : {unique_visitors}") # It will not add Duplicate Values

#Checking for Membership
name = input("Tell me your Name Please Sir : ")
if name  in unique_visitors:
    print(f"{name} has Visited the Site")
else:
    print(f"{name} has not visited the Site Once till now!")

anonymous_visitors ={"Charlie","John"}

#Union of all Visitors
Total_Visitors_Lists = unique_visitors.union(anonymous_visitors)
print(f"Now the Total Visitors are : {Total_Visitors_Lists}")


#DICTIONARIES -- A Collection with Key Value Pairs
print("--------DICTIONARIES EXAMPLE--------")

product_catalogs = {
    101:{
        "name":"Biscuits",
        "price": 30,
        "stock":10
    },
    102:{
        "name":"OIL",
        "price":300,
        "stock":5
    }
}


product_id = 102
product = product_catalogs.get(product_id)
print(f"The Product Details are : {product['name']} & {product['price']} INR & {product['stock']} Stocks")

#Tuples -- Same as Lists but Immutable
print("--------TUPLES EXAMPLE--------")

city_Details =("Bangalore","Karnataka","INDIA")

#Accessing elements in a Tuple
print(f"City Name is : {city_Details[0]} and the State is {city_Details[1]} and which is under Country {city_Details[2]}")