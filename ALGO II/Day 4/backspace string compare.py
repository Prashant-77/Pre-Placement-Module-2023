class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def helper(s):
            result = []

            for c in s:
                if c != '#':
                    result.append(c)
                elif result:
                    result.pop()
        
            return "".join(result)
            
        return helper(S) == helper(T)