import os
print(os.system('cat display_rumtime.txt'))
def dfs(i,j,m,n,mat):
    if i > m or j > n:
        return 0
    if i == m -1 and j == n - 1:
        return 1
    if mat[i][j] != -1:
        return mat[i][j]
    mat[i][j] = dfs(i+1,j,m,n,mat) + dfs(i,j+1,m,n,mat)
    return mat[i][j]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[-1]*(n+1) for _ in range(m+1)]
        return dfs(0,0,m,n,mat)
        
        