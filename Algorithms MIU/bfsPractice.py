def bfs(root, graph):
    if len(graph) <= 0:
        return
    else:
        queue = []
        visited = [False] * len(graph)
        queue.append(root)
        mainRoot = root
        prev = root
        lastNode = None
        while queue:
            root = queue.pop(0)
            visited[root] = True
            if mainRoot == root:
                print(f"Visiting {root}")
            else:
                print(f"Visiting {prev} --> {root}")
            for node in graph[root]:
                if not visited[node] and node not in queue:
                    queue.append(node)
                    lastNode = node
            if prev == lastNode:
                prev = root


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
    bfs(11, graph)
