import heapq
from collections import deque

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start, goal = (0, 0), (0, 4)

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        curr, path = queue.popleft()
        if curr == goal:
            return path, len(visited)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None, len(visited)

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    h = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    pq = [(h(start, goal), 0, start, [start])]
    visited = set()
    while pq:
        _, g, curr, path = heapq.heappop(pq)
        if curr == goal:
            return path, len(visited)
        if curr in visited:
            continue
        visited.add(curr)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                heapq.heappush(pq, (g + 1 + h((nr, nc), goal), g + 1, (nr, nc), path + [(nr, nc)]))
    return None, len(visited)

bfs_path, bfs_visited = bfs(maze, start, goal)
astar_path, astar_visited = astar(maze, start, goal)

print(f"BFS  -> Steps: {len(bfs_path)-1}, Visited: {bfs_visited}, Path: {bfs_path}")
print(f"A*   -> Steps: {len(astar_path)-1}, Visited: {astar_visited}, Path: {astar_path}")
