if __name__ == "__main__":
    # qtd_perfis = int(input())
    # qtd_por_perfil = list(map(int, input().split()))
    # qtd_regions = int(input())
    
    # regions = []
    # for _ in range(qtd_regions):
    #     in_str = input().split()
    #     new_region = (in_str[0], list(map(int, in_str[1:])))
    #     regions.append(new_region)

    qtd_profiles = 4
    min_profile = [2, 1, 3, 1]
    qtd_regions = 3
    regions = [("ABC01", [5, 3, 8, 1]), ("DRG32", [7, 9, 8, 4]), ("O2932", [3, 3, 2, 9])]

    for region in regions:
        print(region[0], min(map(lambda p: p[0] // p[1], zip(region[1], min_profile))))
