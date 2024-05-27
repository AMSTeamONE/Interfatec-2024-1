import sys

# PROBLEMA L
def swap(c):
    if c == 'T': return 'A'
    if c == 'A': return 'T'
    if c == 'C': return 'G'
    if c == 'G': return 'C'

def analyse_strand(strand: str):
    for i in range(len(strand)):
        for j in range(i + 1, len(strand)):
            window = strand[i:j+1]
            if [swap(c) for c in window] == list(reversed(window)) and len(window) > 2:
                return f"{i + 1} {len(window)}"
    return "false"

dnas = sys.stdin.readlines()

# while True:
#     entrada = input()
#     if entrada == "":
#         break    
#     dnas.append(entrada)

for strand in dnas:
    print(analyse_strand(strand))
