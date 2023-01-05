def bfs(graph, root, visited):
    if root in visited:
        return
    else:
        que = [root]
        visited.append(root)
        print(f"Visiting node, {root}")
        while que:
            node = que.pop(0)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    que.append(neighbor)
                    visited.append(neighbor)
                    print(f"Visiting node, {neighbor}")


visited = []
graph = [[1, 9],
         [0, 8],
         [3],
         [2, 4, 5],
         [3],
         [3, 6],
         [5, 7],
         [3, 6, 8, 10, 11],
         [1, 7, 9],
         [0, 8],
         [7, 11],
         [7, 10],
         []]

bfs(graph, 1, visited)
