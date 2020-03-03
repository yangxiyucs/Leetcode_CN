# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         d = {}
#         res =0
#         index = 0
#         for i in range(len(s)):
#             if s[i] in d:
#               index = max(index, d.get(s[i]))
#             res = max(res, i - index +1)
#             d[s[i]] = i + 1
#         return res
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #优化的，利用hashmap
        # d = {}
        # res =0
        # index = 0
        # for i in range(len(s)):
        #     if s[i] in d:
        #       index = max(index, d.get(s[i]))
        #     res = max(res, i - index +1)
        #     d[s[i]] = i + 1
        # return res


        ##利用 滑动数组
        # i, j, res = 0,0,0
        # n = len(s)
        # set1 =set()
        # while i < n and j < n:
        #     if s[j] not in set1:
        #         set1.add(s[j])
        #         j = j + 1
        #         res = max(res,j - i)
        #
        #     else:
        #         set1.remove(s[i])
        #         i+=1
        # return res
s = Solution()
x= "abcabcbb"
s.lengthOfLongestSubstring(x)