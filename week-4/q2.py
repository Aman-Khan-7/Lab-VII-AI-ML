import heapq
import math

cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

def euclidean(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.hypot(x2 - x1, y2 - y1)

def best_first_search(start, goal):
    pq = [(euclidean(start, goal), start, [start])]
    visited = set()

    while pq:
        _, curr, path = heapq.heappop(pq)
        if curr == goal:
            return path
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                heapq.heappush(pq, (euclidean(neighbor, goal), neighbor, path + [neighbor]))
    return None

print("Best-First Path (A to E):", best_first_search('A', 'E'))
