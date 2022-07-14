class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if matrix[mid][0] == target:
                return True            
            elif matrix[mid][0] > target:
                end = mid
            else:
                if self.binary_search(matrix[mid], target):
                    return True
                
                start = mid
                
        if self.binary_search(matrix[start], target) or self.binary_search(matrix[end], target):
            return True
        
        return False
    
    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2                

            if nums[mid] == target:
                return True        
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target or nums[end] == target:
            return True
        
        return False
