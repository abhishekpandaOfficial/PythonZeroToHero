print("--------Coding on Numpy Fundamentals and Numpy Array-------")

import numpy as np

# Creating a NumPy array from a list
python_lists = [1,2,3,4,5,6,5,3]
numpy_array = np.array(python_lists)

print(f"Numpy Array is : {numpy_array}") # O/P : Numpy Array is : [1 2 3 4 5 6 5 3]

# Zeros Array:
zeros_array = np.zeros((2,3)) # 2x3 array filled with Zeros means 2 Rows and 3 Columns
print("Zeros Array : \n", zeros_array)
# Zeros Array :
#  [[0. 0. 0.]
#  [0. 0. 0.]]

# Ones Array:
one_array = np.ones((2,3)) # 2x3 array filled with Zeros means 2 Rows and 3 Columns
print(("Ones Array : \n"), one_array)
# Ones Array :
#  [[1. 1. 1.]
#  [1. 1. 1.]]

# Range Array:
range_array = np.arange(10) # Array with values from 0 to 9
print("Range Arrays : \n", range_array)
# Range Arrays :
#  [0 1 2 3 4 5 6 7 8 9]

# np.linspace() -> Creating an array with 5 equally spaced values between 0 and 1
linespace_array = np.linspace(0,1,5)
print("Values are : \n ", linespace_array)
# Values are :
#   [0.   0.25 0.5  0.75 1.  ]

# Shape: This gives the dimensions of the array.
# Creating a 2D array
array_2D = np.array([[1,2,3], [7,8,9]])
print("Shape of 2D Array is : ", array_2D.shape) # Shape of 2D Array is :  (2, 3)

# Size: This gives the total number of elements in the array.
print("Size of the Array : ",array_2D.size) # Size of the Array :  6

# Data Type: This tells you the data type of the array elements.
print("Data types of the Array is : ", array_2D.dtype) # Data types of the Array is :  int64

# Dimension: This shows how many dimensions the array has.
print("Dimension of the Array : ", array_2D.ndim) # Dimension of the Array :  2

# Using reshape(): Reshaping a 1D array to a 2D array
reshaped_arr = np.arange(12).reshape(3,4)
print("Reshaped Array :\n", reshaped_arr)
# Reshaped Array :
#  [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Using ravel(): This flattens a multi-dimensional array into a 1D array.
flat_array = reshaped_arr.ravel()
print("Flat Array is : ", flat_array) # Flat Array is :  [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Slicing and Indexing
# Accessing Elements:
element = reshaped_arr[0,1]
print("Element at (0,1):",element) #Element at (0,1): 1

#Accessing Rows and Columns:

#Accessing the 1st Row
first_row = reshaped_arr[0,:]
print("first Row : ", first_row) # first Row :  [0 1 2 3]

# Accessing the second column
second_column = reshaped_arr[:,1]
print("Second Column : ", second_column) #Second Column :  [1 5 9]

# ------------------------
# Reshaped Array :
#  [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# ------------------------

# Slicing a sub-array
sub_array = reshaped_arr[0:2,1:3]
print("Sub Array is : \n ", sub_array)

# Sub Array is :
#  [[1 2]
#  [5 6]]

# Advance Indexing
arr = np.array([1,2,3,4,5,6])

# Boolean indexing to get even numbers
even_arr = arr[arr % 2 == 0]
print("Even Number Array is : ", even_arr) #Even Number Array is :  [2 4 6]

# Copying an Array:
original_arr = np.array([1,2,3,4,5])
#  create a new array that does not affect the original array when modified, you should use the copy() method.
copied_arr = original_arr.copy()

copied_arr[0] =99
print("Original Array : ", original_arr) # Original Array :  [1 2 3 4 5]
print("Copied Array : ", copied_arr) # Copied Array :  [99  2  3  4  5]

# Referenced Array

referenced_arr = original_arr
referenced_arr[0]= 42
print("original Array After referencing is : ", original_arr) # original Array After referencing is :  [42  2  3  4  5]
print("Referenced Array : ",referenced_arr )  # Referenced Array :  [42  2  3  4  5]

# ----------------------------NumPy arrays in a real-time scenario, such as data analysis for a sales dataset.-------
print(" NumPy arrays in a real-time scenario, such as data analysis for a sales dataset.")

# 2D NumPy array to store sales data and calculated the total sales for each item efficiently using NumPy operations
# Sample sales data: [Item ID, Quantity Sold, Price per Item]
sales_data = np.array([
        [101, 5, 20.0],
        [102, 3, 15.0],
        [103, 2, 30.0],
        [104, 4, 10.0]
])

# # Calculating total sales per item
total_sales = sales_data[:,1] * sales_data[:,2]  # The colon (:) means to select all rows. and
                                                # The 1 refers to the second column (since indexing starts at 0, 1 is the second column).

# Displaying the results
for i , total in enumerate(total_sales):
    print(f"Total sales for Item ID {sales_data[i, 0]}: ${total:.2f}")

# Total sales for Item ID 101.0: $100.00
# Total sales for Item ID 102.0: $45.00
# Total sales for Item ID 103.0: $60.00
# Total sales for Item ID 104.0: $40.00





