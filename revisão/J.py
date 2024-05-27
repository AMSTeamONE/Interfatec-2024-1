# PROBLEMA J
qtd = int(input())
# qtd = 2
names = [input() for _ in range(qtd)]
# names = ["LILO", "STICH"]
points = [0 for _ in range(qtd)]
qtd_rodadas = int(input())
# qtd_rodadas = 3
rodadas = [
    (
        sum(map(int, input().split())), # total de palitos
        list(map(int, input().split())) # palpite de cada um
    )
    for _ in range(qtd_rodadas)
]
# rodadas = [[2, [3, 2]], [1, [4, 1]], [3, [3, 1]]]

def winner_rodada(rodada):
    # proximidade = [abs(rodada[0] - rodada[1][i]) for i in range(qtd)]
    for i in range(qtd):
        if rodada[0] - rodada[1][i] == 0:
            points[i] += 1
    # print(proximidade)

for rodada in rodadas:
    winner_rodada(rodada)

if len([p for p in points if p == max(points)]) > 1:
    print("EMPATE")
else:
    print(names[points.index(max(points))], "GANHOU")