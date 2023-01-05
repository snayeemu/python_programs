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

    for node, neighborsList in graph.items():
        if node not in visited:
            count += 1
        dfs(node, visited, graph)
    return count


if __name__ == "__main__":
    graph = {
                0:  [0, 3],
                1: [0, 2],
                2: [1, 3],
                3: [0, 2],
                4: [5],
                5: [4, 6, 9],
                6: [5, 7, 8],
                7: [6],
                8: [6],
                9: [5, 10],
                10: [11, 13, 15, 16],
                11: [10],
                12: [30],
                13: [10, 14],
                14: [13, 19, 20],
                15: [10],
                16: [10, 17],
                17: [16, 18],
                18: [17, 23],
                19: [14],
                20: [14, 21, 22],
                21: [20],
                22: [20, 23],
                23: [18, 22, 24],
                24: [23, 25, 26],
                25: [24],
                26: [24],
                27: [28],
                28: [27, 29, 35],
                29: [28, 34, 35],
                30: [12, 35],
                32: [33, 34],
                33: [32],
                34: [29, 32],
                35: [29, 30]
    }
    connectedComponent = numberOfConnectedComponent(graph)
    print(connectedComponent)
