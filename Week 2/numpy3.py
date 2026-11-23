# Array Slicing

import numpy as np

numbers = np.array([10,20,30,40,50,60,70])

print("First three:",numbers[0:3])
print("Last three:",numbers[4:])
print("Every second element:",numbers[::2])
print("Array in reverse:",numbers[::-1])
