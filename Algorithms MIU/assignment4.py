"""
Name: Shaikh Nayeem Uddin
Batch: 56
ID: 2156CSE00913
"""


def shortestPath(graph, root, nodeToReach):
    prev = [-1] * len(graph)
    queue = []

    queue.append(root)

    visited = [False] * len(graph)

    visited[root] = True

    while queue:
        node = queue.pop(0)

        for neighbor in graph[node]:

            if not visited[neighbor]:
                queue.append(neighbor)
                prev[neighbor] = node
                visited[neighbor] = True
                if neighbor == nodeToReach:
                    break

    path = []

    i = nodeToReach
    while i != -1:
        path.append(i)
        i = prev[i]

    path.reverse()
    return path


if __name__ == "__main__":
    numberOfNodes = int(input())
    weightForEachNode = list(map(int, input().strip().split()))[0:numberOfNodes]
    adjacencyList = [
        [] for i in range(numberOfNodes)
    ]
    for i in range(numberOfNodes - 1):
        nameOfTwoNodesWhereAnEdgeExist = list(map(int, input().strip().split()))[0:2]
        firstNode, secondNode = nameOfTwoNodesWhereAnEdgeExist
        adjacencyList[firstNode - 1].append(secondNode - 1)
        adjacencyList[secondNode - 1].append(firstNode - 1)

    shortestPathToTravel = [
        [] for i in range(numberOfNodes)
    ]
    for i in range(numberOfNodes):
        shortestPathToTravel[i] = shortestPath(adjacencyList, 0, i)

    allWeightsHaveToTravelForReadingTheNode = [
        [] for i in range(numberOfNodes)
    ]

    for i in range(numberOfNodes):
        for node in shortestPathToTravel[i]:
            weight = weightForEachNode[node]
            allWeightsHaveToTravelForReadingTheNode[i].append(weight)

    allMEXs = []
    for i in range(numberOfNodes):
        count = 0
        for j in range(len(allWeightsHaveToTravelForReadingTheNode[i])):
            if count in allWeightsHaveToTravelForReadingTheNode[i]:
                count += 1
            else:
                break
        allMEXs.append(count)

    MEXimum = allMEXs[0]

    for MEX in allMEXs:
        if MEXimum < MEX:
            MEXimum = MEX

    print(MEXimum)
