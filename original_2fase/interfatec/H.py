# width = 15
# phrase = "o rato roeu a roupa do rei de roma".split(" ")
width = int(input())
phrase = input().split()

# print(phrase)
lines = []
while len(phrase) > 0:
    line = []
    
    while len(phrase) > 0 and len("".join(line)) + len(phrase[0]) + len(line) - 1 < width:
        line.append(phrase.pop(0))
    

    if len(phrase) == 0 and len(line) != 1:
        just_width = 1
    elif len(line) == 1:
        just_width = 0
    else:
        just_width = (width - len("".join(line))) / ((len(line) - 1) or 1)
    
    lines.append(f"{just_width:.3f}")

print(*lines)
