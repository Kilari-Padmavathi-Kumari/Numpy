import numpy as np
n=np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print("3D Array = \n",n)

resap=n.reshape(-1)
print("\nReshaped to 1D array = ",resap)