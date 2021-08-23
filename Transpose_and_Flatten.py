import numpy

n, m = map(int, input().split())
lst = []

for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

arr = numpy.array(lst)
print(numpy.transpose(arr))
print(arr.flatten())