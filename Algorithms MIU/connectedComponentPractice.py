


def dfs(graph, visited, node):
    if node in visited:
        return
    else:
        stack = [node]
        while stack:
            node = stack.pop()
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def connectedComponent(graph):
    visited = []
    count = 0
    for node in range(len(graph)):
        if node not in visited:
            count += 1
            dfs(graph, visited, node)

    return count


if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 2],
        [1, 0],
        [6],
        [5],
        [4],
        [3],
        [8],
        [7]
    ]
    connectedComponent = connectedComponent(graph)
    print(connectedComponent)
