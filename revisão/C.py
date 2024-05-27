# Problema não aceito
import itertools as it

def calc_frete(cart: int, prods: list[int]) -> bool:
    return any(sum(trio) + cart == 200 for trio in it.combinations(prods, 3))


if __name__ == "__main__":
    total, qtd = list(map(int, input().split()))
    prods = [int(input()) for _ in range(qtd)]

    print(calc_frete(total, prods) and "fretegratis" or "fretepago")