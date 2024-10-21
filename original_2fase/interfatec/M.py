import itertools as it

verba = int(input())
qtd = int(input())

# id, custo, população
locais = [tuple(map(int, input().split())) for _ in range(qtd)]

plans = []

# todas as organizações de locais
for groups in it.permutations(locais):
    # ver o limite de verba para cada ordenação
    for i in range(qtd):
        if sum(g[1] for g in groups[:i]) > verba:
            plans.append(groups[:i-1])
            break

plans = [groups[:i-1] for groups in it.permutations(locais) for i in range(qtd) if sum(g[1] for g in groups[:i]) <= verba]

top = sorted(plans, key=lambda p: sum(g[2] for g in p))[-1]
print(sum(l[2] for l in top))