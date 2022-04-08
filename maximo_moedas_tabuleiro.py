def maximoMoedas(tabuleiro, l, c):

	r = [0] * c

	for i in range(l):
		m = -1
		for j in range(c):
			if j > 0 and i > 0:
				m = max(m, tabuleiro[i][j] + r[j-1], tabuleiro[i][j] + r[j])
			elif i > 0:
				m = max(m, tabuleiro[i][j] + r[j])
			elif j > 0:
				m = max(m, tabuleiro[i][j] + r[j-1])
			else:
				m = max(m, tabuleiro[i][j])
			r[j] = m

	return r[j]


l = int(input())
c = int(input())
tabuleiro = []
#tabuleiro = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[0,0,1,0],[0,1,0,0]]

for i in range(l):
	tabuleiro.append([])
	for j in range(c):
		x = int(input())
		tabuleiro[i].append(x)

for i in range(len(tabuleiro)):
	print(tabuleiro[i])
print('Máximo de moedas:', maximoMoedas(tabuleiro, l, c))
