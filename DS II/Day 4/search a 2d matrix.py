import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        i = 0
        for row in matrix:
            if row[-1] < target:
                continue
            # Run Binary search
            elif row[-1] > target:
                i = bisect.bisect_left(row,target)
                if i < len(row) and row[i] == target:
                    return True
            else:
                return True
        return False