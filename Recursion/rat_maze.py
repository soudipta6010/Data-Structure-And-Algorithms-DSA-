def is_safe(x, y, maze, visited, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

def solve_maze_util(maze, x, y, visited, path, all_paths, n):
    # If destination (n-1, n-1) is reached
    if x == n - 1 and y == n - 1:
        all_paths.append(path)
        return

    # Directions: Down, Left, Right, Up
    dir_x = [1, 0, 0, -1]
    dir_y = [0, -1, 1, 0]
    dir_char = ['D', 'L', 'R', 'U']

    # Mark current cell as visited
    visited[x][y] = True

    for i in range(4):
        next_x = x + dir_x[i]
        next_y = y + dir_y[i]

        if is_safe(next_x, next_y, maze, visited, n):
            solve_maze_util(maze, next_x, next_y, visited, path + dir_char[i], all_paths, n)

    # Backtrack
    visited[x][y] = False

def find_all_paths(maze):
    n = len(maze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    all_paths = []

    if maze[0][0] == 1:
        solve_maze_util(maze, 0, 0, visited, "", all_paths, n)

    return all_paths

# Sample maze input
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

paths = find_all_paths(maze)
print("All possible paths:")
for path in paths:
    print(path)
