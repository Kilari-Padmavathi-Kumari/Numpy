import numpy as np
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

result = np.hsplit(b, 2)
print(result)
