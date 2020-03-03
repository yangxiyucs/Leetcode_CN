# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
# 示例:
#
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-string

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res, multi =[],"", 0
        for i in s:
            #"3[a2[c]]"
            #如果是左括号， 就弹出栈，清空栈，置零数组
            #res = last_res  + multi * res
            print(i)
            if i == '[':
              stack.append([multi, res])
              res,multi = "" , 0
            elif i ==']' :
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <=i<= '9':
                multi = multi*10 + int(i)
            else:
                res += i
        return res