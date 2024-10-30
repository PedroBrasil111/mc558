#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Grafo {
private:
    vector<vector<pair<int, long int>>> adj;

public:
    Grafo(int n = 0) {
        adj.resize(n);
    }

    void add_aresta(int u, int v, long int peso) {
        adj[u].emplace_back(v, peso);
    }

    int find(vector<int>& pai, int i) {
        if (pai[i] != i) {
            pai[i] = find(pai, pai[i]);
        }
        return pai[i];
    }

    void union_sets(vector<int>& pai, vector<int>& rank, int x, int y) {
        if (rank[x] < rank[y]) {
            pai[x] = y;
        } else if (rank[x] > rank[y]) {
            pai[y] = x;
        } else {
            pai[y] = x;
            rank[x]++;
        }
    }

    pair<int, long int> kruskal() {
        vector<int> pai(adj.size());
        vector<int> rank(adj.size(), 0);
        vector<tuple<long int, int, int>> arestas;

        for (int i = 0; i < adj.size(); ++i) {
            pai[i] = i;
            for (auto& [v, peso] : adj[i]) {
                arestas.emplace_back(peso, i, v);
            }
        }
        sort(arestas.begin(), arestas.end());

        long int pesos = 0;
        for (auto& [peso, u, v] : arestas) {
            int x = find(pai, u);
            int y = find(pai, v);
            if (x != y) {
                pesos += peso;
                union_sets(pai, rank, x, y);
            }
        }

        int componentes = 0;
        for (int i = 0; i < pai.size(); ++i) {
            if (pai[i] == i) {
                componentes++;
            }
        }
        return {componentes, pesos};
    }
};

int main() {
    int n, v, k;
    long int peso;
    cin >> n;
    Grafo g(n);
    for (int i = 0; i < n - 1; ++i) {
        cin >> k;
        for (int j = 0; j < k; ++j) {
            cin >> v >> peso;
            g.add_aresta(i, v - 1, peso);
            g.add_aresta(v - 1, i, peso);
        }
    }
    auto [componentes, pesos] = g.kruskal();
    cout << componentes << " " << pesos << endl;
    return 0;
}
