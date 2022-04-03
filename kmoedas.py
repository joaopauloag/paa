def kMoedas(moedas, v, k):
	
	n = len(moedas)
	r = [0] * (k+1)

	for i in range(1, k+1):
		maximo = 0
		for j in range(n):
			if r[i-1] + moedas[j] <= v and moedas[j] > maximo:
				maximo = moedas[j]
		r[i] = r[i-1] + maximo

	return r[i] == v


moedas = [5, 25, 10]
v = 90
k = 5
print(kMoedas(moedas, v, k))
