# Initialize the graph and a variable to store the count of connected components
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
component_count = 0
visited = []

# A helper function to perform depth-first search
def dfs(graph, start, visited):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Find the connected components of the graph
for node in graph:
    if node not in visited:
        dfs(graph, node, visited)
        component_count += 1

# Print the number of connected components
print(component_count)
