m = int(input())
n = int(input())

matrix = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = i*j
    print()

for k in range(m):
    for z in range(n):
        print(matrix[k][z], end=' ')
    print()
