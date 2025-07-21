class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            arr.append([])
        #print(arr)
        for i in range(1,numRows+1):
            for j in range(i):
                if j == 0 or j == (i-1):
                    arr[i-1].append(1)
                else:
                    arr[i-1].append(arr[i-2][j] + arr[i-2][j-1])
                #print(arr , i , j)
        return arr