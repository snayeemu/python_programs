def dfs(graph, visited, node):
    if node in visited:
        return
    else:
        stack = [node]
        while stack:
            node = stack.pop()
            visited.append(node)
            print(f"Visiting node, {node}")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)



graph = [
    [3, 1],
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
