n = int(input())

matrix = []

for row in range(n):
    matrix.append([])
    for col in range(n):
        matrix[row].append(col + 1 + row * n)

sums = []
for row in matrix:
    row_sum = sum(row)
    sums.append(row_sum)

for i in range(n):
    print(sums[i])