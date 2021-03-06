# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, paths, path):
        if root == None:
            return 
        if root.left == None and root.right == None:
            path.append(root.val)
            paths.append(path)
            return 
    
        if root.left != None:
            self.dfs(root.left, paths, path + [root.val])
        if root.right != None:
            self.dfs(root.right, paths, path + [root.val])
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        paths = []
        path = []
        self.dfs(root, paths, path)
        for i in paths:
            if sum(i) == targetSum:
                return True
        return False
        return(paths)
        