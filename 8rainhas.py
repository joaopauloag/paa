n = 8
solucao = [0] * n

def rainhas(pos):
	if pos == n:
		print(solucao)
	l = 0
	while l < n:
		for i in range(pos+1):
			if solucao[i] == l or (abs(l - solucao[i]) == abs(i - pos)):
				break
		if i == pos:
			solucao[pos] = l
			rainhas(pos+1)
		l += 1

rainhas(0)
