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


# 4. Reshaping & Flattening
arr = np.arange(1, 7)
reshaped = arr.reshape((2, 3))
print("Reshaped 2x3:\n", reshaped)
print("Flattened:", reshaped.flatten())

# 5. Indexing & Slicing
matrix = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at row 1, col 2:", matrix[1, 2])
print("Second column:", matrix[:, 1])
print("Submatrix (rows 0-1, cols 1-2):\n", matrix[0:2, 1:3])