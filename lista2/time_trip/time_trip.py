class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]

    def add_aresta(self, u, v, peso):
        self.adj[u].append((v, peso))

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

    def teste(self):
        pai = []
        rank = []
        for i in range(len(self.adj)):
            pai.append(i)
            rank.append(0)

        arestas = []
        for u in range(len(self.adj)):
            for v, peso in self.adj[u]:
                arestas.append((peso, u, v))
        arestas.sort(key=lambda x: x[0])

    def dfs(self):
        visitados = [False]*len(self.adj)
        tempo = 0
        for i in range(len(self.adj)):
            if not visitados[i]:
                self.dfs_visit(i, visitados, tempo)

    def dfs_visit(self, u, visitados):
        visitados[u] = True
        for v, _ in self.adj[u]:
            if not visitados[v]:
                self.dfs_visit(v, visitados)
    
    def 



def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        g = Grafo(n)
        peso_total = 0
        for _ in range(m):
            entrada = [int(x) for x in input().split()]
            g.add_aresta(entrada[0] - 1, entrada[1] - 1, -entrada[2])
            g.add_aresta(entrada[1] - 1, entrada[0] - 1, -entrada[2])
            peso_total += 2*entrada[2]
        pai = g.kruskal()
        min_peso = float('inf')

if __name__ == '__main__':
    main()