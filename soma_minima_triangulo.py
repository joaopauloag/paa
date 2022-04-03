def somaMinima(triangulo):

    n = len(triangulo)
    r = [None] * n

    for i in range(n):
        r[i] = triangulo[n-1][i]

    for i in range(n - 2, -1, -1):
        m = len(triangulo[i])
        for j in range(m):
            r[j] = triangulo[i][j] + min(r[j], r[j+1])
    
    return r[0]

triangulo = [[2], [15, 4], [3, 4, 17], [1, 6, 9, 6]]

print(somaMinima(triangulo))
