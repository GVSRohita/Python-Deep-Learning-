import numpy as np

'''creating a  random vector of size 15 having only Integers in the range 1-20
np.random.randint(low=1, high=100, size=4, dtype)'''
vector = np.random.randint(1, 20, 15)
print("vector with random values and of size 15 having only Integers in the range 1-20")
print(vector)
# reshape the array to 3 by 5 array = np.reshape(row, column)
print("Reshaping the array to 3 by 5 ")
array = vector.reshape(3, 5)
print(array)
'''' replacing  the max in each row by 0
 where(condition, if true this value , false this value)
 numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)'''
array1 = np.where(array == np.amax(array, axis=1, keepdims=True), 0, array)
print("After replacing  the max in each row by 0")
print(array1)