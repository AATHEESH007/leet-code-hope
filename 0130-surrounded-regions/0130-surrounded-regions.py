class Solution:
    def solve(self, g: List[List[str]]) -> None:
        if len(g) == 1:
            return g
        def dfs(i,j):
            if i<0 or i>=len(g) or j<0 or j>=len(g[0]) or g[i][j] != "O":
                return
            g[i][j] = "R"
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if (i == 0 or j == 0 or i == len(g)-1 or j == len(g[0])-1) and g[i][j] == "O":
                    dfs(i,j)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] == "O":
                    g[i][j] = "X"
                if g[i][j] == "R":
                    g[i][j] = "O"
        return g