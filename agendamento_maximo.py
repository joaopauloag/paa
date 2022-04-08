#a = [(1, s1, f1), ..., (n, sn, fn)]

def fi(e):
    return e[2]

def agendamentoMaximo(a):
	#Ordena a lista de atividades segundo fi.
    a.sort(key=fi)
    n = len(a)
    agendamento = [a[0][0]]
    k = 0
    for i in range(1, n):
        '''Verifica se a próxima atividade não se
        sobrepõe a última adicionada ao agendamento.'''
        if a[i][1] >= a[k][2]:
            agendamento.append(a[i][0])
            k = i
    return agendamento

a = [(1,12,16),(2,3,5),(3,0,6),(4,8,12),
    (5,5,7),(6,3,9),(7,5,9),(8,1,4),
    (9,8,11),(10,2,14),(11,6,10)]

print('Agendamento:', agendamentoMaximo(a))
