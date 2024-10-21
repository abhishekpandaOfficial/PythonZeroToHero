import json

from DataStructure import product

print("Welcome to File Handling Master Class!")

# Writing to CSV file

import csv

# Customer purchased details to be written
customer_details =[

                    ["ID","Name","Product","Price"],
                    [101,"Abhishek","IPhone",120000.00],
                    [102,"Namrata","Samsung",45000.70],
                    [103,"Reyansh","Motorola",65000.00],
                    [104,"Akshita","TV",35000.00]
                ]

# Writing data to a CSV file
with open('Customer.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(customer_details)
print(f"Customer data written to 'customers.csv'")

#Reading from a CSV file:

with open('Customer.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Customer data to be written in JSON format
customer_data = {
    "customers": [
        {"CustomerID": 101, "Name": "Alice", "Product": "MacBook", "Price": 17000.80},
        {"CustomerID": 102, "Name": "Bob", "Product": "iPhone", "Price": 1200.50},
        {"CustomerID": 103, "Name": "Charlie", "Product": "iPad", "Price": 999.99}
    ]
}
# Writing data to a JSON file
with open('customers.json', mode='w') as file:
    json.dump(customer_data,file,indent=4)
print("Customer data written to 'customers.json'")

# Reading data From a JSON file
with open('customers.json', mode='r') as file:
    customer_data=json.load(file)

# Printing the customer data
for customer in customer_data['customers']:
    print(f"CustomerID: {customer['CustomerID']}, Name: {customer['Name']}, Product: {customer['Product']}, Price: {customer['Price']}")

import os

# Get current working directory
current_directory = os.getcwd()
print(f"The Current Working Directory is : {current_directory}")

#Check if a File Exists
file_exists = os.path.exists('customers.csv')
print(f"The File Exists or Not ? {file_exists}")

# Creating a new directory
new_directory = "Test"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"The Directory is Created and that is  {new_directory}")
else:
    file = os.path.exists(new_directory)
    print(f"The File Exists or Not ? {file}")



#pathlib - The pathlib module provides an object-oriented approach to working with file paths.
from pathlib import Path
# Create a Path object for the current directory
Current_Directory = Path.cwd() # /Users/abhishekpanda/Documents/study/ML/Python/Study1
print(f"The Current Directory  from path Lib is : {current_directory}")

# Check if a file exists
csv_file = Current_Directory/'customers.csv'
print(f"Does 'customers.csv' exist?: {csv_file.exists()}")

# Creating a new directory using Path
new_dir = Current_Directory/'backup'
if not new_dir.exists():
    new_dir.mkdir()
    print(f"Created new directory: {new_dir}")

# Creating a new file path using Path
new_file_path = new_dir/'customer.csv'
print(f"New file path: {new_file_path}")