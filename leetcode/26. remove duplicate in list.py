class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 = {}

        for key, value in enumerate(nums):
            if num1[value] > 1:
                nums.pop(key)
            num1[value] += 1
        return nums

nums=[1,2,1]
rem = Solution.removeDuplicates(nums)
print(rem)
