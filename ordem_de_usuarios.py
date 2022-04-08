#usuarios = [(1, t1), ..., (n, tn)]

def ti(e):
    return e[1]

def ordemDeUsuarios(usuarios):
    #Ordena a lista de usuarios segundo ti
    usuarios.sort(key=ti)
    ordem = []
    for u in usuarios:
        ordem.append(u[0])
    return ordem

u = [(1,12),(2,3),(3,6),(4,12),
    (5,7),(6,9),(7,5),(8,4),
	(9,7),(10,14),(11,10)]

print('Ordem dos usuários:', ordemDeUsuarios(u))
