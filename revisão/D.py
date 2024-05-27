# Problema não aceito
from math import sin, cos, radians
from typing import Tuple


def rotate(point: Tuple[float, float], angle: float) -> Tuple[float, float]:
    x = point[0] * cos(angle) - point[1] * sin(angle)
    y = point[0] * sin(angle) + point[1] * cos(angle)
    return x, y


if __name__ == "__main__":
    qtd_points, theta = 5, radians(37.5)
    # qtd_points, theta = list(map(int, input().split()))
    # theta = radians(theta)

    points = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
    # points = [list(map(int, input().split())) for _ in range(qtd_points)]

    for p in points:
        x, y = rotate(p, theta)
        print("{:.2f} {:.2f}".format(x, y))
