class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        counter = 0
        for val in nums:
            if counter == 0:
                candidate = val

            if candidate == val:
                counter += 1
            else:
                counter -= 1

        return candidate

# O(NlogN)
from collections import Counter
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for key in counter:
            if counter[key] > len(nums)//2:
                return key


# O(NlogN)
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums)//2
        return nums[mid]
        