class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]
        self.pesos = [[0] * n for _ in range(n)]

    def add_aresta(self, u, v, peso):
        self.adj[u].append(v)
        self.pesos[u][v] = peso

    def find(self, pai, i):
        if pai[i] != i:
            pai[i] = self.find(pai, pai[i])
        return pai[i]

    def union(self, pai, rank, x, y):
        if rank[x] < rank[y]:
            pai[x] = y
        elif rank[x] > rank[y]:
            pai[y] = x
        else:
            pai[y] = x
            rank[x] += 1

    def kruskal(self):
        pai = []
        rank = []
        for i in range(len(self.adj)):
            pai.append(i)
            rank.append(0)

        arestas = []
        for u in range(len(self.adj)):
            for v in self.adj[u]:
                arestas.append((u, v, self.pesos[u][v]))
        arestas.sort(key=lambda x: x[2])

        pesos = 0
        for u, v, peso in arestas:
            x = self.find(pai, u)
            y = self.find(pai, v)
            if x != y:
                pesos += peso
                self.union(pai, rank, x, y)

        componentes = 0
        for i in range(len(pai)):
            if pai[i] == i:
                componentes += 1
        return componentes, pesos

def main():
    n = int(input())
    g = Grafo(n)
    for i in range(n - 1):
        entrada = [int(x) for x in input().split()]
        for j in range(1, len(entrada), 2):
            g.add_aresta(i, entrada[j] - 1, entrada[j + 1])
            g.add_aresta(entrada[j] - 1, i, entrada[j + 1])
    componentes, pesos = g.kruskal()
    print(componentes, pesos)

if __name__ == '__main__':
    main()