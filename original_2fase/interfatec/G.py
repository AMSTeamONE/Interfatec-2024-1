qtd = int(input())

# largura total, qtd, largura individual
projs = [[int(s) for s in input().split()] for _ in range(qtd)]

for proj in projs:
    total = proj[0]
    sobra = total - proj[1] * proj[2]
    espacamento = sobra // proj[1] + 1
    
    if espacamento < 10:
        print("projeto superdimensionado")
    elif espacamento > 20:
        print("projeto subdimensionado")
    else:
        print("projeto ok")
print("")