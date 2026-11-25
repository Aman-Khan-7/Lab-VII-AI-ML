import heapq

grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    h = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    pq = [(h(start, goal), 0, start, [start])]
    visited = set()

    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr == goal:
            return path
        if curr in visited:
            continue
        visited.add(curr)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                heapq.heappush(pq, (g + 1 + h((nr, nc), goal), g + 1, (nr, nc), path + [(nr, nc)]))
    return None

print("A* Shortest Path:", astar(grid, (0, 0), (3, 3)))
