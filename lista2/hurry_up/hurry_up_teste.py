
def processamento():
    N, M = map(int, input().split())

    jogadores = {}
    for i in range(N):
        jogador = input().split()
        x, y = [int(x) for x in jogador[:2]]
        s = float(jogador[2])
        jogadores[i+1] = (x, y, s)
        if x + y == 0:
            return False

    chegadas = []
    for i in range(M):
        chegada = input().split()
        x, y = [int(x) for x in chegada[:2]]
        cores = [int(x) for x in chegada[2:]]
        chegadas.append((x, y, cores))
        
    dists = []
    for i in range(N):
        x, y, s = jogadores[i+1]
        

    return True

def main():
    while processamento():
        pass

if __name__ == '__main__':
    main()