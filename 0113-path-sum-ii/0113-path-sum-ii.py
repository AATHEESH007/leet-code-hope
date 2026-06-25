# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        arr = []

        def dfs(root,sum,a):
            if not root:
                return
            sum += root.val
            a.append(root.val)
            if not root.left and not root.right and sum == target:
                arr.append(a[:])
            
            dfs(root.left,sum,a)
            dfs(root.right,sum,a)

            a.pop()

        dfs(root,0,[])
        return arr