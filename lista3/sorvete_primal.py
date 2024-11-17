from pulp import GUROBI, LpProblem, LpVariable, LpMinimize, lpSum, value

def criar_restricao(vars, coef, nome=None, tipo=None, valor=None):
    if tipo == '==':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) == valor
    elif tipo == '<=':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) <= valor
    elif tipo == '>=':
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]) >= valor
    # s/ restricao (objetivo)
    else:
        return lpSum([coef[i]*vars[i] for i in range(len(vars))]), nome

def sorvete(quantidades: dict, recursos: dict):
    # lowBound omite restricoes do tipo x >= <valor>
    x_c = LpVariable("x_c", lowBound=quantidades['demanda'][0])
    x_b = LpVariable("x_b", lowBound=quantidades['demanda'][1])
    x_m = LpVariable("x_m", lowBound=quantidades['demanda'][2])
    vars = [x_c, x_b, x_m]
    problema = LpProblem("Sorvete", LpMinimize)
    # objetivo (negativo para inverter a maximizacao)
    problema += criar_restricao(vars, [-q for q in quantidades['lucro']], 'objetivo')
    # restricoes (negativo para inverter a direcao)
    for rec in recursos:
        problema += criar_restricao(vars, [-q for q in quantidades[rec]], tipo='>=', valor=-recursos[rec])
    problema.solve(GUROBI(msg=0))
    print('Valor otimo:', value(problema.objective))
    print('Solucao otima:')
    for variavel in problema.variables():
        print(f'\t{variavel.name} = {variavel.varValue}')

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