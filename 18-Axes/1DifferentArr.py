import numpy as np
n1=np.array([5,10,15,20,25,30,35,40,45,50])
n2=np.array([30,35,50,55,60,65,75,85,95,100])

print("Interating arra1...")
for a in n1:
    print(a)

print("Interating arra2...")
for a in n2:
    print(a)

resap=np.setdiff1d(n1,n2)
print("difference b/w two arrays = ",resap)

