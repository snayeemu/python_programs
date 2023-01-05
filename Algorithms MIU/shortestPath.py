

def shortestPath(graph, source, destination):
    que = [source]
    visited = [source]
    prev = [-1] * len(graph)

    while que:
        node = que.pop(0)

        for neighbor in graph[node]:
            if neighbor not in visited:
                que.append(neighbor)
                prev[neighbor] = node
                visited.append(neighbor)

    path = []
    
    i = destination
    while i != -1:
        path.append(i)
        i = prev[i]
    
    path.reverse()
    for element in path:
        if element == destination:
            print(element)
            break
        print(element, end="-->")


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
         []
         ]
shortestPath(graph, 1, 7)
