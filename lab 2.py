from typing import List, Tuple

def tsp(graph: List[List[int]]) -> Tuple[List[int], int]:
    n = len(graph)
    best_path = None
    best_cost = float('inf')

    def dfs(path, cost, visited):
        nonlocal best_path, best_cost
        if len(path) == n:
            cost += graph[path[-1]][path[0]]
            if cost < best_cost:
                best_cost = cost
                best_path = path
            return

        for i in range(n):
            if i not in visited:
                new_path = path + [i]
                new_cost = cost + graph[path[-1]][i]
                if new_cost < best_cost:
                    dfs(new_path, new_cost, visited | {i})

    for i in range(n):
        dfs([i], 0, {i})

    return best_path, best_cost

if __name__ == '__main__':
    graph = [
        [0, 0, 0, 0, 86, 94, 51, 82],
        [0, 0, 81, 0, 20, 87, 0, 0],
        [0, 81, 0, 83, 41, 0, 0, 0],
        [0, 0, 83, 0, 8, 0, 0, 0],
        [86, 20, 41, 8, 0, 40, 0, 54],
        [94, 87, 0, 0, 40, 0, 89, 0],
        [51, 0, 0, 0, 0, 89, 0, 18],
        [82, 0, 0, 0, 54, 0, 18, 0],
    ]
    path, cost = tsp(graph)
    print(f"Optimal pathtt: {path}")
    print(f"Total cost: {cost}") 
