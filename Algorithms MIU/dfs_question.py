

def dfs(u):
    visited[u] = True
    print("Visiting the node, ", u)

    for v in graph[u]:
        if not visited[v]:
            dfs(v)

    print("Backtracking from node, ", u)


graph = [
    [1, 3],
    [0],
    [4],
    [0],
    [2]
]
n = 5
visited = [False] * n
for u in range(n):
    if not visited[u]:
        dfs(u)