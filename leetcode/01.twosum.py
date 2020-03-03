#[2,3,5,7,9] 2+7=9
#返回2,7对应的坐标
# return [0,3]
#github test

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for x, y in enumerate(nums):
            if target - y in nums:
                return [dict1[target - y], x]
            dict1[y] = x
