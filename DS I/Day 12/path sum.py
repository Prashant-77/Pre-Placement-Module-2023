class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, n, s, a):
        if n == None: return False
        if n.left == None and n.right == None:
            if s == a+n.val: return True
        return self.search(n.left, s, a+n.val) \
            or self.search(n.right, s, a+n.val)
        
    def hasPathSum(self, n, s):
        """
        :type n: TreeNode
        :type s: int
        :rtype: bool
        """
        return self.search(n, s, 0)