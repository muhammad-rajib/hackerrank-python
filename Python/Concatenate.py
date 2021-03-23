import numpy

n, m, p = map(int, input().split())
lst = []
lst2 = []

for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

for i in range(m):
    l2 = list(map(int, input().split()))
    lst2.append(l2)

arr1 = numpy.array(lst)
arr2 = numpy.array(lst2)
print(numpy.concatenate((arr1, arr2)))