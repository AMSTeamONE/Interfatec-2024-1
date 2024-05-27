# PROBLEMA G
from collections import defaultdict
qtd_max_vagas = int(input())
cadastros = []
while True:
    entrada = input().split()
    # print(entrada)
    if entrada == []:
        break
    cadastros.append((entrada[0], list(map(int, entrada[1:]))))

categories = [
    "Algoritmos", "Boas praticas", "Desempenho", "Fluxogramas", "Interpretacao de enunciados", "Sintaxe da linguagem"
]


ficou_fora = cadastros[qtd_max_vagas:]
matriculados = cadastros[:qtd_max_vagas]

numsei = defaultdict(list)
for m in matriculados:
    for cat in m[1]:
        numsei[cat - 1].append(m[0])


line = "-" * 30

print(numsei)

for i, cat in enumerate(categories):
    print(line)
    print(cat.upper())
    print(line)
    for name in sorted(numsei[i]):
        print(name)
    print()
    # print(categories[int(cat_index) - 1].upper())

# for cat_index, names in numsei.items():
#     print(line)
#     for name in sorted(names):
#         print(name)

if len(ficou_fora) > 0:
    print(line)
    print("FICA PARA A PROXIMA!")
    print(line)
    for out in ficou_fora:
        print(out[0])
