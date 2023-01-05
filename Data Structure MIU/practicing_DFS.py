def DFS(self, s):
    visited = [False for i in range(self.v)]
    stack = []
    stack.append(s)
    while len(stack):
        s = stack.pop()
        if not visited[s]:
            print(s, end=" ")
            visited[s] = True
        for node in self.adj[s]:
            if not visited[node]:
                stack.append(node)
