#1679. Max Number of K-Sum Pairs

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l =0
        r = len(nums)-1
        count = 0
        print(nums)
        while l<r:
            if k - nums[l] > nums[r]:
                l+=1
            elif k - nums[l] < nums[r]:
                r-=1
            else:
                r-=1
                l+=1
                count+=1
        return count
