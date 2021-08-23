n = int(input())
l1 = map(int, input().split())
b = int(input())
l2 = map(int, input().split())
l1 = set(l1)
l2 = set(l2)

print(len(l1.union(l2)))