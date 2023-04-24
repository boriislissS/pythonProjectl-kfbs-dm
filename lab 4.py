from typing import List

def max_flow_ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    n = len(graph)
    # ініціалізація потоку на 0
    flow = 0
    # допоки існує шлях з додатнім потоком
    while True:
        # список, що містить батьківські вершини для кожної вершини
        parent = [-1] * n
        # через нульовий потік усі ребра є доступними
        visited = [False] * n
        visited[source] = True
        queue = [source]
        while queue:
            u = queue.pop(0)
            for v in range(n):
                if not visited[v] and graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        # якщо немає шляху, вихід з циклу
        if not visited[sink]:
            break
        # шукаємо мінімальний потік у шляху
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        # віднімаємо потік шляху від графу та додаємо потік до загального потоку
        flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
    return flow

if __name__ == '__main__':
    graph = [
        [0, 20, 20, 20, 0, 0, 0, 0],
        [0, 0, 0, 0, 30, 0, 0, 0],
        [0, 10, 0, 0, 0, 10, 20, 0],
        [0, 0, 0, 0, 0, 15, 0, 0],
        [0, 0, 10, 0, 0, 10, 0, 20],
        [0, 0, 0, 0, 0, 0, 10, 20],
        [0, 0, 0, 10, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    source = 0
    sink = 7
    max_flow = max_flow_ford_fulkerson(graph, source, sink)
    print(f"Max flow from {source} to {sink}: {max_flow}")
