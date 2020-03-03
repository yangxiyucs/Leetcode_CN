# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。
# #
# # 若队列为空，pop_front 和 max_value 需要返回 -1
# #
# # 示例 1：
# #
# # 输入:
# # ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# # [[],[1],[2],[],[],[]]
# # 输出: [null,null,null,2,1,2]
# # 示例 2：
# #
# # 输入:
# # ["MaxQueue","pop_front","max_value"]
# # [[],[],[]]
# # 输出: [null,-1,-1]
# #  
# #
# # 限制：
# #
# # 1 <= push_back,pop_front,max_value的总操作数 <= 10000
# # 1 <= value <= 10^5
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#使用双队列来实现，
#queue中存储正常队列
#deque中存储递减队列
class MaxQueue(object):

    def __init__(self):
        # queue存储正常队列
        self.queue = []
        # deque 存储递减队列，用来返回队列的最大值deque[0]
        self.deque = []

    def max_value(self):
        """
        :rtype: int
        """
        return self.deque[0] if self.deque else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop(-1)
        self.deque.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        # deque,queue队首相同，则deque同时弹出
        front = self.queue and self.queue.pop(0)
        if self.deque and self.deque[0] == front:
            self.deque.pop(0)
        return front or -1

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()