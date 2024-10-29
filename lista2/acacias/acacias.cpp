#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

class Grafo {
private:
    vector<tuple<int, int, int>> arestas; // Armazena (peso, u, v)

public:
    void add_aresta(int u, int v, int peso) {
        arestas.emplace_back(peso, u, v);
    }

    int find(vector<int>& pai, int i) {
        if (pai[i] != i)
            pai[i] = find(pai, pai[i]);
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

    pair<int, int> kruskal(int n) {
        vector<int> pai(n);
        vector<int> rank(n);
        for (int i = 0; i < n; i++) {
            pai[i] = i;
            rank[i] = 0;
        }

        sort(arestas.begin(), arestas.end(), [](const auto& a, const auto& b) {
            return get<0>(a) < get<0>(b);
        });

        long int total_pesos = 0;
        for (const auto& [peso, u, v] : arestas) {
            int x = find(pai, u);
            int y = find(pai, v);
            if (x != y) {
                total_pesos += peso;
                union_sets(pai, rank, x, y);
            }
        }

        int componentes = 0;
        for (int i = 0; i < pai.size(); i++) {
            if (pai[i] == i) {
                componentes++;
            }
        }
        return {componentes, total_pesos};
    }
};

int main() {
    int n;
    cin >> n;
    Grafo g;
    for (int i = 0; i < n - 1; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int x, peso;
            cin >> x >> peso;
            g.add_aresta(i, x - 1, peso);
        }
    }
    auto [componentes, pesos] = g.kruskal(n);
    cout << componentes << " " << pesos << endl;

    return 0;
}
