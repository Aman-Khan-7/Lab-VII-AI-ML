import heapq

# None = cliff (blocked), 1 = bonus cell (low cost), 2 = normal cell
grid = [
    [2, 2, None, 2],
    [1, 1, 2, 2],
    [None, 1, None, 2],
    [2, 1, 1, 2]
]

def treasure_astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    h = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    pq = [(h(start, goal), 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        _, g, curr, path = heapq.heappop(pq)
        if curr == goal:
            return path, g
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] is not None:
                new_g = g + grid[nr][nc]
                if new_g < best_cost.get((nr, nc), float('inf')):
                    best_cost[(nr, nc)] = new_g
                    heapq.heappush(pq, (new_g + h((nr, nc), goal), new_g, (nr, nc), path + [(nr, nc)]))
    return None, None

path, cost = treasure_astar(grid, (0, 0), (3, 3))
print(f"Most Efficient Path: {path} (Total Cost: {cost})")
