class Aresta():
    def __init__(self, u, v, peso=0, capacidade=1):
        self.u = u
        self.v = v
        self.peso = peso
        self.capacidade = capacidade
        self.fluxo = 0
        self.reversa = None
    def __str__(self):
        return f'[ {self.u} -> {self.v}, peso: {self.peso}, fluxo: {self.fluxo}]'
    def __repr__(self):
        return str(self)

class Grafo():
    # n: numero de vertices
    def __init__(self, n=0):
        self.adj = [[] for _ in range(n)]

    def add_aresta_dirigida(self, u, v, peso):
        self.adj[u].append(Aresta(u, v, peso, 1))

    def print_arestas(self):
        for u in range(len(self.adj)):
            for a in self.adj[u]:
                print(a)

    def relax(self, a: Aresta, dist, pai):
        if dist[a.u] + a.peso < dist[a.v]:
            dist[a.v] = dist[a.u] + a.peso
            pai[a.v] = a
            return True
        return False

    def initialize_single_source(self, s):
        dist = [float('inf')]*len(self.adj)
        dist[s] = 0
        pai = {}
        return dist, pai
    
    def bellman_ford(self, s):
        dist, pai = self.initialize_single_source(s)
        for _ in range(len(self.adj) - 1):
            alterou = False
            for u in range(len(self.adj)):
                    for a in self.adj[u]:
                        if a.capacidade - a.fluxo > 0:
                            alterou = alterou or self.relax(a, dist, pai)
            if not alterou:
                break
        return dist, pai

    def edmonds_karp(self, s, t):
        fluxo = 0
        tem_caminho = True
        adj_reversas = [[]] * len(self.adj)
        for u in range(len(self.adj)):
            # cria arestas reversas
            for a in self.adj[u]:
                a.reversa = Aresta(a.v, u, -a.peso, 1)
                a.reversa.reversa = a
                adj_reversas[a.v].append(a.reversa)
        for u in range(len(self.adj)):
            self.adj[u] += adj_reversas[u]
        while tem_caminho:
            dist, aresta_pai = self.bellman_ford(s)
            arestas = []
            menor_capacidade = float('inf')
            v = t
            while v != s:
                a = aresta_pai.get(v)
                if not a:
                    tem_caminho = False
                    break
                arestas.append(a)
                menor_capacidade = min(menor_capacidade, a.capacidade - a.fluxo)
                v = a.u
            if tem_caminho:
                for a in arestas:
                    a.fluxo += menor_capacidade
                    a.reversa.fluxo = a.capacidade - a.fluxo
                    v = a.u
                fluxo += menor_capacidade
            print('Fluxo:', fluxo, 'Arestas:', arestas)
        total = 0
        for u in range(len(self.adj)):
            for a in self.adj[u]:
                if a.fluxo > 0:
                    total += a.peso
        print('Pai:', aresta_pai)
        print('Total:', total)
        print()
        return fluxo

def processar_equipe(n, m):
    # Inicializacao
    # vertices 1 a n: jogadores, vertices n+1 a n+m: chegadas
    g = Grafo(n + m + 2)
    S, T = 0, n + m + 1
    jogadores = []
    # Arestas fonte -> jogadores, chegadas -> sorvedouro
    for i in range(1, n+1):
        g.add_aresta_dirigida(S, i, 0)
    for i in range(n+1, n+m+1):
        g.add_aresta_dirigida(i, T, 0)
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
        # Arestas jogadores -> chegadas
        for cor in cores:
            i = cor - 1
            dist = ((jogadores[i][0] - x)**2 + (jogadores[i][1] - y)**2)**(1/2)
            g.add_aresta_dirigida(i+1, n+j+1, dist/jogadores[i][2])
    fluxo = g.edmonds_karp(S, T)

def caso_teste():   
    n, m = 2, 2
    g = Grafo(n + m + 2)
    S, T = 0, n + m + 1
    jogadores = []
    # Arestas fonte -> jogadores, chegadas -> sorvedouro
    for i in range(1, n+1):
        g.add_aresta_dirigida(S, i, 0)
    for i in range(n+1, n+m+1):
        g.add_aresta_dirigida(i, T, 0)
    # Leitura das chegadas
    arestas = [(1, 3, 1), (1, 4, 4), (2, 3, 1.4), (2, 4, 4.2)]
    for a in arestas:
        g.add_aresta_dirigida(a[0], a[1], a[2])
    fluxo = g.edmonds_karp(S, T)

def main():
    n, m = map(int, input().split())
    while n != 0 and m != 0:
        processar_equipe(n, m)
        n, m = map(int, input().split())
    caso_teste()

if __name__ == '__main__':
    main()