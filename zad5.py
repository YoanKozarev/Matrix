N = int(input())
matrix = []

for _ in range(N):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

secondary_diagonal_sum = sum(matrix[а][N - а - 1] for а in range(N))

print(secondary_diagonal_sum)
