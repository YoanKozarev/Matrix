N = int(input())
matrix = []

for _ in range(N):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

diagonal = sum(matrix[a][a] for a in range(N))

print(diagonal)
