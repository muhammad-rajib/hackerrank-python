N = int(input())
L = []

for i in range(N):
    value = input().split(' ')
    
    if value[0] == 'insert':
        L.insert(int(value[1]), int(value[2]))
    elif value[0] == 'print':
        print(L)
    elif value [0] == 'append':
        L.append(int(value[1]))
    elif value[0] == 'sort':
        L.sort()
    elif value[0] == 'remove':
        L.remove(int(value[1]))
    elif value[0] == 'pop':
        L.pop()
    elif value[0] == 'reverse':
        L.reverse()
