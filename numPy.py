import numpy as np

data = []
stop = False

while not stop:
    element = input()

    if element < 0:
        stop = True
    else:
        data.append(element)

arr = np.array(data)

print(arr.dtype)
print(arr.ndim)
print(arr)