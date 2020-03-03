#反转int 数字
class Solution(object):
    def  reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #pop operation:
        y, rev =abs(x), 0
        boundary  = 2**31-1 if x > 0 else 2**31
        while y != 0:
            rev = rev * 10 + y%10
            if rev > boundary:
                return 0
            y  = y // 10
        return rev  if x >0 else (-rev)