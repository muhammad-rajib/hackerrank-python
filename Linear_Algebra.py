import numpy

n = int(input())
lst = []

for i in range(n):
    l = list(map(float, input().split()))
    lst.append(l)

print(round(numpy.linalg.det(lst), 2))