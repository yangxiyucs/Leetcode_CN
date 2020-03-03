#
# class Solution(object):
#     def minSwaps(self, data):
#         """
#         :type data: List[int]
#         :rtype: int
#         """
#
#         count1 = 0
#         for i in data:
#             if i == 1:
#                 count1 += 1
#         print("count1==", count1)
#         maxSum = 0
#         for i in range(count1):
#             maxSum += data[i]
#         print("maxSum=====", maxSum)
#         temp = maxSum
#         for i in range(count1, len(data)):
#             temp += data[i] - data[i - count1]
#             maxSum = max(maxSum, temp)
#             print(i ,maxSum)
#         return count1 - maxSum
#
#
# s = Solution()
# s.minSwaps([1,0,1,0,1,0,1,1,1,0])
