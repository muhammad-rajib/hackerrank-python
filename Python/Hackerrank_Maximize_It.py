# K, M = map(int, input().split())

# max_container = []

# for i in range(K):
#     l = input().split()
#     x = 0
#     for i in l:
#         i = int(i)
#         if x < i:
#             x = i
#     max_container.append(x)

# S = 0
# for v in max_container:
#     S += v**2

# print(S % M)
k, m = map(int, input().split())
A = []
lengths = []

for i in range(k):
    raw = input().split()
    A.append([int(a) for a in raw[1:]])
    lengths.append(int(raw[0]))

indexes = [0] * k
totalCombinations = 1
for length in lengths:
    totalCombinations *= length
    
maximum = 0
for _ in range(totalCombinations):
    f = 0
    for j in range(k):
        f += (A[j][indexes[j]] ** 2)
    f %= m
    if f > maximum:
        maximum = f
    indexes[-1] += 1
    for i in range(k - 1, -1, -1):
        if indexes[i] == lengths[i]:
            indexes[i] = 0
            indexes[i - 1] += 1

print(maximum)