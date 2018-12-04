"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    """
        :type nums: List[int]
        :rtype: int
    """
    """ Try 1 exceeds time limit
    def singleNumber(self, nums):
        matched = False
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (nums[i] == nums[j] and i != j):
                    matched = True
            if (matched == True):
                matched = False
            else:
                return nums[i]
        return -1
    """
    """ Try 2 runs in nlogn time
    def singleNumber(self, nums):
        nums.sort()
        #stack = [nums[0], nums[1]]
        stack = []
        for i in range(0, len(nums)):
            stack.append(nums[i])
            if (len(nums) > 1 and nums[i] == nums[i-1]):
                stack.pop();
                stack.pop();
        return stack.pop()
    """
    # Try 3 runs in n time
    def singleNumber(self, nums):
        ref = {}
        for i in range(0, len(nums)):
            if (nums[i] in ref):
                ref[nums[i]] = 1
            else:
                ref[nums[i]] = 0
        for key, value in ref.items():
            if (value == 0):
                return int(key)
