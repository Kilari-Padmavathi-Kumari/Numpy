import numpy as np
n=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Iterating")
for a in n:
    print("Each matrix(2D)=")
    print(a)
print("Type = ",type(n))
print("Data Type = ",n.dtype)
print("Dimensions = ",n.ndim) 