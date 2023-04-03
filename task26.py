def raise_to_degree(a, b):
    if b == 0:
        return 1
    return a * raise_to_degree(a, b - 1)

N = int(input('Enter number: '))
M = int(input('Enter a degree: '))
print(raise_to_degree(N, M))