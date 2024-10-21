heigth, width, qtd_moves, y, x = [int(s) for s in input().split()]
moves = list(input())

pos = [y, x]
for m in moves:
    if m == "C":
        pos[0] += 1
    if m == "B":
        pos[0] -= 1
    if m == "D":
        pos[1] -= 1
    if m == "E":
        pos[1] += 1

if pos[0] < 0 or pos[0] > heigth or pos[1] < 0 or pos[1] > width:
    print("-1 -1")
else:
    print(*pos)