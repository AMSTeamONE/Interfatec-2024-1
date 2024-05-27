# PROBLEMA E

qtd_perfis = int(input())
if 0 >= qtd_perfis > 15:
    exit()

# qtd_perfis = 4
qtd_por_perfil = list(map(int, input().split()))
if any(q > 30 for q in qtd_por_perfil):
    exit()


# qtd_por_perfil = [2, 1, 3, 1]
qtd_regions = int(input())
if 0 >= qtd_regions > 50:
    exit()

# qtd_regions = 3
# regions = [("ABC01", [5, 3, 8, 1]), ("DRG32", [7, 9, 8, 4]), ("O2932", [3, 3, 2, 9])]
regions = []

for _ in range(qtd_regions):
    in_str = input().split()
    new_region = (in_str[0], list(map(int, in_str[1:])))
    regions.append(new_region)
    if len(in_str[0]) > 10:
        exit()
    if any(n > 300 for n in new_region[1]):
        exit()


for region in regions:
    print(region[0], min(map(lambda p: p[0]//p[1], zip(region[1], qtd_por_perfil))))
