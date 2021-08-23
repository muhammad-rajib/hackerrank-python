from collections import deque

N = int(input())
d = deque()

for i in range(N):
    value = input().split()

    if value[0] == 'append':
        d.append(value[1])
    elif value[0] == 'pop':
        d.pop()
    elif value[0] == 'popleft':
        d.popleft()
    elif value[0] == 'appendleft':
        d.appendleft(value[1])

print(' '.join(d))