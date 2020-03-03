
# {}()[] 判断是否闭合
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mappings = {"}":"{","]":"[",")":"("}

        for c in s:
            if c in mappings:
                match = stack.pop() if stack else "#"
                if mappings[c] != match:
                    return False
            else:
                stack.append(c)
        #in the end , the result wont be empty like ((()
        return not stack