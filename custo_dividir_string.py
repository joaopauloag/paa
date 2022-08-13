import math

def custoDividirString(n, cortes):

	if len(cortes) == 0: 
		return 0

	custoMinimo = math.inf

	for c in cortes:
		cortesEsquerda = [i for i in cortes if i < c]
		# Assume c como posição inicial da string cortada
		cortesDireita = [i-c for i in cortes if i > c]

		custoEsquerda = custoDividirString(c, cortesEsquerda)
		custoDireita = custoDividirString(n-c, cortesDireita)

		# Soma o custo do corte atual aos demais
		custo = n + custoEsquerda + custoDireita

		if custo < custoMinimo:
			custoMinimo = custo

	return custoMinimo

print ('Custo mínimo:', custoDividirString(20, [3,10,16]))
print ('Custo mínimo:', custoDividirString(20, [3,10]))
print ('Custo mínimo:', custoDividirString(5, [1,2,3,4]))
print ('Custo mínimo:', custoDividirString(1, [1]))
