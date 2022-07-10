class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temps = []
        
        for i in range(len(nums) - k, len(nums)):
            temps.append(nums[i])
        
        for i in range(0, len(nums) - k):
            temps.append(nums[i])
            
        for i in range(0, len(nums)):            
            nums[i] = temps[i]     