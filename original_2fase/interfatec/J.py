from itertools import it

vertices, qtd_connections = map(int, input().split())

# start, end, length
edges = [map(int, input().split()) for _ in qtd_connections]



# menor caminho q passe por todas as estações
