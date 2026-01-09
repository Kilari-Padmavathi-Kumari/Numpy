import numpy as np
n=np.array([10,20,30,40,20,30])
print("Iterating")
for a in n:
    print(a)

#Search
res=np.where(n==30)
print("\nElement 30 found at the following indexes : ")
print(res)