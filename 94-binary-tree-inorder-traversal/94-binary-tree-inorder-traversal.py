# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        l= self.inorderTraversal(root.left)
        r= self.inorderTraversal(root.right)
        
        res=[]
        if l: res.extend(l)
        res.append(root.val)
        if r: res.extend(r)
            
        return res
