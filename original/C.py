import itertools as it
carrinho, qtd_prods = list(map(int, input().split()))
valores = [int(input()) for _ in range(qtd_prods)]

def calc_frete():
    for trio in it.combinations(valores, 3):
        if sum(trio) + carrinho == 200:
            return "fretegratis"
    return "fretepago"

print(calc_frete())