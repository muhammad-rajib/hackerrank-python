def merge_the_tools(string, k):
    length = len(string)//k
    lst = [string[i:i+k] for i in range(0, len(string), k)]
    print(lst)

    for val in lst:
        l = []
        for i in range(len(val)):
            if val[i] not in l:
                l.append(val[i])
        
        res = ''.join(l)
        print(res)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    