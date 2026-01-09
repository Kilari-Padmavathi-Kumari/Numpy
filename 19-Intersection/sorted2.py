import numpy as np
n1=np.array([10,50,100,30,60,40])
n2=np.array([80,50,90,100,40,70])

print("Interating arra1...")
for a in n1:
    print(a)

print("Interating arra2...")
for a in n2:
    print(a)

resap=np.intersect1d(n1,n2)
print("Intersection = ",resap)

