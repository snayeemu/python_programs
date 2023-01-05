


def dfs(graph, topsort, visited, visiting, rootToNode, u):
    visited[u] = True
    visiting.append(u)
    print('Visiting ', u)

    for v in graph[u]:
        if not visited[v]:
            dfs(graph, topsort, visited, visiting, rootToNode, v)
    print('Backtracking ', u)
    for i in range(len(visiting)):
        node = visiting.pop()
        rootToNode[u].append(node)
    topsort.append(u)
    return topsort


if __name__ == "__main__":
    numberOfNodes = int(input())
    weightForEachNode = list(map(int, input().strip().split()))[0:6]
    adjacencyList = [
        [] for i in range(numberOfNodes)
    ]
    for i in range(numberOfNodes - 1):
        nameOfTwoNodesWhereAnEdgeExist = list(map(int, input().strip().split()))[0:2]
        firstNode, secondNode = nameOfTwoNodesWhereAnEdgeExist
        adjacencyList[firstNode - 1].append(secondNode - 1)
        adjacencyList[secondNode - 1].append(firstNode - 1)

    visited = [False] * len(adjacencyList)
    rootToNode = [
        [] for i in range(numberOfNodes)
    ]
    print(dfs(adjacencyList, [], visited, [], rootToNode, 0))

