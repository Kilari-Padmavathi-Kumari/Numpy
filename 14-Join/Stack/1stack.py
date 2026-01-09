import numpy as np
n1=np.array([1,2,3,4,5,6])
n2=np.array([6,5,4,3,2,1])
print("Iterating array1")
for a in n1:
    print(a)
print("Iterating array2")
for a in n2:
    print(a)
resap=np.stack((n1,n2))
print("after joining = ",resap)