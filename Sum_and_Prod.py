import numpy

n, m = map(int, input().split())
lst = []

for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

arr = numpy.array(lst)
print(numpy.prod(numpy.sum(arr, axis = 0)))


## Solution 2
"""
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))

"""