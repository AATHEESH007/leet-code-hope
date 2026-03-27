class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        if n == 1:
            return [1,1]
        if n == 2:
            return [1,2,1]
        arr = [1,2,1]
        for i in range(2,n):
            ans = [1]
            for j in range(1,i+1):
                ans.append(arr[j] + arr[j-1])
            ans.append(1)
            arr = ans
        return arr