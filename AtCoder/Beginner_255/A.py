row, col = input().split(' ')

matrix = [ [ 0 for _ in range(2) ] for _ in range(2) ]

for i in range(2):
    values = input().split(' ')
    matrix[i][0] = values[0]
    matrix[i][1] = values[1]

print(matrix[int(row)-1][int(col)-1])