qtd_aceitos = int(input())
ranges_aceitas = [[int(s.replace("-", "")) for s in input().split()] for _ in range(qtd_aceitos)]

qtd_testes = int(input())
testes = [input() for _ in range(qtd_testes)]

served = []
not_served = []

for test in testes:
    if any(rang[0] <= int(test.replace("-", "")) <= rang[1] for rang in ranges_aceitas):
        served.append(test)
    else:
        not_served.append(test)

for s in sorted(served, key=lambda t: int(t.replace("-", ""))):
    print(f"{s} is served by our delivery system")

for s in sorted(not_served, key=lambda t: int(t.replace("-", ""))):
    print(f"{s} is not served by our delivery system")