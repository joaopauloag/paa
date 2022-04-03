def somaMaxima(s):

	maximoAtual = temp = inicio = fim = 0
	maximoGlobal = -1
	n = len(s)

	for i in range(n):
		maximoAtual += s[i]
		if maximoAtual < 0:
			maximoAtual = 0
			temp = i+1
		if maximoAtual > maximoGlobal:
			maximoGlobal = maximoAtual
			inicio = temp
			fim = i
	return s[inicio:fim+1], maximoGlobal

v = [5, 15, -30, 10, -5, 40, 10, -50]

saida = somaMaxima(v)
print('Subsequência:', saida[0])
print('Soma:', saida[1])
