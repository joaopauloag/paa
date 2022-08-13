def elementoMajoritario(elementos):
	
	n = len(elementos)
	if n == 1:
		return elementos[0]

	maj = []

	for i in range(n-1):
		if elementos[i] == elementos[i+1]:
			maj.append(elementos[i])

	return elementoMajoritario(maj) if len(maj) > 0 else None


A = [7, 4, 'joao', 4, 4, 4, 'oi', 7.6, 4, 'z', 4, 5.7, 4, 4, 4, 10, 4, 9]
print('Elemento Majoritário:', elementoMajoritario(A))
B = [4, 5, 6, 10, 20, 7, 30]
print('Elemento Majoritário:', elementoMajoritario(B))
C = [4, 5, 4, 6, 4, 7]
print('Elemento Majoritário:', elementoMajoritario(C))
D = [2, 'a', 'a', 5, 'a']
print('Elemento Majoritário:', elementoMajoritario(D))
