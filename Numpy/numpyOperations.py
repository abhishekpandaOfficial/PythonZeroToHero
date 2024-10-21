print("Coding on Numpy basic Operations ----")

import numpy as np

# Array Arithmetic:

a=np.array([1,2,3,4,5])
b=np.array([10,20,30,40,50])

sum_array = a + b
print("Sum of the Arrays are : ", sum_array) # Sum of the Arrays are :  [11 22 33 44 55]

# Statistical Functions:
mean_value = np.mean(a)
print("Mean value : ", mean_value) # Mean value :  3.0

# Reshaping an Array:
reshaped_array = np.arange(12).reshape(3, 4)  # Create a 3x4 array
print("Reshaped Array : \n ", reshaped_array)
# Reshaped Array :
#   [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Create a 1D array
data = np.array([10,20,30,40,50])

# Perform Operations
data_sum = np.sum(data)
print("Sum of the Array",data_sum) # Sum of the Array 150

data_mean = np.mean(data)
print("Mean of the Array : ", data_mean) # Mean of the Array :  30.0

data_squared = np.square(data)
print("Square of Array : ", data_squared) # Square of Array :  [ 100  400  900 1600 2500]

