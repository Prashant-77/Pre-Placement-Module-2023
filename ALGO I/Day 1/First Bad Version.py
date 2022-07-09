first_bad = 0
def isBadVersion(version):
   if version >= first_bad:
      return True
   return False
class Solution:
   def firstBadVersion(self, n):
      if n <2:
         return n
      start = 1
      end = n
      while(start<=end):
         mid = (start+end)//2
         if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
         elif isBadVersion(mid-1):
            end = mid-1
         else:
            start = mid+1
ob1 = Solution()
first_bad = 4
op = ob1.firstBadVersion(5)
print(op)