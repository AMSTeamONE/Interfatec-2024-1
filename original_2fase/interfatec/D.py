sides = sorted([float(s) for s in input().split()])
base = sides[0]

prop = sides[1] / (sides[1] + sides[2])
h = (sides[1]**2 - (base * prop)**2) ** 0.5
h = round(h)

print(f"{base * h / 2:.2f}")