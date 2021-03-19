t = int(input())

for i in range(t):
    a = int(input())
    s1 = input().split()
    b = int(input())
    s2 = input().split()

    check = 'True'


    for i in range(len(s1)):
        if s1[i] not in s2:
            check = 'False'

    print(check)
