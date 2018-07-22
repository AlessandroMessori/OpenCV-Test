import numpy as np


def create_np_array(text):
    print(text)
    data = []
    stop = False
    while not stop:
        element = input()

        if element < 0:
            stop = True
        else:
            data.append(element)

    return np.array(data)


arr1 = create_np_array("add integer numbers to add to first sequence:")
# arr2 = create_np_array("add integer numbers to add to second sequence:")

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
# print(arr1 + arr2)
# print(arr1.dot(arr2))

for el in np.nditer(arr1, order="F"):
    print(el)
