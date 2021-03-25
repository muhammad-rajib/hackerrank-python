import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Solution 2
"""
import numpy

a = numpy.array(input().split(), float)
print(a[::-1])
"""