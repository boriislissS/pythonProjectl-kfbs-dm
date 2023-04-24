from typing import List, Tuple

def prim(graph: List[List[int]]) -> Tuple[List[Tuple[int, int]], int]:
    n = len(graph)
    visited = [False] * n
    mst = []
    total_cost = 0

    visited[0] = True
    for _ in range(n - 1):
        min_edge = None
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if min_edge is None or graph[i][j] < graph[min_edge[0]][min_edge[1]]:
                            min_edge = (i, j)
        if min_edge is None:
            return [], float('inf')

        mst.append(min_edge)
        total_cost += graph[min_edge[0]][min_edge[1]]
        visited[min_edge[1]] = True

    return mst, total_cost

if __name__ == '__main__':
    graph = [
        [0, 0, 7, 0, 0, 0, 46, 98],
        [0, 0, 33, 0, 0, 99, 0, 0],
        [7, 33, 0, 99, 92, 28, 0, 64],
        [0, 0, 99, 0, 15, 52, 0, 0],
        [0, 0, 92, 15, 0, 0, 0, 58],
        [0, 99, 28, 52, 0, 0, 0, 0],
        [46, 0, 0, 0, 0, 0, 0, 36],
        [98, 0, 64, 0, 58, 0, 36, 0],
    ]
    mst, cost = prim(graph)
    print(f"Minimum Spanning Tree: {mst}")
    print(f"Total cost: {cost}") 
