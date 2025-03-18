class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        ind=0
        for i in range(1,n+1):
            if ind>=len(target):
                break
            if i==target[ind]:
                s.append("Push")
                ind+=1
            else:
                s.append("Push")
                s.append("Pop")
                
        return s