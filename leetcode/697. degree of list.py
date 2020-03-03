# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 示例 2:
#
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/degree-of-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {},{},{}
        for key, value in enumerate(nums):
           if value not in left:
               left[value] =key
           #右边词典更新，并保存最后value最后一次出现的key
           right[value] = key
               #获取对应数字出现的次数
           count[value] = count.get(value,0) + 1
        #假定N个数字都不同， N为nums的长度
        degree = len(nums)
        maxNum = max(count.values())
        for i in count:
            if count[i] == maxNum:
                degree = min(degree, right[i]-left[i]+1)
        return degree