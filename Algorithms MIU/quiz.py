"""
Name: Shaikh Nayeem Uddin
Batch: 56
ID: 2156CSE00913
"""


def dfs(rootNode, visited, graph):
    if visited[rootNode]:
        return
    else:
        visited[rootNode] = True

        for connectedNode in graph[rootNode]:
            if not visited[connectedNode]:
                dfs(connectedNode, visited, graph)



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

