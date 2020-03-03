# 输入: -121
# # # 输出: false
# # # 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = 0
        x1 = x
        while(x1>0):
          s = s*10 + x1 % 10
          x1/= 10
        return s == x