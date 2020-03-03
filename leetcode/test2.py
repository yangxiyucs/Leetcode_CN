class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxSum = nums[0]
        # maxCurr = 0
        # for i in range(len(nums)):
        #   maxCurr = max(nums[i], maxCurr + nums[i])
        #   maxSum = max(maxSum,maxCurr)

        # return maxSum

        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
                print("i==",i)
                print(f"nums[i]= {nums[i]}")
            max_sum = max(nums[i], max_sum)
            print("max--",max_sum)
        return max_sum
s = Solution()
x= [-2,1,-3,4,-1,2,1,-5,4]
s.maxSubArray(x)