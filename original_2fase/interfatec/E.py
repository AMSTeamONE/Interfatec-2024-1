inp = []
while True:
    cur = tuple(map(int, input().split()))
    if cur == (0, 0, 0):
        break
    inp.append(cur)

timer = 0
finished = []
for _ in range(len(inp)):
    priority = sorted([p for p in inp if timer >= p[0] and p not in finished], key=lambda p: p[2])
    if not priority:
        priority = sorted([p for p in inp if timer < p[0] and p not in finished], key=lambda p: p[0])
        timer = priority[0][0]
    nextp = priority[0]
    finished.append(nextp)
    # print(nextp)
    print(nextp[1], timer, timer + nextp[2])
    timer += nextp[2]
    
