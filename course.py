import numpy as np

array_1d = np.array([1,2,532])

for i in range (0,len(array_1d)):
    if array_1d[i]<10:
        print (bin(array_1d[i])[2:])
        
    else:
        print (array_1d[i])


array_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2d)