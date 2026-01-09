import numpy as np

n1 = np.array([1, 2, 3, 4, 5, 6])

print("Iterating array1")
for a in n1:
    print(a)

resap = np.array_split(n1, indices_or_sections=2)

print("Array after splitting return 2 arrays")
for a in resap:
    print(a)
