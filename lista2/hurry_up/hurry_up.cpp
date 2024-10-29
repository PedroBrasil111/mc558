#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <limits>
#include <map>
#include <tuple>
#include <iomanip> 

using namespace std;

class Grafo {
public:
    vector<vector<int>> adj;
    vector<vector<double>> pesos;

    Grafo(int n = 0) {
        adj.resize(n);
        pesos.resize(n, vector<double>(n, 0));
    }
};

void add_aresta(Grafo &g, int u, int v, double peso) {
    g.adj[u].push_back(v);
    g.pesos[u][v] = peso;
}

map<int, int> prim(Grafo &g, int raiz) {
    int n = g.adj.size();
    vector<double> dist(n, numeric_limits<double>::infinity());
    vector<bool> inMST(n, false);
    map<int, int> pai;
    dist[raiz] = 0;

    // Min-heap para escolher a aresta de menor custo
    priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> minHeap;
    minHeap.push({0, raiz});

    while (!minHeap.empty()) {
        int u = minHeap.top().second;
        minHeap.pop();

        // Ignora se já está na MST
        if (inMST[u]) continue;
        inMST[u] = true;

        // Atualiza distâncias dos vizinhos
        for (int v : g.adj[u]) {
            double peso = g.pesos[u][v];
            if (!inMST[v] && peso < dist[v]) {
                dist[v] = peso;
                pai[v] = u;
                minHeap.push({peso, v});
            }
        }
    }
    return pai;
}

void processar_equipe(int n, int m) {
    Grafo g(n + m + 1);
    int R = 0;
    vector<tuple<int, int, double>> jogadores;

    for (int i = 1; i <= n; ++i) {
        add_aresta(g, R, i, 0);
    }

    for (int i = 0; i < n; ++i) {
        int x, y;
        double s;
        cin >> x >> y >> s;
        jogadores.push_back({x, y, s});
    }

    for (int j = 0; j < m; ++j) {
        int x, y;
        cin >> x >> y;
        vector<int> cores;
        int cor;

        while (cin.peek() != '\n' && cin >> cor) {
            cores.push_back(cor);
        }

        for (int cor : cores) {
            int i = cor - 1;
            double dist = sqrt(pow(get<0>(jogadores[i]) - x, 2) + pow(get<1>(jogadores[i]) - y, 2));
            add_aresta(g, i + 1, n + j + 1, dist / get<2>(jogadores[i]));
        }
    }

    map<int, int> pai = prim(g, R);
    map<int, double> tempo;

    for (int i = 1; i <= n; ++i) {
        tempo[i] = numeric_limits<double>::infinity();
    }

    for (int j = n + 1; j <= n + m; ++j) {
        if (pai.find(j) != pai.end() && g.pesos[pai[j]][j] < tempo[pai[j]]) {
            tempo[pai[j]] = g.pesos[pai[j]][j];
        }
    }

    double soma = 0;
    for (const auto &t : tempo) {
        soma += t.second;
    }
    cout << fixed << setprecision(1) << soma << endl;
}

int main() {
    int n, m;
    cin >> n >> m;

    while (n != 0 || m != 0) {
        processar_equipe(n, m);
        cin >> n >> m;
    }

    return 0;
}
