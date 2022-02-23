m, n = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for i in range(m)]
matrix_list = []
for row in matrix:
    matrix_list.extend(row)
matrix_list.sort()
for i in range(m):
    print(*matrix_list[:n])
    matrix_list = matrix_list[n:]