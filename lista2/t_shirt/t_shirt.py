class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]
        self.pesos = [[0] * n for _ in range(n)]

def bfs(g, u):
    pai = {}
    fila = [u]
    peso_min = float('inf')
    while fila:
        w = fila.pop(0)
        for v in g.adj[w]:
            if v != u and pai.get(v) == None:
                pai[v] = w
                fila.append(v)
                peso_min = min(peso_min, g.pesos[w][v])
    return pai, peso_min

def add_aresta(g, u, v, peso):
    g.adj[u].append(v)
    g.pesos[u][v] = peso

def somar_peso(g, u, v, peso):
    # aresta n existe
    if g.pesos[u][v] == 0:
        g.adj[u].append(v)
        g.pesos[u][v] = peso
    # aresta deve ser removida
    elif g.pesos[u][v] + peso == 0:
        g.adj[u].remove(v)
        g.pesos[u][v] = 0
    # so deve somar o peso
    else:
        g.pesos[u][v] += peso

def ford_fulkerson(g, s, t):
    fluxo = 0
    while True:
        pai, alpha = bfs(g, s)
        # nao ha caminho aumentador
        if pai.get(t) == None:
            break
        fluxo += alpha # alpha eh o menor peso do caminho aumentador
        v = t
        # atualiza arestas
        while v != s:
            u = pai[v]
            somar_peso(g, u, v, -alpha)
            somar_peso(g, v, u, alpha)
            v = u
    return fluxo

def existe_distribuicao():
    n, m = map(int, input().split())
    g = Grafo(m+8)

    # Criacao inicial da rede
    # s = 0, t = 1, XXL = 2, XL = 3, L = 4, M = 5, S = 6, XS = 7, pessoas = 8+
    S, T = 0, 1
    tam_idx = {'XXL': 2, 'XL': 3, 'L' : 4, 'M' : 5, 'S' : 6, 'XS': 7}
    for idx in tam_idx.values():
        # aresta indo de s ate a camiseta c/ peso n//6
        add_aresta(g, S, idx, n//6)

    # Leitura dos tamanhos
    for i in range(m):
        tamanhos = input().split() # tamanhos que pode vestir
        id_pes = i+8 # id da pessoa
        # aresta indo da pessoa ate t c/ peso 1
        add_aresta(g, id_pes, T, 1)
        # aresta indo da camiseta ate pessoa c/ peso 1
        for tam in tamanhos:
            add_aresta(g, tam_idx[tam], id_pes, 1)

    # Sucesso se fluxo for igual ao numero de pessoas
    return 'YES' if ford_fulkerson(g, S, T) == m else 'NO'

def main():
    for _ in range(int(input())):
        print(existe_distribuicao())

if __name__ == '__main__':
    main()