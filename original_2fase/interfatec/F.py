while True:
    inp = input()
    if inp == ".":
        break

    op_stack = []
    val_stack = []
    prev = ""
    for c in inp:
        if c in "()":
            print("".join(reversed(op_stack)), end="")
            op_stack.clear()
            
        elif c not in "+-/*^":
            print(c, end="")
        else:
            op_stack.append(c)
        prev = c
    print("".join(reversed(op_stack)))
