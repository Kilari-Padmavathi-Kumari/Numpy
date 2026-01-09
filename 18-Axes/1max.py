import numpy as np
n=np.array([[2,3,4,5],[6,7,8,9],[10,11,12,13]])
print("Iterating 2D array...")
for a in n:
    print(a)

print("\nMinimum value = ",n.min())
print("Minimum value with axis 0 (vertical axes) = ",n.min(axis=0))
print("Minimum value with axis 1 (vertical axes) = ",n.min(axis=1))