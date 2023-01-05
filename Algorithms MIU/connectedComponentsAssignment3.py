"""
Name: Shaikh Nayeem Uddin
Batch: 56
ID: 2156CSE00913
"""


def dfs(rootNode, visited, graph):
    if rootNode in visited:
        return
    else:
        visited.append(rootNode)

        for connectedNode in graph[rootNode]:
            if connectedNode not in visited:
                dfs(connectedNode, visited, graph)


def numberOfConnectedComponent(graph):
    count = 0
    visited = []

    for i in range(len(graph)):
        if i not in visited:
            count += 1
        dfs(i, visited, graph)
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
    connectedComponent = numberOfConnectedComponent(graph)
    print(connectedComponent)
