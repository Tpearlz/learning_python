# Import Numpy
import numpy as np

#1 Creating Arrays
#create a 1D array from a list
a = np.array([1,2,3])
print("1D Array:\n",a)

#create a 2D array (matrix)
b = np.array([[1,2], [3,4]])
print("2D Array:\n",b)

#2 Array Properties
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data type:", a.dtype)
print("Total elements:", a.size)

# 3. Special Arrays
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 3)))
print("Full with 7s:\n", np.full((2, 2), 7))
print("Identity Matrix:\n", np.eye(3))
print("Range with step:\n", np.arange(0, 10, 2))
print("Evenly spaced:\n", np.linspace(0, 1, 5))

