"""
Created by Allen on '2018/11/28 11:06'
"""
__author__ = 'Allen'

"""
Two Sum II - Input array is sorted
"""


# 方法一
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lists = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    lists.append(i+1)
                    lists.append(j+1)
                    return lists


numbers = [2, 7, 11, 15]
target = 26

print(Solution().twoSum(numbers, target))


# 方法二
# 时间复杂度: O(lgN)  空间复杂度: O(1)
# 二分法+双指针，beats 86.15%
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1


numbers = [2, 7, 11, 15]
target = 26

print(Solution().twoSum(numbers, target))