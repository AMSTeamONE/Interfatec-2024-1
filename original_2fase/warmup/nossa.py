def seq(n):
    pyramid = [str(n)]
    for i in range(n):
        pyramid.append(pyramid[i] + str(int(pyramid[i][-1]) * 3))
    
    return "\n".join(pyramid)

print(seq(4))
