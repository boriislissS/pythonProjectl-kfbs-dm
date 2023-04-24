import itertools


def isomorphic(graph1, graph2):
    # Перевіряємо чи графи мають однакову кількість вершин
    if len(graph1) != len(graph2):
        return False
    
    # Знаходимо степені вершин у графах
    degrees1 = [sum(graph1[i]) for i in range(len(graph1))]
    degrees2 = [sum(graph2[i]) for i in range(len(graph2))]
    
    # Перевіряємо чи графи мають однакову послідовність степенів вершин
    if sorted(degrees1) != sorted(degrees2):
        return False
    
    # Перебираємо всі можливі співставлення вершин у графах
    n = len(graph1)
    for mapping in itertools.permutations(range(n)):
        is_isomorphic = True
        for i in range(n):
            for j in range(i, n):
                # Перевіряємо чи зберігається сусідство вершин
                if graph1[i][j] != graph1[mapping[i]][mapping[j]] or \
                   graph2[i][j] != graph2[mapping[i]][mapping[j]]:
                    is_isomorphic = False
                    break
            if not is_isomorphic:
                break
        if is_isomorphic:
            return True
    
    return False

# Приклад використання
graph1 = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
graph2 = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]

if isomorphic(graph1, graph2):
    print("Графи ізоморфні")
else:
    print("Графи неізоморфні")
