def dfs(graph, visited, root):
    visited.append(root)
    print("Visiting the node, ", root)

    for v in graph[root]:
        if v not in visited:
            dfs(graph, visited, v)

    print("Backtracking from node, ", root)


graph = [
    [1, 3],
    [0],
    [4],
    [0],
    [2]
]
n = 5
visited = []
for u in range(n):
    if u not in visited:
        dfs(graph, visited, u)
