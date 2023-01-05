def myBfs(root, graph):
    visited = [False] * len(graph)
    queue = []
    if len(graph) == 0:
        return
    else:
        visited[root] = True
        queue.append(root)
        for node in graph[root]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                print(f"Visiting {root} to {node}")
        while queue:
            root = queue.pop(0)
            for node in graph[root]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    print(f"Visiting {root} to {node}")


if __name__ == "__main__":
    graph = [
        [1],
        [0, 2, 3],
        [1, 3, 4, 5],
        [1, 2, 6, 7],
        [2, 8],
        [2, 9],
        [3, 10],
        [3, 11],
        [4, 9],
        [5, 8],
        [6],
        [7]
    ]

    myBfs(0, graph)
