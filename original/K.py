# problema K
num = int(input())
# num = 99998   3
print("sim" if len([n for n in range(1, num + 1) if num % n == 0]) == 3 else "nao")