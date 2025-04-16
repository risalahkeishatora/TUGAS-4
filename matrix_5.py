A = [
    [3, 7, 1, 4, 9],
    [2, 5, 6, 8, 1],
    [9, 3, 2, 7, 6],
    [4, 8, 5, 1, 0],
    [6, 2, 3, 9, 7]
]

B = [
    [1, 6, 4, 3, 7],
    [5, 2, 0, 8, 1],
    [9, 3, 6, 2, 4],
    [0, 1, 5, 7, 3],
    [8, 4, 2, 6, 9]
]

result = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(5):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)

print("Matriks A", A)
print("Matriks B", B)
print("Hasil A x B", result)