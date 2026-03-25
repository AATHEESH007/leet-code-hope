class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans =[[None for _ in range(n)] for _ in range(n)]
        top = left = 0
        bottom = n-1
        right = n-1
        x = 1
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                ans[top][i] = x
                x += 1
            top += 1
            for i in range(top,bottom+1):
                ans[i][right] = x
                x += 1
            right -= 1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans[bottom][i] = x
                    x += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans[i][left] = x
                    x += 1
                left += 1
        return ans
