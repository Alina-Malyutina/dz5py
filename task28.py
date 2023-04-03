def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

N = int(input('Enter first number: '))
M = int(input('Enter second number: '))
print(sum(N, M))