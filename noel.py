# O(dist(u,v))
def calcula_presentes(pai, dist, presentes, u, v):
    contados = {}
    total = 0
    while u != v:
        if dist[u] >= dist[v]:
            presente = presentes[u]
            u = pai[u]
        else:
            presente = presentes[v]
            v = pai[v]
        if presente not in contados:
            total += 1
            contados[presente] = True
    if presentes[u] not in contados:
        return total + 1
    return total

# O(V+E) = O(V)
def bfs(adj, u):
    dist = [-1] * len(adj)
    dist[u] = 0
    pai = [-1] * len(adj)
    fila = [u]
    while fila:
        w = fila.pop(0)
        for v in adj[w]:
            if v != u and pai[v] == -1:
                pai[v] = w
                dist[v] = dist[w] + 1
                fila.append(v)
    return pai, dist

n, m = [int(x) for x in input().split()]
presentes = input().split()
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = [int(x) - 1 for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)
pai, dist = bfs(adj, 0)
for _ in range(m):
    u, v = [int(x) - 1 for x in input().split()]
    print(calcula_presentes(pai, dist, presentes, u, v))
