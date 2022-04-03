def elementoMajoritario(A, inicio, fim):
	
	if inicio == fim:
		return A[inicio]

	meio = (inicio + fim) // 2
	esquerda = elementoMajoritario(A, inicio, meio)
	direita = elementoMajoritario(A, meio+1, fim)

	if esquerda == direita:
		return esquerda

	cnt_esquerda = cnt_direita = 0
	n = len(A)

	for a in A:
		if a == esquerda:
			cnt_esquerda += 1
		if a == direita:
			cnt_direita += 1

	if cnt_esquerda > meio + 1:
		return esquerda
	elif cnt_direita > meio + 1:
		return direita
	else:
		return None

A = [7, 4, 'joao', 4, 4, 4, 7, 4, 'oi', 7.6, 4, 'z', 4, 5.7, 4, 4, 4, 10, 4, 9]
print('Elemento Majoritário:', elementoMajoritario(A, 0, len(A)-1))
