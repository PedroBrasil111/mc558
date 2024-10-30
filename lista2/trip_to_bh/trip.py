class HeapMin:
    def __init__(self):
        self.v = []
        self.pos = {}
        self.tam = 0

    def pai(self, i):
        return (i - 1) // 2
    
    def filho_esq(self, i):
        return 2 * i + 1
    
    def filho_dir(self, i):
        return 2 * i + 2
    
    def troca(self, i, j):
        self.v[i], self.v[j] = self.v[j], self.v[i]
        self.pos[self.v[i][1]] = i
        self.pos[self.v[j][1]] = j

    def insere(self, u, peso):
        self.v.append((peso, u))
        self.pos[u] = self.tam
        self.tam += 1
        i = self.tam - 1
        while i > 0 and self.v[self.pai(i)][0] > self.v[i][0]:
            self.troca(i, self.pai(i))
            i = self.pai(i)

    def diminui_chave(self, u, peso):
        i = self.pos.get(u)
        if i is not None and self.v[i][0] > peso:
            self.v[i] = (peso, u)
            while i > 0 and self.v[self.pai(i)][0] > self.v[i][0]:
                self.troca(i, self.pai(i))
                i = self.pai(i)

    def extrai_min(self):
        if self.tam == 0:
            return None
        raiz = self.v[0][1]
        self.v[0] = self.v[self.tam - 1]
        self.pos[self.v[0][1]] = 0
        self.pos.pop(raiz)
        self.tam -= 1
        self.v.pop()
        if self.tam > 0:
            self.min_heapify(0)
        return raiz

    def min_heapify(self, i):
        esq = self.filho_esq(i)
        dir = self.filho_dir(i)
        menor = i
        if esq < self.tam and self.v[esq][0] < self.v[i][0]:
            menor = esq
        if dir < self.tam and self.v[dir][0] < self.v[menor][0]:
            menor = dir
        if menor != i:
            self.troca(i, menor)
            self.min_heapify(menor)
    
    def vazio(self):
        return self.tam == 0

class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]

    def add_aresta(self, u, v, tipo, peso):
        self.adj[u].append((v, tipo, peso))

    def relax(self, u, v, peso, dist):
        if dist[v] > dist[u] + peso:
            dist[v] = dist[u] + peso

    # O((V+E)logV)
    def dijkstra(self, s, tipo_busca):
        dist = [float('inf')] * len(self.adj)
        dist[s] = 0
        heap = HeapMin()
        for u in range(len(self.adj)):
            heap.insere(u, dist[u])
        while not heap.vazio():
            u = heap.extrai_min()
            for v, tipo, peso in self.adj[u]:
                if tipo == tipo_busca:
                    self.relax(u, v, peso, dist)
                    heap.diminui_chave(v, dist[v])
        return dist

def main():
    while True:
        try:
            n, m = [int(x) for x in input().split()]
            g = Grafo(n)
            for _ in range(m):
                entrada = [int(x) for x in input().split()]
                g.add_aresta(entrada[0] - 1, entrada[1] - 1, *entrada[2:])
            print(min(g.dijkstra(0, 0)[n - 1], g.dijkstra(0, 1)[n - 1]))
        except EOFError:
            break

if __name__ == '__main__':
    main()