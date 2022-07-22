class Solution(object):
    def inorderTraversal(self, root):
        # inorder traversal of the BST
        # return a list 
        if (root is None):
            return []
        else:
            res = []
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # first traverse the tree and put everything in a list 
        nums = self.inorderTraversal(root)
        i = 0
        j = len(nums)-1
        while(i < j):
            curr = nums[i] + nums[j]
            if (curr == k):
                return True
            elif (curr > k):
                j -= 1
            else :
                i += 1
        return False
        