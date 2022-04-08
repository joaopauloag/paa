# pessoas = [p1, p2, ..., pn]
# pares = [(pi,pj), ..., (pi,pj)]

def escolherConvidados(pessoas, pares):
    convidados = []
    n = len(pessoas)
    for pessoa in pessoas:
        cnt = 0
        for par in pares:
            if pessoa in par:
                cnt += 1
        if cnt >= 5 and (n-1-cnt) >= 5:
            convidados.append(pessoa)
    return convidados

pessoas = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
pares = [
    ('a','b'),('a','d'),('a','e'),('a','f'),('a','m'),
    ('b','d'),('b','e'),('b','f'),('c','e'),('c','h'),
    ('d','e'),('d','k'),('d','h'),('e','f'),('e','h'),
    ('f','h'),('f','i'),('g','i'),('h','i'),('h','j'),
    ('h','l'),('i','j'),('i','k'),('i','m'),('j','k'),
    ('j','l'),('j','m'),('k','l'),('k','m'),('l','m')
    ]

print(escolherConvidados(pessoas, pares))
