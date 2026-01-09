
import numpy as np

n1 = np.array([[1, 2, 3],[ 4, 5, 6]])

print("Iterating array1")
for a in n1:
    print(a)
#split array into 2
resap = np.array_split(n1, indices_or_sections=2)
print("\n array after splitting... ",resap)
print("Access splitting array individually....")
print("Array1 = ",resap[0])
print("Array2 = ",resap[1])
