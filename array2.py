# 1. Positive Indexing
import array
from copy import error
from operator import index


arr = [10, 20, 30, 40, 50]
print("Positive Indexing:")
print(arr[0])  # Output: 10
print(arr[2])  # Output: 30
print(arr[4])  # Output: 50

# 2. Negative Indexing
print("\nNegative Indexing:")
print(arr[-1])  # Output: 50 (last element)
print(arr[-2])  # Output: 40
print(arr[-5])  # Output: 10 (first element)

# 3. Modifying Elements Using Index
print("\nModifying Elements:")
print("Original array:", arr)
arr[1] = 25
arr[-1] = 55
print("Modified array:", arr)

# 4. Index Error # Index out of range
arr = array('i', [10, 20, 30])
    print(arr[3])  # Index out of range.