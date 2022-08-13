import numpy as np

def maiorSubstringComum(X, Y):

	n = len(X)
	m = len(Y)

	substring = np.zeros((n+1, m+1), dtype='int')

	for i in range(1, n+1):
		for j in range(1, m+1):
			if X[i-1] == Y[j-1]:
				substring[i][j] = substring[i-1][j-1] + 1

	return substring.max()

X = 'vou passar em calculo 4 diferencial'
Y = 'talvez eu passe em calculo diferencial'

print(maiorSubstringComum(X, Y))
