class Solution:
    def findCircleNum(self, con: List[List[int]]) -> int:
        def dfs(visted,adj,x):
            visted.add(x)
            for i in adj[x]:
                if i not in visted:
                    dfs(visted,adj,i)

        adj = [[]]
        for i in range(len(con)):
            l = []
            for j in range(len(con[i])):
                if i == j:
                    continue
                if con[i][j] == 1:
                    l.append(j+1)
            adj.append(l)

        print(adj)

        visted = set()
        c = 0
        for i in range(1,len(adj)):
            if i not in visted:
                    c += 1
                    dfs(visted,adj,i)
        return c