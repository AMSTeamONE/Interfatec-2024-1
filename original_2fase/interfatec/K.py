t = list(range(1, 10))
alpha = list("ABCDEFGHI")
n = int(input())

triangle = n // 9 + 1

if n % 9 == 0:
    triangle -= 1

c = alpha[n % 9 - 1]
print(f"{triangle}{c}")