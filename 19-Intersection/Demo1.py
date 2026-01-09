import numpy as np
n1=np.array([1,2,3,4])
n2=np.array([6,7,2,9])

print("Interating arra1...")
for a in n1:
    print(a)

print("Interating arra2...")
for a in n2:
    print(a)

resap=np.intersect1d(n1,n2)
print("Intersection = ",resap)

