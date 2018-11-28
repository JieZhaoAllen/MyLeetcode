"""
Created by Allen on '2018/11/26 11:30'
"""
__author__ = 'Allen'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            print(i, num)
            if target - num in lookup:
                return [lookup[target - num], i]
            else:
                lookup[num] = i


nums = [2, 7, 11, 15]
target = 26


w = Solution().twoSum(nums, target)
print(w)