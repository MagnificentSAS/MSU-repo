def m_mul(m1, m2, i, j):
    res = 0
    for k in range(len(m1)):
        res += m1[j][k] * m2[k][i]
    return res

matrix1 = []
matrix2 = []
line = list(eval(input()))
matrix1.append(line)
l = len(line)
for i in range(1, l):
    line = list(eval(input()))
    matrix1.append(line)

for i in range(l):
    line = list(eval(input()))
    matrix2.append(line)

matrix_res = [[m_mul(matrix1, matrix2, i, j) for i in range(l)] for j in range(l)]

for l in matrix_res:
    print(*l, sep = ',')
