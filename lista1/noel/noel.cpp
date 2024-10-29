#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

/*
    Calcula quantos presentes unicos ha no caminho entre u e v,
    dada uma arvore geradora do grafo e as respectivas distancias ate a raiz.
    Parametros:
        pai: vetor de pais de cada vertice na arvore geradora
        dist: vetor de distancias entre cada vertice e a raiz
        presentes: vetor de presentes de cada vertice
        u: vertice u
        v: vertice v
    Retorno:
        Quantidade de presentes unicos no caminho entre u e v
*/
int calcula_presentes(const vector<int>& pai,
                      const vector<int>& dist,
                      const vector<string>& presentes,
                      int u, int v) {
    // contados = conjunto (hash table) de presentes ja vistos no caminho
    // custos amortizados esperados: insercao e busca em O(1)
    unordered_set<string> contados;
    int total = 0; // total de presentes unicos
    string presente;
    // enquanto o pai em comum nao for alcancado
    while (u != v) {
        // escolhe o vertice mais distante da raiz e substitui por seu pai
        if (dist[u] >= dist[v]) {
            presente = presentes[u];
            u = pai[u];
        } else {
            presente = presentes[v];
            v = pai[v];
        }
        // se o presente nao foi contado, adiciona ao conjunto
        if (contados.find(presente) == contados.end()) {
            total += 1;
            contados.insert(presente);
        }
    }
    // verifica se o presente do vertice final nao foi contado
    if (contados.find(presentes[u]) == contados.end())
        return total + 1;
    return total;
}

/*
    Realiza uma busca em largura a partir do vertice u.
    Parametros:
        adj: lista de adjacencia
        u: vertice de inicio
    Retorno:
        Par de vetores (pai, dist) onde:
            pai[v] = pai do vertice v na arvore gerada pela bfs
            dist[v] = dist(u, v) na arvore gerada pela bfs
*/
pair<vector<int>, vector<int>> bfs(const vector<vector<int>>& adj, int u) {
    int w;
    vector<int> dist(adj.size(), -1);
    vector<int> pai(adj.size(), -1);
    queue<int> fila; // fila Q
    dist[u] = 0;
    fila.push(u); // enqueue(Q, u)
    while (!fila.empty()) {
        w = fila.front(); // w = dequeue(Q)
        fila.pop();
        // para cada vertice v adjacente a w
        for (int v : adj[w]) {
            // se v nao eh a raiz e ainda nao foi visitado
            if (v != u && pai[v] == -1) {
                // atualiza pai e distancia de v
                pai[v] = w;
                dist[v] = dist[w] + 1;
                fila.push(v); // enqueue(Q, v)
            }
        }
    }
    return {pai, dist};
}

/*
    Le um vertice do input e converte para 0-indexado.
    Retorno:
        Vertice lido
*/
int ler_vertice() {
    int v;
    cin >> v;     // vertices sao 1-indexados
    return v - 1; // converte para 0-indexado
}

int main() {
    int u, v;                    // vertices u e v (usados para leitura)
    int n, m;                    // numero de vertices e de consultas
    cin >> n >> m;               // leitura de n e m
    vector<string> presentes(n); // presente[i] = presente do vertice i
    vector<vector<int>> adj(n);  // lista de adjacencia
    // leitura dos presentes
    for (int i = 0; i < n; i++)
        cin >> presentes[i];
    // leitura das arestas
    for (int i = 0; i < n - 1; i++) {
        u = ler_vertice();
        v = ler_vertice();
        // adiciona aresta u-v
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    // bfs selecionando vertice arbitrario (0) como raiz
    // pai = vetor de pais de cada vertice na arvore
    // dist = vetor de distancias entre cada vertice e a raiz
    auto [pai, dist] = bfs(adj, 0);
    // leitura e processamento das consultas
    for (int i = 0; i < m; i++) {
        u = ler_vertice();
        v = ler_vertice();
        // impressao do resultado
        cout << calcula_presentes(pai, dist, presentes, u, v) << endl;
    }
    return 0;
}
