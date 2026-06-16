class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        idx = [(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        if not fresh: return 0
        time = 0
        while q:
            size = len(q)
            while size:
                x,y = q.popleft()
                size -= 1
                for i,j in idx:
                    xx = x + i
                    xy = y + j
                    if 0<=xx<len(grid) and 0<=xy<len(grid[0]) and grid[xx][xy] == 1:
                        fresh -= 1
                        grid[xx][xy] = 2
                        q.append((xx,xy))
            time += 1
            if not fresh:
                return time

        return -1
                
