# Problema D
import sys
from math import sin, cos, radians

qtd_points, angle = list(map(int, input().split()))
angle = radians(angle)

points = [list(map(int, l.split())) for l in sys.stdin.readlines()]

for p in points:
    x = (p[0] * cos(angle)) - (p[1] * sin(angle))
    y = (p[0] * sin(angle)) + (p[1] * cos(angle))
    print("{:.2f} {:.2f}".format(x, y))
