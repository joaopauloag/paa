def dfs(u, visitados):
    visitados[u] = True
    comprimento = 0
    for v in graph[u]:
        if not visitados[v]:
            comprimento = max(comprimento, 1 + dfs(v, visitados))
    return comprimento

def caminhoMaisLongo(graph):
    n = len(graph)
    caminhoMaisLongo = 0
    for i in range(n):
        caminhoMaisLongo = max(caminhoMaisLongo, dfs(i, [False] * n))
    return caminhoMaisLongo

graph = [
    [4],
    [0, 2],
    [1],
    [],
    [3, 5],
    [6],
    []
]

print('Caminho mais longo:', caminhoMaisLongo(graph))
