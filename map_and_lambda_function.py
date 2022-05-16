# Solution: 01
cube = lambda x: x**3

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Solution: 02
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print(list(map(lambda x: x**3, fib[:int(input())])))
