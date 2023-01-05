def myDfs(root, graph):
    visited = [False] * len(graph)
    stack = []
    if len(graph) == 0:
        return
    else:
        visited[root] = True
        stack.append(root)
        while stack:
            root = stack[-1]
            for node in graph[root]:
                stack.append()


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

    myDfs(0, graph)
