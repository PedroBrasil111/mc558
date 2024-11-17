'''
1. Selecione um dos problemas desta lista e para ele entregue:

(a) Um programa linear explicando as variáveis, função objetivo e restrições.

(b) O programa dual do entregue no item anterior. Proponha uma interpretação para as variáveis
duais.

(c) Uma solução viável mas não ótima do primal e, usando folgas completares, mostre como
deduzir que tal solução não é ótima.

(d) Uma solução ótima do primal e, usando folgas complementares, mostre como provar a otima-
lidade.

(e) Nos dois itens anteriores, explique o passo a passo.

(f) Codifique o primal usando Python e pulp. Solucione-o.
'''

from pulp import *

def criar_restricao(vars, coef, nome=None, tipo=None, valor=None):
    if tipo == '==':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) == valor
    elif tipo == '<=':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) <= valor
    elif tipo == '>=':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) >= valor
    else:
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]), nome

def sorvete(quantidades: dict, recursos: dict):
    x_c = LpVariable("x_c", lowBound=quantidades['demanda'][0])
    x_b = LpVariable("x_b", lowBound=quantidades['demanda'][1])
    x_m = LpVariable("x_m", lowBound=quantidades['demanda'][2])
    vars = [x_c, x_b, x_m]

    problema = LpProblem("Sorvete", LpMinimize)

    problema += criar_restricao(vars, [-x for x in quantidades['lucro']], 'objetivo')

    for rec in recursos:
        problema += criar_restricao(vars,[-x for x in quantidades[rec]], tipo='>=', valor=-recursos[rec])

    print(problema)
    problema.solve(GUROBI(msg=0))   

    print('Valor otimo:', value(problema.objective))
    print('Solucao otima:')
    for variavel in problema.variables():
        print(f'  {variavel.name} = {variavel.varValue}')

def main():
    quantidades = {
        'leite': [0.5, 0.4, 0.45],
        'acucar': [0.1, 0.15, 0.12],
        'saborizante': [10, 8, 9],
        'lucro': [12, 10, 11],
        'demanda': [80, 60, 50],
    }
    recursos = {
        'leite': 500,
        'acucar': 80,
        'saborizante': 2000,
    }
    sorvete(quantidades, recursos)

if __name__ == '__main__':
    main()  