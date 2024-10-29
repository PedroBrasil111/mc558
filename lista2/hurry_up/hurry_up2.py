class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]
        self.pesos = [[0] * n for _ in range(n)]

def add_aresta(g, u, v, peso):
    g.adj[u].append(v)
    g.pesos[u][v] = peso

def prim(g, u):
    pai = {}
    dist = [float('inf')] * len(g.adj)
    dist[u] = 0
    fila = [u]
    while fila:
        w = fila.pop(0)
        for v in g.adj[w]:
            if g.pesos[w][v] < dist[v]:
                pai[v] = w
                dist[v] = g.pesos[w][v]
                fila.append(v)
    return pai

def processar_equipe(n, m):
    # Inicializacao
    # vertice 0: raiz R, vertices 1 a n: jogadores, vertices n+1 a n+m: chegadas
    g = Grafo(n + m + 1)
    R = 0
    jogadores = []
    for i in range(1, n+1):
        add_aresta(g, R, i, 0)

    # Leitura dos jogadores
    for _ in range(n):
        l = input().split()
        # x, y, s
        jogadores.append((int(l[0]), int(l[1]), float(l[2])))

    # Leitura das chegadas
    for j in range(m):
        chegada = input().split()
        x, y = [int(x) for x in chegada[:2]]
        cores = [int(x) for x in chegada[2:-1]]
        for cor in cores:
            i = cor - 1
            dist = ((jogadores[i][0] - x)**2 + (jogadores[i][1] - y)**2)**(1/2)
            add_aresta(g, i+1, n+j+1, dist/jogadores[i][2])
    
    # pai define uma AGM enraizada em R
    pai = prim(g, R)
    #pai = prim(g, R)

    # Calculo do tempo
    tempo = {}
    for i in range(1, n+1):
        tempo[i] = float('inf')
    for j in range(n+1, n+m+1):
        if pai.get(j) and g.pesos[pai[j]][j] < tempo[pai[j]]:
            tempo[pai[j]] = g.pesos[pai[j]][j]
    soma = 0
    for _, t in tempo.items():
        soma += t
    print(f'{soma:.1f}')

def main():
    n, m = map(int, input().split())
    # while n != 0 and m != 0
    while n + m != 0:
        processar_equipe(n, m)
        n, m = map(int, input().split())

if __name__ == '__main__':
    main()