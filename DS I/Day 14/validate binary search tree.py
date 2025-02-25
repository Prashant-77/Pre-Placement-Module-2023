class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.helper(root, sys.maxsize, -sys.maxsize)
    
    def helper(self, root, max_value, min_value):
        if not root:
            return True
                
        left = self.helper(root.left, root.val, min_value)
        right = self.helper(root.right, max_value, root.val)
        
        return left and right and root.val < max_value and root.val > min_value
        