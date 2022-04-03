from time import *

def printTabuleiro():
	print('\nSolução:\n')
	for i in range(n):
		for j in range(n):
			print('%2d' % tabuleiro[i][j], end = '  ')
		print()

def eValido(x, y):
	return 0 <= x < n and 0 <= y < n
		
def passeioDoCavalo(x, y, k):
	tabuleiro[x][y] = k

	if k == n**2:
		printTabuleiro()
		print('\nTempo de execução:', time() - t)
		exit()

	for l in range(8):
		prox_x = x + movX[l]
		prox_y = y + movY[l]
		if eValido(prox_x, prox_y) and tabuleiro[prox_x][prox_y] == -1:
			passeioDoCavalo(prox_x, prox_y, k+1)
			tabuleiro[prox_x][prox_y] = -1

n = 8
movX = [-2, -1, 1, 2, 2, 1, -1, -2]
movY = [1, 2, 2, 1, -1, -2, -2, -1]
tabuleiro = [[-1] * n for i in range(n)]
t = time()
passeioDoCavalo(0, 0, 1)

