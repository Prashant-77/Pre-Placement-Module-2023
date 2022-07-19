class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        self.helper(root, result)
        
        return result
    
    
    def helper(self, root, result):
        if root == None:
            return
        
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)